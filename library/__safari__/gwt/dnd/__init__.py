
def makeDraggable(widget):
    element = widget.getElement()
    DOM.setAttribute(element, 'draggable', True)
    # the following are needed for older versions of webkit/safari
    widget.setStyleAttribute('-webkit-user-drag', 'element')
    widget.setStyleAttribute('-webkit-user-select', 'none')
