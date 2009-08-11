
# vim: set ts=4 sw=4 expandtab:

import puremvc.patterns.command
import puremvc.interfaces

from model.TimeProxy import TimeProxy

from view.DialogMediator import DialogMediator
from view.MenuMediator import MenuMediator
from view.DatePickerMediator import DatePickerMediator
from view.TimeGridMediator import TimeGridMediator
from view.SummaryMediator import SummaryMediator

class StartupCommand(puremvc.patterns.command.SimpleCommand, puremvc.interfaces.ICommand):
    def execute(self,note):
        self.facade.registerProxy(TimeProxy())

        mainPanel = note.getBody()
        self.facade.registerMediator(DialogMediator(mainPanel))
        self.facade.registerMediator(MenuMediator(mainPanel.menuBar))
        self.facade.registerMediator(TimeGridMediator(mainPanel.timeGrid))
        self.facade.registerMediator(SummaryMediator(mainPanel.summary))

        # This one must be registered last, or at least after TimeGridMediator
        # Fires DATE_SELECTED notification, which is used in TimeGridMediator
        self.facade.registerMediator(DatePickerMediator(mainPanel.datePicker))
