from pyjamas import log

import browser
import gdk
#import lxml.etree

# WINDOW TYPES
WINDOW_TOPLEVEL = 1

# GTK OPTIONS (flags)
EXPAND = 1
FILL = 2

# GTK WIDGET FALGS
TOPLEVEL = 1
NO_WINDOW = 2
REALIZED = 4
MAPPED = 8
VISIBLE = 16
SENSITIVE = 32
PARENT_SENSITIVE = 64
CAN_FOCUS = 128
HAS_FOCUS = 256
CAN_DEFAULT = 512
HAS_DEFAULT = 1024
HAS_GRAB = 2048
RC_STYLE = 4096
COMPOSITE_CHILD	 = 8192
NO_REPARENT = 16384
APP_PAINTABLE = 32768
RECEIVES_DEFAULT = 65536
DOUBLE_BUFFERED = 131072

# GTK Update Type Constants
UPDATE_CONTINUOUS = 1
UPDATE_DISCONTINUOUS = 2
UPDATE_DELAYED = 4

# GTK Position Type Constants
POS_LEFT = 1
POS_RIGHT = 2
POS_TOP = 4
POS_BOTTOM = 8

class GObject:
    def __init__(self):
        self.callbacks = {}
        self.connections = 0

    def connect(self, detailed_signal, handler, data=None):
        detailed_signal = detailed_signal.replace('_', '-')
        l = self.callbacks.setdefault(detailed_signal,[])
        l.append((handler, data))
        self.connections += 1
        return self.connections

    def connect_object(self, detailed_signal, handler, gobject, data=None):
        detailed_signal = detailed_signal.replace('_', '-')
        def inner(widget, data):
            handler(widget, data)
        self.connect(detailed_signal, inner, data)

    def emit(self, detailed_signal, *args):
        detailed_signal = detailed_signal.replace('_', '-')
        if self.callbacks.has_key(detailed_signal):
            for pair in self.callbacks[detailed_signal]:
                pair[0](self,pair[1])

    def dom_event(self, event, element):
        pass

class Object(GObject):
    def __init__(self):
        GObject.__init__(self)
        self.flags = 0

    def set_flags(self, flags):
        self.flags = flags

class Widget(Object):
    def __init__(self):
        Object.__init__(self)
        self._visible = False
        self.widget_cont = browser.Element('div')
        self.widget_cont.setStyle('visibility', 'hidden')
        self.widget_cont.setStyle('position', 'absolute')
        self.widget_cont.setStyle('overflow', 'hidden')
        self.minheight = 1
        self.minwidth = 1
        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')
        self.margin = 0
        self.widget_cont.setStyle('margin', str(self.margin) + 'px')
        self._parent = None

    def get_allocation(self):
        x = self.widget_cont.getX()
        y = self.widget_cont.getY()
        w = self.widget_cont.getWidth()
        h = self.widget_cont.getHeight()
        return gdk.Rectangle(x,y,w,h)

    def show(self):
        self._visible = True
        self.widget_cont.setStyle('visibility', 'visible')
        self._redraw()

    def hide(self):
        self._visible = False
        self.widget_cont.setStyle('visibility', 'hidden')

    def show_all(self):
        self.show()

    def hide_all(self):
        self.hide()

    def destroy(self):
        self.emit('destroy')

    def grab_default(self):
        pass #TODO

    def set_size_request(self, width, height):
        pass

    def _redraw(self):
        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')
        self.widget_cont.setStyle('margin', str(self.margin) + 'px')

class Entry(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.widget_int = browser.Document.createElement('input')
        self.widget_cont.append(self.widget_int)

class Container(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.childs = []
        self.widget_int = browser.Document.createElement('div')
        self.widget_int.setStyle('position', 'absolute')
        self.widget_cont.append(self.widget_int)

    def add(self, child):
        if self._visible: child.show()
        child._parent = self
        self.childs.append(child)
        self.widget_int.append(child.widget_cont)
        self.minwidth += child.minwidth
        self.minheight += child.minheight

    def set_border_width(self, border_width):
        self.margin = border_width
        self._redraw()

    def get_border_width(self):
        return self.margin

    def _redraw(self):
        Widget._redraw(self)
        self.widget_int.setStyle('width', self.widget_cont.getWidth() + 'px')
        self.widget_int.setStyle('height', self.widget_cont.getHeight() + 'px')
        self.minwidth = 2 * self.margin
        self.minheight = 2 * self.margin
        for child in self.childs:
            child._redraw()
        if len(self.childs) == 1:
            self.minwidth += self.childs[0].minwidth
            self.minheight += self.childs[0].minheight
        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')

    def show_all(self):
        for child in self.childs:
            child.show_all()
        Widget.show_all(self)

    def hide_all(self):
        for child in self.childs:
            child.hide_all()
        Widget.hide_all(self)

    def child_set_property(self, child, prop, value):
        setattr(child, prop, value)

class Bin(Container):
    def __init__(self):
        Container.__init__(self)

    def get_child(self):
        if len(self.childs)>0:
            return self.childs[0]
        else:
            return None

    def add(self, child):
        if len(self.childs)>0:
            pass #TODO: GtkWarning !!!
        Container.add(self, child)

class Table(Container):
    def __init__(self, rows=1, columns=1, homogeneous=False):
        Container.__init__(self)
        self.rows = rows
        self.columns = columns
        self.vert_inc = 100.0/rows
        self.horitz_inc = 100.0/columns

    def attach(self, child, left_attach, right_attach,
               top_attach, bottom_attach, xoptions=None,
               yoptions=None, xpadding=0, ypadding=0):

        global EXPAND
        global FILL

        if xoptions is None:
            xoptions = EXPAND|FILL
        if yoptions is None:
            yoptions = EXPAND|FILL

        Container.add(self, child)
        child.widget_cont.setStyle('left',str(left_attach*self.horitz_inc)+'%')
        child.widget_cont.setStyle('right',str(100-(right_attach*self.horitz_inc))+'%')
        child.widget_cont.setStyle('top',str(top_attach*self.vert_inc)+'%')
        child.widget_cont.setStyle('bottom',str(100-(bottom_attach*self.vert_inc))+'%')


class Box(Container):
    def __init__(self):
        Container.__init__(self)

    def _add_element(self, element):
        Container.add(self, element)

    def pack_start(self, child, expand=True, fill=True, padding=0):
        child.expand = expand
        child.fill = fill
        child.padding = padding
        self._add_element(child)

    def add(self, child):
        child.expand = True
        child.fill = True
        child.padding = 0
        self._add_element(child)

class HBox(Box):
    def __init__(self, homogeneous=False, spacing=0):
        Box.__init__(self)
        self.homogeneous = homogeneous
        self.spacing = spacing

    def _add_element(self, element):
        Box._add_element(self, element)
        element.widget_cont.setStyle('height',
                str(self.widget_cont.getHeight() - 2 * self.margin) + 'px')
        self._redraw()

    def _redraw(self):
        Box._redraw(self)
        count = 0
        fix_width = 0
        if not self.homogeneous:
            for child in self.childs:
                if child.expand:
                    count += 1
                else:
                    fix_width += child.minwidth + self.spacing + child.padding + 2 * child.margin
        else:
            count = len(self.childs)
        horitz_inc = (self.widget_cont.getWidth() - 2 * self.margin - fix_width) / count
        left = self.margin
        for child in self.childs:
            if len(self.childs) != 1:
                if child.minheight + 2 * self.margin > self.minheight:
                    self.minheight = child.minheight + 2 * self.margin
                self.minwidth += child.minwidth + 2 * child.margin + self.spacing + child.padding
        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')

        for child in self.childs:
            child.widget_cont.setStyle('height',
                    str(self.widget_cont.getHeight() - 2 * self.margin) + 'px')
            child.widget_cont.setStyle('left',
                    str(left + self.spacing / 2 + child.padding / 2) + 'px')
            if child.expand:
                left += horitz_inc
            else:
                left += child.minwidth + 2 * child.margin + self.spacing + child.padding

            right = self.widget_cont.getWidth() - self.margin - left
            if right < self.margin:
                right = self.margin
            child.widget_cont.setStyle('right',
                    str(right + self.spacing / 2 + child.padding / 2) + 'px')
            child._redraw()

class VBox(Box):
    def __init__(self, homogeneous=False, spacing=0):
        Box.__init__(self)
        self.homogeneous = homogeneous
        self.spacing = spacing

    def _add_element(self, element):
        Box._add_element(self, element)
        element.widget_cont.setStyle('width',
                str(self.widget_cont.getWidth() - 2 * self.margin) + 'px')
        self._redraw()

    def _redraw(self):
        Box._redraw(self)
        count = 0
        fix_height = 0
        if not self.homogeneous:
            for child in self.childs:
                if child.expand:
                    count += 1
                else:
                    fix_height += child.minheight + self.spacing + child.padding + 2 * child.margin
        else:
            count = len(self.childs)
        vert_inc = (self.widget_cont.getHeight() - 2 * self.margin - fix_height) / count
        top = self.margin
        for child in self.childs:
            if len(self.childs) != 1:
                if child.minwidth + 2 * self.margin > self.minwidth:
                    self.minwidth = child.minwidth + 2 * self.margin
                self.minheight += child.minheight + 2 * child.margin + self.spacing + child.padding

        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')

        for child in self.childs:
            child.widget_cont.setStyle('width',
                    str(self.widget_cont.getWidth() - 2 * self.margin) + 'px')
            child.widget_cont.setStyle('top',
                    str(top + self.spacing / 2 + child.padding / 2) + 'px')
            if child.expand:
                top += vert_inc
            else:
                top += child.minheight + 2 * child.margin + self.spacing + child.padding

            bottom = self.widget_cont.getHeight() - self.margin - top
            if bottom < self.margin:
                bottom = self.margin
            child.widget_cont.setStyle('bottom',
                    str(bottom + self.spacing / 2 + child.padding / 2) + 'px')
            child._redraw()

class Window(Bin):
    def __init__(self, type=WINDOW_TOPLEVEL):
        global WINDOW_TOPLEVEL
        Bin.__init__(self)
        browser.Document.window.catchEvents(['resize'], self)

        self.type = type
        self.title = ''
        self.child = None
        self.widget_cont.setStyle('top', '0px')
        self.widget_cont.setStyle('bottom', '0px')
        self.widget_cont.setStyle('right', '0px')
        self.widget_cont.setStyle('left', '0px')
        if self.type == WINDOW_TOPLEVEL:
            browser.Document.append(self.widget_cont)
        else:
            pass #TODO: Create pop-up

    def add(self, child):
        Bin.add(self, child)
        child.widget_cont.setStyle('width', self.widget_cont.getWidth() + 'px')
        child.widget_cont.setStyle('height', self.widget_cont.getHeight() + 'px')
        self.child = child

    def set_title(self, title):
        global WINDOW_TOPLEVEL
        self.title = title
        if self.type == WINDOW_TOPLEVEL:
            browser.Document.setTitle(title)
        else:
            pass #TODO

    def show(self):
        self._redraw()
        Bin.show(self)

    def _redraw(self):
        if self.child:
            self.child.widget_cont.setStyle('width',
                    self.widget_cont.getWidth() + 'px')
            self.child.widget_cont.setStyle('height',
                    self.widget_cont.getHeight() + 'px')
        Bin._redraw(self)

    def dom_event(self, event, element):
        if event.type in ['resize']:
            self._redraw()

class Button(Bin):
    def __init__(self, label=None):
        Bin.__init__(self)
        self.widget_cont.catchEvents(['click'], self)
        self.child = None
        if label != None:
            self.add(Label(label))

        self.widget_int.setStyle('textAlign','center')
        self.widget_int.setProperty('className','button')
        self.minheight = 25
        self.minwidth = 20

    def add(self, child):
        Bin.add(self, child)
        self.child = child
        self._redraw()

    def _redraw(self):
        Bin._redraw(self)
        self.minheight += self.child.minheight
        self.minwidth += self.child.minwidth
        width = self.widget_cont.getWidth()
        if width - 2 < self.minwidth:
            width = self.minwidth + 2
        height = self.widget_cont.getHeight()
        if height - 2 < self.minheight:
            height = self.minheight + 2
        self.widget_int.setStyle('width', width - 2 + 'px')
        self.widget_int.setStyle('height', height - 2 + 'px')
        self.child.widget_cont.setStyle('width', width + 'px')
        self.child.widget_cont.setStyle('height', height + 'px')
        self.child._redraw()

    def dom_event(self, event, element):
        if event.type == 'click':
            self.emit('clicked')

class ToggleButton(Button):
    def __init__(self, label=None):
        Button.__init__(self, label)
        self.connect("toggled", self.toggled)
        self.istoggled = False
        self.widget_int.setProperty('className','togglebutton')

    def toggled(self, widget, event, data=None):
        self.istoggled = not self.istoggled
        if self.istoggled:
            self.widget_int.setProperty('className','togglebutton-toggled')
        else:
            self.widget_int.setProperty('className','togglebutton')

    def set_active(self, is_active):
        if is_active and not self.istoggled:
            self.emit('toggled')
        elif not is_active and self.istoggled:
            self.emit('toggled')

    def get_active(self):
        return self.istoggled

    def dom_event(self, event, element):
        if event.type == 'click':
            self.emit('toggled')

class CheckButton(ToggleButton):
    def __init__(self, label=None):
        ToggleButton.__init__(self)
        self.check = browser.Element('input')
        self.check.setStyle('position', 'absolute')
        self.check.setStyle('width','auto')
        self.check.setStyle('height','auto')
        self.check.setStyle('left', '0px')
        self.check.setProperty('type','checkbox')
        self.check_widget = Widget()
        self.check_widget.widget_cont.append(self.check)
        self.check_widget.show()

        self.box = HBox(spacing=6)
        self.box.show()
        self.box.pack_start(self.check_widget, False)
        self.add(self.box)

        if label!=None:
            self.label = Label(label)
            self.box.pack_start(self.label, False)
        self.widget_int.setProperty('className','checkbutton')

    def add(self, child):
        #TODO Check that no more than one widget is added.
        ToggleButton.add(self, child)

    def toggled(self, widget, event, data=None):
        self.istoggled = not self.istoggled
        if self.istoggled:
            self.check.setProperty('checked',True)
        else:
            self.check.setProperty('checked',False)

    def _redraw(self):
        ToggleButton._redraw(self)
        self.check.setStyle('top',
                self.check_widget.widget_cont.getHeight() / 2 - self.check.getHeight() / 2 - 2.5 + 'px')
        self.check_widget.minwidth = self.check.getWidth() + 2
        self.check_widget.minheight = self.check.getHeight() + 2
        self.check_widget._redraw()

class RadioButton(CheckButton):
    counter = 0
    groups = {}
    running = False

    def __init__(self, group=None, label=None):
        CheckButton.__init__(self, label)
        self.check.setProperty('type','radio')
        if group==None:
            self.group = RadioButton.counter
            RadioButton.counter += 1
            RadioButton.groups[self.group] = [self]
        else:
            self.group = group.group
            RadioButton.groups[self.group].append(self)

    def toggled(self, widget, event, data=None):
        if RadioButton.running:
            return
        RadioButton.running = True
        for b in RadioButton.groups[self.group]:
            if b.istoggled:
                b.check.setProperty('checked',False)
                b.istoggled = False
                b.emit('toggled')
        self.check.setProperty('checked',True)
        self.istoggled = True
        RadioButton.running = False

class Misc(Widget):

    def __init__(self):
        Widget.__init__(self)
        self.xalign = 0.5
        self.yalign = 0.5

    def set_alignment(self, xalign, yalign):
        self.xalign = xalign
        self.yalign = yalign

    def get_alignment(self):
        return (self.xalign, self.yalign)

class Image(Misc):
    def __init__(self):
        Misc.__init__(self)
        self.img = browser.Element('img')
        self.img.setStyle('position','absolute')
        self.img.setStyle('width','auto')
        self.img.setStyle('height','auto')
        self.widget_cont.append(self.img)
        self.widget_cont.setProperty('className','image')

    def set_from_file(self, filename):
        self.img.setProperty('src', filename)

    def _redraw(self):
        Misc._redraw(self)
        self.img.setStyle('top', str((self.widget_cont.getHeight() - self.img.getHeight()) * self.yalign)  + 'px')
        self.img.setStyle('left', str((self.widget_cont.getWidth() - self.img.getWidth()) * self.xalign) + 'px')
        self.minwidth = self.img.getWidth()
        self.minheight = self.img.getHeight()

class Label(Misc):

    def __init__(self, str=None):
        Misc.__init__(self)

        self.label = browser.Element('div')
        self.label.setStyle('position','absolute')
        self.label.setStyle('width','auto')
        self.label.setStyle('height','auto')
        self.label.setStyle('whiteSpace', 'nowrap')
        self.label.setHTML(str)

        self.widget_cont.append(self.label)
        self.widget_cont.setStyle('visibility','visible')
        self.widget_cont.setProperty('className','label')

    def set_text(self, str):
        self.label.setHTML(str)

    def get_text(self):
        return self.label.getHTML()

    def _redraw(self):
        Misc._redraw(self)
        self.label.setStyle('top', str((self.widget_cont.getHeight() - self.label.getHeight()) * self.yalign)  + 'px')
        self.label.setStyle('left', str((self.widget_cont.getWidth() - self.label.getWidth()) * self.xalign) + 'px')
        self.minwidth = self.label.getWidth()
        self.minheight = self.label.getHeight()

class Separator(Widget):
    def __init__(self):
        Widget.__init__(self)

class HSeparator(Separator):
    def __init__(self):
        Separator.__init__(self)
        self.separator = browser.Element('hr')
        self.widget_cont.append(self.separator)
        self.widget_cont.setProperty('className','hseparator')
        self.minheight = 10

class Adjustment(Object):

    def __init__(self, value=0, lower=0, upper=0, step_incr=0, page_incr=0,
            page_size=0):
        Object.__init__(self)
        self.value = value
        self.lower = lower
        self.upper = upper
        self.step_incr = step_incr
        self.page_incr = page_incr
        self.page_size = page_size

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value
        if self.value < self.lower:
            self.value = self.lower
        if self.value > self.upper:
            self.value = self.upper
        self.emit('value-changed')

    def changed(self):
        self.emit('changed')


class Range(Widget):

    def __init__(self, adjustment=None):
        Widget.__init__(self)
        self.value = browser.Element('div')
        self.value.setStyle('position', 'absolute')
        self.widget_cont.append(self.value)
        if adjustment!=None:
            self.adjustment = adjustment
        else:
            self.adjustment = Adjustment()
        self.adjustment.connect('value-changed', self._adjustment_value_changed)
        self.adjustment.connect('changed', self._adjustment_changed)
        self.value.setHTML(str(self.adjustment.get_value()))

    def set_update_policy(self, policy):
        pass

    def _adjustment_value_changed(self):
        self.value.setHTML(str(self.adjustment.get_value()))

    def _adjustment_changed(self):
        self._redraw()

class Scale(Range):

    def __init__(self, adjustment=None):
        global POS_TOP
        Range.__init__(self, adjustment)
        self.line = browser.Element('div')
        self.line.setStyle('position','absolute')
        self.line.setProperty('className', 'scale')
        self.line.catchEvents(['click'], self)
        self.cursor = browser.Element('div')
        self.cursor.setStyle('position', 'absolute')
        self.cursor.setProperty('className', 'scale-cursor')
        self.widget_cont.append(self.line)
        self.mouseover = False
        self.value_pos = POS_TOP
        self.draw_value = True
        self.digits = 1
        self.cursor.catchEvents(['mousedown'], self)
        browser.Document.document.catchEvents(['mousemove'], self)
        browser.Document.document.catchEvents(['mouseup'], self)

    def set_digits(self, digits):
        self.digits = digits
        self._redraw()

    def set_draw_value(self, draw_value):
        self.draw_value = draw_value
        self._redraw()

    def get_draw_value(self):
        return self.draw_value

    def set_value_pos(self, pos):
        self.value_pos = pos
        self._redraw()

    def get_value_pos(self):
        return self.value_pos

    def _adjustment_value_changed(self):
        value = self.adjustment.get_value()
        JS('''
        value = value.toFixed(self.digits);
        ''')
        self.value.setHTML(str(value))

    def _move_cursor(self, event):
        pass

    def dom_event(self, event, element):
        if event.type == 'mousedown':
            self.mouseover = True
        elif event.type == 'mousemove' and self.mouseover:
            self._move_cursor(event)
        elif event.type == 'click':
            self._move_cursor(event)
        elif event.type == 'mouseup':
            self.mouseover = False

class VScale(Scale):
    def __init__(self, adjustment=None):
        Scale.__init__(self, adjustment)
        self.line.setStyle('width','15px')
        self.cursor.setStyle('height', '30px')
        self.cursor.setStyle('width', '13px')
        self.line.append(self.cursor)
        self.minwidth = 30
        self.minheight = 60

    def _redraw(self):
        global POS_TOP
        global POS_LEFT
        global POS_RIGHT
        Scale._redraw(self)
        if not self.draw_value:
            self.line.setStyle('left',
                    str((self.widget_cont.getWidth() - self.line.getWidth()) / 2) + 'px')
            self.line.setStyle('top', '0px')
            self.line.setStyle('height', str(self.widget_cont.getHeight() - 2) + 'px')
            self.value.setStyle('visibility', 'hidden')
        else:
            self.value.setStyle('visibility', 'visible')
            if self.value_pos == POS_TOP:
                self.value.setStyle('left',
                        str((self.widget_cont.getWidth() - self.value.getWidth()) / 2) + 'px')
                self.value.setStyle('top', '0px')
                self.line.setStyle('left',
                        str((self.widget_cont.getWidth() - self.line.getWidth()) / 2) + 'px')
                self.line.setStyle('top', str(self.value.getHeight() + 2) + 'px')
                self.line.setStyle('height',
                        str(self.widget_cont.getHeight() - self.value.getHeight() - 4) + 'px')
            elif self.value_pos == POS_LEFT:
                self.value.setStyle('left',
                        str((self.widget_cont.getWidth() / 2) - ((self.value.getWidth() + self.line.getWidth()) / 2)) + 'px')
                self.line.setStyle('left',
                        str((self.widget_cont.getWidth() / 2) + ((self.value.getWidth() + self.line.getWidth()) / 2)) + 'px')
                self.line.setStyle('top', '0px')
                self.line.setStyle('height', str(self.widget_cont.getHeight() - 2) + 'px')
            elif self.value_pos == POS_RIGHT:
                self.value.setStyle('left',
                        str((self.widget_cont.getWidth() / 2) + ((self.value.getWidth() + self.line.getWidth()) / 2)) + 'px')
                self.line.setStyle('left',
                        str((self.widget_cont.getWidth() / 2) - ((self.value.getWidth() + self.line.getWidth()) / 2)) + 'px')
                self.line.setStyle('top', '0px')
                self.line.setStyle('height', str(self.widget_cont.getHeight() - 2) + 'px')
            else:
                self.value.setStyle('left',
                        str((self.widget_cont.getWidth() - self.value.getWidth()) / 2) + 'px')
                self.value.setStyle('top',
                        str((self.widget_cont.getHeight() - self.value.getHeight())) + 'px')
                self.line.setStyle('left',
                        str((self.widget_cont.getWidth() - self.line.getWidth()) / 2) + 'px')
                self.line.setStyle('top', '0px')
                self.line.setStyle('height',
                        str(self.widget_cont.getHeight() - self.value.getHeight() - 4) + 'px')
        self._adjustment_value_changed()

    def _move_cursor(self, event):
        Scale._move_cursor(self, event)
        y = event.clientY - self.line.getY() - self.cursor.getHeight() / 2
        if y < 0:
            y = 0
        if y > self.line.getHeight() - self.cursor.getHeight() - 2:
            y = self.line.getHeight() - self.cursor.getHeight() - 2

        value = (y / (self.line.getHeight() - self.cursor.getHeight() - 2)) \
                * (self.adjustment.upper - self.adjustment.page_size)
        if self.draw_value:
            value = round(value, self.digits)
        if event.type == 'click':
            old_value = self.adjustment.get_value()
            incr = self.adjustment.page_incr
            if value > old_value:
                self.adjustment.set_value(old_value + incr)
            elif value < old_value:
                self.adjustment.set_value(old_value - incr)
        else:
            self.adjustment.set_value(value)

    def _adjustment_value_changed(self):
        global POS_LEFT
        global POS_RIGHT
        Scale._adjustment_value_changed(self)
        value = self.adjustment.get_value()
        if self.draw_value:
            value = round(value, self.digits)
        y = (value - self.adjustment.lower) / \
                (self.adjustment.upper - self.adjustment.page_size) \
                * (self.line.getHeight() - self.cursor.getHeight() - 2)
        self.cursor.setStyle('top', str(y) + 'px')
        if self.value_pos in (POS_LEFT, POS_RIGHT):
            pos = y - self.value.getHeight() / 2 + self.cursor.getHeight() / 2
            self.value.setStyle('top', str(pos) + 'px')

class HScale(Scale):
    def __init__(self, adjustment=None):
        Scale.__init__(self, adjustment)
        self.line.setStyle('height','15px')
        self.cursor.setStyle('height', '13px')
        self.cursor.setStyle('width', '30px')
        self.line.append(self.cursor)
        self.minwidth = 60
        self.minheight = 37

    def _redraw(self):
        global POS_TOP
        global POS_LEFT
        global POS_RIGHT
        Scale._redraw(self)
        if not self.draw_value:
            self.line.setStyle('top',
                    str((self.widget_cont.getHeight() - self.line.getHeight()) / 2) + 'px')
            self.line.setStyle('width', str(self.widget_cont.getWidth() - 2) + 'px')
            self.value.setStyle('visibility', 'hidden')
        else:
            self.value.setStyle('visibility', 'visible')
            if self.value_pos == POS_TOP:
                self.value.setStyle('top',
                        str((self.widget_cont.getHeight() / 2) - (self.line.getHeight() + self.value.getHeight() + 2) / 2) + 'px')
                self.line.setStyle('left', '0px')
                self.line.setStyle('top',
                        str((self.widget_cont.getHeight() / 2) + self.line.getHeight() / 2 - self.value.getHeight() / 2 + 1) + 'px')
                self.line.setStyle('width',
                        str(self.widget_cont.getWidth() - 2) + 'px')
            elif self.value_pos == POS_LEFT:
                self.value.setStyle('left', '0px')
                self.value.setStyle('top',
                        str((self.widget_cont.getHeight() - self.value.getHeight()) / 2) + 'px')
                self.line.setStyle('left', str(self.value.getWidth() + 2) + 'px')
                self.line.setStyle('top',
                        str((self.widget_cont.getHeight() - self.line.getHeight()) / 2) + 'px')
                self.line.setStyle('width',
                        str((self.widget_cont.getWidth() - (self.value.getWidth() + 2) - 2)) + 'px')
            elif self.value_pos == POS_RIGHT:
                self.value.setStyle('left',
                        str(self.widget_cont.getWidth() - self.value.getWidth()) + 'px')
                self.value.setStyle('top',
                        str((self.widget_cont.getHeight() - self.value.getHeight()) / 2) + 'px')
                self.line.setStyle('left', '0px')
                self.line.setStyle('top',
                        str((self.widget_cont.getHeight() - self.line.getHeight()) / 2) + 'px')
                self.line.setStyle('width',
                        str((self.widget_cont.getWidth() - (self.value.getWidth() + 2) - 2)) + 'px')
            else:
                self.value.setStyle('top',
                        str((self.widget_cont.getHeight() / 2) + self.line.getHeight() / 2 - self.value.getHeight() / 2 + 1) + 'px')
                self.line.setStyle('left', '0px')
                self.line.setStyle('top',
                        str((self.widget_cont.getHeight() / 2) - (self.line.getHeight() + self.value.getHeight() + 2) / 2) + 'px')
                self.line.setStyle('width',
                        str(self.widget_cont.getWidth() - 2) + 'px')
        self._adjustment_value_changed()

    def _move_cursor(self, event):
        Scale._move_cursor(self, event)
        x = event.clientX - self.line.getX() - self.cursor.getWidth() / 2

        if x < 0:
            x = 0
        if x > self.line.getWidth() - self.cursor.getWidth() - 2:
            x = self.line.getWidth() - self.cursor.getWidth() - 2

        value = (x / (self.line.getWidth() - self.cursor.getWidth() - 2)) \
                * (self.adjustment.upper - self.adjustment.page_size)
        if self.draw_value:
            value = round(value, self.digits)
        if event.type == 'click':
            old_value = self.adjustment.get_value()
            incr = self.adjustment.page_incr
            if value > old_value:
                self.adjustment.set_value(old_value + incr)
            elif value < old_value:
                self.adjustment.set_value(old_value - incr)
        else:
            self.adjustment.set_value(value)

    def _adjustment_value_changed(self):
        global POS_TOP
        global POS_BOTTOM
        Scale._adjustment_value_changed(self)
        value = self.adjustment.get_value()
        if self.draw_value:
            value = round(value, self.digits)
        x = (value - self.adjustment.lower) / \
                (self.adjustment.upper - self.adjustment.page_size) \
                * (self.line.getWidth() - self.cursor.getWidth() - 2)
        self.cursor.setStyle('left', str(x) + 'px')
        if self.value_pos in (POS_TOP, POS_BOTTOM):
            pos = x - self.value.getWidth() / 2 + self.cursor.getWidth() / 2
            if pos < 0:
                pos = 0
            elif pos > self.line.getWidth() - self.value.getWidth():
                pos = self.line.getWidth() - self.value.getWidth()
            self.value.setStyle('left', str(pos) + 'px')


class Scrollbar(Range):

    def __init__(self, adjustment=None):
        Range.__init__(self, adjustment)
        self.down_arrow = browser.Element('div')
        self.down_arrow.setStyle('position', 'absolute')
        self.down_arrow.setStyle('height', '15px')
        self.down_arrow.setStyle('width', '15px')
        self.down_arrow.catchEvents(['click'], self)
        self.up_arrow = browser.Element('div')
        self.up_arrow.setStyle('position', 'absolute')
        self.up_arrow.setStyle('height', '15px')
        self.up_arrow.setStyle('width', '15px')
        self.up_arrow.catchEvents(['click'], self)
        self.line = browser.Element('div')
        self.line.setStyle('position', 'absolute')
        self.line.setProperty('className', 'scrollbar')
        self.line.catchEvents(['click'], self)
        self.cursor = browser.Element('div')
        self.cursor.setStyle('position', 'absolute')
        self.cursor.setProperty('className', 'scrollbar-cursor')
        self.widget_cont.append(self.down_arrow)
        self.widget_cont.append(self.line)
        self.widget_cont.append(self.up_arrow)
        self.mouseover = False
        self.cursor.catchEvents(['mousedown'], self)
        self.value.setStyle('visibility', 'hidden')
        browser.Document.document.catchEvents(['mousemove'], self)
        browser.Document.document.catchEvents(['mouseup'], self)

    def _adjustment_value_changed(self):
        pass

    def _move_cursor(self, event):
        pass

    def dom_event(self, event, element):
        if event.type == 'mousedown':
            self.mouseover = True
        elif event.type == 'mousemove' and self.mouseover:
            self._move_cursor(event)
        elif event.type == 'click':
            self._move_cursor(event)
        elif event.type == 'mouseup':
            self.mouseover = False


class HScrollbar(Scrollbar):

    def __init__(self, adjustment=None):
        Scrollbar.__init__(self, adjustment)
        self.down_arrow.setProperty('className', 'scrollbar-left-arrow')
        self.up_arrow.setProperty('className', 'scrollbar-right-arrow')
        self.line.setStyle('height', '15px')
        self.cursor.setStyle('height', '13px')
        self.line.append(self.cursor)
        self.minwidth = 60
        self.minheight = 37

    def _redraw(self):
        Scrollbar._redraw(self)
        top = (self.widget_cont.getHeight() - self.line.getHeight()) / 2
        self.down_arrow.setStyle('top', str(top) + 'px')
        self.down_arrow.setStyle('left', '0px')
        self.line.setStyle('top', str(top) + 'px')
        self.line.setStyle('left', str(self.down_arrow.getWidth()) + 'px')
        self.line.setStyle('width', str(self.widget_cont.getWidth() - 2 - self.down_arrow.getWidth() - self.up_arrow.getWidth()) + 'px')
        self.up_arrow.setStyle('top', str(top) + 'px')
        self.up_arrow.setStyle('left', str(self.down_arrow.getWidth() + self.line.getWidth()) + 'px')

        cursor_size = (self.widget_cont.getWidth() - 2) * self.adjustment.page_size / 100.0
        if cursor_size < 30:
            cursor_size = 30
        self.cursor.setStyle('width', str(cursor_size) + 'px')
        self._adjustment_value_changed()

    def _move_cursor(self, event):
        Scrollbar._move_cursor(self, event)
        pos = event.clientX - self.line.getX()

        x = pos - self.cursor.getWidth() / 2
        if x < 0:
            x = 0
        if x > self.line.getWidth() - self.cursor.getWidth() - 2:
            x = self.line.getWidth() - self.cursor.getWidth() - 2

        value = (x / (self.line.getWidth() - self.cursor.getWidth() - 2)) \
                * (self.adjustment.upper - self.adjustment.page_size)
        if event.type == 'click':
            old_value = self.adjustment.get_value()
            if pos < 0:
                incr = self.adjustment.step_incr
                self.adjustment.set_value(old_value - incr)
            elif pos > self.line.getWidth():
                incr = self.adjustment.step_incr
                self.adjustment.set_value(old_value + incr)
            else:
                incr = self.adjustment.page_incr
                if value > old_value:
                    self.adjustment.set_value(old_value + incr)
                elif value < old_value:
                    self.adjustment.set_value(old_value - incr)
        else:
            self.adjustment.set_value(value)

    def _adjustment_value_changed(self):
        Scrollbar._adjustment_value_changed(self)
        value = self.adjustment.get_value()
        x = (value - self.adjustment.lower) / \
                (self.adjustment.upper - self.adjustment.page_size) \
                * (self.line.getWidth() - self.cursor.getWidth() - 2)
        self.cursor.setStyle('left', str(x) + 'px')


class VScrollbar(Scrollbar):

    def __init__(self, adjustment=None):
        Scrollbar.__init__(self, adjustment)
        self.down_arrow.setProperty('className', 'scrollbar-down-arrow')
        self.up_arrow.setProperty('className', 'scrollbar-up-arrow')
        self.line.setStyle('width', '15px')
        self.cursor.setStyle('width', '13px')
        self.line.append(self.cursor)
        self.minwidth = 30
        self.minheight = 90

    def _redraw(self):
        Scrollbar._redraw(self)
        left = (self.widget_cont.getWidth() - self.line.getWidth()) / 2
        self.up_arrow.setStyle('left', str(left) + 'px')
        self.up_arrow.setStyle('top', '0px')
        self.line.setStyle('top', str(self.up_arrow.getHeight()) + 'px')
        self.line.setStyle('left', str(left) + 'px')
        self.line.setStyle('height', str(self.widget_cont.getHeight() - 2 - self.up_arrow.getHeight() - self.down_arrow.getHeight()) + 'px')
        self.down_arrow.setStyle('top', str(self.up_arrow.getHeight() + self.line.getHeight()) + 'px')
        self.down_arrow.setStyle('left', str(left) + 'px')

        cursor_size = (self.widget_cont.getHeight() - 2) * self.adjustment.page_size / 100.0
        if cursor_size < 30:
            cursor_size = 30
        self.cursor.setStyle('height', str(cursor_size) + 'px')
        self._adjustment_value_changed()

    def _move_cursor(self, event):
        Scrollbar._move_cursor(self, event)
        pos = event.clientY - self.line.getY()

        y = pos - self.cursor.getHeight() / 2
        if y < 0:
            y = 0
        if y > self.line.getHeight() - self.cursor.getHeight() - 2:
            y = self.line.getHeight() - self.cursor.getHeight() - 2

        value = (y / (self.line.getHeight() - self.cursor.getHeight() - 2)) \
                * (self.adjustment.upper - self.adjustment.page_size)
        if event.type == 'click':
            old_value = self.adjustment.get_value()
            if pos < 0:
                incr = self.adjustment.step_incr
                self.adjustment.set_value(old_value - incr)
            elif pos > self.line.getHeight():
                incr = self.adjustment.step_incr
                self.adjustment.set_value(old_value + incr)
            else:
                incr = self.adjustment.page_incr
                if value > old_value:
                    self.adjustment.set_value(old_value + incr)
                elif value < old_value:
                    self.adjustment.set_value(old_value - incr)
        else:
            self.adjustment.set_value(value)

    def _adjustment_value_changed(self):
        Scrollbar._adjustment_value_changed(self)
        value = self.adjustment.get_value()
        y = (value - self.adjustment.lower) / \
                (self.adjustment.upper - self.adjustment.page_size) \
                * (self.line.getHeight() - self.cursor.getHeight() - 2)
        self.cursor.setStyle('top', str(y) + 'px')


class OptionMenu(Button):
    def __init__(self):
        Button.__init__(self)
        self.ico = browser.Element('img')
        self.ico.setProperty('src','arr.png')
        self.ico.setStyle('position','absolute')
        self.ico.setStyle('right','2px')
        self.widget_int.append(self.ico)
        self.connect('clicked', self._clicked, None)
        self.menu = None
        self.menu_open = False
        self.label = Label('')
        self.label.set_alignment(0, 0.5)
        self.add(self.label)

    def _redraw(self):
        Button._redraw(self)
        rect = self.get_allocation()
        pad = rect.height / 2 - self.ico.getHeight() / 2
        self.ico.setStyle('top', str(pad) + 'px')

    def _clicked(self, elem, data=None):
        self.menu_open = not self.menu_open
        if not self.menu._visible:
            rect = self.get_allocation()
            self.menu.widget_cont.setStyle('left',rect.x+'px')
            self.menu.widget_cont.setStyle('top',str(rect.y+rect.height)+'px')
            self.menu.show_all()
        else:
            self.menu.hide_all()

    def _selected(self, elem, data=None):
        act = self.menu.get_active()
        if act!=None:
            self.label.set_text(act.label_cont)

    def set_menu(self, menu):
        self.label.set_text(menu.items[0].label_cont)
        self.menu = menu
        self.menu.connect('selection-done', self._selected, None)

class MenuShell(Container):
    def __init__(self):
        Container.__init__(self)
        self.items = []
        self.widget_cont.setStyle('border','1px solid gray')
        self.widget_cont.setStyle('position','absolute')
        self.widget_cont.setStyle('width','auto')
        self.widget_cont.setStyle('height','')
        self.widget_cont.setStyle('left','')
        self.widget_cont.setStyle('right','')
        self.widget_cont.setStyle('bottom','')
        self.widget_cont.setStyle('top','')
        self.widget_cont.setStyle('zIndex','100')
        self.widget_int.setStyle('position','absolute')
        self.widget_int = self.widget_cont
        self.widget_cont.setProperty('className','menushell')
        self.hide()
        browser.Document.append(self.widget_cont)

    def append(self, child):
        child.hide()
        child.connect('select', self._selected, None)
        self.items.append(child)
        self.add(child)

    def _selected(self, elem, data=None):
        self.emit('selection-done')
        self.hide_all()

    def _redraw(self):
        Container._redraw(self)
        for child in self.childs:
            if child.minwidth > self.minwidth:
                self.minwidth = child.minwidth
            self.minheight += child.minheight
        self.widget_cont.setStyle('minHeight', str(self.minheight) + 'px')
        self.widget_cont.setStyle('minWidth', str(self.minwidth) + 'px')

class Menu(MenuShell):
    def append(self, child):
        child.connect('select', self._catch_active, None)
        MenuShell.append(self, child)
        self._active = None

    def _catch_active(self, elem, data=None):
        self._active = elem

    def get_active(self):
        return self._active

class Item(Bin):
    def __init__(self, name):
        Bin.__init__(self)
        self.label_cont = name
        self.widget_cont.catchEvents(['click'], self)
        self.widget_cont.setStyle('position','')
        self.widget_cont.setStyle('width', '100%')
        self.widget_cont.setStyle('bottom','')
        self.widget_cont.setStyle('top','')
        self.widget_int.setStyle('position','absolute')
        self.widget_int = self.widget_cont
        self.widget_cont.setProperty('className','menuitem')

        self.content = Label(name)
        self.content.hide()
        self.add(self.content)

    def dom_event(self, event, element):
        if event.type == 'click':
            self.emit('select')
            self.emit('toggle')

    def show(self):
        Bin.show(self)
        self.content.show()

    def hide(self):
        Bin.hide(self)
        self.content.hide()

    def _redraw(self):
        Bin._redraw(self)
        self.widget_cont.setStyle('width', '100%')

class MenuItem(Item):
    def dom_event(self, event, element):
        Item.dom_event(self, event, element)
        if event.type == 'click':
            self.emit('activate')

gtkbuildermap = {'GtkWindow': gtk.Window,
          'GtkTable': gtk.Table,
          'GtkLabel': gtk.Label,
          'GtkVBox': gtk.VBox,
          'GtkHBox': gtk.HBox,
          'GtkEntry': gtk.Entry
          }

def find_props(node):
    res = {}
    if not node:
        return {}
    props = node.getElementsByTagName("property")
    for i in range(props.length):
        n = props.item(n)
        name = n.attributes.getNamedItem('name').nodeValue
        log.write("find_props ")
        log.write(name)
        log.write(" ")
        log.write(n.textContent)
        log.writebr("")
        res[name] = n.textContent
    return res

class BuilderETree:

    def __init__(self):
        self.objects = []

    def create_object_from_xml_node(self, node):
        klsname = node.attrib['class']
        id = node.attrib['id']
        obj = gtkmap[klsname]()
        for prop in node.findall("property"):
            name = prop.attrib['name']
            value = prop.textContent
            try:
                setattr(obj.props, name, value)
            except:
                if value.isdigit():
                    setattr(obj.props, name, int(value))
                else:
                    print "setattr failed", klsname, name, value
        for childnode in node.findall("child"):
            childobj = childnode.find("object")
            if childobj is None:
                continue
            child = self.create_object_from_xml_node(childobj)
            obj.add_child(gtk.Builder(), child, klsname)
            props = find_props(childnode.find("packing"))
            for prop, value in props.items():
                if value.isdigit():
                    value = int(value)
                obj.child_set_property(child, prop, value)
            print props
        return obj

    def add_from_file(self, fname):
        s = open(fname).read()
        return s.add_from_string(s)

    def add_from_string(self, f):
        s = open(fname).read() # whoops don't expect this to work in pyjamas!
        doc = lxml.etree.fromstring(s)
        for x in doc:
            if x.tag != 'object':
                continue
            obj = self.create_object_from_xml_node(x)
            self.objects.append(obj)

    def get_objects(self):
        return self.objects

gtkmap = {  'GtkWindow': Window,
            'GtkTable': Table,
            'GtkLabel': Label,
            'GtkVBox': VBox,
            'GtkHBox': HBox,
            'GtkEntry': Entry
        }


class Builder:

    def __init__(self):
        self.objects = []

    def create_object_from_xml_node(self, node):
        klsname = node.attributes.getNamedItem('class').nodeValue
        id = node.attributes.getNamedItem('id').nodeValue
        log.writebr("%s %s" % (klsname, id))
        global gtkmap
        obj = gtkmap[klsname]()
        props = node.getElementsByTagName("property")
        log.writebr("%s %d" % (klsname, props.length))
        for i in range(props.length):
            prop = props.item(i)
            name = prop.attributes.getNamedItem('name').nodeValue
            value = prop.textContent
            try:
                setattr(obj, name, value)
            except:
                if value and value.isdigit():
                    setattr(obj, name, int(value))
                else:
                    print "setattr failed", klsname, name, value
        childnodes = node.getElementsByTagName("child")
        log.writebr("%s children %d" % (klsname, childnodes.length))
        for i in range(childnodes.length):
            childnode = childnodes.item(i)
            childobj = childnode.getElementsByTagName("object")
            if childobj is None:
                continue
            if childobj.length == 0:
                continue
            childobj = childobj.item(0)
            child = self.create_object_from_xml_node(childobj)
            #obj.add_child(gtk.Builder(), child, klsname)
            obj.add(child)
            packing = childnode.getElementsByTagName("packing")
            if packing is None:
                continue
            if packing.length == 0:
                continue
            packing = packing.item(0)
            props = find_props(packing)
            for prop, value in props.items():
                if value.isdigit():
                    value = int(value)
                obj.child_set_property(child, prop, value)
        return obj

    def add_from_file(self, fname):
        s = open(fname).read()
        return s.add_from_string(s)

    def add_from_string(self, xmldoc):
        x = xmldoc.firstChild.firstChild
        while x:
            log.writebr(x.nodeName)
            if x.nodeName == 'object':
                log.writebr("creating object")
                obj = self.create_object_from_xml_node(x)
                self.objects.append(obj)
            x = x.nextSibling

    def get_objects(self):
        return self.objects

def main():
    pass

def main_quit():
    #TODO: In popups, close it !
    browser.Document.setContent('This application has finalized !')
