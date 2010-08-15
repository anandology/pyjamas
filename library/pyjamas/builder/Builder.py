from pyjamas.builder.XMLFile import XMLFile
from pyjamas import Factory
from pyjamas import ui
from pyjamas.ui.MultiListener import MultiListener

eventListeners = dict(
    onClick = ("addClickListener", "sender"),
    onDoubleClick = ("addDoubleClickListener", "sender"),
    onChange = ("addChangeListener", "sender"),
    onFocus = ("addFocusListener", "sender"),
    onLostFocus = ("addFocusListener", "sender"),
    onLoad = ("addLoadListener", "sender"),
    onError = ("addLoadListener", "sender"),
    onKeyDown = ("addKeyboardListener", "sender", "keycode", "modifiers"),
    onKeyUp = ("addKeyboardListener", "sender", "keycode", "modifiers"),
    onKeyPress = ("addKeyboardListener", "sender", "keycode", "modifiers"),
    onMouseDown = ("addMouseListener", "sender", "x", "y"),
    onMouseUp = ("addMouseListener", "sender", "x", "y"),
    onMouseMove = ("addMouseListener", "sender", "x", "y"),
    onMouseEnter = ("addMouseListener", "sender"),
    onMouseLeave = ("addMouseListener", "sender"),
    onScroll = ("addScrollListener", "sender", "row", "col"),
    onCellClicked = ("addTableListener", "sender", "row", "col"),
    onTabSelected = ("addTabListener", "sender", "tabIndex"),
    onBeforeTabSelected = ("addTabListener", "sender", "tabIndex"),
    onTreeItemSelected = ("addTreeListener", "sender"),
        )


class Builder(object):

    def __init__(self, text):
        xmlFile = XMLFile(text)
        self.properties, self.components = xmlFile.parse()

    def createInstance(self, instancename,
                             eventTarget=None, targetItem=None, index=None):

        def addItem(comp, props, childs, parentInstance, eventTarget):
            klsname = comp['name']
            kls = Factory.lookupClass("pyjamas.ui.%s" % klsname)
            args = {}
            wprops = {}
            if props.has_key("common"):
                wprops.update(props['common'])
            if props.has_key("widget"):
                wprops.update(props['widget'])
            for n in kls._getProps():
                name = n[ui.PROP_NAME]
                if not wprops.has_key(name):
                    continue
                fname = n[ui.PROP_FNAM]
                args[fname] = wprops[name]
            item = kls(**args)

            #if parentInstance is not None:
            #    context = parentInstance.getIndexedChild(comp['index'])
            #    context.add(item.componentInstance)
            for (index, child) in enumerate(childs):
                if child[0]["type"] is None:
                    continue
                childitem = addItem(child[0], child[1], child[2], item,
                                    eventTarget)
                item.addIndexedItem(child[0]["index"], childitem)
                if not "elements" in props:
                    props["elements"] = {}
                if not index in props["elements"]:
                    props["elements"][index] = {}

                elemprops = props['elements'][index]
                childitem.setElementProperties(item, elemprops)

                # add child (by name) to item
                cname = child[0]["id"] 
                setattr(item, cname, childitem)

            # make the event target the recipient of all events
            if eventTarget and props.has_key("events"):
                added_already = []
                #print props["events"]
                for listener_name, listener_fn in props["events"].items():
                    if  listener_name in added_already:
                        continue
                    args = {}
                    args[listener_name] = listener_fn
                    fname = eventListeners[listener_name][0]
                    listener = MultiListener(eventTarget, **args)
                    setattr(item, "_%sListener" % fname, listener)
                    #print "add listener", listener_name, fname
                    listen_add_fn = getattr(item, fname)
                    listen_add_fn(listener)
            return item

        for frame, props, childs in self.components:
            if frame["id"] != instancename:
                continue
            if index is not None:
                frame["index"] = index
            item = addItem(frame, props, childs, targetItem, eventTarget)
            #left = frame.get("left")
            #top = frame.get("top")
            #if left is not None and top is not None:
            #    item.applicationVO.frame.setPopupPosition(left, top)
            #if frame.get("visible", True):
            #    item.show()
            #else:
            #    item.hide()
            return item
        return None

