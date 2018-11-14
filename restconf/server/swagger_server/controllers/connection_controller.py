import connexion
import six
import swagger_server.database as database

from swagger_server.models.connection_connection import ConnectionConnection  # noqa: E501
from swagger_server import util


def data_connection_post(connection_Connection_body_param=None):  # noqa: E501
    if connexion.request.is_json:
        connection_Connection_body_param = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
        connection_Connection_body_param.connection_id=str(database.last_connection_id)
        database.connection[str(database.last_connection_id)] = connection_Connection_body_param
        database.last_connection_id+=1
    return connection_Connection_body_param


def data_connectionconnection_id_delete(connection_id):  # noqa: E501
    del database.connection[connection_id]
    return 'ok'


def data_connectionconnection_id_get(connection_id):  # noqa: E501
    print(database.connection)
    return database.connection[connection_id]


def data_connectionconnection_id_post(connection_id, connection_Connection_body_param=None):  # noqa: E501
    """data_connectionconnection_id_post

    creates connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str
    :param connection_Connection_body_param: connection.Connection to be added to list
    :type connection_Connection_body_param: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        connection_Connection_body_param = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_connectionconnection_id_put(connection_id, connection_Connection_body_param=None):  # noqa: E501
    """data_connectionconnection_id_put

    creates or updates connection.Connection # noqa: E501

    :param connection_id: Id of connection
    :type connection_id: str
    :param connection_Connection_body_param: connection.Connection to be added or updated
    :type connection_Connection_body_param: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        connection_Connection_body_param = ConnectionConnection.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
