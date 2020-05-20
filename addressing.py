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


def ip_binary_to_ip_list(ip_binary):
    """ Change list of parts of a binary IP to integer

    :param ip_binary: List of parts of a binary IP
    :type ip_binary: list
    :return: List of parts of an IP in integer
    :rtype: list
    """
    return [binary_to_integer(x) for x in ip_binary]


def ip_list_to_ip_string(ip_list):
    """ Change list of parts of an IP to string.

    :param ip_list: List of parts of an IP
    :type ip_list: list
    :return: IP in string format
    :rtype: str
    """
    return '.'.join([str(x) for x in ip_list])


def ip_string_to_ip_binary(ip_string):
    """ Change raw IP to binary IP.

    :param ip_string: Raw IP
    :type ip_string: str
    :return: List of parts of an IP in binary
    :rtype: list
    """
    return ip_list_to_ip_binary(ip_string_to_ip_list(ip_string))


def ip_binary_to_ip_string(ip_binary):
    """ Change list of parts of a binary IP to string.

    :param ip_binary: List of parts of a binary IP
    :type ip_binary: list
    :return: IP in string format
    :rtype: str
    """
    return ip_list_to_ip_string(ip_binary_to_ip_list(ip_binary))


def host_count(ip_string):
    """ Counting available hosts by IP address.

    :param ip_string: IP address in raw string format
    :type ip_string: str
    :return: Count of available host
    :rtype: int
    """
    ip_binary = ip_string_to_ip_binary(ip_string)
    summation = 0
    for part in reversed(ip_binary):
        for bit in reversed(part):
            if not bit:
                summation += 1
            else:
                return 2 ** summation
    return 2 ** summation


def mask_ip(ip_string, mask_string):
    """ TODO

    :param ip_string: [description]
    :type ip_string: [type]
    :param mask_string: [description]
    :type mask_string: [type]
    """
    ip_binary = ip_string_to_ip_binary(ip_string)
    mask_binary = ip_string_to_ip_binary(mask_string)
    network_ip = [[[] for _ in range(8)] for _ in range(4)]
    for i in range(4):
        for j in range(8):
            network_ip[i][j] = ip_binary[i][j] and mask_binary[i][j]
    return ip_binary_to_ip_string(network_ip)


def ip_class(ip_string):
    """ TODO

    :param ip_string: [description]
    :type ip_string: [type]
    :return: [description]
    :rtype: [type]
    """
    ip_list = ip_string_to_ip_list(ip_string)
    first_byte = ip_list[0]
    if first_byte < 128:
        return 'A'
    if first_byte < 192:
        return 'B'
    if first_byte < 224:
        return 'C'
    if first_byte < 240:
        return 'D'
    return 'E'
