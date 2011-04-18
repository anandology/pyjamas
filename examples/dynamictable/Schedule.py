from TimeSlot import TimeSlot

class Schedule:

    def __init__(self, timeSlots = None):
        self.timeSlots = []
        if timeSlots is not None:
            self.timeSlots = timeSlots

    def addTimeSlot(self, timeSlot):
        self.timeSlots.append(timeSlot)
        
    def getDescription(self, daysFilter):
        s = None
        for timeSlot in self.timeSlots:
            if daysFilter[timeSlot.dayOfWeek]:
                if s is None:
                    s = timeSlot.getDescription()
                else:
                    s += ", " + timeSlot.getDescription()
        if s is None:
            return ""
        else:
            return s
