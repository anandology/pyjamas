# Copyright (C) 2010, Daniel Popowich <danielpopowich@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# for desktop
import pyjd
# ui imports
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Button import Button
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.Grid import Grid
from pyjamas.ui.HorizontalSlider import HorizontalSlider
from pyjamas.ui.Label import Label
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.CaptionPanel import CaptionPanel

# other pyjamas imports
from pyjamas import DOM

# pyjamas client-side library
from random import random
from datetime import datetime

# Timer class
from pyjamas.Timer import Timer

######################################################################
# The next three classes demonstrate three ways to create/use timers
######################################################################

class Clock:

    # pyjamas doesn't generate __doc__
    __doc__ = '''This demonstrates using Timer instantiated with the
    notify keyword, as in:<pre> timer = Timer(notify=func) </pre>When
    the timer fires it will call func() with no arguments (or
    <code>self</code> if it is a bound method as in this example).
    This timer is scheduled with the <code>scheduleRepeating()</code>
    method, so after func() is called, it is automatically rescheduled
    to fire again after the specified period.  The timer can be
    cancelled by calling the <code>cancel()</code> method; this
    happens when you click on the button.
    '''

    
    start_txt = 'Click to start the clock'
    stop_txt = 'Click to stop the clock'
    
    def __init__(self):

        # the button
        self.button = Button(listener=self)
        # set an attr on the button to keep track of its state
        self.button.stop = False
        # date label
        self.datelabel = Label(StyleName='clock')
        # the timer
        self.timer = Timer(notify=self.updateclock)
        # kick start
        self.onClick(self.button)

    def onClick(self, button):
        if self.button.stop:
            # we're stopping the clock
            self.button.stop = False
            self.timer.cancel()
            self.button.setText(self.start_txt)
        else:
            # we're starting the clock
            self.button.stop = True
            self.timer.scheduleRepeating(1000)
            self.button.setText(self.stop_txt)

    def updateclock(self, timer):

        # the callable attached to the timer with notify
        dt = datetime.now().replace(microsecond=0)
        self.datelabel.setText(dt.isoformat(' '))

class PopupTimerButton(Timer, Button):

    __doc__ = '''The timer in this demo is a subclass of Timer which
    implements the <code>run()</code> method.  Worth noting in this
    example is the use of the method <code>schedule()</code> at the
    end of <code>run()</code> (contrast this to the use of
    <code>scheduleRepeating()</code> in the previous example).  In this
    demo when the timer counts down to zero it creates a popup which
    will appear in the box to the left.  The timer can be cancelled by
    clicking the button before it reaches zero.
    '''

    def __init__(self, countdown):
        # It's a Timer, no it's a Button, WAIT!  It's BOTH!!
        Timer.__init__(self)
        Button.__init__(self)

        # save the countdown value
        self.countdown_save = countdown
        # this instance handles the clicks
        self.addClickListener(self)
        # the box the popups go into
        self.box = SimplePanel(StyleName='popupbox')
        # kickstart
        self.reset()

    def run(self):

        # When subclassing, we just implement the run method

        # update the countdown
        self.setHTML('Popup in <b>%d</b> seconds! (Click to cancel)'
                     % self.countdown)
        # reschdule if we're not to zero else create the popup
        self.countdown -= 1
        if self.countdown >= 0:
            self.schedule(1000)
        else:
            self.create_popup()
            self.reset()
    
    def reset(self):
        # reset to starting state
        self.setHTML('Click for countdown popup')
        self.countdown = self.countdown_save
        self.start = True

    def onClick(self, *arg):

        # handle button clicks

        # are we cancelling?
        if not self.start:
            self.cancel()
            self.reset()
            return

        # no we're starting
        self.start = False
        self.schedule(1)

    def create_popup(self):

        # create the popup in the middle box
        popup = DialogBox(False, False)
        popup.onClick = lambda w: popup.hide()
        popup.setHTML('<b>Hello!</b>')
        popup.setWidget(Button('Close', popup))
        x = self.box.getAbsoluteLeft() + random()*100
        y = self.box.getAbsoluteTop() + random()*100
        popup.setPopupPosition(x, y)
        popup.show()

class RandomColor:

    __doc__ = '''This last example demonstrates what most pyjamas
    programmers currently do with timers: create a Timer instance
    specifying <code>notify</code> with an object that has an
    <code>onTimer</code> attribute that is callable.  The slider on
    the left will adjust how often the middle panel changes color; it
    is either OFF or a value of seconds from 1 to 5.  Changing the
    slider immediately cancels the current timer and starts a new
    timer to change the color in the newly specified time.  Like the
    previous example, this timer reschedules itself (if it wasn't
    turned off) at the end of the call to <code>onTimer()</code>.
    '''

    def __init__(self):

        # create the label and slider
        self.__label = Label('OFF')
        self.slider = slider = HorizontalSlider(0, 5, step=1,
                                                StyleName="slider")
        slider.setDragable(True)
        slider.addControlValueListener(self)

        # put them in a hpanel
        self.hpanel = hpanel = HorizontalPanel(Spacing=10)
        hpanel.add(slider)
        hpanel.add(self.__label)

        # create the color panel and give it color
        self.colorpanel = CaptionPanel('Color:',
                                       SimplePanel(StyleName='colorpanel'))
        self.randomcolor()

        # we're initially off
        self.value = 0
        # create our timer
        self.timer = Timer(notify=self)

    def initialize(self):

        # this method solves an apparent bug with the slider: the
        # slider doesn't draw its handle if the position is set before
        # showing, so instead of doing this in __init__ (where I
        # originally had it), this method gets called after it is
        # shown on the root panel.  See below when it gets called.
        self.slider.setValue(self.value)
        self.slider.setControlPos(self.value)

    def onTimer(self, timer):

        # when the timer fires we randomize the color and (maybe)
        # reschedule ourselves.
        self.randomcolor()
        v = self.value * 1000
        if v:
            self.timer.schedule(v)

    def onControlValueChanged(self, sender, old, new):

        # event handler for when the slider is moved.
        if new == self.value:
            return
        self.value = new

        # is it being turned off?
        if new == 0:
            self.__label.setText('OFF')
            self.timer.cancel()
        else:
            # no it's being reset
            self.__label.setText(str(new) + ' sec')
            self.onTimer(self.timer)
            
    def randomcolor(self):

        # randomize the color and set the panel accordingly
        r = random()*256
        g = random()*256
        b = random()*256
        e = self.colorpanel.getWidget().getElement()
        color = '#%02x%02x%02x' % (r, g, b)
        self.colorpanel.setCaption('Color: %s' % color)
        DOM.setStyleAttribute(e, "background", color)


######################################################################
# The app
######################################################################
class timerdemo:

    def __init__(self):

        # layed out in a grid with odd rows a different color for
        # visual separation
        grid = Grid(4,3,CellPadding=50,CellSpacing=0)
        rf = grid.getRowFormatter()
        rf.setStyleName(1, 'oddrow')
        rf.setStyleName(3, 'oddrow')

        # the clock
        clock = Clock()
        grid.setWidget(0, 0, CaptionPanel('Using notify()', clock.button, StyleName='left'))
        grid.setWidget(0, 1, clock.datelabel)
        grid.setWidget(0, 2, HTML(Clock.__doc__, StyleName='desc'))

        # popup timer buttons
        ptb = PopupTimerButton(5)
        grid.setWidget(1, 0, CaptionPanel('Subclassing Timer()', ptb, StyleName='left'))
        grid.setWidget(1, 1, ptb.box)
        grid.setWidget(1, 2, HTML(PopupTimerButton.__doc__, StyleName='desc'))

        # the second instance
        ptb = PopupTimerButton(15)
        grid.setWidget(2, 0, CaptionPanel('Subclassing Timer()&nbsp;&nbsp;(<em>again</em>)',
                                          ptb, StyleName='left'))
        grid.setWidget(2, 1, ptb.box)
        grid.setWidget(2, 2, HTML('''This is the same as the previous
                                  example and is here to demonstrate
                                  creating multiple timers (each with
                                  their own state) which is difficult
                                  to do without sublcassing''', StyleName='desc'))

        # random color
        randomcolor = RandomColor()
        grid.setWidget(3, 0, CaptionPanel('Using onTimer()', randomcolor.hpanel, StyleName='left'))
        grid.setWidget(3, 1, randomcolor.colorpanel)
        grid.setWidget(3, 2, HTML(RandomColor.__doc__, StyleName='desc'))

        # add it all to the root panel
        RootPanel().add(grid)

        # kickstart the slider handle (see above concerning a
        # potential bug)
        randomcolor.initialize()

def onModuleLoad():
    timerdemo()

if __name__ == '__main__':

    pyjd.setup("public/timerdemo.html")
    onModuleLoad()
    pyjd.run()
