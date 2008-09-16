from pyjamas.ui import RootPanel
from DayFilterWidget import DayFilterWidget
from SchoolCalendarWidget import SchoolCalendarWidget
from pyjamas import Window

class DynaTable:

    def onModuleLoad(self):
        slot = RootPanel("calendar")
        Window.alert("slot:" + slot)
        if slot:
            calendar = SchoolCalendarWidget(15)
            Window.alert(len(slot.children))
            Window.alert(slot.children)
            slot.add(calendar)
            
            slot = RootPanel("days")
            if slot:
                filterWidget = DayFilterWidget(calendar)
                slot.add(filterWidget)
