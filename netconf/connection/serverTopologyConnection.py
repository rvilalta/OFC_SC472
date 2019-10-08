import sys
import time
import logging
import os

import binding_topology
import binding_connection

from pyangbind.lib.serialise import pybindIETFXMLEncoder, pybindIETFXMLDecoder

from netconf import nsmap_add, NSMAP
from netconf import server, util
from lxml import etree

logging.basicConfig(level=logging.DEBUG)


nsmap_add("topology", "urn:topology")
nsmap_add("connection", "urn:connection")

class MyServer(object):

    def __init__(self, username, password, port):
        host_key_value = os.path.join(os.path.abspath(os.path.dirname(__file__)), "server-key")
        auth = server.SSHUserPassController(username=username, password=password)
        auth.check_auth_none(username)
        self.server = server.NetconfSSHServer(server_ctl=auth, server_methods=self, host_key=host_key_value, port=port, debug=True)
        self.data = None
        self.load_file()

    def load_file(self):    
        # create configuration
        xml_root = open('topology.xml', 'r').read()
        print(xml_root)
        topo = pybindIETFXMLDecoder.decode(xml_root, binding_topology, "topology")
        xml = pybindIETFXMLEncoder.serialise(topo)
        tree = etree.XML(xml)
        data = util.elm("nc:data")
        data.append(tree)
        connection = etree.XML( pybindIETFXMLEncoder.serialise( binding_connection.connection() ) )
        data.append(connection)
        
        self.data = data

    def nc_append_capabilities(self, capabilities): 
        logging.debug("--GET capabilities--")
        util.subelm(capabilities, "capability").text = "urn:ietf:params:netconf:capability:xpath:1.0"
        util.subelm(capabilities, "capability").text = NSMAP["topology"]
        util.subelm(capabilities, "capability").text = NSMAP["connection"]        

    def rpc_get_config(self, session, rpc, source_elm, filter_or_none):
        logging.debug("--GET CONFIG--")
        logging.debug(session)
        logging.debug(etree.tostring(rpc))

        return util.filter_results(rpc, self.data, None)


    def rpc_edit_config(self, session, rpc, target, new_config):
        logging.debug("--EDIT CONFIG--")
        logging.debug(session)
        
        data_list = new_config.findall(".//xmlns:connection", namespaces={'xmlns': 'urn:connection'})
        for connect in data_list:
            logging.debug("connect: " )
            logging.debug(etree.tostring(connect) )
            logging.debug("CURRENT CONNECTION")
            logging.debug(etree.tostring(self.data[1]) )
            self.data[1].append(connect)
            break  
        return util.filter_results(rpc, self.data, None)

    def close(self):
        self.server.close()




def main(*margs):
    s = MyServer("admin","admin", 830)
    
    if sys.stdout.isatty():
        logging.debug("^C to quit server")

    try:
        while True:
            time.sleep(1)
    
    except Exception:
        logging.debug("quitting server")

    s.close()

if __name__ == "__main__":
    main()
