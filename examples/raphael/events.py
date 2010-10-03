""" test.py

    Simple testing framework for the raphael wrapper.
"""

import pyjd
from pyjamas.ui.RootPanel   import RootPanel
from pyjamas.ui.TabPanel import TabPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.HTML import HTML
from pyjamas.ui import HasAlignment
from pyjamas import DOM
from pyjamas import log
from pyjamas.raphael.raphael import Raphael

class Events(VerticalPanel):            
    def __init__(self,width=600,height=300):
        VerticalPanel.__init__(self)    
        self.elements=[]
        self.desc=[]
        
        self.canvas = Raphael(width, height)        
        self.canvas.addListener('mouseup',self.onCanvasMouseup)
        self.canvas.addListener('mousemove',self.onCanvasMousemove)
        self.canvas.addListener('dblclick',self.onCanvasDblClick)
        self.canvas.addListener('contextmenu',self.onCanvasContextmenu)
        self.canvas.addListener('mousedown',self.onCanvasMousedown)
        
        self.add(self.canvas)
        self.status=Label('Execute any events on the canvas!')
        self.add(self.status)
        
    def set_status(self,status):
        self.status.setText(status)        

    def draw(self):

        circle1=self.canvas.circle(50,50,25)
        circle1.setAttr('fill','#000')
        circle1.setAttrs({'cursor':'move','opacity':0.6})
        circle1.addListener('mouseup',self.onElementMouseup)
        circle1.addListener('mousemove',self.onElementMousemove)
        circle1.addListener('dblclick',self.onElementDblClick)
        circle1.addListener('contextmenu',self.onElementContextmenu)
        circle1.addListener('mousedown',self.onElementMousedown)        
        self.elements.append(circle1)
        self.desc.append('Circle 1')
        
        circle2=self.canvas.circle(100,100,25)
        circle2.setAttr('fill','#000')
        circle2.setAttrs({'cursor':'move','opacity':0.6})                
        circle2.addListener('mouseup',self.onElementMouseup)
        circle2.addListener('mousemove',self.onElementMousemove)
        circle2.addListener('dblclick',self.onElementDblClick)
        circle2.addListener('contextmenu',self.onElementContextmenu)
        circle2.addListener('mousedown',self.onElementMousedown)
        self.elements.append(circle2)
        self.desc.append('Circle 2')

        rect1=self.canvas.rect(200,100,30,30)
        rect1.setAttr('fill','#000')
        rect1.addListener('mouseup',self.onElementMouseup)
        rect1.addListener('mousemove',self.onElementMousemove)
        rect1.addListener('dblclick',self.onElementDblClick)
        rect1.addListener('contextmenu',self.onElementContextmenu)
        rect1.addListener('mousedown',self.onElementMousedown)
        self.elements.append(rect1)
        self.desc.append('Rectangle 1')
        
        rect2=self.canvas.rect(200,150,30,30)
        rect2.setAttr('fill','#000')
        rect2.addListener('mouseup',self.onElementMouseup)
        rect2.addListener('mousemove',self.onElementMousemove)
        rect2.addListener('dblclick',self.onElementDblClick)
        rect2.addListener('contextmenu',self.onElementContextmenu)
        rect2.addListener('mousedown',self.onElementMousedown)        
        self.elements.append(rect2)
        self.desc.append('Rectangle 2')
                
        connection=self.canvas.connection(rect1,rect2)
        connection.addListener('mouseup',self.onElementMouseup)
        connection.addListener('mousemove',self.onElementMousemove)
        connection.addListener('dblclick',self.onElementDblClick)
        connection.addListener('contextmenu',self.onElementContextmenu)
        connection.addListener('mousedown',self.onElementMousedown)        
        self.elements.append(connection)
        self.desc.append('Connection')   
        
        ellipse=self.canvas.ellipse(200,200,25,40)
        text=self.canvas.text(200,200,'ABC')   
        set=self.canvas.set()
        set.add(ellipse)
        set.add(text)      
        set.addListener('mousemove',self.onElementMousemove)
        self.elements.append(set)
        self.desc.append('Set')           

    def onCanvasMousedown(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        self.set_status('Mousedown on Canvas at '+str(x)+', '+str(y))

    def onCanvasMouseup(self,obj,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        self.set_status('Mousemove on Canvas at '+str(x)+', '+str(y))
    
    def onCanvasMousemove(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        self.set_status('Mousemove on Canvas at '+str(x)+', '+str(y))

    def onCanvasDblClick(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        self.set_status('Doubleclick on Canvas at '+str(x)+', '+str(y))
        
    def onCanvasContextmenu(self, sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        self.set_status('Contextmenue on Canvas at '+str(x)+', '+str(y))
        DOM.eventPreventDefault(event)

    def onElementMousedown(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        s = self.desc[self.elements.index(sender)]
        self.set_status('Mousedown on Element '+s+' at '+str(x)+', '+str(y))
        DOM.eventCancelBubble(event,True)
                
    def onElementMouseup(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        s = self.desc[self.elements.index(sender)]
        self.set_status('Mouseup on Element '+s+' at '+str(x)+', '+str(y))
        DOM.eventCancelBubble(event,True)
    
    def onElementMousemove(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        s = self.desc[self.elements.index(sender)]
        self.set_status('Mousemove on Element '+s+' at '+str(x)+', '+str(y))
        DOM.eventCancelBubble(event,True)

    def onElementDblClick(self,sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        s = self.desc[self.elements.index(sender)]
        self.set_status('Doubleclick on Element '+s+' at '+str(x)+', '+str(y))
        DOM.eventCancelBubble(event,True)
        
    def onElementContextmenu(self, sender,event):
        x = DOM.eventGetClientX(event) - DOM.getAbsoluteLeft(self.canvas.getElement())
        y = DOM.eventGetClientY(event) - DOM.getAbsoluteTop(self.canvas.getElement())
        s = self.desc[self.elements.index(sender)]
        self.set_status('Contextmenue on Element '+s+' at '+str(x)+', '+str(y))
        DOM.eventCancelBubble(event,True)
        DOM.eventPreventDefault(event)
        
if __name__ == "__main__":    
    pyjd.setup("./media/events.html")
    events=Events()
    RootPanel().add(events)
    events.draw()
    pyjd.run()

