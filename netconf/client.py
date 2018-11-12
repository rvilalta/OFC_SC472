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
c = session.capabilities
print(c)

# get config
print("---GET CONFIG---")
config = session.get_config()
xmlstr = etree.tostring(config, encoding='utf8', xml_declaration=True)
print(xmlstr)

# close connexion
session.close()
