class Datetime:
    def __init__(self, year=None, month=None, day=None, hours=None, minutes=None, seconds=None):
        JS("""	
	if (seconds != null)
	    this.date = new Date(year, month, day, hours, minutes, seconds);
	else if (minutes != null)
	    this.date = new Date(year, month, day, hours, minutes);
	else if (hours != null)
	    this.date = new Date(year, month, day, hours);
	else if (day != null)
	    this.date = new Date(year, month, day);
	else if (month != null)
	    this.date = new Date(year, month);
	else if (year != null)
    {
        if (pyjslib.isNumber(year))
        {
            /* a number on its own is a "value" */
            this.date = new Date(year);
        }
        else if (pyjslib.isinstance(year, Date.DateTime))
        {
            /* Datetime object */
            this.date = new Date(year.date.valueOf());
        }
    }
	else
	    this.date = new Date();
        """)

    def getValue(self):
        JS("""
	return this.date.valueOf();
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

