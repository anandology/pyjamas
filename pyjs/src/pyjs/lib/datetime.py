from __pyjamas__ import JS

class Datetime:
    def __init__(self, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        JS("""	
	if (seconds != null)
	    self.date = new Date(year, month, day, hours, minutes, seconds);
	else if (minutes != null)
	    self.date = new Date(year, month, day, hours, minutes);
	else if (hours != null)
	    self.date = new Date(year, month, day, hours);
	else if (day != null)
	    self.date = new Date(year, month, day);
	else if (month != null)
	    self.date = new Date(year, month);
	else if (year != null)
    {
        if (pyjslib.isNumber(year))
        {
            /* a number on its own is a "value" */
            self.date = new Date(year);
        }
        else if (pyjslib.isinstance(year, Date.DateTime))
        {
            /* Datetime object */
            self.date = new Date(year.date.valueOf());
        }
    }
	else
	    self.date = new Date();
        """)

    def getValue(self):
	return self.date.valueOf()

    def getDate(self):
	return self.date.getDate()

    def getDay(self):
	return self.date.getDay()
	
    def getHours(self):
	return self.date.getHours()
	
    def getMinutes(self):
	return self.date.getMinutes()

    def getMonth(self):
	return self.date.getMonth()

    def getSeconds(self):
	return self.date.getSeconds()

    def getTime(self):
	return self.date.getTime()

    def getYear(self):
	return self.date.getYear()

    def setDate(self, value):
	self.date.setDate(value)

    def setDay(self, value):
	self.date.setDay(value)
	
    def setHours(self, value):
	self.date.setHours(value)
	
    def setMinutes(self, value):
	self.date.setMinutes(value)

    def setMonth(self, value):
	self.date.setMonth(value)

    def setSeconds(self, value):
	self.date.setSeconds(value)

    def setTime(self, value):
	self.date.setTime(value)

    def setYear(self, value):
	self.date.setYear(value)

