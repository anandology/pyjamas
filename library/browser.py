class Element:
    def __init__(self, tag=None, element=None):
        if tag != None:
            ___tojs___('''
            self.element = __document.createElement(tag);
            ''')
        elif element != None:
            self.element = element
        else:
            raise Exception
        
        self.element.__ref = self;
        self.activeEvents = []

    def append(self, element):
        ___tojs___('''
        self.element.appendChild(element.element);
        ''')

    def prepend(self, element):
        ___tojs___('''
        self.element.insertBefore(element.element, self.element.firstChild);
        ''')

    def getX(self):
        ___tojs___('''
        var obj = self.element;
	    var curleft = 0;
    	if (obj.offsetParent) {
	    	curleft = obj.offsetLeft
		    while (obj = obj.offsetParent) {
			    curleft += obj.offsetLeft
		    }
	    }
	    return curleft;
        ''')

    def getY(self):
        ___tojs___('''
        var obj = self.element;
	    var curtop = 0;
    	if (obj.offsetParent) {
	    	curtop = obj.offsetTop
		    while (obj = obj.offsetParent) {
			    curtop += obj.offsetTop
		    }
	    }
	    return curtop;
        ''')

    def getWidth(self):
        ___tojs___('''
        return self.element.offsetWidth;
        ''')

    def getHeight(self):
        ___tojs___('''
        return self.element.offsetHeight;
        ''')

    def setWidth(self, width):
        self.setStyle('width',width)

    def setHeight(self, height):
        self.setStyle('height',height)

    def setStyle(self, property, value):
        ___tojs___('''
        self.element.style[property] = value;
        ''')

    def getStyle(self, property):
        ___tojs___('''
        return self.element.style[property];
        ''')

    def setProperty(self, property, value):
        ___tojs___('''
        //self.element.setAttribute(property,value);
        self.element[property] = value;
        ''')

    def getProperty(self, property):
        ___tojs___('''
        //return self.element.getAttribute(property);
        return self.element[property];
        ''')

    def setHTML(self, content):
        ___tojs___('''
        self.element.innerHTML = content;
        ''')

    def getHTML(self):
        ___tojs___('''
        return self.element.innerHTML;
        ''')

    def catchEvents(self, name, object):
        ___tojs___('''
        var tmp = function(e) {
            if (!e) var e = __window.event;
        	if (e.target) targ = e.target;
	        else if (e.srcElement) targ = e.srcElement;
	        if (targ.nodeType == 3) targ = targ.parentNode;
            if (targ.__ref)
                object.dom_event([e, targ.__ref],{});
            else
                object.dom_event([e, null],{});
        };
        ''')
        self.activeEvents.append((name, object))
        ___tojs___('''
        var old_callback = self.element['on'+name];
        self.element['on'+name] = function(e){if(old_callback){old_callback(e);}tmp(e);};
        ''')

class Document:
    window = Element(element= ___tojs___('__window'))
    document = Element(element= ___tojs___('__document'))
    body = Element(element= ___tojs___('__document.body'))

    @staticmethod
    def createElement(tag):
        return Element(tag)
    
    @staticmethod
    def append(element):
        ___tojs___('''
        __document.body.appendChild(element.element);
        ''')

    @staticmethod
    def setContent(message):
        ___tojs___('''
        __document.body.innerHTML = message;
        ''')

    @staticmethod
    def setTitle(title):
        ___tojs___('''
        __document.title = title;
        ''')
