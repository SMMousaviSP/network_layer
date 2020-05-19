""" Addressing for IP protocol in network layer.
"""


def normalize_ip_binary(ip_list):
    """ Make each part of binary IP 8 bit.

    :param ip_list: List of parts of an IP in binary
    :type ip_list: list
    :return: List of parts of an IP in binary, which each part is exactly 8 bit
    :rtype: list
    """
    for i, part in enumerate(ip_list):
        remaining_zero = 8 - len(part)
        if remaining_zero > 0:
            for _ in range(remaining_zero):
                ip_list[i].insert(0, False)
    return ip_list


def binary_to_integer(binary_list):
    """ Change binary to integer.

    :param binary_list: List of several bits
    :type binary_list: list
    :return: int
    :rtype: Decimal number of binary list
    """
    summation = 0
    base = len(binary_list) - 1
    for i, bit in enumerate(binary_list):
        if not bit:
            continue
        summation += 2 ** (base - i)
    return summation


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
    return normalize_ip_binary(ip_binary)
