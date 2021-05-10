#Example CURL for TAPI 2.0

#Get Context
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/ 

#Get Service Interface Points
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/

#Get SIP sip-pe1-uni1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip-pe1-uni1/

#Get topologies
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/

#Get topology topo-nwk
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/

#Get nodes
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/

#Get node 1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pe-1/

#Get NEP list
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pe-1/owned-node-edge-point/

#Get NEP NEP_PE_01_UNI1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/node/node-pe-1/owned-node-edge-point/NEP_PE_01_UNI1/

#Get links
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/link/

#Get link 1-3
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/topo-nwk/link/PE1_NNI3_PI3_NNI1/

#Create Connectivity Service
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/ -d @cs1.json

#Get Connectivity Services
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/

curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/

#Get connection
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connection/cs1/

#Delete Connectivity Services
curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/



