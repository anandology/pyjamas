from Person import Person
from Schedule import Schedule

class Professor(Person):

    def __init__(self, teachingSchedule=None, **kwargs):
        Person.__init__(self, **kwargs)
        if teachingSchedule is None:
            self.teachingSchedule = Schedule()
        else:
            self.teachingSchedule = teachingSchedule
        
    def getSchedule(self, daysFilter):
        return self.teachingSchedule.getDescription(daysFilter)
    
    def getTeachingSchedule(self):
        return self.teachingSchedule
