from Schedule import Schedule
from Person import Person

class Student(Person):

    def __init__(self, classSchedule=None, **kwargs):
        Person.__init__(self, **kwargs)
        if classSchedule is None:
            self.classSchedule = Schedule()
        else:
            self.classSchedule = classSchedule

    def getSchedule(self, daysFilter):
        return self.classSchedule.getDescription(daysFilter)
    
    def getClassSchedule(self):
        return self.classSchedule
