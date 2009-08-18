# Copyright (C) 2009, Radoslav Kirov
#
# Lightout game, by Radoslav Kirov

import pyjd # this is dummy in pyjs.
from pyjamas.ui.FlowPanel import FlowPanel
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Button import Button
from pyjamas.ui.CheckBox import CheckBox
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Label import Label
from pyjamas.ui.Grid import Grid
from pyjamas import Window
from pyjamas import DOM
from pyjamas.ui.FocusWidget import FocusWidget

class GridCell(FocusWidget):
    def __init__(self,i,j):
        self.i = i
        self.j = j
        self.light = True
        element = DOM.createDiv()
        #DOM.setInnerHTML(element,'<b>%i%i</b>' % (i,j))
        FocusWidget.__init__(self, element)
        self.redraw()
        self.addClickListener(self)
    
    def redraw(self):
        if self.light:
            self.setStyleName("on")
        else:
            self.setStyleName("off")
    
    def toggle(self):
        if self.light:
            self.light = False
        else:
            self.light = True
        self.redraw()
            
    def onClick(self, sender):
        if self.i>0:
            self.parent.getWidget(self.i-1,self.j).toggle()
        if self.i<self.parent.getRowCount()-1:
            print self.i+1, self.j
            self.parent.getWidget(self.i+1,self.j).toggle()
        if self.j>0:
            self.parent.getWidget(self.i,self.j-1).toggle()
        if self.j<self.parent.getColumnCount()-1:
            self.parent.getWidget(self.i,self.j+1).toggle()
        self.toggle()
        self.check_win()
        
    def check_win(self):
        for i in range(self.parent.getRowCount()):
            for j in range(self.parent.getColumnCount()):
                if self.parent.getWidget(i,j).light:
                    return 
        Window.alert('You win!!! But can you beat the next level?')
        global game
        game.next_level()

class Game(SimplePanel):
    def __init__(self,level):
        self.level = level
        SimplePanel.__init__(self)
        self.start_game()
        
    def start_game(self):
        dim = self.level
        grid = Grid(dim,dim)
        grid.setStyleName("grid")
        for i in range(dim):
            for j in range(dim):
                gc = GridCell(i,j)
                grid.setWidget(i,j,gc)
        self.add(grid)
    
    def next_level(self):
        self.remove(self.getWidget())
        self.level+=1
        self.start_game()
        
if __name__ == '__main__':
    pyjd.setup("public/lightout.html")
    game = Game(3)
    RootPanel().get('game').add(game)
    #RootPanel().add(game)
    pyjd.run()
