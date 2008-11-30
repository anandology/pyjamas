class Datetime:
    def __init__(self, year=None, month=None, date=None, hours=None, minutes=None, seconds=None):
        JS("""	
	if (seconds != null)
	    this.date = new Date(year, month, date, hours, minutes, seconds);
	else if (minutes != null)
	    this.date = new Date(year, month, date, hours, minutes);
	else if (hours != null)
	    this.date = new Date(year, month, date, hours);
	else if (date != null)
	    this.date = new Date(year, month, date);
	else if (month != null)
	    this.date = new Date(year, month);
	else if (year != null)
	    this.date = new Date(year);
	else
	    this.date = new Date();
        """)

    def getDate(self):
        JS("""
	return this.date.getDate();
	""")

    def getDay(self):
        JS("""
	return this.date.getDay();
	""")
	
    def getHours(self):
        JS("""
	return this.date.getHours();
	""")
	
    def getMinutes(self):
        JS("""
	return this.date.getMinutes();
	""")

    def getMonth(self):
        JS("""
	return this.date.getMonth();
	""")

    def getSeconds(self):
        JS("""
	return this.date.getSeconds();
	""")

    def getTime(self):
        JS("""
	return this.date.getTime();
	""")

    def getYear(self):
        JS("""
	return this.date.getYear();
	""")

    def setDate(self, value):
        JS("""
	this.date.setDate(value);
	""")

    def setDay(self, value):
        JS("""
	this.date.setDay(value);
	""")
	
    def setHours(self, value):
        JS("""
	this.date.setHours(value);
	""")
	
    def setMinutes(self, value):
        JS("""
	this.date.setMinutes(value);
	""")

    def setMonth(self, value):
        JS("""
	this.date.setMonth(value);
	""")

    def setSeconds(self, value):
        JS("""
	this.date.setSeconds(value);
	""")

    def setTime(self, value):
        JS("""
	this.date.setTime(value);
	""")

    def setYear(self, value):
        JS("""
	this.date.setYear(value);
	""")

