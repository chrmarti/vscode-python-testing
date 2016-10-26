"""Hello library"""

def read_name():
    """Return a name read from stdin."""
    return input('Name: ')

def printHello(name):
    """Say hello to name on stdout.
    :param name: The name.
    """
    print('Hello {0}'.format(name))
