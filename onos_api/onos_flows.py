#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json

IP='localhost'
PORT='8181'
USER='onos'
PASSWORD='rocks'

URL = 'http://' + IP + ':' + PORT + '/onos/v1/flows/'

def insertFlow( nodeId, priority, inport, outport ):

    flow='{ "priority": '+priority+', "timeout": 0, "isPermanent": true, "deviceId": "'+nodeId+'", "treatment": { "instructions": [ { "type": "OUTPUT", "port": "'+outport+'" } ] }, "selector": { "criteria": [ { "type": "IN_PORT", "port": "'+inport+'" } ] } }'


    print ("Flow: " + flow)
    url = URL + nodeId + '?appId=tuto' 
    headers = {'content-type': 'application/json'}
    print (url)
    response = requests.post(url, data=flow,
	                    headers=headers, auth=HTTPBasicAuth(USER,
	                    PASSWORD))
    print (response)
    return response.status_code

def deleteFlows():
    
    url = URL + '' + 'application/'+'tuto' 
    response = requests.delete(url, auth=HTTPBasicAuth(USER, PASSWORD))
    print (response)
    return response.status_code



if __name__ == "__main__":

    print ("Setting flow")
    
    res = insertFlow(nodeId="of:0000000000000001", priority="40001", inport="1", outport="2")
    print (res)
 
    #deleteFlows()






    
