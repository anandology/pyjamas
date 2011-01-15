# Simple canvas demo game
# Copyright (C) 2010 James Hedley (jameskhedley@gmail.com)
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
#
# Distributed as part of pyjamas (http://pyjs.org)
# Wordlists derived from http://wordlist.sourceforge.net

from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Composite import Composite
from pyjamas.ui.Button import Button
from pyjamas.ui.HTML import HTML
from pyjamas.ui.RadioButton import RadioButton
from pyjamas.Canvas.GWTCanvas import GWTCanvas
from pyjamas import Window
import math
import random
import string
import Wordlist_20
import Wordlist_15
import Wordlist_10
import Wordlist_5

class HangManWidget(Composite):
    def __init__(self):
        Composite.__init__(self)
        self.guesses = 0
        self.score = 0
        self.level = 5
        self.answer = ''
        self.blanks = ''

        self.vp_main = VerticalPanel()
        self.vp_main.setSpacing(4)
        self.hangdude = HangDude()
        self.cmdNew = Button("Start", self)

        self.radLevel5 = RadioButton("group0", "5-10 letters")
        self.radLevel5.setChecked(True)
        self.radLevel10 = RadioButton("group0", "10-15 letters")
        self.radLevel15 = RadioButton("group0", "15-20 letters")
        self.radLevel20 = RadioButton("group0", "20+ letters")

        self.radLevel5.addClickListener(self.onRadioSelect)
        self.radLevel10.addClickListener(self.onRadioSelect) 
        self.radLevel15.addClickListener(self.onRadioSelect)
        self.radLevel20.addClickListener(self.onRadioSelect) 

        self.rad_hp = HorizontalPanel()
        self.rad_hp.setSpacing(4)
        self.rad_hp.add(self.radLevel5)
        self.rad_hp.add(self.radLevel10)
        self.rad_hp.add(self.radLevel15)
        self.rad_hp.add(self.radLevel20)
        self.rad_hp.add(self.cmdNew)

        self.puzzlestring = HTML()

        self.key_widgets = []
        for i in range (len(string.uppercase)):
            self.key_widgets.append(Button(string.uppercase[i:i+1], self))

        self.toprow = HorizontalPanel()
        self.midrow = HorizontalPanel()
        self.botrow = HorizontalPanel()

        for i in range(len(self.key_widgets)):
            if i <= 7:
                 self.toprow.add(self.key_widgets[i])
            elif i <= 16:
                 self.midrow.add(self.key_widgets[i])
            else:
                 self.botrow.add(self.key_widgets[i])
        
        self.vp_main.add(self.hangdude)
        self.vp_main.add(self.puzzlestring)
        self.vp_main.add(self.toprow)
        self.vp_main.add(self.midrow)
        self.vp_main.add(self.botrow)
        self.vp_main.add(self.rad_hp)

        for i in range(1,12):
            self.hangdude.draw(i)

        self.setWidget(self.vp_main)

    def onClick(self, sender):
        found = False
        if sender == self.cmdNew:
            self.blanks = ''
            self.hangdude.clear()
            self.guesses = 0
            self.score = 0
            for i in range(len(self.key_widgets)):
                self.key_widgets[i].setEnabled(True)
            if self.level == 5: 
                words = Wordlist_5.words
            elif self.level == 10: 
                words = Wordlist_10.words
            elif self.level == 15: 
                words = Wordlist_15.words
            elif self.level == 20: 
                words = Wordlist_20.words
            #pick a random word
            g = random.Random()
            r = int( g.random() * len(words))
            self.answer = words[r].upper()
            for i in range(len(self.answer)):
                if self.answer[i] == ' ':
                    self.blanks += '  '
                else:
                    self.blanks += '_ '
            self.puzzlestring.setHTML(self.blanks)
        else:
            guess_letter = sender.getText()
            sender.setEnabled(False)
            for i in range(len(self.answer)):
                if self.answer[i:i+1] == guess_letter:
                    j=i+1
                    self.blanks = self.blanks[0:(j*2)-2] + guess_letter + ' ' + self.blanks[j*2:]
                    found = True
                    self.score += 1
            self.puzzlestring.setHTML(self.blanks)
            if not found:
                self.guesses += 1
                self.hangdude.draw(self.guesses)
                if self.guesses >= 11:
                    Window.alert("You lose! Answer: " + self.answer)
            else:
                if self.score >= len(self.answer):
                    Window.alert("You win!")

    def onRadioSelect(self, sender, keyCode=None, modifiers=None):
        if sender == self.radLevel5:
            self.level = 5
        elif sender == self.radLevel10:
            self.level = 10
        elif sender == self.radLevel15:
            self.level = 15
        elif sender == self.radLevel20:
            self.level = 20

class HangDude(HorizontalPanel):
    def __init__(self):
        HorizontalPanel.__init__(self)
        self.context = GWTCanvas(300,300,300,300)
        self.context.addStyleName("gwt-canvas")
        self.add(self.context)

    def clear(self):
        self.context.clear()

    def draw(self, guesses):
        self.context.fillStyle = '#000'
        self.context.lineWidth = 2 
        if guesses == 1:
            self.context.fillRect(20, 280, 200,10)
        elif guesses == 2:
            self.context.fillRect(40, 20, 10, 260)
        elif guesses == 3:
            self.context.fillRect(20, 20, 160,10)
        elif guesses == 4:
            self.context.saveContext()
            self.context.translate(80,30)
            self.context.rotate(130 * math.pi / 180)
            self.context.fillRect(0,0, 50,10)
            self.context.restoreContext()
        elif guesses == 5:
            self.context.fillRect(140, 20, 10, 50)
        elif guesses == 6:
            self.context.beginPath()
            self.context.arc(145, 100, 30, 0, math.pi * 2, True)
            self.context.closePath()
            self.context.stroke()
        elif guesses == 7:
            self.context.fillRect(145, 130, 2, 80)
        elif guesses == 8:
            self.context.saveContext()
            self.context.translate(147,160)
            self.context.rotate(130 * math.pi / 180)
            self.context.fillRect(0,0, 50,2)
            self.context.restoreContext()
        elif guesses == 9:
            self.context.saveContext()
            self.context.translate(147,160)
            self.context.rotate(45 * math.pi / 180)
            self.context.fillRect(0,0, 50,2)
            self.context.restoreContext()
        elif guesses == 10:
            self.context.saveContext()
            self.context.translate(147,210)
            self.context.rotate(130 * math.pi / 180)
            self.context.fillRect(0,0, 60,2)
            self.context.restoreContext()
        elif guesses == 11:
            self.context.saveContext()
            self.context.translate(147,210)
            self.context.rotate(45 * math.pi / 180)
            self.context.fillRect(0,0, 60,2)
            self.context.restoreContext()
        self.context.restoreContext()

