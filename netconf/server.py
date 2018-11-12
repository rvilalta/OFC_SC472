import sys
import time
import logging

from binding_topology import topology

from netconf import nsmap_add, NSMAP
from netconf import server, util
from lxml import etree

logging.basicConfig(level=logging.DEBUG)


nsmap_add("topology", "urn:topology")

class MyServer(object):

    def __init__(self, username, password, port):
        auth = server.SSHUserPassController(username=username, password=password)
        self.server = server.NetconfSSHServer(server_ctl=auth, server_methods=self, port=port, debug=False)


    def nc_append_capabilities(self, capabilities): 
        util.subelm(capabilities, "capability").text = "urn:ietf:params:netconf:capability:xpath:1.0"
        util.subelm(capabilities, "capability").text = NSMAP["topology"]

    def rpc_get_config(self, session, rpc, source_elm, filter_or_none):
        logging.debug("--GET CONFIG--")
        logging.debug(session)
        logging.debug(etree.tostring(rpc))
        data = '''
        <data><topology xmlns="urn:topology"/></data>'''
        root = etree.fromstring(data)
        return util.filter_results(rpc, root, None)


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