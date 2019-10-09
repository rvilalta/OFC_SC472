import connexion
import six

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
        body = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_connectionconnection_id_delete(connection_id):  # noqa: E501
    """data_connectionconnection_id_delete

    removes connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_connectionconnection_id_get(connection_id):  # noqa: E501
    """data_connectionconnection_id_get

    returns connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str

    :rtype: ConnectionConnection
    """
    return 'do some magic!'


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
