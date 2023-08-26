def handleNone(value, value_type='string'):
    """
    Return empty string instead of None or null
    """
    if value_type == 'string' or value_type == 'str':
        r = value if value is not None else ""
    elif value_type == 'array' or value_type == 'list':
        r = value if value is not None else [""]
    else:
        raise Exception("value_type must be one of the following: { string|str, array|list }")
    return r

