""" Addressing for IP protocol in network layer.
"""


def ip_string_to_ip_list(ip_string):
    """ Change raw IP address to list of each part.

    :param ip_string: String containing raw IP
    :type ip_string: str
    :return: List containing 4 int
    :rtype: list
    """
    return [int(x) for x in ip_string.split('.')]


def ip_list_to_ip_binary(ip_list):
    """ Change list of parts of an IP to binary.

    :param ip_list: List of parts of an IP
    :type ip_list: list
    :return: List of each part of an IP in binary
    :rtype: list
    """
    ip_binary = [[] for _ in range(4)]
    for i, part in enumerate(ip_list):
        ip_binary[i] = [bool(x) for x in [int(y) for y in f"{part:b}"]]
    return ip_binary
