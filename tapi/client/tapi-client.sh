#Example CURL for TAPI 2.0

#Get Context
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/ 

#Get topologies
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/

#Get topology Top0
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top0/

#Get nodes
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top0/node/

#Get node 1
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top0/node/node0/

#Get links
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top0/link/

#Get link 1-3
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/topology/top0/link/link0/

#Get Service End Points
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip1/
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/service-interface-point/sip2/

#Create Connectivity Service
curl -X POST -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/ -d @cs1.json

#Get Connectivity Services
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/

curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/

#Delete Connectivity Services
curl -X DELETE -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connectivity-service/cs1/

#Get connection
curl -X GET -H "Content-Type: application/json" http://127.0.0.1:8080/restconf/config/context/connection/cs1/

