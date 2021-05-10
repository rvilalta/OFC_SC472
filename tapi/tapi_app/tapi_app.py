#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from requests.auth import HTTPBasicAuth
import json
import matplotlib.pyplot as plt
import networkx as nx
import random

IP = '127.0.0.1'
PORT = '8080'


def retrieveTopology(ip, port, user='', password=''):
    print ("Reading network-topology")
    topologies = []
    topo_list_url = 'http://' + ip + ':' + port + '/restconf/config/context/topology/topo-nwk/'
    response = requests.get(topo_list_url, auth=HTTPBasicAuth(user, password))
    topologies.append(response.json())
    print ("Retrieved Topology: " + json.dumps(response.json(), indent=4))
    return topologies

def draw_topologies (topo) :
    nwk_graph = nx.Graph()

    for node in topo[0]['node']:
        if node['owned-node-edge-point']:
            uuid = node['uuid']
            layer = node['layer-protocol-name'][0]
            nwk_graph.add_node(uuid)
    for link in topo[0]['link']:
        nep1_path = link['node-edge-point'][0].split('/')
        nep2_path = link['node-edge-point'][1].split('/')
        layer = link['layer-protocol-name'][0]
        nwk_graph.add_edge(nep1_path[7], nep2_path[7])

    nx.draw_networkx(nwk_graph)

if __name__ == "__main__":
    topologies = retrieveTopology(IP, PORT)
    draw_topologies(topologies)
    plt.show()
