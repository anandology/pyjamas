def init():
    eventbits[0x040000] = ("mousewheel", ["DOMMouseScroll"])
    _create_eventmap()
