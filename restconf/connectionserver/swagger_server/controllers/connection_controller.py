import connexion
import six
import swagger_server.database as database

from swagger_server.models.connection_connection import ConnectionConnection  # noqa: E501
from swagger_server import util


def data_connection_post(body=None):  # noqa: E501
    """data_connection_post

    creates connection.Connection # noqa: E501

    :param body: connection.Connection to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ConnectionConnection.from_dict(connexion.request.get_json())     
        body.connection_id=str(database.last_connection_id)
        database.connection[str(database.last_connection_id)] = body
        database.last_connection_id+=1
        return body


def data_connectionconnection_id_delete(connection_id):  # noqa: E501
    """data_connectionconnection_id_delete

    removes connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str

    :rtype: None
    """
    del database.connection[connection_id]
    return 'ok'



def data_connectionconnection_id_get(connection_id):  # noqa: E501
    """data_connectionconnection_id_get

    returns connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str

    :rtype: ConnectionConnection
    """
    print(database.connection)
    if connection_id in database.connection:
        return database.connection[connection_id]
    return "Error", 400


def data_connectionconnection_id_post(connection_id, body=None):  # noqa: E501
    """data_connectionconnection_id_post

    creates connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str
    :param body: connection.Connection to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_connectionconnection_id_put(connection_id, body=None):  # noqa: E501
    """data_connectionconnection_id_put

    creates or updates connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str
    :param body: connection.Connection to be added or updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
