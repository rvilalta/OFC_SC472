# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.topology_link import TopologyLink  # noqa: E501
from swagger_server.models.topology_node import TopologyNode  # noqa: E501
from swagger_server.models.topology_port import TopologyPort  # noqa: E501
from swagger_server.models.topology_topology import TopologyTopology  # noqa: E501
from swagger_server.test import BaseTestCase


class TestTopologyController(BaseTestCase):
    """TopologyController integration test stubs"""

    def test_data_topology_delete(self):
        """Test case for data_topology_delete

        
        """
        response = self.client.open(
            '/data/topology/',
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_get(self):
        """Test case for data_topology_get

        
        """
        response = self.client.open(
            '/data/topology/',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_link_post(self):
        """Test case for data_topology_link_post

        
        """
        body = TopologyLink()
        response = self.client.open(
            '/data/topology/link/',
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_linklink_id_delete(self):
        """Test case for data_topology_linklink_id_delete

        
        """
        response = self.client.open(
            '/data/topology/link={link-id}/'.format(link_id='link_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_linklink_id_get(self):
        """Test case for data_topology_linklink_id_get

        
        """
        response = self.client.open(
            '/data/topology/link={link-id}/'.format(link_id='link_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_linklink_id_post(self):
        """Test case for data_topology_linklink_id_post

        
        """
        body = TopologyLink()
        response = self.client.open(
            '/data/topology/link={link-id}/'.format(link_id='link_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_linklink_id_put(self):
        """Test case for data_topology_linklink_id_put

        
        """
        body = TopologyLink()
        response = self.client.open(
            '/data/topology/link={link-id}/'.format(link_id='link_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_node_post(self):
        """Test case for data_topology_node_post

        
        """
        body = TopologyNode()
        response = self.client.open(
            '/data/topology/node/',
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_delete(self):
        """Test case for data_topology_nodenode_id_delete

        
        """
        response = self.client.open(
            '/data/topology/node={node-id}/'.format(node_id='node_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_get(self):
        """Test case for data_topology_nodenode_id_get

        
        """
        response = self.client.open(
            '/data/topology/node={node-id}/'.format(node_id='node_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_port_post(self):
        """Test case for data_topology_nodenode_id_port_post

        
        """
        body = TopologyPort()
        response = self.client.open(
            '/data/topology/node={node-id}/port/'.format(node_id='node_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_portport_id_delete(self):
        """Test case for data_topology_nodenode_id_portport_id_delete

        
        """
        response = self.client.open(
            '/data/topology/node={node-id}/port={port-id}/'.format(node_id='node_id_example', port_id='port_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_portport_id_get(self):
        """Test case for data_topology_nodenode_id_portport_id_get

        
        """
        response = self.client.open(
            '/data/topology/node={node-id}/port={port-id}/'.format(node_id='node_id_example', port_id='port_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_portport_id_post(self):
        """Test case for data_topology_nodenode_id_portport_id_post

        
        """
        body = TopologyPort()
        response = self.client.open(
            '/data/topology/node={node-id}/port={port-id}/'.format(node_id='node_id_example', port_id='port_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_portport_id_put(self):
        """Test case for data_topology_nodenode_id_portport_id_put

        
        """
        body = TopologyPort()
        response = self.client.open(
            '/data/topology/node={node-id}/port={port-id}/'.format(node_id='node_id_example', port_id='port_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_post(self):
        """Test case for data_topology_nodenode_id_post

        
        """
        body = TopologyNode()
        response = self.client.open(
            '/data/topology/node={node-id}/'.format(node_id='node_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_nodenode_id_put(self):
        """Test case for data_topology_nodenode_id_put

        
        """
        body = TopologyNode()
        response = self.client.open(
            '/data/topology/node={node-id}/'.format(node_id='node_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_post(self):
        """Test case for data_topology_post

        
        """
        body = TopologyTopology()
        response = self.client.open(
            '/data/topology/',
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_topology_put(self):
        """Test case for data_topology_put

        
        """
        body = TopologyTopology()
        response = self.client.open(
            '/data/topology/',
            method='PUT',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
