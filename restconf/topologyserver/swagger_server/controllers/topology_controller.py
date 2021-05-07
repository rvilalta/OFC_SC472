import connexion
import six

from swagger_server.models.topology_link import TopologyLink  # noqa: E501
from swagger_server.models.topology_node import TopologyNode  # noqa: E501
from swagger_server.models.topology_port import TopologyPort  # noqa: E501
from swagger_server.models.topology_topology import TopologyTopology  # noqa: E501
from swagger_server import util


def data_topology_delete():  # noqa: E501
    """data_topology_delete

    removes topology.Topology # noqa: E501


    :rtype: None
    """
    return 'do some magic!'


def data_topology_get():  # noqa: E501
    """data_topology_get

    returns topology.Topology # noqa: E501


    :rtype: TopologyTopology
    """
    return 'do some magic!'


def data_topology_link_post(body=None):  # noqa: E501
    """data_topology_link_post

    creates topology.Link # noqa: E501

    :param body: topology.Link to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyLink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_linklink_id_delete(link_id):  # noqa: E501
    """data_topology_linklink_id_delete

    removes topology.Link # noqa: E501

    :param link_id: Id of link
    :type link_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_topology_linklink_id_get(link_id):  # noqa: E501
    """data_topology_linklink_id_get

    returns topology.Link # noqa: E501

    :param link_id: Id of link
    :type link_id: str

    :rtype: TopologyLink
    """
    return 'do some magic!'


def data_topology_linklink_id_post(link_id, body=None):  # noqa: E501
    """data_topology_linklink_id_post

    creates topology.Link # noqa: E501

    :param link_id: Id of link
    :type link_id: str
    :param body: topology.Link to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyLink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_linklink_id_put(link_id, body=None):  # noqa: E501
    """data_topology_linklink_id_put

    creates or updates topology.Link # noqa: E501

    :param link_id: Id of link
    :type link_id: str
    :param body: topology.Link to be added or updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyLink.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_node_post(body=None):  # noqa: E501
    """data_topology_node_post

    creates topology.Node # noqa: E501

    :param body: topology.Node to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyNode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_nodenode_id_delete(node_id):  # noqa: E501
    """data_topology_nodenode_id_delete

    removes topology.Node # noqa: E501

    :param node_id: Id of node
    :type node_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_topology_nodenode_id_get(node_id):  # noqa: E501
    """data_topology_nodenode_id_get

    returns topology.Node # noqa: E501

    :param node_id: Id of node
    :type node_id: str

    :rtype: TopologyNode
    """
    return 'do some magic!'


def data_topology_nodenode_id_port_post(node_id, body=None):  # noqa: E501
    """data_topology_nodenode_id_port_post

    creates topology.Port # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param body: topology.Port to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyPort.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_nodenode_id_portport_id_delete(node_id, port_id):  # noqa: E501
    """data_topology_nodenode_id_portport_id_delete

    removes topology.Port # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param port_id: Id of port
    :type port_id: str

    :rtype: None
    """
    return 'do some magic!'


def data_topology_nodenode_id_portport_id_get(node_id, port_id):  # noqa: E501
    """data_topology_nodenode_id_portport_id_get

    returns topology.Port # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param port_id: Id of port
    :type port_id: str

    :rtype: TopologyPort
    """
    return 'do some magic!'


def data_topology_nodenode_id_portport_id_post(node_id, port_id, body=None):  # noqa: E501
    """data_topology_nodenode_id_portport_id_post

    creates topology.Port # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param port_id: Id of port
    :type port_id: str
    :param body: topology.Port to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyPort.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_nodenode_id_portport_id_put(node_id, port_id, body=None):  # noqa: E501
    """data_topology_nodenode_id_portport_id_put

    creates or updates topology.Port # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param port_id: Id of port
    :type port_id: str
    :param body: topology.Port to be added or updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyPort.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_nodenode_id_post(node_id, body=None):  # noqa: E501
    """data_topology_nodenode_id_post

    creates topology.Node # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param body: topology.Node to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyNode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_nodenode_id_put(node_id, body=None):  # noqa: E501
    """data_topology_nodenode_id_put

    creates or updates topology.Node # noqa: E501

    :param node_id: Id of node
    :type node_id: str
    :param body: topology.Node to be added or updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyNode.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_post(body=None):  # noqa: E501
    """data_topology_post

    creates topology.Topology # noqa: E501

    :param body: topology.Topology to be added to list
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyTopology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def data_topology_put(body=None):  # noqa: E501
    """data_topology_put

    creates or updates topology.Topology # noqa: E501

    :param body: topology.Topology to be added or updated
    :type body: dict | bytes

    :rtype: None
    """
    if connexion.request.is_json:
        body = TopologyTopology.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
