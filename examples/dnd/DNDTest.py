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

from datetime import datetime

from __pyjamas__ import doc

from pyjamas.ui.Widget import Widget
from pyjamas import DOM
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel

from pyjamas.Canvas.GWTCanvas import GWTCanvas
import pyjamas.Canvas.Color as Color

from pyjamas.dnd import makeDraggable
from pyjamas.ui.DragWidget import DragWidget, DragContainer
from pyjamas.ui.DropWidget import DropWidget
from pyjamas.ui.Panel import Panel
from pyjamas.dnd import getTypes, getTarget


class DNDDemos(VerticalPanel):
    def __init__(self):
        VerticalPanel.__init__(self)
        self.width = '100%'
        self.setID('content')
        self.add(TopVerbage())
        self.add(NewSchool())
        self.add(Delegated())
        self.add(ImageDrop())
        self.add(DataTransfer())
        self.add(DragEffects())

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
        self.setStyleName('dragme')

    def onDragStart(self, event):
        dt= event.dataTransfer
        dt.setData('Text', 'Dropped in zone!')
        dt.setDragImage(self.getElement(), 15, 15)
        dt.effectAllowed = 'copy'

    def onDragEnd(self, event):
        self.addMessage('Drag ended')

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
        DOM.eventPreventDefault(event)

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
    title = "Drag and drop"
    id = 'newschool'
    drag_widget = DragWidget1()
    drop_widget = DropWidget1()


class DragWidget2(DragContainer, AddablePanel):

    def onDragStart(self, event):
        target = getTarget(event)
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
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        dt = event.dataTransfer
        dt.dropEffect = 'copy'
        if class_names is not None:
            if 'drophere' in class_names:
                t.addStyleName('dragover')
                DOM.eventPreventDefault(event)

    def onDragOver(self, event):
        target = getTarget(event)
        t = Widget(Element=target)
        dt = event.dataTransfer
        dt.dropEffect = 'copy'
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                DOM.eventPreventDefault(event)

    def onDragLeave(self, event):
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                t.removeStyleName('dragover')

    def onDrop(self, event):
        dt = event.dataTransfer
        text = dt.getData('Text')
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                self.addMessage('%s onto %s' % (text, target.id))
                return

    def makeButton(self):
        button = Button("+ Add another")
        return button

    def onClick(self):
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
        ctx.moveTo(25, 0)
        ctx.lineTo(50, 50)
        ctx.lineTo(0, 50)
        ctx.lineTo(25, 0)
        ctx.stroke()

    def onDragStart(self, event):
        dt = event.dataTransfer
        target = getTarget(event)
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
            # TODO: canvas only seems to work in Firefox and IE
            ctx = GWTCanvas(50, 50)
            dt.setDragImage(ctx.canvas, 25, 25)
            self.makeCanvasImg(ctx)

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
    title = "Using drag feedback images"
    id = "feedback_image"
    drop_widget = DropWidget3()
    drag_widget = DragWidget3()


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
            """
                )
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
        target = getTarget(event)
        target = Widget(Element=target)
        id = target.getID()
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


class DataTransfer(DNDDemo):
    title = "Using data transfer content types"
    id = "data_transfer"
    drag_widget = DragWidget4()
    drop_widget = DropWidgetPanel4()

class DragWidget5(DragWidget2):

    def onDragStart(self, event):
        target = getTarget(event)
        dt = event.dataTransfer
        id = Widget(Element=target).getID()
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
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                t.addStyleName('dragover')
                DOM.eventPreventDefault(event)

    def onDragOver(self, event):
        target = getTarget(event)
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
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                t.removeStyleName('dragover')

    def onDrop(self, event):
        dt = event.dataTransfer
        text = dt.getData('Text')
        target = getTarget(event)
        t = Widget(Element=target)
        class_names = t.getStyleName()
        if class_names is not None:
            if 'drophere' in class_names:
                self.addMessage('%s onto %s<br>effectAllowed=%s, dropEffect=%s'
            % (text, target.id, dt.effectAllowed, dt.dropEffect))


class DragEffects(DNDDemo):
    title = "Using drag effects"
    id = "data_transfer"
    drag_widget = DragWidget5()
    drop_widget = DropWidget5()




if __name__ == '__main__':
    j = RootPanel()
    j.add(DNDDemos())
