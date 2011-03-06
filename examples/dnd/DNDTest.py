# Copyright (C) 2010 Jim Washington
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# ui borrowed from http://decafbad.com/2009/07/drag-and-drop/api-demos.html
from gwt.ui import HasVerticalAlignment
from pyjamas.Timer import Timer
from pyjamas.Window import alert
from pyjamas.dnd.utils import eventCoordinates
from pyjamas.ui.DragHandler import DragHandler
from pyjamas.ui.InnerText import InnerText

import pyjd
from datetime import datetime

from __pyjamas__ import doc, wnd

from pyjamas.ui.Widget import Widget
from pyjamas import DOM
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.AbsolutePanel import AbsolutePanel

from pyjamas.Canvas.GWTCanvas import GWTCanvas
import pyjamas.Canvas.Color as Color

from pyjamas.dnd import makeDraggable
from pyjamas.ui.DragWidget import DragWidget, DragContainer
from pyjamas.ui.DropWidget import DropWidget
from pyjamas.ui.Panel import Panel
from pyjamas.dnd import getTypes
from pyjamas.JSONParser import JSONParser
from pyjamas import Window
import random

json = JSONParser()

class DNDDemos(VerticalPanel):
    def __init__(self):
        VerticalPanel.__init__(self)
        self.width = '100%'
        self.setID('content')
        self.add(TopVerbage())
        self.add(NewSchool())
        self.add(Delegated())
        self.add(ImageDrop())
        self.add(DataTransferDemo())
        self.add(DragEffects())
        self.add(AbsolutePosition())
        self.add(MultiTargetDemo())

class AddablePanel(Panel):
    def __init__(self, **kw):
        Panel.__init__(self, **kw)

    def add(self, widget, container=None):
        self.adopt(widget,self.getElement())
        self.children.append(widget)

    def remove(self,widget):
        self.disown(widget)
        self.children.remove(widget)


class TopVerbage(AddablePanel):
    title = "Drag and Drop in %s Pyjamas"

    def __init__(self):
        AddablePanel.__init__(self, Element=DOM.createElement('div'))
        self.setID('toc')
        img = '<img id="logo" src="pyjamas.png">'
        self.add(HTML('<h1>%s</h1>' % (self.title % img,)))
        self.add(HTML(
        """
        <p>This page is a reimagining of
        <a href="http://decafbad.com/2009/07/drag-and-drop/api-demos.html">
        http://decafbad.com/2009/07/drag-and-drop/api-demos.html</a> using
        pyjamas.</p>
        <p>
        <p>This page offers a few demonstrations and experiments, mostly
        as a test tool for the background implementation.</p>
        """
       ))


class DragWidget1(DragWidget, Label):
    def __init__(self):
        Label.__init__(self, Element=DOM.createElement('div'))
        self.setText("Drag me!")
        DragWidget.__init__(self)
        self.setStyleName('dragme1')

    def onDragStart(self, event):
        dt = event.dataTransfer
        #self.addMessage('types is %s' % dt.getTypes())
        dt.setData('Text', 'Dropped in zone!')
        #self.addMessage('after setting, len is %s' % len(dt.dataStore.items))
        #self.addMessage('types is %s' % dt.getTypes())
        #dt.setDragImage(self.getElement(), 15, 15)
        dt.effectAllowed = 'copy'
        #self.addMessage('mode is %s' % dt.dataStore.items.mode)

    def onDragEnd(self, event):
        self.addMessage('Drag ended')
        #self.addMessage('mode is %s' % dt._data.mode)

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)


class DropWidget1(DropWidget, Label):
    def __init__(self):
        Label.__init__(self, Element=DOM.createElement('div'))
        DropWidget.__init__(self)
        self.setText("Drop here!")
        self.setStyleName('drophere')

    def onDragEnter(self, event):
        self.addStyleName('dragover')
        DOM.eventPreventDefault(event)

    def onDragLeave(self, event):
        self.removeStyleName('dragover')

    def onDragOver(self, event):
        DOM.eventPreventDefault(event)

    def onDrop(self, event):
        dt = event.dataTransfer
        #'text', 'text/plain', and 'Text' are equivalent.
        try:
            item = dt.getData("text/plain")
            self.addMessage(item)
        except:
            self.addMessage('unsupported data type')
        #DOM.eventPreventDefault(event)

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)


class Messages(Widget):

    def __init__(self):
        Widget.__init__(self, Element=DOM.createElement('ul'))
        self.setStyleName('messages')
        self.addStyleName('events_monitor')

    def addMessage(self, text):
        d = datetime.now().strftime("%x %X")
        li = DOM.createElement('li')
        DOM.setInnerHTML(li,
                         '<dt class="time">%s</dt><dd class="txt">%s</dd>' % (
                         d, text))
        DOM.insertChild(self.element, li, 0)


class DNDDemo(AddablePanel):
    """
    Template for the demos.

    drag_widget goes on the left. drop_widget goes
    on the right, and the message display goes on the bottom. add_message makes
    it easy to display anything you want for debugging.
    """
    title = "DND Demo"
    id = 'none'
    drag_widget = None
    drop_widget = None

    def __init__(self):
        AddablePanel.__init__(self, Element=DOM.createElement('div'))
        self.setID(self.id)
        self.h2 = HTML('<h2>%s</h2>' % self.title)
        self.append(self.h2)
        demo_div = AddablePanel(Element=DOM.createElement('div'))
        demo_div.setStyleName('demo')
        top_frame = HorizontalPanel()
        g = self.drag_widget
        if g is not None:
            top_frame.add(g)
        p = self.drop_widget
        if p is not None:
            top_frame.add(p)
        demo_div.add(top_frame)
        self.messages = Messages()
        demo_div.append(self.messages)
        self.add(demo_div)

    def addMessage(self, message):
        self.messages.addMessage(message)


class NewSchool(DNDDemo):
    def __init__(self):
        self.title = "Drag and drop"
        self.id = 'newschool'
        self.drag_widget = DragWidget1()
        self.drop_widget = DropWidget1()
        DNDDemo.__init__(self)


class DragWidget2(DragContainer, AddablePanel):

    def onDragStart(self, event):
        target = DOM.eventGetTarget(event)
        dt = event.dataTransfer
        dt.setData("Text", "Dropped %s" % target.id)
        dt.effectAllowed = 'copy'

    def __init__(self):
        self.setElement(DOM.createElement('ul'))
        DragContainer.__init__(self)
        AddablePanel.__init__(self)

    def onLoad(self):
        link = self.makeLink()
        link.addClickListener(self)
        li = AddablePanel(Element=DOM.createElement('li'))
        li.add(link)
        self.button = li
        self.add(self.button)

        for k in range(3):
            self.addDragWidget()

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)

    def addDragWidget(self):
        self.remove(self.button)
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setID('drag' + str(s))
        w.setStyleName('dragme')
        w.setText('Drag ' + str(s))
        self.add(w)
        makeDraggable(w)
        self.add(self.button)

    def makeLink(self):
        link = Button()
        link.setText("+ Add another")
        return link

    def onClick(self, sender):
        self.addDragWidget()


class DropWidget2(DropWidget, AddablePanel):
    def __init__(self):
        self.setElement(DOM.createElement('ul'))
        DropWidget.__init__(self)
        AddablePanel.__init__(self)

    def onLoad(self):
        button = self.makeButton()
        button.addClickListener(self)
        li = AddablePanel(Element=DOM.createElement('li'))
        li.add(button)
        self.button = li
        self.add(self.button)
        for k in range(3):
            self.addDropWidget()

    def addDropWidget(self):
        self.remove(self.button)
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setID('drop' + str(s))
        w.setStyleName('drophere')
        w.setText('Drop ' + str(s))
        self.append(w)
        self.append(self.button)

    def onDragEnter(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        try:
            class_names = t.getStyleName()
        except:
            class_names = None
        dt = event.dataTransfer
        dt.dropEffect = 'copy'
        if class_names is not None:
            if 'drophere' in class_names:
                t.addStyleName('dragover')
                DOM.eventPreventDefault(event)

    def onDragOver(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        dt = event.dataTransfer
        dt.dropEffect = 'copy'
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                DOM.eventPreventDefault(event)

    def onDragLeave(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        try:
            class_names = t.getStyleName()
        except:
            class_names = None
        if class_names is not None:
            if 'drophere' in class_names:
                t.removeStyleName('dragover')

    def onDrop(self, event):
        dt = event.dataTransfer
        text = dt.getData('Text')
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                self.addMessage('%s onto %s' % (text, target.id))
                return

    def makeButton(self):
        button = Button("+ Add another")
        return button

    def onClick(self, sender):
        self.addDropWidget()

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)


class Delegated(DNDDemo):
    title = "DND with Event Delegation"
    id = "delegated"

    def __init__(self):
        self.drag_widget = DragWidget2()
        drag = self.drag_widget
        drag.setStyleName('drag_delegates')
        drag.addStyleName('draglist')
        self.drop_widget = DropWidget2()
        drop = self.drop_widget
        drop.setStyleName('drop_delegates')
        drop.addStyleName('droplist')
        DNDDemo.__init__(self)


class DragWidget3(DragWidget2):


    def __init__(self):
        self.setElement(DOM.createElement('ul'))
        super(DragWidget3, self).__init__()

    def onLoad(self):
        self.setStyleName('drag_delegates')
        self.addStyleName('draglist')
        for k in range(4):
            self.addDragWidget()

    def makeCanvasImg(self, canvas):
        ctx = canvas
        ctx.beginPath()
        ctx.setLineWidth(3)
        ctx.setStrokeStyle(Color.ORANGE)
        ctx.moveTo(25,1.5)
        ctx.lineTo(50, 50)
        ctx.lineTo(1.5, 50)
        ctx.lineTo(25, 1.5)
        ctx.stroke()

    def onDragStart(self, event):
        dt = event.dataTransfer
        target = DOM.eventGetTarget(event)
        target = Widget(Element=target)
        id = target.getID()
        dt.setData("Text", "Dropped %s" % target.getID())
        dt.effectAllowed = 'copy'
        if id == 'imgdrag1':
            parent = self.getParent()
            while not hasattr(parent, 'h2'):
                parent = parent.getParent()
            dt.setDragImage(parent.h2.getElement(), 10, 10)
        elif id == 'imgdrag2':
            dt.setDragImage(doc().getElementById('logo'), 10, 10)
        elif id == 'imgdrag3':
            # OK, it's a bit of a cheat, but the following works on current
            # Opera, IE, Firefox, Safari, Chrome.
            ctx = GWTCanvas(50, 50)
            self.makeCanvasImg(ctx)
            try:
                img = DOM.createImg()
                DOM.setAttribute(img, 'src', ctx.canvas.toDataURL())
                dt.setDragImage(img, 25, 25)
            except:
                dt.setDragImage(ctx.canvas, 25,25)

    def addDragWidget(self):
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setStyleName('dragme')
        w.setID('imgdrag' + str(s))
        texts = ['Default',
                 'Element',
                 'Image',
                 'Canvas'
        ]
        w.setText(texts[s])
        self.add(w)
        makeDraggable(w)


class DropWidget3(DropWidget1):
    def onLoad(self):
        self.setID("imgdrop")


class ImageDrop(DNDDemo):
    def __init__(self):
        self.title = "Using drag feedback images"
        self.id = "feedback_image"
        self.drop_widget = DropWidget3()
        self.drag_widget = DragWidget3()
        DNDDemo.__init__(self)


class DragWidget4(DragWidget2):
    def __init__(self):
        self.setElement(DOM.createElement('ul'))
        super(DragWidget4, self).__init__()

    def onLoad(self):
        self.setStyleName('drag_delegates')
        self.addStyleName('draglist')
        self.following_text = HTML("""<li><p>
               ... and try dragging to other windows and applications.
               </p></li>
            """)
        for k in range(3):
            self.addDragWidget()
        self.append(self.following_text)

    def addDragWidget(self):
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setID('datadrag' + str(s))
        w.setStyleName('dragme')
        texts = ['Text',
                 'Text / HTML / URI',
                 'Disallowed']
        w.setText(texts[s])
        self.append(w)
        makeDraggable(w)

    def onDragStart(self, event):
        dt = event.dataTransfer
        target = DOM.eventGetTarget(event)
        target = Widget(Element=target)
        try:
            id = target.getID()
        except:
            id = ''
        if id == 'datadrag0':
            dt.setData('text/plain', 'Hello World!')
        elif id == 'datadrag1':
            logo = doc().getElementById('logo')
            logo_parent_element = DOM.getParent(logo)
            text = DOM.getInnerText(logo_parent_element)
            html = DOM.getInnerHTML(logo_parent_element)
            uri = DOM.getAttribute(logo, 'src')
            dt.setData('text/plain', text)
            dt.setData('text/html', html)
            dt.setData('text/uri-list', uri)
        elif id == 'datadrag2':
            dt.setData('x-star-trek/tribble', 'I am a tribble')


class DropWidget4(DropWidget1):
    def onLoad(self):
        self.setText('''Drop here from items on the left - and selected
        content from other windows and applications.''')
        self.setID('datadrop')

    def onDrop(self, event):
        dt = event.dataTransfer
        types = getTypes(event)
        self.addMessage("drop types received: " + ", ".join(types))
        parent = self.getParent()
        parent.clearContent()
        self.addMessage('dt: ' + str(dt))
        types.sort()
        for ctype in types:
            data = dt.getData(ctype)
            if ctype == 'Files':
                file_names = []
                files = dt.files
                # files is a FileList
                # http://help.dottoro.com/ljuelxgf.php
                for idx in range(files.length):
                    item = files.item(idx)
                    try:
                        name = item.name
                    except:
                        name = item.fileName
                    file_names.append(name)
                data = '<br>'.join(file_names)
            parent.addContent(ctype, data)
        # cancel bubble so first file is not opened in browser.
        DOM.eventCancelBubble(event, True)


    def onDragOver(self, event):
        types = getTypes(event)
        if not 'x-star-trek/tribble' in types:
            self.addStyleName('dragover')
            DOM.eventPreventDefault(event)

    def onDragEnter(self, event):
        types = getTypes(event)
        if not 'x-star-trek/tribble' in types:
            self.addStyleName('dragover')
            DOM.eventPreventDefault(event)


class ContentDisplay(Label, AddablePanel):
    def __init__(self, ctype, data):
        Label.__init__(self)
        AddablePanel.__init__(self)
        self.setStyleName('content_text')
        self.setText("'%s' content:" % ctype)
        self.content = HTML(data, StyleName='content')
        self.append(self.content)


class DropWidgetPanel4(AddablePanel):
    def __init__(self):
        AddablePanel.__init__(self, Element=DOM.createElement('div'))

    def onLoad(self):
        self.drop_widget = DropWidget4()
        self.add(self.drop_widget)
        self.contentPanel = AddablePanel(Element = DOM.createElement('div'))
        self.add(self.contentPanel)

    def clearContent(self):
        self.contentPanel.clear()

    def addContent(self, ctype, data):
        display = ContentDisplay(ctype, data)
        self.contentPanel.add(display)


class DataTransferDemo(DNDDemo):
    def __init__(self):
        self.title = "Using data transfer content types"
        self.id = "data_transfer"
        self.drag_widget = DragWidget4()
        self.drop_widget = DropWidgetPanel4()
        DNDDemo.__init__(self)

class DragWidget5(DragWidget2):

    def onDragStart(self, event):
        target = DOM.eventGetTarget(event)
        dt = event.dataTransfer
        try:
            id = Widget(Element=target).getID()
        except:
            id = ''
        dt.setData("Text", "Dropped %s" % id)
        effect_allowed = self.data[int(id[-1])]
        dt.effectAllowed = effect_allowed

    def onLoad(self):
        self.setStyleName('drag_delegates')
        self.addStyleName('draglist')
        self.data =['copy', 'move','link','all','none']
        for k in range(5):
            self.addDragWidget()

    def addDragWidget(self):
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setID('effectdrag' + str(s))
        w.setStyleName('dragme')
        w.setText('Drag %s (%s)' % (s, self.data[s]))
        self.add(w)
        makeDraggable(w)

class DropWidget5(DropWidget2):
    def onLoad(self):
        self.data =['copy', 'move','link','all','none']
        self.setStyleName('drop_delegates')
        self.addStyleName('droplist')
        for k in range(5):
            self.addDropWidget()

    def addDropWidget(self):
        s = len(self.children)
        w = Label(Element=DOM.createElement('li'))
        w.setID('effectdrop' + str(s))
        w.setStyleName('drophere')
        w.setText('Drop %s (%s)' % (s, self.data[s]))
        self.append(w)

    def onDragEnter(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        try:
            class_names = t.getStyleName()
        except:
            class_names = None
        if class_names is not None:
            if 'drophere' in class_names:
                t.addStyleName('dragover')
                DOM.eventPreventDefault(event)

    def onDragOver(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                dt = event.dataTransfer
                id = Widget(Element=target).getID()
                drop_effect = self.data[int(id[-1])]
                dt.dropEffect = drop_effect
                DOM.eventPreventDefault(event)

    def onDragLeave(self, event):
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        try:
            class_names = t.getStyleName()
        except:
            class_names = None
        if class_names is not None:
            if 'drophere' in class_names:
                t.removeStyleName('dragover')

    def onDrop(self, event):
        dt = event.dataTransfer
        text = dt.getData('Text')
        target = DOM.eventGetTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                self.addMessage('%s onto %s<br>effectAllowed=%s, dropEffect=%s'
            % (text, target.id, dt.effectAllowed, dt.dropEffect))


class DragEffects(DNDDemo):
    def __init__(self):
        self.title = "Using drag effects"
        self.id = "data_transfer"
        self.drag_widget = DragWidget5()
        self.drop_widget = DropWidget5()
        DNDDemo.__init__(self)




class AbsolutePosition(DNDDemo):
    def __init__(self):
        self.title = "Absolute Position Drag and Drop"
        self.id = "absolute_position"
        self.drop_widget = Drop6Container()
        DNDDemo.__init__(self)

class Drop6Container(HorizontalPanel):
    def __init__(self):
        HorizontalPanel.__init__(self)
        left = DropWidget6()
        right = DropWidget6()
        self.setSpacing('10px')

        drag = DragWidget6("Drag1")
        drag2 = DragWidget6("Drag2")
        left.add(drag2)
        drag2.setStyleAttribute('top', 0)
        drag2.setStyleAttribute('left', 0)
        makeDraggable(drag2)
        left.add(drag)
        drag.setStyleAttribute('top', 0)
        drag.setStyleAttribute('left', 100)
        makeDraggable(drag)

        self.add(left)
        self.add(right)


class DragWidget6(Label):
    def __init__(self,text):
        Label.__init__(self, text)
        self.setStyleName('dragme2')
        self.setStyleAttribute('position', 'absolute')



class DropWidget6(DropWidget, DragContainer, AddablePanel):
    def __init__(self):
        AddablePanel.__init__(self, Element=DOM.createElement('div'))
        DropWidget.__init__(self)
        DragContainer.__init__(self)
        self.setStyleName('drophere2')
        self.setStyleAttribute('position', 'relative')
        self.setSize('300px', '300px')

    def onDragStart(self, event):
        dt= event.dataTransfer
        target = DOM.eventGetTarget(event)
        clientX = event.clientX
        clientY = event.clientY
        absx = clientX + Window.getScrollLeft()
        absy = clientY + Window.getScrollTop()
        package = json.encode({"text":DOM.getInnerText(target),
                            "offsetX":absx - DOM.getAbsoluteLeft(target) ,
                            "offsetY":absy - DOM.getAbsoluteTop(target)})
        dt.setData('text', package)
        # using "copy" here because Windows Chrome does not like "move"
        dt.allowedEffects='copy'
        self.movingWidget = None
        for widget in self.children:
            if target == widget.getElement():
                self.movingWidget = widget

    def onDragLeave(self, event):
        dt = event.dataTransfer
        dt.dropEffect = 'none'

    def onDrag(self,event):
        self.movingWidget.addStyleName('invisible')

    def onDragEnd(self, event):
        dt = event.dataTransfer
        self.addMessage('Drop effect is "%s"' % dt.dropEffect)
        if dt.dropEffect != 'none':
            self.remove(self.movingWidget)
        else:
            # Restore widget visibility. Allow 0.5 seconds for the fly-back.
            def ontimer():
                self.movingWidget.removeStyleName('invisible')
            Timer(500, notify=ontimer)

    def onDragEnter(self, event):
        DOM.eventPreventDefault(event)

    def onDragOver(self, event):
        dt = event.dataTransfer
        dt.dropEffect = 'copy'
        DOM.eventPreventDefault(event)
        
    def onDrop(self, event):
        dt = event.dataTransfer
        text = dt.getData('text')
        package = json.decode(text)
        x =  event.clientX
        y =  event.clientY
        scrollY = Window.getScrollTop()
        scrollX = Window.getScrollLeft()
        offsetX = int(package['offsetX'])
        offsetY = int(package['offsetY'])
        at = self.getAbsoluteTop()
        al = self.getAbsoluteLeft()
        posX, posY = x - (al - scrollX),  y - (at - scrollY)
        w = DragWidget6(package['text'])
        self.add(w)
        makeDraggable(w)
        # firefox seems to be off-by-one in x.
        # firefox-specific code?
        #w.setStyleAttribute('left', posX - offsetX -1)
        w.setStyleAttribute('left', posX - offsetX)
        w.setStyleAttribute('top', posY - offsetY)
        w.removeStyleName('invisible')
        self.addMessage("top:%s, left:%s, cy:%s cx:%s, sy:%s sx:%s dropy:%s dropx:%s" % (at, al, y, x, scrollY, scrollX, posY, posX))

        DOM.eventPreventDefault(event)

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)

class StudentWidget(Label):
    def __init__(self, name, age):
        #Label.__init__(self, Element=DOM.createElement('div'))
        #self.dragHandler = DragHandler()
        #self.dragHandler.addDragListener(self)
        Label.__init__(self, Element=DOM.createElement('li'))
        self.student_name = name
        self.age = int(age)
        self.setText("%s (%s)" % (self.student_name, self.age))
        self.setStyleName('dragme')
        self.addStyleName('age_%s' % self.age)

    def onClick(self, sender):
        self.addMessage("clicked")

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)


class StudentContainer(DragContainer, DropWidget, VerticalPanel):
    def __init__(self, min_age, max_age, id):
        self.min_age = min_age
        self.max_age = max_age
        VerticalPanel.__init__(self)
        DropWidget.__init__(self)
        DragContainer.__init__(self)
        self.setID(id)
        self.setWidth(200)
        self.setHeight(300)
        self.setVerticalAlignment(HasVerticalAlignment.ALIGN_TOP)
        self.setStyleName('drophere2')
        self.addTitle()

    def getNames(self):
        names = []
        for item in self.children:
            if isinstance(item, StudentWidget):
                names.append((item.student_name, item.age))
        return names

    def addTitle(self):
        self.append(Label("Allowed: %s to %s" % (self.min_age, self.max_age)))

    def addStudent(self, name, age):
        new_names = self.getNames()
        found = False
        for item in new_names:
            if item == (name, age):
                found = True
                break
        if not found:
            new_names.append((name, age))
        new_names.sort()
        while len(self.children):
            self.remove(self.children[0])
        #self.clear()
        self.addTitle()
        for student in new_names:
            sw = StudentWidget(student[0], student[1])
            makeDraggable(sw)
            self.append(sw)
            self.setCellVerticalAlignment(sw, HasVerticalAlignment.ALIGN_TOP)

    def onDragStart(self, event):
        self.removeStyleName('drop_fail')
        dt= event.dataTransfer
        dt.effectAllowed = 'copy'
        target = DOM.eventGetTarget(event)
        widget = None
        for widget in self.children:
            if widget.getElement() == target:
                self.movingWidget = widget
                break
        dt.setData('Text', json.encode({'name':widget.student_name,
                                        'age':widget.age,
                                        'parent':self.getID()}))

    def onDrag(self, event):
        self.movingWidget.addStyleName('invisible')

    def onDragEnd(self, event):
        dt = event.dataTransfer
        styles = self.getStyleName()
        if dt.dropEffect != 'none' and not 'drop_fail' in styles:
            self.remove(self.movingWidget)
            msg = 'drop succeeded'
        else:
            self.movingWidget.removeStyleName('invisible')
            msg = 'drop failed'
        self.addMessage(msg)

    def onDragEnter(self, event):
        self.addStyleName('dragover')
        DOM.eventPreventDefault(event)

    def onDragLeave(self, event):
        self.removeStyleName('dragover')

    def onDragOver(self, event):
        DOM.eventPreventDefault(event)

    def age_is_ok(self, age):
        return age >= self.min_age and age <= self.max_age

    def onDrop(self, event):
        dt = event.dataTransfer

        item = dt.getData("Text")
        data = json.decode(item)
        if 'name' in data and 'age' in data:
            age = data['age']
            name = data['name']
            if self.age_is_ok(age):
                self.addStudent(name, age)
                dt.dropEffect = 'copy'
            else:
                dt.dropEffect = 'none'
                self.addMessage('student could not be added')
                # setting dropEffect to 'none' should be sufficient to notify
                # that the drop failed, but
                # we need to cheat a bit for now...
                # this is the only reason for parent id in data
                item_parent_id = data['parent']
                item_parent = self.parent.containerFromId(item_parent_id)
                item_parent.addStyleName('drop_fail')
        # prevent default allows onDragEnd to see the dropEffect we set here
        DOM.eventPreventDefault(event)

    def addMessage(self, message):
        parent = self.getParent()
        while not hasattr(parent, 'addMessage'):
            parent = parent.getParent()
        parent.addMessage(message)


class ClassContainer(HorizontalPanel):
    def __init__(self):
        HorizontalPanel.__init__(self)
        #self.setSpacing('10px')

        pool = StudentContainer(1, 20, 'pool_1')
        for item in [['Fred', 12], ['Jane', 10], ['Sam', 18],
                     ['Ginger', 8],['Mary', 4]]:
            pool.addStudent(name=item[0], age=item[1])
        self.append(pool)
        self.append(StudentContainer(6, 13, 'pool_2'))
        self.append(StudentContainer(11, 20, 'pool_3'))
        self.setSpacing('10px')

    def containerFromId(self, id):
        for item in self.children:
            if item.getID() == id:
                return item

class MultiTargetDemo(DNDDemo):
    def __init__(self):
        self.drop_widget = ClassContainer()
        self.title = 'Drop with Validation'
        self.id = 'multi'
        DNDDemo.__init__(self)

if __name__ == '__main__':
    pyjd.setup("./public/DNDTest.html")
    j = RootPanel()
    j.add(DNDDemos())
    pyjd.run()
