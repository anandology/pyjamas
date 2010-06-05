""" This is a fairly sophisticated animation demo which has TextBoxes
    floating around under "gravity".  The mouse can be click-held to
    "attract" the red box, and all other boxes will be attracted to each
    other in a chain.  Right-mouse button will "repel" the red box.

    The demo shows features such as how to use Timers in combination with
    the time module, in order to get smooth animation regardless of the
    browser speed; event handling including mouse events as well as TextBox
    input changes; DeferredCommands in order to ensure that the Panel's
    correct Width and Height will be available at the time that the TextBoxes
    are added.

    As default mouse-events are prevented, to stop context menu, text
    drag/select effects etc. it is necessary to do TextBox focus selection
    "by hand", by checking whether a mouse-down happens to be inside the
    TextBox.
"""
   
import pyjd # this is dummy in pyjs.

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.AbsolutePanel import AbsolutePanel

from pyjamas.ui.MouseListener import MouseHandler

from pyjamas.Timer import Timer
from pyjamas import DeferredCommand
from pyjamas import Window
from pyjamas import DOM

from random import randint
from time import time
import math

class AnimatedBox(TextBox):

    def __init__(self, panel, **kwargs):

        TextBox.__init__(self, **kwargs)

        self.panel = panel
        self.x = randint(0, panel.getOffsetWidth())
        self.y = randint(0, panel.getOffsetHeight())
        self.x_vel = randint(-5, 5)
        self.y_vel = 0
        self.x_accel = 0
        self.y_accel = 20.0
        self.x_accel_extra = 0.0
        self.y_accel_extra = 0.0
        self.weight = 50
        self.panel.add(self, self.x, self.y)

        self.addChangeListener(self)

    def onChange(self, sender):
        try:
            txt = self.getText()
            self.weight = int(txt)
        except:
            self.weight = 50
            Window.alert("Please enter an integer")

    def get_x_accel(self):
        xa = self.x_accel + self.x_accel_extra
        self.x_accel_extra = 0.0
        return xa

    def get_y_accel(self):
        ya = self.y_accel + self.y_accel_extra
        self.y_accel_extra = 0.0
        return ya

    def move(self, diff_time):
        # v = u + at etc. etc.
        self.x_vel += diff_time * self.get_x_accel() * 20.0
        self.y_vel += diff_time * self.get_y_accel() * 20.0
        self.x_vel *= 0.95 # friction
        self.y_vel *= 0.95 # friction
        self.x += diff_time * self.x_vel
        self.y += diff_time * self.y_vel

        # restrict position (bounce!)
        max_width = self.panel.getOffsetWidth() - self.getOffsetWidth() 
        max_height = self.panel.getOffsetHeight() - self.getOffsetHeight() - 40
        
        if self.y < 0:
            self.y = -self.y
            self.y_vel = -self.y_vel
        if self.y >= max_height:
            self.y = max_height * 2 - self.y
            self.y_vel = -self.y_vel

        if self.x < 0:
            self.x = -self.x
            self.x_vel = -self.x_vel
        if self.x >= max_width:
            self.x = max_width * 2 - self.x
            self.x_vel = -self.x_vel

        # finally move the box in the panel
        self.panel.setWidgetPosition(self, self.x, self.y)

    def alter_accel(self, x, y, mult_factor):
        dx = self.x - x
        dy = self.y - y
        dist = math.pow(dx * dx + dy * dy, 0.5)
        if abs(dist) < 1e-5: # too small - don't do it!
            return
        self.x_accel_extra = mult_factor * self.weight / (dist/dx)
        self.y_accel_extra = mult_factor * self.weight / (dist/dy)
        
    def check_focus(self, x, y):
        """ check whether the mouse is within the bounds of this box:
            if so, set Focus on it, to allow data entry.
        """
        width = self.getOffsetWidth() 
        height = self.getOffsetHeight()
        if (x < self.x or y < self.y or
           x > self.x + width or y > self.y + width):
            return
        self.setFocus(True)

class AnimatedBoxes(AbsolutePanel, MouseHandler):

    def __init__(self):
        AbsolutePanel.__init__(self,
                               Width="100%",
                               Height="100%")
        # preventDefault=True stops context menu, drag, focus etc.
        MouseHandler.__init__(self, preventDefault=True)

        self.boxes = []
        self.mouse_down = False

        self.addMouseListener(self)

        self.add(HTML("""
            Click-hold left button to attract "0" box;<br />
            Click-hold right button to repel "0" box.<br />
            Other boxes will follow their neighbours.<br />
            "Gravity" always applies.<br />
            A small amount of "friction" keeps things reasonable.<br />
            If you click in a box, you can enter a new weight:<br />
            Press return and the box will react differently to the mouse.<br />
            Make sure you enter an integer.<br />
            """, 0, 0))

        DeferredCommand.add(self) # deferred call to self.execute()

    def execute(self):
        """ add animated boxes after Panel Width and Height settle down.
        """
        for i in range(10):
            if i == 0:
                style = "leadboxstyle"
            else:
                style = "boxstyle"
            box = AnimatedBox(self, Text="50",
                                    VisibleLength=1,
                                    StyleName=style)
            self.boxes.append(box)

        # begin animation
        self.cur_time = time()
        Timer(1, self)

    def accel_boxes(self, x, y, accel_factor):
        """ cause box 0 to follow or repel from the specified position;
            all other boxes are attracted to their next neighbour.
        """
        self.boxes[0].alter_accel(x, y, accel_factor)
        for i in range(1, len(self.boxes)):
            prev_box = self.boxes[i-1]
            self.boxes[i].alter_accel(prev_box.x, prev_box.y, -1.0)

    def move(self, diff_time):
        for box in self.boxes:
            box.move(diff_time)

    def onTimer(self, timer):
        new_time = time()
        diff_time = new_time - self.cur_time
        self.cur_time = new_time
        if self.mouse_down:
            self.accel_boxes(self.mouse_x, self.mouse_y, self.mul_factor)
        self.move(diff_time)
        Timer(50, self)
        
    def onMouseMove(self, sender, x, y):
        if not self.mouse_down:
            return
        self.mouse_x = x - self.getAbsoluteLeft()
        self.mouse_y = y - self.getAbsoluteTop()

    def onMouseDown(self, sender, x, y):
        self.mouse_down = True

        self.mouse_x = x - self.getAbsoluteLeft()
        self.mouse_y = y - self.getAbsoluteTop()

        for box in self.boxes:
            box.check_focus(self.mouse_x, self.mouse_y)

        event = DOM.eventGetCurrentEvent()
        if DOM.eventGetButton(event) == 2:
            self.mul_factor = 1.0
        else:
            self.mul_factor = -1.0
        self.onMouseMove(sender, x, y)

    def onMouseUp(self, sender, x, y):
        self.mouse_down = False


if __name__ == '__main__':
    pyjd.setup("public/linuxjournal.html")
    RootPanel().add(AnimatedBoxes())
    pyjd.run()

