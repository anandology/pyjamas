# Date Time Example
# Copyright (C) 2009 Yi Choong (http://code.google.com/u/yitchoong/)

import pyjd # dummy in pyjs

from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import  VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.DockPanel import DockPanel
from pyjamas.ui.RootPanel import  RootPanel
from pyjamas.ui.PopupPanel import  PopupPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Composite import Composite
from pyjamas.ui.Label import Label
from pyjamas.ui.Hyperlink import Hyperlink
from pyjamas.ui.HTML import HTML
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.Image import Image
from pyjamas.ui.Frame import Frame
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui import HasAlignment
from pyjamas.ui.Tooltip import Tooltip, TooltipListener
from pyjamas import DOM, Window
from pyjamas.ui import Event
from pyjamas.ui import MouseListener

import time

#def navLanguage():
#    JS("""
#       if (navigator.userLanguage)
#        return navigator.userLanguage.substring(0, 2);
#       if (navigator.language) 
#        return navigator.language.substring(0, 2);
#       return 'en';
#       """)

# # quickElement(tagType, parentReference, textInChildNode, [, attribute, attributeValue ...]);

# def quickElement( elementType , parent, textInChild , attributes=None): # list of tuples e.g. [(key,value),(key,value)...]
    # child = DOM.createElement( elementType)
    # if textInChild:
        # child.setInnerText(textInChild)
    # if attributes:
        # for attr in attributes:
            # k, v = attr
            # DOM.setAttribute(child, k, v)
    
    # DOM.appendChild(parent,child)        
    # return child
       
class Calendar(FocusPanel):
    def __init__(self):
        FocusPanel.__init__(self)
        self.monthsOfYear = ['January','February','March','April','May','June','July','August','September','October','November','December']
        self.daysOfWeek = ['S','M','T','W','T','F','S']
        yy,mm,dd = self.today().split("-") 
        todayYear = yy
        todayMonth = mm
        todayDay = dd
        self.currentMonth = todayMonth
        self.currentYear = todayYear
        self.currentDay = todayDay
        
        self.todayYear = todayYear
        self.todayMonth = todayMonth
        self.todayDay = todayDay
        
        self.selectedDateListeners = []
        self.vp = VerticalPanel()
        self.setWidget(self.vp)
                 
    def today(self):
        return time.strftime("%y-%m-%d")
    
    def addSelectedDateListener(self,listener):
        self.selectedDateListeners.append(listener)
    
    def removeSelectedDateListener(self,listener):
        self.selectedDateListeners.remove(listener)
    
    def isLeapYear(self,year):
        if (year % 4 == 0 and year % 100 != 0) or ( year % 400 == 0):
            return True
        else:
            return False
            
    def getDaysInMonth(self,month,year):
        days = 0
        mth = month + 1
        if mth in (1,3,5,7,8,10,12):
            days=31
        elif mth in (4,6,8,11):
            days = 30
        elif (mth==2 and self.isLeapYear(year)):
            days = 29
        else:
            days = 28
        return days

    def setPosition(self, left, top):
        element = self.getElement()
        DOM.setStyleAttribute(element, "left", "%dpx" % left)
        DOM.setStyleAttribute(element, "top", "%dpx" % top)
                
    def show(self, left, top):
        if left < 0:
            left = 0
        if top < 0:
            top = 0
        self.setPosition(left,top)
        self.drawCurrent()
        self.setVisible(True)
        
    def onCellClicked(self, grid, row, col):
        if row == 0:
            return
        text = grid.getText(row, col)
        if text == "":
            return
        self.selectedDay = int(text)  
        # well if anyone is listening to the listener, fire that event
        for listener in self.selectedDateListeners:
            if hasattr(listener, "onDateSelected"):
                listener.onDateSelected(self.currentYear, self.currentMonth,
                                        self.selectedDay)
            else: 
                listener(self.currentYear, self.currentMonth, self.selectedDay)                         
        self.setVisible(False)
        
    def draw(self, month , year, to_day=None): 
        # remove the old widget
        self.remove(self.vp)
            
        mth = int(month)
        yr = int(year)
        if to_day:
            dd = int(to_day)
        else:
            dd = 0

        self.vp = VerticalPanel()
        tp = HorizontalPanel()
        tp.addStyleName("calendar-top-panel")
        tp.setSpacing(5)
        
        h1 = Hyperlink('<<')
        h1.addClickListener( getattr(self,'onPreviousYear') )
        h2 = Hyperlink('<')
        h2.addClickListener( getattr(self,'onPreviousMonth') )
        h4 = Hyperlink('>')
        h4.addClickListener( getattr(self,'onNextMonth') )
        h5 = Hyperlink('>>')
        h5.addClickListener( getattr(self,'onNextYear') )

        tp.add(h1)
        tp.add(h2)
        sp = SimplePanel()
        sp.add(HTML("<b>" + self.monthsOfYear[mth] + " " + str(yr) + "</b>" ) )
        sp.setStyleName("calendar-center")
        tp.add( sp)
        tp.add(h4)
        tp.add(h5)
        tvp = VerticalPanel()
        tvp.setSpacing(10)
        tvp.add(tp)
        
        self.vp.add(tvp)

        # done with top panel
        
        daysInMonth = self.getDaysInMonth(mth, yr)
        startPos = 1
        slots = startPos + daysInMonth
        rows = int(slots/7) + 1
        #Window.alert("fn:draw, rows=" + rows)
        self.grid = Grid(rows+1, 7) # extra row for the days in the week
        self.grid.setWidth("100%")
        self.grid.addTableListener(self)
        self.vp.add(self.grid)
        #
        # some links & handlers 
        #
        bh1 = Hyperlink('Yesterday')
        bh1.addClickListener( getattr(self,'onYesterday') )
        bh2 = Hyperlink('Today')
        bh2.addClickListener( getattr(self,'onToday') )
        bh3 = Hyperlink('Tomorrow')
        bh3.addClickListener( getattr(self,'onTomorrow') )
        bh4 = Hyperlink('Cancel')
        bh4.addClickListener( getattr(self,'onCancel') )
        #
        # add code to test another way of doing the layout
        #
        b = HorizontalPanel()
        b.add(bh1)
        b.add(bh2)
        b.add(bh3)
        #b.setSpacing(5)
        b.addStyleName("calendar-shortcuts")
        # self.bottomPanel = b
        self.vp.add(b)
        b2 = SimplePanel()
        b2.add(bh4)
        b2.addStyleName("calendar-cancel")
        self.vp.add(b2)        
        #
        # put some content into the grid cells
        #
        for i in range(7):
            self.grid.setText(0, i, self.daysOfWeek[i] )
            self.grid.cellFormatter.addStyleName(0,i,"calendar-header")
        startPos = 1
        days = self.getDaysInMonth(mth,year)        
        #Window.alert("fn:draw " + mth + " " + yr + ' startpos=' + startPos + ' days=' + days)
        #
        # draw cells which are empty first
        #
        day =0
        pos = 0
        while pos < startPos:
            self.grid.setText(1, pos , " ")
            self.grid.cellFormatter.setStyleAttr(1,pos,"background","#f3f3f3")
            self.grid.cellFormatter.addStyleName(1,pos,"calendar-blank-cell")
            pos += 1
        # now for days of the month
        row = 1 
        day = 1
        col = startPos
        while day <= days:
            if pos % 7 == 0 and day <> 1:
                row += 1
            col = pos % 7
            self.grid.setText(row,col, str(day) )
            if self.currentYear == self.todayYear and self.currentMonth == self.todayMonth and day == self.todayDay:
                self.grid.cellFormatter.addStyleName(row,col,"calendar-cell-today")
            else:
                self.grid.cellFormatter.addStyleName(row,col,"calendar-day-cell")
            day += 1
            pos += 1
        #
        # now blank lines on the last row
        #
        col += 1
        while col < 7:
            self.grid.setText(row,col," ")
            self.grid.cellFormatter.setStyleAttr(row,col,"background","#f3f3f3")
            self.grid.cellFormatter.addStyleName(row,col,"calendar-blank-cell")
            col += 1
        #
        # default some values
        #
        if dd:
            self.selectedDay = dd
        self.selectedMonth = mth
        self.selectedYear = yr

        self.vp.setSpacing(2)
        self.add(self.vp)
        self.vp.addStyleName("calendarbox calendar-module calendar")
        self.setWidget(self.vp)
        return
        
    def onPreviousYear(self,event):
        self.drawPreviousYear()
    
    def onPreviousMonth(self,event):
        self.drawPreviousMonth()
        
    def onNextMonth(self,event):
        self.drawNextMonth()
        
    def onNextYear(self,event):
        self.drawNextYear()
        
    def onDate(self, event, yy, mm, dd):
        for listener in self.selectedDateListeners:
            if hasattr(listener, "onDateSelected"):
                listener.onDateSelected(yy,mm,dd)
            else: 
                listener(yy,mm,dd)
        self.setVisible(False)
    
    def onYesterday(self,event):
        yesterday = time.gmtime(time.time() - 3600 * 24)
        mm = yesterday.tm_mon
        dd = yesterday.tm_mday
        yy = yesterday.tm_year
        self.onDate(event, yy, mm, dd)
    
    def onToday(self,event):
        tod = time.gmtime()
        mm = tod.tm_mon
        dd = tod.tm_mday
        yy = tod.tm_year
        self.onDate(event, yy, mm, dd)
    
    def onTomorrow(self,event):
        tom = time.gmtime(time.time() + 3600 * 24)
        mm = tom.tm_mon
        dd = tom.tm_mday
        yy = tom.tm_year
        self.onDate(event, yy, mm, dd)
    
    def onCancel(self,event):
        self.setVisible(False)
    
    def drawCurrent(self):
        #Window.alert( self.currentYear + ' ' + self.currentMonth )
        self.draw( self.currentMonth, self.currentYear, self.currentDay )

    def drawDate(self, month, year ):
        if year == self.currentYear and month == self.currentYear():
            self.drawCurrent()
            
        self.currentMonth = month
        self.currentYear = year        
        self.draw(self.currentMonth, self.currentYear)
    
    def drawPreviousMonth(self):
        if int(self.currentMonth) == 1:
            self.currentMonth = 12
            self.currentYear = int(self.currentYear) - 1
        else:
            self.currentMonth = int(self.currentMonth) - 1
        self.draw(self.currentMonth, self.currentYear)
        
    def drawNextMonth(self):
        if int(self.currentMonth) == 12:
            self.currentMonth = 1
            self.currentYear = int(self.currentYear) + 1
        else:
            self.currentMonth = int(self.currentMonth) + 1
        self.draw(self.currentMonth, self.currentYear)
    
    def drawPreviousYear(self):
        self.currentYear = int(self.currentYear) - 1
        self.draw(self.currentMonth, self.currentYear)

    def drawNextYear(self):
        self.currentYear = int(self.currentYear) + 1
        self.draw(self.currentMonth, self.currentYear)
             
class DateField(Composite):

    def __init__(self,sep='-'):
        self.sep = sep
        self.tbox = TextBox()
        self.tbox.setVisibleLength(10)
        self.calendar = Calendar()
        img = Image("icon_calendar.gif")
        self.calendarLink = HyperlinkImage(img)
        self.todayLink = Hyperlink('Today')
        self.todayLink.addStyleName("calendar-today-link")
        #
        # lay it out
        #
        hp = HorizontalPanel()
        hp.setSpacing(2)
        vp = VerticalPanel()
        hp.add(self.tbox)
        vp.add(self.calendarLink)
        vp.add(self.todayLink)
        #vp.add(self.calendar)
        hp.add(vp)

        Composite.__init__(self)
        self.initWidget(hp)
        # 
        # done with layout, so now set up some listeners
        #
        self.tbox.addFocusListener(self) # hook to onLostFocus
        self.calendar.addSelectedDateListener(getattr(self,"onDateSelected"))
        self.todayLink.addClickListener(getattr(self,"onTodayClicked"))
        self.calendarLink.addClickListener(getattr(self,"onShowCalendar"))
        #self.calendar.show(10,10)
        

    def getTextBox(self):
        return self.tbox
        
    def getCalendar(self):
        return self.calendar
        
    def setID(self,id):
        self.tbox.setID(id)
        
    def onDateSelected(self, yyyy, mm, dd):
        m = str(int(mm)+1)
        if len(m) == 1: m = '0' + m
        d = str(dd)
        if len(d) == 1: d = '0' + d
        yyyy = str(yyyy)
        
        self.tbox.setText(  d + self.sep + m + self.sep + yyyy )
        
    def onLostFocus(self, sender):
        # hide the calendar -- no more since it is now in a popup
        #self.calendar.setVisible(False)
        # thing about formatting, if no separator provided, put in "-"
        #
        text = self.tbox.getText().strip()
        # if blank - leave it alone
        if text and len(text) == 8:
            # ok what format do we have? assume ddmmyyyy
            self.tbox.setText( text[0:2] + '-' + text[2:4] + '-' + text[4:8] )
            
    def onFocus(self, sender):
        pass
        
    def onTodayClicked(self):
        tod = time.gmtime()
        todayDay = tod.tm_mday
        todayMonth = tod.tm_mon
        todayYear = tod.tm_year
        if todayYear < 1900:
            todayYear += 1900;
        dd = "%0.2d" % int(todayDay)
        dd = str(dd)
        if len(dd) == 1: dd = '0' + dd        
        mm = str(todayMonth+1)
        if len(mm) == 1: mm = '0' + mm
        yyyy = str(todayYear)
        #Window.alert( dd + " " + mm + " " + yyyy)
        self.tbox.setText( dd + self.sep + mm + self.sep + yyyy )
        
    def onShowCalendar(self, sender):
        p = CalendarPopup(self.calendar)
        x = self.tbox.getAbsoluteLeft() + 10
        y = self.tbox.getAbsoluteTop() + 10
        p.setPopupPosition(x,y)
        p.show()
    

class CalendarPopup(PopupPanel):
    def __init__(self, c):
        PopupPanel.__init__(self, True)        
        p = SimplePanel()
        p.add(c)
        c.show(10,10)
        p.setWidth("100%")        
        self.setWidget(p)        
    
class HyperlinkImage(Hyperlink):
    def __init__(self, img, targetHistoryToken=''):
        Hyperlink.__init__(self)        
        DOM.appendChild(DOM.getFirstChild(self.getElement()), img.getElement());
        self.setTargetHistoryToken(targetHistoryToken);
        img.unsinkEvents(Event.ONCLICK | Event.MOUSEEVENTS);
        self.sinkEvents(Event.ONCLICK | Event.MOUSEEVENTS);        
        self.mouseListeners = []
            
    def addMouseListener(self, listener):
        self.mouseListeners.append(listener)
        
    def removeMouseListener(self,listener):
        self.mouseListeners.remove(listener)
        
    def onBrowserEvent(self, event):
        type = DOM.eventGetType(event)
        if type in ('mousedown','mouseup','mousemove','mouseover','mouseout'):
            MouseListener.fireMouseEvent(self.mouseListeners, self, event)
            
        else:
            Hyperlink.onBrowserEvent(self,event)        
        
             
class App:
    def onModuleLoad(self):
        
        text = TextBox()
        df1 = DateField()
        df2 = DateField()
        b = Button("Show Calendar", getattr(self,"onClick"))
        cal = Calendar()
        cal.drawCurrent()
        
        vp = VerticalPanel()
        vp.setSpacing(10)
        vp.add(df1)
        vp.add(b)
        vp.add(df2)
        
        RootPanel().add(vp)
        
    def onClick(self,sender):
        cal = Calendar()
        p = CalendarPopup(cal)
        x = sender.getAbsoluteLeft() + 10
        y = sender.getAbsoluteTop() + 10
        p.setPopupPosition(x,y)
        p.show()

        # cal = Calendar()
        # x = sender.getAbsoluteLeft() + 10
        # y = sender.getAbsoluteTop() + 10
        # cal.show(x,y)
        # RootPanel().add(cal)
        
if __name__ == '__main__':
    pyjd.setup("./public/DateField.html")
    app = App()
    app.onModuleLoad()
    pyjd.run()
