# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.connection_connection import ConnectionConnection  # noqa: E501
from swagger_server.test import BaseTestCase


class TestConnectionController(BaseTestCase):
    """ConnectionController integration test stubs"""

    def test_data_connection_post(self):
        """Test case for data_connection_post

        
        """
        body = ConnectionConnection()
        response = self.client.open(
            '/data/connection/',
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_connectionconnection_id_delete(self):
        """Test case for data_connectionconnection_id_delete

        
        """
        response = self.client.open(
            '/data/connection={connection-id}/'.format(connection_id='connection_id_example'),
            method='DELETE')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_connectionconnection_id_get(self):
        """Test case for data_connectionconnection_id_get

        
        """
        response = self.client.open(
            '/data/connection={connection-id}/'.format(connection_id='connection_id_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_connectionconnection_id_post(self):
        """Test case for data_connectionconnection_id_post

        
        """
        body = ConnectionConnection()
        response = self.client.open(
            '/data/connection={connection-id}/'.format(connection_id='connection_id_example'),
            method='POST',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_data_connectionconnection_id_put(self):
        """Test case for data_connectionconnection_id_put

        
        """
        body = ConnectionConnection()
        response = self.client.open(
            '/data/connection={connection-id}/'.format(connection_id='connection_id_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/yang-data+json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
