from lxml import etree
from netconf.client import NetconfSSHSession

# connexion parameters
host = 'localhost'
port = 830
username = "admin"
password = "admin"

# connexion to server
session = NetconfSSHSession(host, port, username, password)

# server capabilities
print("---GET C---")
c = session.capabilities
print(c)

# get config
print("---GET CONFIG---")
config = session.get_config()
xmlstr = etree.tostring(config, encoding='utf8', xml_declaration=True)
print(xmlstr)

# edit config
new_config = '''
<config>
        <connection xmlns="urn:connection" operation="merge">
            <connection-id>connection1</connection-id>
            <source-node>node1</source-node>
            <source-port>node1portA</source-port>
            <target-node>node2</target-node>
            <target-port>node2portA</target-port>
            <bandwidth>10</bandwidth>
            <layer-protocol-name>ETH</layer-protocol-name>                       
        </connection>
</config>
'''
print("---EDIT CONFIG---")
config = session.edit_config(newconf=new_config)
xmlstr = etree.tostring(config, encoding='utf8', xml_declaration=True)
print(xmlstr)

# close connexion
session.close()
