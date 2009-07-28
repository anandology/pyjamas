# TODO: implement safe
def quote(s, safe=''):
    """
    This function is equivalent to urllib.quote().

    Example:

    >>> quote("hey")
    'hey'
    >>> quote("$%&/?/+ s")
    '%24%25%26%2F%3F%2F%2B%20s'

    """
    JS("""return encodeURIComponent(s);""")

def urlencode(d):
    """
    Equivalent of urllib.urlencode().

    Examples:
    >>> urlencode({"a": 34, "bbb": "ccc"})
    'a=34&bbb=ccc'
    >>> urlencode({"a": 34, "bbb": "$%&/?/+ s"})
    'a=34&bbb=%24%25%26%2F%3F%2F%2B%20s'
    >>> urlencode({"a": 34})
    'a=34'
    >>> urlencode({})
    ''

    """
    s = ""
    for i, v in d.iteritems():
        s += "%s=%s&" % (i, quote(str(v)))
    if s != "":
        s = s[:-1]
    return s
