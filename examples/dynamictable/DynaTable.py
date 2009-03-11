from pyjamas.ui.RootPanel import RootPanel
from DayFilterWidget import DayFilterWidget
from SchoolCalendarWidget import SchoolCalendarWidget

class DynaTable:

    def onModuleLoad(self):
        slot = RootPanel("calendar")
        if slot:
            calendar = SchoolCalendarWidget(15)
            slot.add(calendar)
            
            slot = RootPanel("days")
            if slot:
                filterWidget = DayFilterWidget(calendar)
                slot.add(filterWidget)


if __name__ == '__main__':
    app = DynaTable()
    app.onModuleLoad()
