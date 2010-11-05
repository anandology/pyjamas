def init():
    eventbits[0x080000] = ("propertychange", ["propertychange"])
    _create_eventmap()
