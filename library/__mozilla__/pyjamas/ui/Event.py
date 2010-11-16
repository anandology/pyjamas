def init():
    eventbits[0x040000] = ("DOMMouseScroll", [])
    eventbits[0x080000] = ("input", [])
    _create_eventmap()
