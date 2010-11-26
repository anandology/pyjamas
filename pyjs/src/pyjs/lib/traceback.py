import sys

def format_exception(etype, value, tb, limit=None):
    return sys._get_traceback_list(value, tb, limit=limit)
