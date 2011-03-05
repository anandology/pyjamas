from pyjamas.Timer import Timer
from pyjamas.dnd.utils import cloneElement, DOMStringList

from pyjamas.dnd import READ_ONLY, READ_WRITE, PROTECTED, DISABLED

def identity(obj):
    return obj

class DataTransferItem(object):
    """
    this is an in-browser string-kind-only implementation.
    see: http://http://dev.w3.org/html5/spec/dnd.html#datatransferitem
    """
    def __init__(self, type, data):
        self._type = type
        self._data = data

    def getType(self):
        if self.mode == DISABLED:
            return ''
        return self._type
    type = property(getType)

    def getKind(self):
        if self.mode == DISABLED:
            return ''
        return 'string'
    kind = property(getKind)

    def getMode(self):
        return self._mode
#        return DISABLED

    def setMode(self, mode):
        self._mode = mode
    mode = property(getMode, setMode)

    def getAsString(self, callback=None):
        if callback and self.kind == 'string':
            if self.mode in [READ_WRITE, READ_ONLY]:
                callback(self._data)

    def __str__(self):
        return self._data

class DataTransferItems(list):

    def getMode(self):
        return self._mode
    def setMode(self, mode):
        self._mode = mode
        for item in self:
            item.mode = mode
    mode = property(getMode, setMode)

#   ack! length is a javascript keyword! Phoo!
#    def getLength(self):
#        if self.mode == DISABLED:
#            return 0
#        return self.__len__()
#    length = property(getLength)

    def __delitem__(self, key):
        if not self.mode == READ_WRITE:
            raise Exception('Cannot delete item except in READ_WRITE mode.')
        else:
            list.__delitem__(self, key)

    def __len__(self):
        if self.mode == DISABLED:
            return 0
        return list.__len__(self)

    def clear(self):
        if self.mode == READ_WRITE:
            while len(self):
                del self[-1]

    def add(self, data, mime):
        if self.mode == READ_WRITE:
            item = DataTransferItem(mime.lower(), data)
            self.append(item)
            idx = self.index(item)
            return self[idx]



class DragDataStore(object):
    _mode = PROTECTED
    def __init__(self):
        self.items = DataTransferItems()
        self.default_feedback = None
        self.elements = []
        self.bitmap = None
        self.hotspot_coordinate = None
        self.allowed_effects_state = 'uninitialized'

    def setMode(self, mode):
        if mode in [PROTECTED, READ_WRITE, READ_ONLY]:
            self._mode = mode
            self.items.mode = mode

    def getMode(self):
        return self._mode
    mode = property(getMode, setMode)


class DataTransfer(object):
    """
    DataTransfer implementation
    http://dev.w3.org/html5/spec/dnd.html#datatransfer
    """

    def __init__(self, dataStore):
        self.dataStore = dataStore
        self.setEffectAllowed(dataStore.allowed_effects_state)
        self._dropEffect = 'none'
        self._value = None

    def acquireData(self, value):
        self._value = value

    def setDropEffect(self, effect):
        if effect in ('none', 'copy', 'link' ,'move'):
            self._dropEffect = effect

    def getDropEffect(self):
        return self._dropEffect

    dropEffect = property(getDropEffect, setDropEffect)

    def setEffectAllowed(self, effect):
        if effect in ('none', 'copy', 'copyLink', 'copyMove',
            'link', 'linkMove', 'move', 'all', 'uninitialized'):
            self._effectAllowed = effect

    def getEffectAllowed(self):
        return self._effectAllowed

    effectAllowed = property(getEffectAllowed, setEffectAllowed)

    def setData(self, format, data):
        if self.dataStore.mode == READ_WRITE:
            format = format.strip().lower()
            if format == 'text':
                format = 'text/plain'
            elif format == 'url':
                format = 'text/uri-list'
            self.clearData(format)
            items = self.dataStore.items
            z = items.add(data, format)
            z.mode = READ_WRITE

    def getTypes(self):
        theList = []
        if self.dataStore is not None:
            items = self.dataStore.items
            for item in items:
                theList.append(item.type)
        return DOMStringList(theList)

    types = property(getTypes)

    def getData(self, format):
        format = format.strip().lower()
        if format == 'text':
            format = 'text/plain'
        elif format == 'url':
            format = 'text/uri-list'
        theList = self.dataStore.items
        for item in theList:
            if item.type == format:
                item.getAsString(self.acquireData)
                return self._value
        return ''

    def clearData(self, format=None):
        thelist = self.dataStore.items
        if self.dataStore is not None:
            if format is None:
                thelist.clear()
            else:
                format = format.lower()
                to_del = []
                for idx, item in enumerate(thelist):
                    if item.type == format:
                        to_del.append(idx)
                to_del.reverse()
                for idx in to_del:
                    del thelist[idx]

    def addElement(self, element):
        self.dataStore.elements.append(cloneElement(element))

    def setDragImage(self, element, x=0, y=0):
        self.dataStore.bitmap = element
        self.dataStore.hotspot_coordinate = (x, y, )
