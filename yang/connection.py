from binding_connection import connection
from pyangbind.lib.serialise import pybindIETFXMLEncoder
import pyangbind.lib.pybindJSON as pybindJSON

con = connection()
con1=con.connection.add("con1")
con1.source_node = "node1"
con1.target_node = "node2"
con1.source_port = "node1portA"
con1.target_port = "node2portA"
con1.bandwidth = 1000
con1.layer_protocol_name = "OPTICAL"
print(pybindIETFXMLEncoder.serialise(con))
print(pybindJSON.dumps(con))
