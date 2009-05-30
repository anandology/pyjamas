# index.py

from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Grid import Grid
from pyjamas.ui.Label import Label
from pyjamas.ui.HTML import HTML
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.ListBox import ListBox
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.TextArea import TextArea
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.DialogBox import DialogBox
from Tooltip import Tooltip, TooltipListener
from pyjamas import DOM, Window
from datetime import Datetime

def navLanguage():
    JS("""
       if (navigator.userLanguage)
        return navigator.userLanguage.substring(0, 2);
       if (navigator.language) 
        return navigator.language.substring(0, 2);
       return 'en';
       """)
    
class TodayListener:
    def __init__(self, proxy):
        self.proxy = proxy

    def onClick(self, sender=None):
        strDate = "%d%s%d%s%d" % (self.proxy.todayYear,
                                  self.proxy.dateSep,
                                  self.proxy.todayMonth + 1,
                                  self.proxy.dateSep,
                                  self.proxy.todayDay)
        if self.proxy.todayMonth != self.proxy.month or \
           self.proxy.todayYear != self.proxy.year:
            self.proxy.monthChanged = True

        self.proxy.setDate(strDate)


class Calendar(FocusPanel):
    daysLabels_es = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    monthsNames_es = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre",
                   "Octubre", "Noviembre", "Diciembre"]
    daysLabels_en = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
    monthsNames_en = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                   "October", "November", "December"]
    monthsDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    daysLabels = {'es': Calendar.daysLabels_es, 'en': Calendar.daysLabels_en}
    monthsNames = {'es': Calendar.monthsNames_es , 'en': Calendar.monthsNames_en}
    otherLabels = {'es': {'lblToday': 'Hoy', 'lblClose': 'Cerrar', 'ttBack10y': 'Atrás 10 años',
                          'ttBack1y': 'Atrás 1 año', 'ttBack1m': 'Atrás 1 mes', 'ttFwd1m': 'Adelante 1 mes',
                          'ttFwd1y': 'Adelante 1 año', 'ttFwd10y': 'Adelante 10 años'},
        'en': {'lblToday': 'Today', 'lblClose': 'Close', 'ttBack10y': 'Back 10 years', 'ttBack1y': 'Back 1 year',
               'ttBack1m': 'Back 1 month', 'ttFwd1m': 'Forward 1 month',
                          'ttFwd1y': 'Forward 1 year', 'ttFwd10y': 'Forward 10 years'}}
    
    def isLeapYear(self):
        if self.year % 4:    
            return False
        if not self.year % 100:
            if not self.year % 400:
                return True
            else:
                return False
        else:
            return True

    def setPopupPosition(self, left, top):
        if left < 0:
            left = 0
        if top < 0:
            top = 0

        element = self.getElement()
        DOM.setStyleAttribute(element, "left", left + "px")
        DOM.setStyleAttribute(element, "top", top + "px")
        
    def onMouseDown(self, sender, x, y):
        if sender == self.lblCurrentMonthYear:
            self.dragging = True
            DOM.setCapture(self.lblCurrentMonthYear.getElement())
            self.dragStartX = x
            self.dragStartY = y
        else:
            FocusPanel.onMouseDown(self, sender, x, y)
            
    def onMouseEnter(self, sender):
        pass

    def onMouseLeave(self, sender):
        pass

    def onMouseMove(self, sender, x, y):
        if self.dragging:
            absX = x + self.getAbsoluteLeft()
            absY = y + self.getAbsoluteTop()
            self.setPopupPosition(absX - self.dragStartX, absY - self.dragStartY)

    def onMouseUp(self, sender, x, y):
        if sender == self.lblCurrentMonthYear:
            self.dragging = False
            DOM.releaseCapture(self.lblCurrentMonthYear.getElement())
        else:
            FocusPanel.onMouseUp(self, sender, x, y)
            
            
    def __init__(self, visible = False, text = "", textbox = None, date = None, dateSep = "-", firstDayOfWeek = 1, 
                 backColor = "#D4D0C8", autoHide = True):
        
        FocusPanel.__init__(self)
        
        self.monthsNames = Calendar.monthsNames[navLanguage()]
        self.daysLabels = Calendar.daysLabels[navLanguage()]
        self.otherLabels = Calendar.otherLabels[navLanguage()]
        
        self.monthChanged = True
        
        self.dragging = False
        self.dragStartX = 0
        self.dragStartY = 0
        
        self.year = 0
        self.month = 0
        self.day = 0
        self.dayOfWeek = 0
        self.fdomDayOfWeek = 0
        self.todayYear = 0
        self.todayMonth = 0
        self.todayDay = 0
        
        if firstDayOfWeek > 1:
            firstDayOfWeek = 1
        if firstDayOfWeek < 0:
            firstDayOfWeek = 0
        self.firstDayOfWeek = firstDayOfWeek
        self.dateSep = dateSep
        self.text = text
        self.textbox = textbox
        
        self.backColor = backColor
        self.autoHide = autoHide

        self.setWidth("19%")
        
        self.vp = VerticalPanel()
        
        self.titlePanel = HorizontalPanel()
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttBack10y']))
        self.btnBack10Years = Button("&lt;&lt;&lt;", getattr(self, "minus10Years"))
        fp.add(self.btnBack10Years)
        self.titlePanel.add(fp)
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttBack1y']))
        self.btnBackYear = Button("&lt;&lt;", getattr(self, "minusYear"))
        fp.add(self.btnBackYear)
        self.titlePanel.add(fp)
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttBack1m']))
        self.btnBackMonth = Button("&lt;", getattr(self, "minusMonth"))
        fp.add(self.btnBackMonth)
        self.titlePanel.add(fp)
        self.lblCurrentMonthYear = Label("")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "marginLeft", "1px")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "marginRight", "1px")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "paddingLeft", "10px")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "paddingRight", "10px")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "color", "#0D4B70")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "backgroundColor", "rgb(255,255,255)")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "fontSize", "small")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "cursor", "move")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "width", "8em")
        DOM.setStyleAttribute(self.lblCurrentMonthYear.getElement(), "textAlign", "center")
        self.titlePanel.add(self.lblCurrentMonthYear)
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttFwd1m']))
        self.btnNextMonth = Button("&gt;", getattr(self, "plusMonth"))
        fp.add(self.btnNextMonth)
        self.titlePanel.add(fp)
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttFwd1y']))
        self.btnNextYear = Button("&gt;&gt;", getattr(self, "plusYear"))
        fp.add(self.btnNextYear)
        self.titlePanel.add(fp)
        fp = FocusPanel()
        fp.addMouseListener(TooltipListener(self.otherLabels['ttFwd10y']))
        self.btnNext10Years = Button("&gt;&gt;&gt;", getattr(self, "plus10Years"))
        fp.add(self.btnNext10Years)
        self.titlePanel.add(fp)
                               
        self.vp.add(self.titlePanel)
        
        self.daysPanel = SimplePanel()
        self.vp.add(self.daysPanel)
        
        proxy = self

        def autoCerrar(self, sender):
            proxy.setVisible(False)
            
        id1 = HTMLPanel.createUniqueId(None)
        id2 = HTMLPanel.createUniqueId(None)
        self.bottomPanel = HTMLPanel("<div style='text-align: right;'><span id=" + id2 + "><span id=" + id1 + "></div>")            
        self.btnToday = Button(self.otherLabels['lblToday'], TodayListener(self))
        self.bottomPanel.add(self.btnToday, id1)
        self.btnClose = Button(self.otherLabels['lblClose'], autoCerrar)
        self.bottomPanel.add(self.btnClose, id2)
        self.btnToday.setWidth("50%")
        self.btnClose.setWidth("50%")
        self.vp.add(self.bottomPanel)
        
        DOM.setStyleAttribute(self.vp.getElement(), "border", "1px solid")
        DOM.setStyleAttribute(self.vp.getElement(), "padding", "2px")

        self.setDate(date)

        today = Datetime()

        self.todayYear = today.getYear()
        if self.todayYear < 1900:
            self.todayYear += 1900;
        self.todayMonth = today.getMonth()
        self.todayDay = today.getDate()
        self.todayDayOfWeek = today.getDay()
        
        DOM.setStyleAttribute(self.vp.getElement(), "backgroundColor", self.backColor)
        self.setWidget(self.vp)
        
        wi = self.vp.getOffsetWidth()
        
        DOM.setStyleAttribute(self.getElement(), "position", "absolute")
        
        
        self.lblCurrentMonthYear.addMouseListener(self)
        self.setVisible(visible)
    
    def setDestination(self, textbox):
        self.textbox = textbox
        
    def _rechargeDate(self):
        strDate = "%d%s%d%s%d" % (self.year, self.dateSep, self.month + 1, self.dateSep, self.day)
        self.setDate(strDate)
        
    def plus10Years(self):
        self.year += 10
        self.monthChanged = True
        self._rechargeDate()
        
    def plusYear(self):
        self.year += 1
        self.monthChanged = True
        self._rechargeDate()
        
    def minus10Years(self):
        self.year -= 10
        self.monthChanged = True
        self._rechargeDate()
        
    def minusYear(self):
        self.year -= 1
        self.monthChanged = True
        self._rechargeDate()

    def plusMonth(self):
        self.month += 1
        if self.month > 11:
            self.year += 1
            self.month = 0
        self.monthChanged = True
        self._rechargeDate()
        
    def minusMonth(self):
        self.month -= 1
        if self.month < 0:
            self.month = 11
            self.year -= 1
        self.monthChanged = True
        self._rechargeDate()
        
    def doSomething(self, sender):
        if self.textbox:
            btnvalue = sender.getText()
            texto = "%s %d" % (self.toString(), btnvalue)
            self.textbox.setText(texto)
        self.setVisible(False)
        
    def setDate(self, date):
        year = None
        month = None
        day = None
        dayOfWeek = None
        
        if not date:
            today = Datetime()
            year = today.getYear()
            if year < 1900:
                year += 1900;
            month= today.getMonth()
            day= today.getDate()
            dayOfWeek = today.getDay()
        else:
            arr = date.split(self.dateSep)
            year = int(arr[0])
            month = int(arr[1]) - 1
            day = int(arr[2])
            newdate = Datetime(year, month, day);
            dayOfWeek = newdate.getDay()
        
        self.year = year
        self.month = month
        self.day = day
        self.dayOfWeek = dayOfWeek

        d = Datetime(year, month, 1);
        fdow = d.getDay()
        
        fdow -= self.firstDayOfWeek
        if fdow < 0:
            fdow = len(self.daysLabels) + fdow
            
        self.fdomDayOfWeek = fdow
        
        if self.monthChanged:
            self.drawDays()
            self.monthChanged = False
        
        self.paintDays()
        
        self.lblCurrentMonthYear.setText("%s %d" % (self.monthsNames[self.month], self.year))
        if self.textbox:
                self.textbox.setText(self.toString())

    def drawDays(self):
        totalDays = self.getTotalDrawDays()
        rows = totalDays / 7
        if totalDays % 7:
            rows += 1
        cols = 7
        self.grid = Grid(rows+1, cols)
        grid = self.grid
        grid.setWidth("100%")
        
        cellformatter = grid.getCellFormatter()
        DOM.setAttribute(grid.getElement(), "border", "1")
        DOM.setStyleAttribute(grid.getElement(), "borderCollapse", "collapse")
        DOM.setStyleAttribute(grid.getElement(), "cursor", "pointer")
        grid.addTableListener(self)
        DOM.setStyleAttribute(grid.getElement(), "backgroundColor", self.backColor)

        
        for c in range(self.firstDayOfWeek, cols):
            grid.setText(0, c-self.firstDayOfWeek, self.daysLabels[c])
            DOM.setStyleAttribute(cellformatter.getElement(0, c-self.firstDayOfWeek), "backgroundColor", "#0D4B70")
            DOM.setStyleAttribute(cellformatter.getElement(0, c-self.firstDayOfWeek), "color", "white")
            DOM.setStyleAttribute(cellformatter.getElement(0, c-self.firstDayOfWeek), "textAlign", "center")
            DOM.setStyleAttribute(cellformatter.getElement(0, c-self.firstDayOfWeek), "fontFamily", "Courier")
        if self.firstDayOfWeek:
            for c in range(0, self.firstDayOfWeek):
                grid.setText(0, c + cols - 1, self.daysLabels[c])
                DOM.setStyleAttribute(cellformatter.getElement(0, c + cols -1), "backgroundColor", "#0D4B70")
                DOM.setStyleAttribute(cellformatter.getElement(0, c + cols -1), "color", "white")
                DOM.setStyleAttribute(cellformatter.getElement(0, c + cols -1), "textAlign", "center")
                DOM.setStyleAttribute(cellformatter.getElement(0, c + cols -1), "fontFamily", "Courier")
            
        counter = 0
            
        for r in range(1, rows + 1):
            for c in range(cols):
                if counter  < self.fdomDayOfWeek or  counter >= totalDays:
                    grid.setText(r,c,"")
                else:
                    grid.setText(r,c, str((counter + 1)  - self.fdomDayOfWeek))
                    DOM.setStyleAttribute(cellformatter.getElement(r, c), "textAlign", "center")
                counter += 1

        self.daysPanel.setWidget(grid)
    
    def paintDays(self):
        formatter = self.grid.getCellFormatter()
        for r in range(1, self.grid.getRowCount()):
            for c in range(7):
                texto = self.grid.getText(r, c)
                if texto != "":
                    num = int(texto)
                    if num == self.day:
                        DOM.setStyleAttribute(formatter.getElement(r, c), "backgroundColor", "white")
                    else:
#                        DOM.setStyleAttribute(formatter.getElement(r, c), "backgroundColor", self.backColor)
                        if num == self.todayDay and self.month == self.todayMonth and self.year == self.todayYear:
                            DOM.setStyleAttribute(formatter.getElement(r, c), "color", "white")
                            DOM.setStyleAttribute(formatter.getElement(r, c), "backgroundColor", "rgb(0,192,0)")
                        else:
                            DOM.setStyleAttribute(formatter.getElement(r, c), "color", "black")
                            DOM.setStyleAttribute(formatter.getElement(r, c), "backgroundColor", self.backColor)
    
    def onCellClicked(self, grid, row, col):
        texto = grid.getText(row, col)
        if texto == "" or row == 0:
            return
        self.day = int(texto)
        self._rechargeDate()
        if self.autoHide:
            self.setVisible(False)
        
    
    def getTotalDrawDays(self):
        monthDays = Calendar.monthsDays[self.month]
        if self.isLeapYear() and self.month == 1:
            monthDays += 1
        monthDays += self.fdomDayOfWeek
        return monthDays
    
    def toString(self):
        return "%d%s%0.2d%s%0.2d" % (self.year, self.dateSep, self.month + 1, self.dateSep, self.day)
    
    def __str__(self):
        return self.__repr__()
    
class index:
    def onModuleLoad(self):
        self.miFecha = None
        
        vp = VerticalPanel()
        vp.setSpacing(4)
        hp = HorizontalPanel()
        hp.setSpacing(4)
        hp.setVerticalAlignment("middle")
#        DOM.setStyleAttribute(hp.getElement(), "verticalAlign", "middle")
        vp.add(hp)
        
        lbl = Label("Fecha: ")
        DOM.setStyleAttribute(lbl.getElement(), "backgroundColor", "rgb(255,255,255)")
        DOM.setStyleAttribute(lbl.getElement(), "padding", "2px")
        hp.add(lbl)

        self.txtFecha = TextBox()
        self.txtFecha.addClickListener(getattr(self, "mostrarCalendar"))
        self.txtFecha.setTextAlignment("right")
        hp.add(self.txtFecha)
        
        self.btnWrapper = FocusPanel()
        DOM.setStyleAttribute(self.btnWrapper.getElement(), "backgroundColor", "transparent")
        self.btnWrapper.addMouseListener(TooltipListener("Mostrar calendario"))
        self.btnCalendar = Button("...")
        self.btnCalendar.addClickListener(getattr(self, "mostrarCalendar"))
        self.btnWrapper.setWidget(self.btnCalendar)
        hp.add(self.btnWrapper)
        
        self.btnIsLeap = Button("Bisiesto?")
        self.btnIsLeap.addClickListener(esBisiesto)
        
        self.calendar = Calendar(visible = False, textbox = self.txtFecha, date = None, dateSep='-',
                                 firstDayOfWeek = 2, autoHide = True)
        
        proxy = self
        
        def esBisiesto():
            if proxy.calendar.isLeapYear():
                stri = "%d es bisiesto" % proxy.calendar.year
            else:
                stri = "%d NO es bisiesto" % proxy.calendar.year
            Window.alert(stri)            
        
        RootPanel().add(vp)
        RootPanel().add(self.calendar)
        y = self.txtFecha.getAbsoluteTop() + self.txtFecha.getOffsetHeight()
        x = self.txtFecha.getAbsoluteLeft()
        self.calendar.setPopupPosition(x, y)
    
    def mostrarCalendar(self):
#        Window.alert("Ahora te muestro el calendario...esperá un rato...")
        self.calendar.setVisible(True)


if __name__ == '__main__':
    app = index()
    app.onModuleLoad()

