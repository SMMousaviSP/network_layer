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
