""" demoInfo.py

    DO NOT EDIT THE CONTENTS OF THIS FILE!

    This file is created automatically by the compile.py
    script out of the various demonstration modules.
"""

from ui import MenuItem
from ui import HorizontalPanel
from ui import Button
from ui import TextBox
from ui import Image
from ui import Label
from ui import PasswordTextBox
from ui import Hidden
from ui import Grid
from ui import PopupPanel
from ui import ScrollPanel
from ui import ListBox
from History import History
from ui import MenuBar
from ui import DialogBox
from ui import DockPanel
from ui import CheckBox
from ui import HTML
from ui import NamedFrame
from ui import Tree
from ui import Frame
from ui import Hyperlink
from ui import FlowPanel
import DOM
from ui import AbsolutePanel
from ui import TreeItem
from ui import FormPanel
from ui import TextArea
from ui import FileUpload
from ui import RadioButton
from ui import SimplePanel
from ui import TabPanel
from ui import StackPanel
from ui import VerticalPanel
from ui import FlexTable
from ui import HasAlignment
import Window
from ui import HTMLPanel



class HorizontalPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = HorizontalPanel()
        panel.setBorderWidth(1)

        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)

        part1 = Label("Part 1")
        part2 = Label("Part 2")
        part3 = Label("Part 3")
        part4 = Label("Part 4")

        panel.add(part1)
        panel.add(part2)
        panel.add(part3)
        panel.add(part4)

        panel.setCellWidth(part1, "10%")
        panel.setCellWidth(part2, "70%")
        panel.setCellWidth(part3, "10%")
        panel.setCellWidth(part4, "10%")

        panel.setCellVerticalAlignment(part3, HasAlignment.ALIGN_BOTTOM)

        panel.setWidth("100%")
        panel.setHeight("200px")

        self.add(panel)





class TextAreaDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = TextArea()
        field.setCharacterWidth(20)
        field.setVisibleLines(4)
        self.add(field)





class PopupPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        vPanel = VerticalPanel()
        vPanel.setSpacing(4)

        self._btn = Button("Click Me", getattr(self, "showPopup"))

        vPanel.add(HTML("Click on the button below to display the popup."))
        vPanel.add(self._btn)

        self.add(vPanel)


    def showPopup(self):
        contents = HTML("Hello, World!")
        contents.addClickListener(getattr(self, "onClick"))

        self._popup = PopupPanel(autoHide=True)
        self._popup.add(contents)
        self._popup.setStyleName("showcase-popup")

        left = self._btn.getAbsoluteLeft() + 10
        top  = self._btn.getAbsoluteTop() + 10
        self._popup.setPopupPosition(left, top)
        self._popup.show()


    def onClick(self):
        self._popup.hide()






class AbsolutePanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = AbsolutePanel()

        panel.add(self.makeBox("Child 1"), 20, 10)
        panel.add(self.makeBox("Child 2"), 30, 30)

        panel.setWidth("100%")
        panel.setHeight("100px")

        self.add(panel)


    def makeBox(self, label):
        wrapper = VerticalPanel()
        wrapper.setBorderWidth(1)
        wrapper.add(HTML(label))
        DOM.setIntAttribute(wrapper.getTable(), "cellPadding", 10)
        DOM.setAttribute(wrapper.getTable(), "bgColor", "#C3D9FF")

        return wrapper





class FrameDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        frame = Frame("http://google.com")
        frame.setWidth("100%")
        frame.setHeight("200px")
        self.add(frame)





class MenubarDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        menu1 = MenuBar(vertical=True)
        menu1.addItem("Item 1", MenuCmd(self, "onMenu1Item1"))
        menu1.addItem("Item 2", MenuCmd(self, "onMenu1Item2"))

        menu2 = MenuBar(vertical=True)
        menu2.addItem("Apples", MenuCmd(self, "onMenu2Apples"))
        menu2.addItem("Oranges", MenuCmd(self, "onMenu2Oranges"))

        menubar = MenuBar(vertical=False)
        menubar.addItem(MenuItem("Menu 1", menu1))
        menubar.addItem(MenuItem("<i>Menu 2</i>", True, menu2))
        self.add(menubar)

    def onMenu1Item1(self):
        Window.alert("Item 1 selected")

    def onMenu1Item2(self):
        Window.alert("Item 2 selected")

    def onMenu2Apples(self):
        Window.alert("Apples selected")

    def onMenu2Oranges(self):
        Window.alert("Oranges selected")


class MenuCmd:
    def __init__(self, object, handler):
        self._object  = object
        self._handler = handler

    def execute(self):
        handler = getattr(self._object, self._handler)
        handler()





class FileUploadDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)
        self.form.setAction("http://nonexistent.com")
        self.form.setTarget("results")

        vPanel = VerticalPanel()

        hPanel = HorizontalPanel()
        hPanel.setSpacing(5)
        hPanel.add(Label("Upload file:"))

        self.field = FileUpload()
        self.field.setName("file")
        hPanel.add(self.field)

        hPanel.add(Button("Submit", getattr(self, "onBtnClick")))

        vPanel.add(hPanel)

        results = NamedFrame("results")
        vPanel.add(results)

        self.form.add(vPanel)
        self.add(self.form)


    def onBtnClick(self):
        self.form.submit()





class TabPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        tabs = TabPanel()
        tabs.add(HTML("The quick brown fox jumps over the lazy dog."), "Tab 1")
        tabs.add(HTML("The early bird catches the worm."), "Tab 2")
        tabs.add(HTML("The smart money is on the black horse."), "Tab 3")

        tabs.selectTab(0)
        tabs.setWidth("100%")
        tabs.setHeight("250px")

        self.add(tabs)





class StackPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        stack = StackPanel()

        stack.add(HTML('The quick<br>brown fox<br>jumps over the<br>lazy dog.'),
                  "Stack 1")
        stack.add(HTML('The<br>early<br>bird<br>catches<br>the<br>worm.'),
                  "Stack 2")
        stack.add(HTML('The smart money<br>is on the<br>black horse.'),
                  "Stack 3")

        stack.setWidth("100%")
        self.add(stack)





class LabelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        label = Label("This is a label", wordWrap=False)
        self.add(label)





class ScrollPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = ScrollPanel()

        contents = HTML("<b>Tao Te Ching, Chapter One</b><p>" +
                        "The Way that can be told of is not an unvarying " +
                        "way;<p>The names that can be named are not " +
                        "unvarying names.<p>It was from the Nameless that " +
                        "Heaven and Earth sprang;<p>The named is but the " +
                        "mother that rears the ten thousand creatures, " +
                        "each after its kind.")

        panel.add(contents)
        panel.setSize("300px", "100px")
        self.add(panel)





class RadioButtonDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel1 = VerticalPanel()

        panel1.add(RadioButton("group1", "Red"))
        panel1.add(RadioButton("group1", "Green"))
        panel1.add(RadioButton("group1", "Blue"))

        panel2 = VerticalPanel()
        panel2.add(RadioButton("group2", "Solid"))
        panel2.add(RadioButton("group2", "Liquid"))
        panel2.add(RadioButton("group2", "Gas"))

        hPanel = HorizontalPanel()
        hPanel.add(panel1)
        hPanel.add(panel2)

        self.add(hPanel)





class HtmlDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        html = HTML("Hello, <b><i>World!</i></b>")
        self.add(html)





class FormPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setAction("http://google.com/search")
        self.form.setTarget("results")

        vPanel = VerticalPanel()
        vPanel.setSpacing(5)

        hPanel = HorizontalPanel()
        hPanel.setSpacing(5)

        hPanel.add(Label("Search for:"))

        self.field = TextBox()
        self.field.setName("q")
        hPanel.add(self.field)

        hPanel.add(Button("Submit", getattr(self, "onBtnClick")))

        vPanel.add(hPanel)

        results = NamedFrame("results")
        vPanel.add(results)

        self.form.add(vPanel)
        self.add(self.form)


    def onBtnClick(self):
        self.form.submit()






class DialogBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.add(Button("Show Dialog", getattr(self, "showDialog")))


    def showDialog(self):
        contents = VerticalPanel()
        contents.setSpacing(4)
        contents.add(HTML('You can place any contents you like in a dialog box.'))
        contents.add(Button("Close", getattr(self, "onClose")))
        contents.setStyleName("Contents")

        self._dialog = DialogBox()
        self._dialog.setHTML('<b>Welcome to the dialog box</b>')
        self._dialog.setWidget(contents)

        left = (Window.getClientWidth() - 200) / 2
        top = (Window.getClientHeight() - 100) / 2
        self._dialog.setPopupPosition(left, top)
        self._dialog.show()


    def onClose(self):
        self._dialog.hide()





class FlowPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        flow = FlowPanel()

        flow.add(Button("Item 1"))
        flow.add(Button("Item 2"))
        flow.add(Button("Item 3"))
        flow.add(Button("Item 4"))
        flow.add(Button("Item 5"))
        flow.add(Button("Item 6"))
        flow.add(Button("Item 7"))
        flow.add(Button("Item 8"))
        flow.add(Button("Item 9"))
        flow.add(Button("Item 10"))
        flow.setWidth("400px")
        self.add(flow)





class ListBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        hPanel = HorizontalPanel()
        hPanel.setSpacing(10)

        self.list1 = ListBox()
        self.list1.setVisibleItemCount(10)
        self.list1.addItem("Item 1")
        self.list1.addItem("Item 2")
        self.list1.addItem("Item 3")
        self.list1.addChangeListener(getattr(self, "onList1ItemSelected"))

        self.list2 = ListBox()
        self.list2.setVisibleItemCount(0)
        self.list2.addItem("Item A")
        self.list2.addItem("Item B")
        self.list2.addItem("Item C")
        self.list2.addChangeListener(getattr(self, "onList2ItemSelected"))

        hPanel.add(self.list1)
        hPanel.add(self.list2)
        self.add(hPanel)


    def onList1ItemSelected(self):
        item = self.list1.getItemText(self.list1.getSelectedIndex())
        Window.alert("You selected " + item + " from list 1")


    def onList2ItemSelected(self):
        item = self.list2.getItemText(self.list2.getSelectedIndex())
        Window.alert("You selected " + item + " from list 2")





class ImageDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        # We display the "myImage.jpg" file, stored in the "public/images"
        # directory, where "public" is in the application's source directory.

        img = Image("images/myImage.jpg")
        img.addClickListener(getattr(self, "onImageClicked"))
        self.add(img)


    def onImageClicked(self):
        Window.alert("Stop that!")





class TextBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = TextBox()
        field.setVisibleLength(20)
        field.setMaxLength(10)

        self.add(field)





class FlexTableDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self._table = FlexTable()
        self._table.setBorderWidth(1)
        self._table.setWidth("100%")

        cellFormatter = self._table.getFlexCellFormatter()
        rowFormatter = self._table.getRowFormatter()

        self._table.setHTML(0, 0, "<b>Mammals</b>")
        self._table.setText(1, 0, "Cow")
        self._table.setText(1, 1, "Rat")
        self._table.setText(1, 2, "Dog")

        cellFormatter.setColSpan(0, 0, 3)
        cellFormatter.setHorizontalAlignment(0, 0, HasAlignment.ALIGN_CENTER)

        self._table.setWidget(2, 0, Button("Hide", getattr(self, "hideRows")))
        self._table.setText(2, 1, "1,1")
        self._table.setText(2, 2, "2,1")
        self._table.setText(3, 0, "1,2")
        self._table.setText(3, 1, "2,2")

        cellFormatter.setRowSpan(2, 0, 2)
        cellFormatter.setVerticalAlignment(2, 0, HasAlignment.ALIGN_MIDDLE)

        self._table.setWidget(4, 0, Button("Show", getattr(self, "showRows")))

        cellFormatter.setColSpan(4, 0, 3)

        rowFormatter.setVisible(4, False)

        self.add(self._table)


    def hideRows(self):
        rowFormatter = self._table.getRowFormatter()
        rowFormatter.setVisible(2, False)
        rowFormatter.setVisible(3, False)
        rowFormatter.setVisible(4, True)


    def showRows(self):
        rowFormatter = self._table.getRowFormatter()
        rowFormatter.setVisible(2, True)
        rowFormatter.setVisible(3, True)
        rowFormatter.setVisible(4, False)





class PasswordTextBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        field = PasswordTextBox()
        field.setWidth("100px")
        self.add(field)





class GridDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        grid = Grid(5, 5)
        grid.setHTML(0, 0, '<b>Hello, World!</b>')
        grid.setBorderWidth(2)
        grid.setCellPadding(4)
        grid.setCellSpacing(1)

        for row in range(1, 5):
            for col in range(1, 5):
                grid.setText(row, col, str(row) + "*" + str(col) + " = " + str(row*col))

        self.add(grid)





class HiddenDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.form = FormPanel()
        self.form.setAction("http://google.com/search")
        self.form.setTarget("results")

        panel = VerticalPanel()
        panel.add(Hidden("q", "python pyjamas"))
        panel.add(Button("Search", getattr(self, "onBtnClick")))

        results = NamedFrame("results")
        panel.add(results)

        self.form.add(panel)
        self.add(self.form)


    def onBtnClick(self):
        self.form.submit()





class VerticalPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = VerticalPanel()
        panel.setBorderWidth(1)

        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)

        part1 = Label("Part 1")
        part2 = Label("Part 2")
        part3 = Label("Part 3")
        part4 = Label("Part 4")

        panel.add(part1)
        panel.add(part2)
        panel.add(part3)
        panel.add(part4)

        panel.setCellHeight(part1, "10%")
        panel.setCellHeight(part2, "70%")
        panel.setCellHeight(part3, "10%")
        panel.setCellHeight(part4, "10%")

        panel.setCellHorizontalAlignment(part3, HasAlignment.ALIGN_RIGHT)

        panel.setWidth("50%")
        panel.setHeight("300px")

        self.add(panel)





class CheckBoxDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        self.box = CheckBox("Print Results?")
        self.box.addClickListener(getattr(self, "onClick"))

        self.add(self.box)


    def onClick(self):
        Window.alert("checkbox status: " + self.box.isChecked())






class HyperlinkDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        History().addHistoryListener(self)

        vPanel = VerticalPanel()

        self.stateDisplay = Label()
        vPanel.add(self.stateDisplay)

        hPanel = HorizontalPanel()
        hPanel.setSpacing(5)
        hPanel.add(Hyperlink("State 1", False, "state number 1"))
        hPanel.add(Hyperlink("State 2", False, "state number 2"))

        vPanel.add(hPanel)
        self.add(vPanel)


    def onHistoryChanged(self, state):
        self.stateDisplay.setText(state)





class NamedFrameDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        vPanel = VerticalPanel()
        vPanel.setSpacing(5)

        frame = NamedFrame("myFrame")
        frame.setWidth("100%")
        frame.setHeight("200px")

        vPanel.add(frame)
        vPanel.add(HTML('<a href="http://google.com" target="myFrame">Google</a>'))
        vPanel.add(HTML('<a href="http://yahoo.com" target="myFrame">Yahoo</a>'))

        self.add(vPanel)




class ButtonDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        btn = Button("Click Me", getattr(self, "onButtonClick"))
        self.add(btn)


    def onButtonClick(self):
        Window.alert("Ouch!")





class TreeDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        tree = Tree()
        tree.addTreeListener(self)

        s1 = self.createItem("Section 1")
        s1.addItem(self.createItem("Item 1.1", value=11))
        s1.addItem(self.createItem("Item 1.2", value=12))

        s2 = self.createItem("Section 2")
        s2.addItem(self.createItem("Item 2.1", value=21))
        s2.addItem(self.createItem("Item 2.2", value=22))

        s1.setState(True, fireEvents=False)
        s2.setState(True, fireEvents=False)

        tree.addItem(s1)
        tree.addItem(s2)
        self.add(tree)


    def createItem(self, label, value=None):
        item = TreeItem(label)
        DOM.setStyleAttribute(item.getElement(), "cursor", "pointer")
        if value != None:
            item.setUserObject(value)
        return item


    def onTreeItemSelected(self, item):
        value = item.getUserObject()
        Window.alert("You clicked on " + value)


    def onTreeItemStateChanged(self, item):
        pass # We ignore this.





class HtmlPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        id1 = HTMLPanel.createUniqueId()
        id2 = HTMLPanel.createUniqueId()

        panel = HTMLPanel('<b>This is some HTML</b><br>' +
                          'First widget:<span id="' + id1 + '"></span><br>' +
                          'Second widget:<span id="' + id2 + '"></span><br>' +
                          'More <i>HTML</i>')

        panel.add(Button("Hi there"), id1)
        panel.add(Label("This label intentionally left blank"), id2)

        self.add(panel)





class DockPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = DockPanel()
        panel.setBorderWidth(1)

        north  = Label("North")
        west   = Label("West")
        center = Label("Center")
        east   = Label("East")
        south  = Label("South")

        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)

        panel.add(north,  DockPanel.NORTH)
        panel.add(west,   DockPanel.WEST)
        panel.add(center, DockPanel.CENTER)
        panel.add(east,   DockPanel.EAST)
        panel.add(south,  DockPanel.SOUTH)

        panel.setCellHeight(center, "200px")
        panel.setCellWidth(center, "400px")

        self.add(panel)




def getDemos():
    demos = []
    demos.append({"name" : "absolutePanel",
                  "title" : "ui.AbsolutePanel",
                  "section" : "panels",
                  "doc" : """``ui.AbsolutePanel`` is a panel that positions its children using absolute pixel positions.  This allows the panel's children to overlap.

Note that the AbsolutePanel does not automatically resize itself to fit its children.  There is no straightforward way of doing this unless all the children are explicitly sized; the easier workaround is just to call ``panel.setWidth(width)`` and ``panel.setHeight(height)`` explicitly after adding the children, choosing an appropriate width and height based on the children you have added. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>absolutePanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">AbsolutePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">DOM</font>


<font color="#0000AF"><b>class</b></font> <font color="#0000FF">AbsolutePanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">AbsolutePanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">makeBox</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Child 1"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#FF2200">20</font><font color="#303000"><b>,</b></font> <font color="#FF2200">10</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">makeBox</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Child 2"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#FF2200">30</font><font color="#303000"><b>,</b></font> <font color="#FF2200">30</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">makeBox</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">label</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">wrapper</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">wrapper</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">wrapper</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#000000">label</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">DOM</font><font color="#303000"><b>.</b></font><font color="#000000">setIntAttribute</font><font color="#303000"><b>(</b></font><font color="#000000">wrapper</font><font color="#303000"><b>.</b></font><font color="#000000">getTable</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"cellPadding"</font><font color="#303000"><b>,</b></font> <font color="#FF2200">10</font><font color="#303000"><b>)</b></font>
        <font color="#000000">DOM</font><font color="#303000"><b>.</b></font><font color="#000000">setAttribute</font><font color="#303000"><b>(</b></font><font color="#000000">wrapper</font><font color="#303000"><b>.</b></font><font color="#000000">getTable</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"bgColor"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"#C3D9FF"</font><font color="#303000"><b>)</b></font>

        <font color="#0000AF"><b>return</b></font> <font color="#000000">wrapper</font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : AbsolutePanelDemo()})

    demos.append({"name" : "dialogBox",
                  "title" : "ui.DialogBox",
                  "section" : "panels",
                  "doc" : """The ``ui.DialogBox`` class implements a panel that behaves like a dialog box.

A dialog box has an optional caption, and a widget which is displayed as the main part of the dialog box.  The user can drag the dialog box around by clicking on the caption.

The DialogBox class makes use of stylesheet definitions; if these are not supplied, the dialog box will look very strange.  The following stylesheet definitions are used by the example shown below:

<blockquote><pre>    .gwt-DialogBox {
      border: 2px outset;
      background-color: white;
    }</pre></blockquote>

<blockquote><pre>    .gwt-DialogBox .Caption {
      background-color: #C3D9FF;
      padding: 3px;
      margin: 2px;
      font-weight: bold;
      cursor: default;
    }</pre></blockquote>

<blockquote><pre>    .gwt-DialogBox .Contents {
        padding: 10px;
    }</pre></blockquote>

Because the ``DialogBox`` class is derived from ``PopupPanel``, the user should be able to click outside the dialog box to close it.  However, because of a problem with Firefox 3, this does not work.  To get around this, the example shown below implements a "Close" button the user can click on. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>dialogBox.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">DialogBox</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">DialogBoxDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Show Dialog"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"showDialog"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">showDialog</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">contents</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">contents</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>)</b></font>
        <font color="#000000">contents</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'You can place any contents you like in a dialog box.'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">contents</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Close"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onClose"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">contents</font><font color="#303000"><b>.</b></font><font color="#000000">setStyleName</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Contents"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font> <font color="#303000"><b>=</b></font> <font color="#000000">DialogBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font><font color="#303000"><b>.</b></font><font color="#000000">setHTML</font><font color="#303000"><b>(</b></font><font color="#600080">'&lt;b&gt;Welcome to the dialog box&lt;/b&gt;'</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font><font color="#303000"><b>.</b></font><font color="#000000">setWidget</font><font color="#303000"><b>(</b></font><font color="#000000">contents</font><font color="#303000"><b>)</b></font>

        <font color="#000000">left</font> <font color="#303000"><b>=</b></font> <font color="#303000"><b>(</b></font><font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">getClientWidth</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font> <font color="#303000"><b>-</b></font> <font color="#FF2200">200</font><font color="#303000"><b>)</b></font> <font color="#303000"><b>/</b></font> <font color="#FF2200">2</font>
        <font color="#000000">top</font> <font color="#303000"><b>=</b></font> <font color="#303000"><b>(</b></font><font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">getClientHeight</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font> <font color="#303000"><b>-</b></font> <font color="#FF2200">100</font><font color="#303000"><b>)</b></font> <font color="#303000"><b>/</b></font> <font color="#FF2200">2</font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font><font color="#303000"><b>.</b></font><font color="#000000">setPopupPosition</font><font color="#303000"><b>(</b></font><font color="#000000">left</font><font color="#303000"><b>,</b></font> <font color="#000000">top</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font><font color="#303000"><b>.</b></font><font color="#000000">show</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onClose</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_dialog</font><font color="#303000"><b>.</b></font><font color="#000000">hide</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : DialogBoxDemo()})

    demos.append({"name" : "dockPanel",
                  "title" : "ui.DockPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.DockPanel`` class divides the panel into five pieces, arranged into North, South, East, West and center pieces.  In general the outer pieces are smaller, with the centre holding the main part of the panel's contents, as shown below.

You can set the alignment and size for each widget within the DockPanel, by calling ``setCellHorizontalAlignment(widget, alignment)``, ``setCellVerticalAlignment(widget, alignment)``, ``setCellHeight(widget, height)`` and ``setCellWidth(widget, width)``.  You can also set the default horizontal and vertical alignment to use for new widgets by calling ``setHorizontalAlignment()`` and ``setVerticalAlignment()`` before the widget is added. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>dockPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">DockPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">DockPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">DockPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>

        <font color="#000000">north</font>  <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"North"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">west</font>   <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"West"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">center</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Center"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">east</font>   <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"East"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">south</font>  <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"South"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHorizontalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_CENTER</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setVerticalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_MIDDLE</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">north</font><font color="#303000"><b>,</b></font>  <font color="#000000">DockPanel</font><font color="#303000"><b>.</b></font><font color="#000000">NORTH</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">west</font><font color="#303000"><b>,</b></font>   <font color="#000000">DockPanel</font><font color="#303000"><b>.</b></font><font color="#000000">WEST</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">center</font><font color="#303000"><b>,</b></font> <font color="#000000">DockPanel</font><font color="#303000"><b>.</b></font><font color="#000000">CENTER</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">east</font><font color="#303000"><b>,</b></font>   <font color="#000000">DockPanel</font><font color="#303000"><b>.</b></font><font color="#000000">EAST</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">south</font><font color="#303000"><b>,</b></font>  <font color="#000000">DockPanel</font><font color="#303000"><b>.</b></font><font color="#000000">SOUTH</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHeight</font><font color="#303000"><b>(</b></font><font color="#000000">center</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"200px"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellWidth</font><font color="#303000"><b>(</b></font><font color="#000000">center</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"400px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : DockPanelDemo()})

    demos.append({"name" : "flexTable",
                  "title" : "ui.FlexTable",
                  "section" : "panels",
                  "doc" : """The ``ui.FlexTable`` class implements a table that can have different numbers of cells in each row, and single cells can span multiple rows and columns.

Each FlexTable has a ``FlexCellFormatter`` which you can use to format the cells in the table.  The ``FlexCellFormatter`` has methods to set the row or column spans for a cell, as well as change the cell alignment, as shown below.

Note that if you use row or column spanning, the cells on the rest of that row or column will be moved over.  This can cause some surprising results.  Imagine that you have a table like this:

<blockquote><pre>    +---+---+---+
    | A | B | C |
    +---+---+---+
    | D | E | F |
    +---+---+---+</pre></blockquote>

If you set up Cell 0,0 to span two columns, like this:

<blockquote><pre>    flexTable.getFlexCellFormatter().setColSpan(0, 0, 2)</pre></blockquote>

This will cause the table to end up looking like this:

<blockquote><pre>    +-------+---+---+
    |   A   | B | C |
    +---+---+---+---+
    | D | E | F |
    +---+---+---+</pre></blockquote>

you might expect cell B to be above cell E, but to make this happen you need to place cell E at (1, 2) rather than (1, 1).

Each FlexTable also has a ``RowFormatter`` which can be used to change style names, attributes, and the visibility of rows in the table. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>flexTable.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FlexTable</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">FlexTableDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font> <font color="#303000"><b>=</b></font> <font color="#000000">FlexTable</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">cellFormatter</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">getFlexCellFormatter</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">getRowFormatter</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setHTML</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"&lt;b&gt;Mammals&lt;/b&gt;"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Cow"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Rat"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Dog"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">cellFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setColSpan</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">3</font><font color="#303000"><b>)</b></font>
        <font color="#000000">cellFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setHorizontalAlignment</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_CENTER</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setWidget</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Hide"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"hideRows"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"1,1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"2,1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">3</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"1,2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#FF2200">3</font><font color="#303000"><b>,</b></font> <font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"2,2"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">cellFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setRowSpan</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">cellFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVerticalAlignment</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_MIDDLE</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">setWidget</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Show"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"showRows"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">cellFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setColSpan</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">3</font><font color="#303000"><b>)</b></font>

        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">hideRows</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">rowFormatter</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">getRowFormatter</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">3</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>,</b></font> <font color="#000000">True</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">showRows</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">rowFormatter</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_table</font><font color="#303000"><b>.</b></font><font color="#000000">getRowFormatter</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>,</b></font> <font color="#000000">True</font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">3</font><font color="#303000"><b>,</b></font> <font color="#000000">True</font><font color="#303000"><b>)</b></font>
        <font color="#000000">rowFormatter</font><font color="#303000"><b>.</b></font><font color="#000000">setVisible</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : FlexTableDemo()})

    demos.append({"name" : "flowPanel",
                  "title" : "ui.FlowPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.FlowPanel`` is a panel that allows its contents to "flow" from left to right, and then from top to bottom, like words on a page.

Because of the way it works, only the width of a FlowPanel needs to be specified; it will automatically take up as much height as is needed to fit the panel's contents.

Unfortunately, the implementation of the FlowPanel is actually quite limited, because of the way other widgets are typically implemented.  Many widgets are wrapped up in a ``<div>`` element, which is a block-level element that overrules the ``<span>`` element used by the FlowPanel, which is an inline element.  As a result, if you add a ``ui.Label`` to a FlowPanel, for example, it will still appear on a line by itself rather than flowing with the other elements.  Because of this, you may want to avoid using FlowPanel unless you are certain that the items you are adding will flow correctly. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>flowPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FlowPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">FlowPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">flow</font> <font color="#303000"><b>=</b></font> <font color="#000000">FlowPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 3"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 4"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 5"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 6"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 7"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 8"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 9"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 10"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">flow</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"400px"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">flow</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : FlowPanelDemo()})

    demos.append({"name" : "formPanel",
                  "title" : "ui.FormPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.FormPanel`` class implements a traditional HTML form.

Any ``TextBox``, ``PasswordTextBox``, ``TextArea``, ``RadioButton``, ``CheckBox``, ``ListBox``, ``FileUpload`` and ``Hidden`` fields contained within the form panel will be sent to the server when the form is submitted.

The example below calls Google to perform a search using the query entered by the user into the text field.  The results are shown in a separate Frame. Alternatively, you can call ``Form.addFormHandler(handler)`` to manually process the results of posting the form.  When this is done, ``handler.onSubmit(event)`` will be called when the user is about to submit the form; call ``event.setCancelled(True)`` to cancel the event within this method. Also, ``handler.onSubmitComplete(event)`` will be called when the results of submitting the form are returned back to the browser.  Call ``event.getResults()`` to retrieve the (plain-text) value returned by the server.

Note that if you use a ``ui.FileUpload`` widget in your form, you must set the form encoding and method like this:

<blockquote><pre>        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)</pre></blockquote>

This will ensure that the form is submitted in a way that allows files to be uploaded. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>formPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">TextBox</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">FormPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font> <font color="#303000"><b>=</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setAction</font><font color="#303000"><b>(</b></font><font color="#A0008A">"http://google.com/search"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setTarget</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Search for:"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font> <font color="#303000"><b>=</b></font> <font color="#000000">TextBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setName</font><font color="#303000"><b>(</b></font><font color="#A0008A">"q"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Submit"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onBtnClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">hPanel</font><font color="#303000"><b>)</b></font>

        <font color="#000000">results</font> <font color="#303000"><b>=</b></font> <font color="#000000">NamedFrame</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">results</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">vPanel</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onBtnClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">submit</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : FormPanelDemo()})

    demos.append({"name" : "grid",
                  "title" : "ui.Grid",
                  "section" : "panels",
                  "doc" : """The ``ui.Grid`` class implements a panel which lays its contents out in a grid-like fashion, very like an HTML table.

You can use the ``setHTML(row, col, html)`` method to set the HTML-formatted text to be displayed at the given row and column within the grid.  Similarly, you can call ``setText(row, col, text)`` to display plain (unformatted) text at the given row and column. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>grid.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Grid</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">GridDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">grid</font> <font color="#303000"><b>=</b></font> <font color="#000000">Grid</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>,</b></font> <font color="#FF2200">5</font><font color="#303000"><b>)</b></font>
        <font color="#000000">grid</font><font color="#303000"><b>.</b></font><font color="#000000">setHTML</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#FF2200">0</font><font color="#303000"><b>,</b></font> <font color="#600080">'&lt;b&gt;Hello, World!&lt;/b&gt;'</font><font color="#303000"><b>)</b></font>
        <font color="#000000">grid</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">grid</font><font color="#303000"><b>.</b></font><font color="#000000">setCellPadding</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>)</b></font>
        <font color="#000000">grid</font><font color="#303000"><b>.</b></font><font color="#000000">setCellSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>

        <font color="#0000AF"><b>for</b></font> <font color="#000000">row</font> <font color="#0000AF"><b>in</b></font> <font color="#000000">range</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#FF2200">5</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
            <font color="#0000AF"><b>for</b></font> <font color="#000000">col</font> <font color="#0000AF"><b>in</b></font> <font color="#000000">range</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>,</b></font> <font color="#FF2200">5</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
                <font color="#000000">grid</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#000000">row</font><font color="#303000"><b>,</b></font> <font color="#000000">col</font><font color="#303000"><b>,</b></font> <font color="#000000">str</font><font color="#303000"><b>(</b></font><font color="#000000">row</font><font color="#303000"><b>)</b></font> <font color="#303000"><b>+</b></font> <font color="#A0008A">"*"</font> <font color="#303000"><b>+</b></font> <font color="#000000">str</font><font color="#303000"><b>(</b></font><font color="#000000">col</font><font color="#303000"><b>)</b></font> <font color="#303000"><b>+</b></font> <font color="#A0008A">" = "</font> <font color="#303000"><b>+</b></font> <font color="#000000">str</font><font color="#303000"><b>(</b></font><font color="#000000">row</font><font color="#303000"><b>*</b></font><font color="#000000">col</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">grid</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : GridDemo()})

    demos.append({"name" : "horizontalPanel",
                  "title" : "ui.HorizontalPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.HorizontalPanel`` class is a panel that lays out its contents from left to right.

It is often useful to call ``setSpacing(spacing)`` to add space between each of the panel's widgets.  You can also call ``setHorizontalAlignment(alignment)`` and ``setVerticalAlignment(alignment)`` before adding widgets to control how those widgets are aligned within the available space.  Alternatively, you can call ``setCellHorizontalAlignment(widget, alignment)`` and ``setCellVerticalAlignment(widget, alignment)`` to change the alignment of a single widget after it has been added.

Note that if you want to have different widgets within the panel take up different amounts of space, don't call ``widget.setWidth(width)`` or ``widget.setHeight(height)`` as these are ignored by the panel.  Instead, call ``panel.setCellWidth(widget, width)`` and ``panel.setCellHeight(widget, height)``. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>horizontalPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">HorizontalPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHorizontalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_CENTER</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setVerticalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_MIDDLE</font><font color="#303000"><b>)</b></font>

        <font color="#000000">part1</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part2</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part3</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 3"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part4</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 4"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part4</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellWidth</font><font color="#303000"><b>(</b></font><font color="#000000">part1</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellWidth</font><font color="#303000"><b>(</b></font><font color="#000000">part2</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"70%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellWidth</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellWidth</font><font color="#303000"><b>(</b></font><font color="#000000">part4</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellVerticalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_BOTTOM</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"200px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : HorizontalPanelDemo()})

    demos.append({"name" : "htmlPanel",
                  "title" : "ui.HtmlPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.HTMLPanel`` class allows you to include HTML within your application, and embed other widgets inside the panel's contents by wrapping them inside a ``&lt;span&gt;`` tag. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>htmlPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTMLPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">HtmlPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">id1</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTMLPanel</font><font color="#303000"><b>.</b></font><font color="#000000">createUniqueId</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">id2</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTMLPanel</font><font color="#303000"><b>.</b></font><font color="#000000">createUniqueId</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTMLPanel</font><font color="#303000"><b>(</b></font><font color="#600080">'&lt;b&gt;This is some HTML&lt;/b&gt;&lt;br&gt;'</font> <font color="#303000"><b>+</b></font>
                          <font color="#600080">'First widget:&lt;span id="'</font> <font color="#303000"><b>+</b></font> <font color="#000000">id1</font> <font color="#303000"><b>+</b></font> <font color="#600080">'"&gt;&lt;/span&gt;&lt;br&gt;'</font> <font color="#303000"><b>+</b></font>
                          <font color="#600080">'Second widget:&lt;span id="'</font> <font color="#303000"><b>+</b></font> <font color="#000000">id2</font> <font color="#303000"><b>+</b></font> <font color="#600080">'"&gt;&lt;/span&gt;&lt;br&gt;'</font> <font color="#303000"><b>+</b></font>
                          <font color="#600080">'More &lt;i&gt;HTML&lt;/i&gt;'</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Hi there"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#000000">id1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"This label intentionally left blank"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#000000">id2</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : HtmlPanelDemo()})

    demos.append({"name" : "popupPanel",
                  "title" : "ui.PopupPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.PopupPanel`` class implements a panel that pops up in the browser window to display some contents.  When the user clicks outside the popup, it disappears again.

The PopupPanel requires stylesheet definitions in order to work properly.  The following stylesheet definitions were used in the example below:

<blockquote><pre>    .showcase-popup {
        background-color: white;
        border: 1px solid #87B3FF;
        padding: 4px;
    }</pre></blockquote>

Note that the popup panel is supposed to close when the user clicks outside of it.  However, this doesn't work under Firefox 3, so the code below adds a click handler so the user can click on the popup itself to close it. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>popupPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font><font color="#303000"><b>,</b></font> <font color="#000000">PopupPanel</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">PopupPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_btn</font> <font color="#303000"><b>=</b></font> <font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Click Me"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"showPopup"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Click on the button below to display the popup."</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_btn</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">vPanel</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">showPopup</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">contents</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Hello, World!"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">contents</font><font color="#303000"><b>.</b></font><font color="#000000">addClickListener</font><font color="#303000"><b>(</b></font><font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font> <font color="#303000"><b>=</b></font> <font color="#000000">PopupPanel</font><font color="#303000"><b>(</b></font><font color="#000000">autoHide</font><font color="#303000"><b>=</b></font><font color="#000000">True</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">contents</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font><font color="#303000"><b>.</b></font><font color="#000000">setStyleName</font><font color="#303000"><b>(</b></font><font color="#A0008A">"showcase-popup"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">left</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_btn</font><font color="#303000"><b>.</b></font><font color="#000000">getAbsoluteLeft</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font> <font color="#303000"><b>+</b></font> <font color="#FF2200">10</font>
        <font color="#000000">top</font>  <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_btn</font><font color="#303000"><b>.</b></font><font color="#000000">getAbsoluteTop</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font> <font color="#303000"><b>+</b></font> <font color="#FF2200">10</font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font><font color="#303000"><b>.</b></font><font color="#000000">setPopupPosition</font><font color="#303000"><b>(</b></font><font color="#000000">left</font><font color="#303000"><b>,</b></font> <font color="#000000">top</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font><font color="#303000"><b>.</b></font><font color="#000000">show</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_popup</font><font color="#303000"><b>.</b></font><font color="#000000">hide</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : PopupPanelDemo()})

    demos.append({"name" : "scrollPanel",
                  "title" : "ui.ScrollPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.ScrollPanel`` class implements a panel that scrolls its contents.

If you want the scroll bars to be always visible, call ``setAlwaysShowScrollBars(True)``.  You can also change the current scrolling position programmatically by calling ``setScrollPosition(vPos)`` and ``setScrollHorizontalPosition(hPos)`` to change the horizontal and vertical scrolling position, respectively. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>scrollPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">ScrollPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">ScrollPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">ScrollPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">contents</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"&lt;b&gt;Tao Te Ching, Chapter One&lt;/b&gt;&lt;p&gt;"</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"The Way that can be told of is not an unvarying "</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"way;&lt;p&gt;The names that can be named are not "</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"unvarying names.&lt;p&gt;It was from the Nameless that "</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"Heaven and Earth sprang;&lt;p&gt;The named is but the "</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"mother that rears the ten thousand creatures, "</font> <font color="#303000"><b>+</b></font>
                        <font color="#A0008A">"each after its kind."</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">contents</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setSize</font><font color="#303000"><b>(</b></font><font color="#A0008A">"300px"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"100px"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : ScrollPanelDemo()})

    demos.append({"name" : "stackPanel",
                  "title" : "ui.StackPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.StackPanel`` class displays a "stack" of sub-panels where only one sub-panel is open at a time.

The StackPanel relies heavily on stylesheet definitions to make it look good; the default look of a StackPanel without any styles defined is almost unusable. The following stylesheet definitions were used for the example given below:

<blockquote><pre>    .gwt-StackPanel {
        border: 5px solid #999999;
        background-color: #CCCCCC;
        border-collapse: collapse;
    }</pre></blockquote>

<blockquote><pre>    .gwt-StackPanel .gwt-StackPanelItem {
        border: 2px solid #000099;
        background-color: #FFFFCC;
        cursor: pointer;
        font-weight: normal;
    }</pre></blockquote>

<blockquote><pre>    .gwt-StackPanel .gwt-StackPanelItem-selected {
        border: 3px solid #FF0000;
        background-color: #FFFF66;
        cursor: default;
        font-weight: bold;
    }</pre></blockquote>

You can programatically change the currently-open panel by calling the ``setStackVisible(index, visible)`` method.  To find out which panel is currently open, call ``getSelectedIndex()``.  To retrieve the widget at a given index, call ``getWidget(index)``.  Finally, you can change the label for a stack item by calling ``setStackText(index, text)``. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>stackPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">StackPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">StackPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">stack</font> <font color="#303000"><b>=</b></font> <font color="#000000">StackPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">stack</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'The quick&lt;br&gt;brown fox&lt;br&gt;jumps over the&lt;br&gt;lazy dog.'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font>
                  <font color="#A0008A">"Stack 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">stack</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'The&lt;br&gt;early&lt;br&gt;bird&lt;br&gt;catches&lt;br&gt;the&lt;br&gt;worm.'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font>
                  <font color="#A0008A">"Stack 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">stack</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'The smart money&lt;br&gt;is on the&lt;br&gt;black horse.'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font>
                  <font color="#A0008A">"Stack 3"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">stack</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">stack</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : StackPanelDemo()})

    demos.append({"name" : "tabPanel",
                  "title" : "ui.TabPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.TabPanel`` class implements a tabbed window, where clicking on a tab causes the associated contents to be displayed.

The TabPanel relies heavily on cascading stylesheet definitions to operate. The following stylesheet definitions are used by the example shown below:

<blockquote><pre>    .gwt-TabPanel {
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabPanelBottom {
      border: 1px solid #87B3FF;
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabBar {
      background-color: #C3D9FF;
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabBar .gwt-TabBarFirst {
      height: 100%;
      padding-left: 3px;
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabBar .gwt-TabBarRest {
      padding-right: 3px;
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabBar .gwt-TabBarItem {
      border-top: 1px solid #C3D9FF;
      border-bottom: 1px solid #C3D9FF;
      padding: 2px;
      cursor: pointer;
    }</pre></blockquote>

<blockquote><pre>    .gwt-TabBar .gwt-TabBarItem-selected {
      font-weight: bold;
      background-color: #E8EEF7;
      border-top: 1px solid #87B3FF;
      border-left: 1px solid #87B3FF;
      border-right: 1px solid #87B3FF;
      border-bottom: 1px solid #E8EEF7;
      padding: 2px;
      cursor: default;
    }</pre></blockquote>

""",
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>tabPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">TabPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">TabPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">tabs</font> <font color="#303000"><b>=</b></font> <font color="#000000">TabPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"The quick brown fox jumps over the lazy dog."</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Tab 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"The early bird catches the worm."</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Tab 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"The smart money is on the black horse."</font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Tab 3"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">selectTab</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>)</b></font>
        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">tabs</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"250px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">tabs</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : TabPanelDemo()})

    demos.append({"name" : "verticalPanel",
                  "title" : "ui.VerticalPanel",
                  "section" : "panels",
                  "doc" : """The ``ui.VerticalPanel`` class is a panel that lays out its contents from top to bottom.

It is often useful to call ``setSpacing(spacing)`` to add space between each of the panel's widgets.  You can also call ``setHorizontalAlignment(alignment)`` and ``setVerticalAlignment(alignment)`` before adding widgets to control how those widgets are aligned within the available space.  Alternatively, you can call ``setCellHorizontalAlignment(widget, alignment)`` and ``setCellVerticalAlignment(widget, alignment)`` to change the alignment of a single widget after it has been added.

Note that if you want to have different widgets within the panel take up different amounts of space, don't call ``widget.setWidth(width)`` or ``widget.setHeight(height)`` as these are ignored by the panel.  Instead, call ``panel.setCellWidth(widget, width)`` and ``panel.setCellHeight(widget, height)``. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>verticalPanel.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">VerticalPanelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setBorderWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">1</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHorizontalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_CENTER</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setVerticalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_MIDDLE</font><font color="#303000"><b>)</b></font>

        <font color="#000000">part1</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part2</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part3</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 3"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">part4</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Part 4"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">part4</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHeight</font><font color="#303000"><b>(</b></font><font color="#000000">part1</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHeight</font><font color="#303000"><b>(</b></font><font color="#000000">part2</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"70%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHeight</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHeight</font><font color="#303000"><b>(</b></font><font color="#000000">part4</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"10%"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setCellHorizontalAlignment</font><font color="#303000"><b>(</b></font><font color="#000000">part3</font><font color="#303000"><b>,</b></font> <font color="#000000">HasAlignment</font><font color="#303000"><b>.</b></font><font color="#000000">ALIGN_RIGHT</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"50%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"300px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : VerticalPanelDemo()})

    demos.append({"name" : "button",
                  "title" : "ui.Button",
                  "section" : "widgets",
                  "doc" : """The ``ui.Button`` class is used to show a button.  When the user clicks on the button, the given listener function is called.

Note that you can use the ``getattr()`` function to specify which method you want called when the button is clicked.  This is the best way to write button click handlers if you have more than one button on your panel.  If you have only one button, you can use ``btn = Button("...", self)`` instead, and define a method called ``onClick()`` to respond to the button click.

Another useful method is ``Button.setEnabled(enabled)``, which enables or disables the button depending on the value of its parameter. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>button.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">ButtonDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">btn</font> <font color="#303000"><b>=</b></font> <font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Click Me"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onButtonClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">btn</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onButtonClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Ouch!"</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : ButtonDemo()})

    demos.append({"name" : "checkBox",
                  "title" : "ui.CheckBox",
                  "section" : "widgets",
                  "doc" : """The ``ui.CheckBox`` class is used to show a standard checkbox.  When the user clicks on the checkbox, the checkbox's state is toggled.

The ``setChecked(checked)`` method checks or unchecks the checkbox depending on the value of the parameter.  To get the current value of the checkbox, call ``isChecked()``.

You can enable or disable a checkbox using ``setEnabled(enabled)``.  You can also call ``addClickListener()`` to respond when the user clicks on the checkbox, as shown below.  This can be useful when building complicated input screens where checking a checkbox causes other input fields to be enabled. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>checkBox.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">CheckBox</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">CheckBoxDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">box</font> <font color="#303000"><b>=</b></font> <font color="#000000">CheckBox</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Print Results?"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">box</font><font color="#303000"><b>.</b></font><font color="#000000">addClickListener</font><font color="#303000"><b>(</b></font><font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">box</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"checkbox status: "</font> <font color="#303000"><b>+</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">box</font><font color="#303000"><b>.</b></font><font color="#000000">isChecked</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : CheckBoxDemo()})

    demos.append({"name" : "fileUpload",
                  "title" : "ui.FileUpload",
                  "section" : "widgets",
                  "doc" : """The ``ui.FileUpload`` class implements a file uploader widget.

The FileUpload widget must be inside a ``ui.FormPanel`` which is used to submit the HTML form to the server.  Note that you must set the form encoding and method like this:

<blockquote><pre>        self.form.setEncoding(FormPanel.ENCODING_MULTIPART)
        self.form.setMethod(FormPanel.METHOD_POST)</pre></blockquote>

This will ensure that the form is submitted in a way that allows files to be uploaded.

The example below doesn't really work, as there is no suitable server at ``nonexistent.com``.  However, it does show how a file upload widget could be used within a FormPanel. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>fileUpload.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FileUpload</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">FileUploadDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font> <font color="#303000"><b>=</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setEncoding</font><font color="#303000"><b>(</b></font><font color="#000000">FormPanel</font><font color="#303000"><b>.</b></font><font color="#000000">ENCODING_MULTIPART</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setMethod</font><font color="#303000"><b>(</b></font><font color="#000000">FormPanel</font><font color="#303000"><b>.</b></font><font color="#000000">METHOD_POST</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setAction</font><font color="#303000"><b>(</b></font><font color="#A0008A">"http://nonexistent.com"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setTarget</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Upload file:"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font> <font color="#303000"><b>=</b></font> <font color="#000000">FileUpload</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setName</font><font color="#303000"><b>(</b></font><font color="#A0008A">"file"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">field</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Submit"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onBtnClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">hPanel</font><font color="#303000"><b>)</b></font>

        <font color="#000000">results</font> <font color="#303000"><b>=</b></font> <font color="#000000">NamedFrame</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">results</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">vPanel</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onBtnClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">submit</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : FileUploadDemo()})

    demos.append({"name" : "frame",
                  "title" : "ui.Frame",
                  "section" : "widgets",
                  "doc" : """The ``ui.Frame`` class is used to embed a separate HTML page within your application.

If you pass a URL when the Frame is created, that URL will be used immediately. Alternatively, you can call the ``Frame.setUrl()`` method to change the URL at any time.  You can also call ``Frame.getUrl()`` to retrieve the current URL for this frame. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>frame.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Frame</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">FrameDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">frame</font> <font color="#303000"><b>=</b></font> <font color="#000000">Frame</font><font color="#303000"><b>(</b></font><font color="#A0008A">"http://google.com"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">frame</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">frame</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"200px"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">frame</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : FrameDemo()})

    demos.append({"name" : "hidden",
                  "title" : "ui.Hidden",
                  "section" : "widgets",
                  "doc" : """The ``ui.Hidden`` class represents a hidden form field.

This is really only useful when the hidden field is part of a ``ui.FormPanel``. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>hidden.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Hidden</font><font color="#303000"><b>,</b></font> <font color="#000000">Button</font><font color="#303000"><b>,</b></font> <font color="#000000">NamedFrame</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">HiddenDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font> <font color="#303000"><b>=</b></font> <font color="#000000">FormPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setAction</font><font color="#303000"><b>(</b></font><font color="#A0008A">"http://google.com/search"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">setTarget</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Hidden</font><font color="#303000"><b>(</b></font><font color="#A0008A">"q"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"python pyjamas"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Button</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Search"</font><font color="#303000"><b>,</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onBtnClick"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">results</font> <font color="#303000"><b>=</b></font> <font color="#000000">NamedFrame</font><font color="#303000"><b>(</b></font><font color="#A0008A">"results"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">results</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onBtnClick</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">form</font><font color="#303000"><b>.</b></font><font color="#000000">submit</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : HiddenDemo()})

    demos.append({"name" : "html",
                  "title" : "ui.Html",
                  "section" : "widgets",
                  "doc" : """The ``ui.HTML`` class displays HTML-formatted text.  To display unformatted text, use ``ui.Label``. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>html.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">HtmlDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">html</font> <font color="#303000"><b>=</b></font> <font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Hello, &lt;b&gt;&lt;i&gt;World!&lt;/i&gt;&lt;/b&gt;"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">html</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : HtmlDemo()})

    demos.append({"name" : "hyperlink",
                  "title" : "ui.Hyperlink",
                  "section" : "widgets",
                  "doc" : """The ``ui.Hyperlink`` class acts as an "internal" hyperlink to a particular state of the application.  These states are stored in the application's history, allowing for the use of the Back and Next buttons in the browser to move between application states.

The ``ui.Hyperlink`` class only makes sense in an application which keeps track of state using the ``History`` module.  When the user clicks on a hyperlink, the application changes state by calling ``History.newItem(newState)``.  The application then uses a history listener function to respond to the change in state in whatever way makes sense. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>hyperlink.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Hyperlink</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font>
<font color="#0000AF"><b>from</b></font> <font color="#000000">History</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">History</font>


<font color="#0000AF"><b>class</b></font> <font color="#0000FF">HyperlinkDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">History</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>.</b></font><font color="#000000">addHistoryListener</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">stateDisplay</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">stateDisplay</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Hyperlink</font><font color="#303000"><b>(</b></font><font color="#A0008A">"State 1"</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"state number 1"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">Hyperlink</font><font color="#303000"><b>(</b></font><font color="#A0008A">"State 2"</font><font color="#303000"><b>,</b></font> <font color="#000000">False</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"state number 2"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">hPanel</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">vPanel</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onHistoryChanged</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">state</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">stateDisplay</font><font color="#303000"><b>.</b></font><font color="#000000">setText</font><font color="#303000"><b>(</b></font><font color="#000000">state</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : HyperlinkDemo()})

    demos.append({"name" : "image",
                  "title" : "ui.Image",
                  "section" : "widgets",
                  "doc" : """The ``ui.Image`` class is used to display an image.

The ``Image`` class can display any image that is specified by a URL.  This can be an image stored somewhere on the internet, or alternatively you can store an image in the "public" directory within your application's source folder, and then access it using a relative URL, as shown below.

In this example, the image file named "myImage.jpg" is stored inside the "images" sub-directory, which is in the "public" directory within the application's main source directory.

As well as passing the image URL to the initialiser, you can call ``setURL()`` to change the image being displayed at any time.  You can also call ``addClickListener()`` to add a listener function to be called when the user clicks on the image. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>image.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Image</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">ImageDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#007F00"># We display the "myImage.jpg" file, stored in the "public/images"
</font>        <font color="#007F00"># directory, where "public" is in the application's source directory.
</font>
        <font color="#000000">img</font> <font color="#303000"><b>=</b></font> <font color="#000000">Image</font><font color="#303000"><b>(</b></font><font color="#A0008A">"images/myImage.jpg"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">img</font><font color="#303000"><b>.</b></font><font color="#000000">addClickListener</font><font color="#303000"><b>(</b></font><font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onImageClicked"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">img</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onImageClicked</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Stop that!"</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : ImageDemo()})

    demos.append({"name" : "label",
                  "title" : "ui.Label",
                  "section" : "widgets",
                  "doc" : """The ``ui.Label`` class is used to display unformatted text.  Unlike the ``ui.HTML`` class, it does not interpret HTML format codes.  If you pass False as the second parameter when creating your label, word wrapping will be disabled, forcing all the text to be on one line. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>label.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Label</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">LabelDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">label</font> <font color="#303000"><b>=</b></font> <font color="#000000">Label</font><font color="#303000"><b>(</b></font><font color="#A0008A">"This is a label"</font><font color="#303000"><b>,</b></font> <font color="#000000">wordWrap</font><font color="#303000"><b>=</b></font><font color="#000000">False</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">label</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : LabelDemo()})

    demos.append({"name" : "listBox",
                  "title" : "ui.ListBox",
                  "section" : "widgets",
                  "doc" : """The ``ui.ListBox`` class allows the user to select one or more items from a list.  There are two variations of the ListBox: a normal list of items the user can click on, and a dropdown menu of items.  Both variations are shown in the example below.

You add items to a list by calling ``ListBox.addItem()``.  This can take the label to display, and also an optional value to associate with that item in the list.  ``ListBox.getSelectedIndex()`` returns the index of the currently selected item, or -1 if nothing is selected.  ``ListBox.getItemText(n)`` returns the text for the given item in the list, while ``ListBox.getValue(n)`` returns the value associated with the given list item.  To detect when the user selects something from a ListBox, call ``addChangeLister()``.  And finally, ``ListBox.clear()`` clears the current contents of the ListBox. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>listBox.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">ListBox</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">ListBoxDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">10</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font> <font color="#303000"><b>=</b></font> <font color="#000000">ListBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">setVisibleItemCount</font><font color="#303000"><b>(</b></font><font color="#FF2200">10</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 3"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">addChangeListener</font><font color="#303000"><b>(</b></font><font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onList1ItemSelected"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font> <font color="#303000"><b>=</b></font> <font color="#000000">ListBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">setVisibleItemCount</font><font color="#303000"><b>(</b></font><font color="#FF2200">0</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item A"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item B"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item C"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">addChangeListener</font><font color="#303000"><b>(</b></font><font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onList2ItemSelected"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">hPanel</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onList1ItemSelected</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">item</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">getItemText</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list1</font><font color="#303000"><b>.</b></font><font color="#000000">getSelectedIndex</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"You selected "</font> <font color="#303000"><b>+</b></font> <font color="#000000">item</font> <font color="#303000"><b>+</b></font> <font color="#A0008A">" from list 1"</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onList2ItemSelected</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">item</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">getItemText</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">list2</font><font color="#303000"><b>.</b></font><font color="#000000">getSelectedIndex</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"You selected "</font> <font color="#303000"><b>+</b></font> <font color="#000000">item</font> <font color="#303000"><b>+</b></font> <font color="#A0008A">" from list 2"</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : ListBoxDemo()})

    demos.append({"name" : "menubar",
                  "title" : "ui.Menubar",
                  "section" : "widgets",
                  "doc" : """The ``ui.MenuBar`` and ``ui.MenuItem`` classes allow you to define menu bars in your application.

There are several important things to be aware of when adding menus to your application:

<ul><li>You have to use a stylesheet to define the look of your menu.  The default    style is terrible, as it makes the menu unusable.  The following stylesheet    entries were used for the example code below:</li></ul>

<blockquote><pre>        .gwt-MenuBar {
          background-color: #C3D9FF;
          border: 1px solid #87B3FF;
          cursor: default;
        }</pre></blockquote>

<blockquote><pre>        .gwt-MenuBar .gwt-MenuItem {
          padding: 1px 4px 1px 4px;
          font-size: smaller;
          cursor: default;
        }</pre></blockquote>

<blockquote><pre>        .gwt-MenuBar .gwt-MenuItem-selected {
          background-color: #E8EEF7;
        }</pre></blockquote>

<ul><li>By default, each menu item can be associated with a class, whose ``execute``    method will be called when that item is selected.  Note that a helper class,    ``MenuCmd``, is defined below to allow more than one menu item handler    method to be defined within a single class.</li></ul>

<ul><li>You add menu items directly, passing the item label and the associated    command to ``MenuBar.addItem()``.  For adding sub-menus, you need to wrap    the sub-menu up in a ``MenuItem``, as shown below.</li></ul>

<ul><li>You can use HTML codes in a menu item's label by calling    ``MenuBar.addItem(label, True, cmd)`` instead of ``MenuBar.addItem(label,    cmd)``.  Similarly, you can use HTML styling in a menu's title by calling    ``MenuItem(label, True, submenu)``, as in the second-to-last line of    ``MenubarDemo.__init__``, below. </li></ul>""",
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>menubar.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuBar</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuItem</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">MenubarDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">menu1</font> <font color="#303000"><b>=</b></font> <font color="#000000">MenuBar</font><font color="#303000"><b>(</b></font><font color="#000000">vertical</font><font color="#303000"><b>=</b></font><font color="#000000">True</font><font color="#303000"><b>)</b></font>
        <font color="#000000">menu1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1"</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuCmd</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onMenu1Item1"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">menu1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2"</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuCmd</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onMenu1Item2"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">menu2</font> <font color="#303000"><b>=</b></font> <font color="#000000">MenuBar</font><font color="#303000"><b>(</b></font><font color="#000000">vertical</font><font color="#303000"><b>=</b></font><font color="#000000">True</font><font color="#303000"><b>)</b></font>
        <font color="#000000">menu2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Apples"</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuCmd</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onMenu2Apples"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">menu2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Oranges"</font><font color="#303000"><b>,</b></font> <font color="#000000">MenuCmd</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"onMenu2Oranges"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">menubar</font> <font color="#303000"><b>=</b></font> <font color="#000000">MenuBar</font><font color="#303000"><b>(</b></font><font color="#000000">vertical</font><font color="#303000"><b>=</b></font><font color="#000000">False</font><font color="#303000"><b>)</b></font>
        <font color="#000000">menubar</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">MenuItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Menu 1"</font><font color="#303000"><b>,</b></font> <font color="#000000">menu1</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">menubar</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">MenuItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"&lt;i&gt;Menu 2&lt;/i&gt;"</font><font color="#303000"><b>,</b></font> <font color="#000000">True</font><font color="#303000"><b>,</b></font> <font color="#000000">menu2</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">menubar</font><font color="#303000"><b>)</b></font>

    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onMenu1Item1</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1 selected"</font><font color="#303000"><b>)</b></font>

    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onMenu1Item2</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2 selected"</font><font color="#303000"><b>)</b></font>

    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onMenu2Apples</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Apples selected"</font><font color="#303000"><b>)</b></font>

    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onMenu2Oranges</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Oranges selected"</font><font color="#303000"><b>)</b></font>


<font color="#0000AF"><b>class</b></font> <font color="#0000FF">MenuCmd</font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">object</font><font color="#303000"><b>,</b></font> <font color="#000000">handler</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_object</font>  <font color="#303000"><b>=</b></font> <font color="#000000">object</font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_handler</font> <font color="#303000"><b>=</b></font> <font color="#000000">handler</font>

    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">execute</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">handler</font> <font color="#303000"><b>=</b></font> <font color="#000000">getattr</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_object</font><font color="#303000"><b>,</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">_handler</font><font color="#303000"><b>)</b></font>
        <font color="#000000">handler</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : MenubarDemo()})

    demos.append({"name" : "namedFrame",
                  "title" : "ui.NamedFrame",
                  "section" : "widgets",
                  "doc" : """The ``ui.NamedFrame`` class is a variation of the ``ui.Frame`` which lets you assign a name to the frame.  Naming a frame allows you to refer to that frame by name in Javascript code, and as the target for a hyperlink. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>namedFrame.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">NamedFrame</font><font color="#303000"><b>,</b></font> <font color="#000000">HTML</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">NamedFrameDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">setSpacing</font><font color="#303000"><b>(</b></font><font color="#FF2200">5</font><font color="#303000"><b>)</b></font>

        <font color="#000000">frame</font> <font color="#303000"><b>=</b></font> <font color="#000000">NamedFrame</font><font color="#303000"><b>(</b></font><font color="#A0008A">"myFrame"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">frame</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100%"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">frame</font><font color="#303000"><b>.</b></font><font color="#000000">setHeight</font><font color="#303000"><b>(</b></font><font color="#A0008A">"200px"</font><font color="#303000"><b>)</b></font>

        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">frame</font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'&lt;a href="http://google.com" target="myFrame"&gt;Google&lt;/a&gt;'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">vPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">HTML</font><font color="#303000"><b>(</b></font><font color="#600080">'&lt;a href="http://yahoo.com" target="myFrame"&gt;Yahoo&lt;/a&gt;'</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">vPanel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : NamedFrameDemo()})

    demos.append({"name" : "passwordTextBox",
                  "title" : "ui.PasswordTextBox",
                  "section" : "widgets",
                  "doc" : """The ``ui.PasswordTextBox`` class implements a standard password input field.

Like its cousins the ``ui.TextBox`` and ``ui.TextArea`` classes, ``ui.PasswordTextBox`` defines many useful methods which you may find useful.

The most important methods are probably ``setText()`` and ``getText()`` which set and retrieve the contents of the input field, and ``setMaxLength()`` to specify how many characters the user can type into the field.

Note that for some reason, the ``setVisibleLength()`` method is not defined for a password field.  This means that you have to specify the width of the field in pixels, as is shown below. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>passwordTextBox.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">PasswordTextBox</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">PasswordTextBoxDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">field</font> <font color="#303000"><b>=</b></font> <font color="#000000">PasswordTextBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setWidth</font><font color="#303000"><b>(</b></font><font color="#A0008A">"100px"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">field</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : PasswordTextBoxDemo()})

    demos.append({"name" : "radioButton",
                  "title" : "ui.RadioButton",
                  "section" : "widgets",
                  "doc" : """The ``ui.RadioButton`` class is used to show a radio button.  Each radio button is given a "group" value; when the user clicks on a radio button, the other radio buttons in that group are deselected, and the clicked on radio button is selected.

You can use the ``setChecked(checked)`` method to select or deselect a radio button, and you can call ``isChecked()`` to see if a radio button is currently selected.  You can also enable or disable a checkbox using ``setEnabled(enabled)``.  And finally, you can call ``addClickListener()`` to respond when the user clicks on the radio button. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>radioButton.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>,</b></font> <font color="#000000">RadioButton</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">RadioButtonDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel1</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel1</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group1"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Red"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel1</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group1"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Green"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel1</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group1"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Blue"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">panel2</font> <font color="#303000"><b>=</b></font> <font color="#000000">VerticalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel2</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group2"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Solid"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel2</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group2"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Liquid"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">panel2</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">RadioButton</font><font color="#303000"><b>(</b></font><font color="#A0008A">"group2"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"Gas"</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">hPanel</font> <font color="#303000"><b>=</b></font> <font color="#000000">HorizontalPanel</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">hPanel</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">panel2</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">hPanel</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : RadioButtonDemo()})

    demos.append({"name" : "textArea",
                  "title" : "ui.TextArea",
                  "section" : "widgets",
                  "doc" : """The ``ui.TextArea`` class implements a standard multi-line input field.

The ``setCharacterWidth()`` method sets the width of the input field, in characters, while ``setVisibleLines()`` sets the height of the field, in lines.

Use the ``getText()`` method to retrieve the field's current text, and ``setText()`` to set it.  There are many other useful methods defined by ``ui.TextArea`` and its parent classes; see the module documentation for more details. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>textArea.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">TextArea</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">TextAreaDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">field</font> <font color="#303000"><b>=</b></font> <font color="#000000">TextArea</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setCharacterWidth</font><font color="#303000"><b>(</b></font><font color="#FF2200">20</font><font color="#303000"><b>)</b></font>
        <font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setVisibleLines</font><font color="#303000"><b>(</b></font><font color="#FF2200">4</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">field</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : TextAreaDemo()})

    demos.append({"name" : "textBox",
                  "title" : "ui.TextBox",
                  "section" : "widgets",
                  "doc" : """The ``ui.TextBox`` class implements a standard one-line input field.

There are many useful methods defined by ``ui.TextBox`` and its parent classes. For example, ``getText()`` returns the current contents of the input field, and ``setText()`` lets you set the field's contents to a given string.

``setVisibleLength()`` lets you set the width of the field, in characters. Similarly, ``setMaxLength()`` lets you set the maximum number of characters the user can enter into the field.

""",
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>textBox.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">TextBox</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">TextBoxDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">field</font> <font color="#303000"><b>=</b></font> <font color="#000000">TextBox</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setVisibleLength</font><font color="#303000"><b>(</b></font><font color="#FF2200">20</font><font color="#303000"><b>)</b></font>
        <font color="#000000">field</font><font color="#303000"><b>.</b></font><font color="#000000">setMaxLength</font><font color="#303000"><b>(</b></font><font color="#FF2200">10</font><font color="#303000"><b>)</b></font>

        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">field</font><font color="#303000"><b>)</b></font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : TextBoxDemo()})

    demos.append({"name" : "tree",
                  "title" : "ui.Tree",
                  "section" : "widgets",
                  "doc" : """The ``ui.Tree`` class lets you add a tree control to your application.

Call ``Tree.addTreeListener()`` to add a tree listener object to a tree, that listener object's ``onTreeItemSelected()`` method will be called as the user clicks on that item in the tree control.  Similarly, the listener object's ``onTreeItemStateChanged()`` method will be called whenever the user opens or closes a branch of the tree.  Both of these methods have to be defined, even if you don't use them both.

To open a branch of the tree, call ``TreeItem.setState()`` method.  If the ``state`` parameter is True, the branch of the tree will be opened; if it is False, the branch of the tree will be closed. """,
                  "src" : """<!DOCTYPE HTML PUBLIC "-//W3C//DTD                           HTML 3.2 Final//EN"
<html><head><title>tree.py</title>
<!--This document created by PySourceColor ver.1 on: Tue Jan 13 08:58:29 2009-->
<meta http-equiv="Content-Type"                          content="text/html;charset=iso-8859-1" />
</head><body bgcolor="#FFFFFF">
<pre><font face="Lucida Console, Courier New">
<font color="#0000AF"><b>from</b></font> <font color="#000000">ui</font> <font color="#0000AF"><b>import</b></font> <font color="#000000">SimplePanel</font><font color="#303000"><b>,</b></font> <font color="#000000">Tree</font><font color="#303000"><b>,</b></font> <font color="#000000">TreeItem</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">DOM</font>
<font color="#0000AF"><b>import</b></font> <font color="#000000">Window</font>

<font color="#0000AF"><b>class</b></font> <font color="#0000FF">TreeDemo</font><font color="#303000"><b>(</b></font><font color="#000000">SimplePanel</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">SimplePanel</font><font color="#303000"><b>.</b></font><font color="#000000">__init__</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">tree</font> <font color="#303000"><b>=</b></font> <font color="#000000">Tree</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">tree</font><font color="#303000"><b>.</b></font><font color="#000000">addTreeListener</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>)</b></font>

        <font color="#000000">s1</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Section 1"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">s1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1.1"</font><font color="#303000"><b>,</b></font> <font color="#000000">value</font><font color="#303000"><b>=</b></font><font color="#FF2200">11</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">s1</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 1.2"</font><font color="#303000"><b>,</b></font> <font color="#000000">value</font><font color="#303000"><b>=</b></font><font color="#FF2200">12</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">s2</font> <font color="#303000"><b>=</b></font> <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Section 2"</font><font color="#303000"><b>)</b></font>
        <font color="#000000">s2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2.1"</font><font color="#303000"><b>,</b></font> <font color="#000000">value</font><font color="#303000"><b>=</b></font><font color="#FF2200">21</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">s2</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">createItem</font><font color="#303000"><b>(</b></font><font color="#A0008A">"Item 2.2"</font><font color="#303000"><b>,</b></font> <font color="#000000">value</font><font color="#303000"><b>=</b></font><font color="#FF2200">22</font><font color="#303000"><b>)</b></font><font color="#303000"><b>)</b></font>

        <font color="#000000">s1</font><font color="#303000"><b>.</b></font><font color="#000000">setState</font><font color="#303000"><b>(</b></font><font color="#000000">True</font><font color="#303000"><b>,</b></font> <font color="#000000">fireEvents</font><font color="#303000"><b>=</b></font><font color="#000000">False</font><font color="#303000"><b>)</b></font>
        <font color="#000000">s2</font><font color="#303000"><b>.</b></font><font color="#000000">setState</font><font color="#303000"><b>(</b></font><font color="#000000">True</font><font color="#303000"><b>,</b></font> <font color="#000000">fireEvents</font><font color="#303000"><b>=</b></font><font color="#000000">False</font><font color="#303000"><b>)</b></font>

        <font color="#000000">tree</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">s1</font><font color="#303000"><b>)</b></font>
        <font color="#000000">tree</font><font color="#303000"><b>.</b></font><font color="#000000">addItem</font><font color="#303000"><b>(</b></font><font color="#000000">s2</font><font color="#303000"><b>)</b></font>
        <font color="#000000">self</font><font color="#303000"><b>.</b></font><font color="#000000">add</font><font color="#303000"><b>(</b></font><font color="#000000">tree</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">createItem</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">label</font><font color="#303000"><b>,</b></font> <font color="#000000">value</font><font color="#303000"><b>=</b></font><font color="#000000">None</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">item</font> <font color="#303000"><b>=</b></font> <font color="#000000">TreeItem</font><font color="#303000"><b>(</b></font><font color="#000000">label</font><font color="#303000"><b>)</b></font>
        <font color="#000000">DOM</font><font color="#303000"><b>.</b></font><font color="#000000">setStyleAttribute</font><font color="#303000"><b>(</b></font><font color="#000000">item</font><font color="#303000"><b>.</b></font><font color="#000000">getElement</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font><font color="#303000"><b>,</b></font> <font color="#A0008A">"cursor"</font><font color="#303000"><b>,</b></font> <font color="#A0008A">"pointer"</font><font color="#303000"><b>)</b></font>
        <font color="#0000AF"><b>if</b></font> <font color="#000000">value</font> <font color="#303000"><b>!=</b></font> <font color="#000000">None</font><font color="#303000"><b>:</b></font>
            <font color="#000000">item</font><font color="#303000"><b>.</b></font><font color="#000000">setUserObject</font><font color="#303000"><b>(</b></font><font color="#000000">value</font><font color="#303000"><b>)</b></font>
        <font color="#0000AF"><b>return</b></font> <font color="#000000">item</font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onTreeItemSelected</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">item</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#000000">value</font> <font color="#303000"><b>=</b></font> <font color="#000000">item</font><font color="#303000"><b>.</b></font><font color="#000000">getUserObject</font><font color="#303000"><b>(</b></font><font color="#303000"><b>)</b></font>
        <font color="#000000">Window</font><font color="#303000"><b>.</b></font><font color="#000000">alert</font><font color="#303000"><b>(</b></font><font color="#A0008A">"You clicked on "</font> <font color="#303000"><b>+</b></font> <font color="#000000">value</font><font color="#303000"><b>)</b></font>


    <font color="#0000AF"><b>def</b></font> <font color="#0000FF">onTreeItemStateChanged</font><font color="#303000"><b>(</b></font><font color="#000000">self</font><font color="#303000"><b>,</b></font> <font color="#000000">item</font><font color="#303000"><b>)</b></font><font color="#303000"><b>:</b></font>
        <font color="#0000AF"><b>pass</b></font> <font color="#007F00"># We ignore this.</font><font color="#000000"></font></pre>
<!--This document created by PySourceColor ver.ver.1 on: Tue Jan 13 08:58:29 2009-->
</body></html>
""",
                  "example" : TreeDemo()})

    return demos
