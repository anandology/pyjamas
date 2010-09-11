# MineSweeper game by Suzan Shakya:suzan.shakya@gmail.com

import pyjd

from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.FocusPanel import FocusPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.MenuBar import MenuBar
from pyjamas.ui.MenuItem import MenuItem
from pyjamas.ui.Grid import Grid
from pyjamas.ui.DialogBox import DialogBox
from pyjamas.ui.PopupPanel import PopupPanel
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Button import Button
from pyjamas.ui.Label import Label
from pyjamas.ui.HTMLPanel import HTMLPanel
from pyjamas.ui import Event
from pyjamas import Window
from pyjamas import DOM
from pyjamas.Timer import Timer
from __pyjamas__ import doc
from pyjamas.JSONService import JSONProxy

import random

class DataService(JSONProxy):
    def __init__(self):
        super(DataService, self).__init__("/minesweeper/default/call/jsonrpc", \
                                          ["add_score", "get_scores"])

def setColorfulHTML(element, count):
    colors = ['#0000fe', '#007a00', '#fe0000', '#00007a',
              '#7a0000', '#007a7a', '#000000', '#7a7a7a']
    html = '<span class="number" style="color:%s;">%d</span>' % \
                                                        (colors[count-1], count)
    DOM.setInnerHTML(element, html)

class MineMenuBar(MenuBar):
    def __init__(self, game):
        self.game = game
        super(MineMenuBar, self).__init__()
        
        body = doc().getElementsByTagName('body').item(0)
        body.setAttribute('id', 'Beginner')
        
        menu_game = MenuBar(True)
        menu_game.addItem('New', MenuCmd(self, 'New'))
        menu_game.addItem(self.span_text('Beginner'), True, \
                                                MenuCmd(self, 'Beginner'))
        menu_game.addItem(self.span_text('Intermediate'), True, \
                                                MenuCmd(self, 'Intermediate'))
        menu_game.addItem(self.span_text('Expert'), True, \
                                                MenuCmd(self, 'Expert'))
        menu_game.addItem(self.span_text('Custom'), True, \
                                                MenuCmd(self, 'Custom'))
        
        menu_help = MenuBar(True)
        #menu_help.addItem('Instructions', MenuCmd(self, 'Instructions'))
        menu_help.addItem('About', MenuCmd(self, 'About'))
        
        self.addItem(MenuItem('Game', menu_game))
        self.addItem(MenuItem('Help', menu_help))
    
    def span_text(self, text):
        return '<span class="%s"></span>%s' % (text, text)

class MenuCmd:
    def __init__(self, menu, command):
        self.menu = menu
        self.command = command
    
    def execute(self):
        if self.command in ('Beginner', 'Intermediate', 'Expert', 'Custom'):
            body = doc().getElementsByTagName('body').item(0)
            body.setAttribute('id', self.command)
        
        modes = {'New': [(0, 0), 0],
                 'Beginner': [(8, 8), 1],
                 'Intermediate': [(16, 16), 2],
                 'Expert': [(16, 32), 3]}
        level = modes.get(self.command)
        if level:
            if level[1]:
                self.menu.game.level = level[1]
            self.menu.game.next_game(level[0])
        elif self.command == 'Custom':
            self.menu.game.level = 4
            self.show_custom()
        elif self.command == 'Instructions':
            pass
        elif self.command == 'About':
            self.show_about()
    
    def show_custom(self):
        self.dialog = DialogBox(StyleName='custom-dialog')
        self.dialog.setHTML('Custom Settings')
        
        contents = VerticalPanel(StyleName='contents')
        self.dialog.setWidget(contents)
        
        # contents of contents
        rows = HorizontalPanel()
        columns = HorizontalPanel()
        bombs = HorizontalPanel()
        buttons = HorizontalPanel()
        
        for each in (rows, columns, bombs, buttons):
            contents.add(each)
        
        rows.add(Label('Rows:'))
        self.row = TextBox()
        rows.add(self.row)
        
        columns.add(Label('Columns:'))
        self.column = TextBox()
        columns.add(self.column)
        
        bombs.add(Label('Bombs:'))
        self.bomb = TextBox()
        bombs.add(self.bomb)
        
        buttons.add(Button("OK", getattr(self, 'new_game')))
        buttons.add(Button("Cancel", getattr(self, 'close_dialog')))
        
        left = (Window.getClientWidth() - 201) / 2
        top = (Window.getClientHeight() - 190) / 2
        self.dialog.setPopupPosition(left, top)
        
        self.dialog.show()
    
    def new_game(self, event):
        try:
            row = int(self.row.getText())
        except:
            Window.alert('Invalid number in rows')
            return
        try:
            column = int(self.column.getText())
        except:
            Window.alert('Invalid number in columns')
            return
        try:
            bomb = int(self.bomb.getText())
        except:
            bomb = 0
        if bomb >= (row * column):
            Window.alert("Number of bombs should not be greater than " \
                         "rows x columns.")
        else:
            self.menu.game.next_game((row, column), bomb)
            self.close_dialog()
    
    def close_dialog(self, event):
        self.dialog.hide()
    
    def show_about(self):
        self.dialog = PopupPanel(StyleName='about', autoHide=True)
        
        contents = HTMLPanel('', StyleName='contents')
        self.dialog.setWidget(contents)
        
        html = '<p class="pyjamas">MineSweeper written in Python with ' \
                    '<a href="http://pyjs.org" target="_blank">Pyjamas</a><p>' \
               '<p class="comments">Send comments to ' \
                    '<a href="mailto:suzan.shakya@gmail.com">' \
                        'suzan.shakya@gmail.com</a>.<p>'
        contents.setHTML(html)
        
        left = (Window.getClientWidth() - 294) / 2
        top = (Window.getClientHeight() - 112) / 2
        self.dialog.setPopupPosition(left, top)
        self.dialog.show()

class Smiley(FocusPanel):
    def __init__(self, game):
        self.game = game
        super(Smiley, self).__init__(StyleName='facesmile')
        
        self.sinkEvents(Event.ONCONTEXTMENU)
        self.addClickListener(self)
        self.addMouseListener(self)
        self.pressed = False
    
    def onClick(self, sender):
        self.game.restart()
    
    def onMouseDown(self, sender, x, y):
        self.pressed = True
        self.previousStyleName = self.getStyleName()
        self.setStyleName('faceooh')
    
    def onMouseUp(self, sender, x, y):
        if self.pressed:
            self.pressed = False
            self.setStyleName(self.previousStyleName)
    
    def onMouseLeave(self, sender):
        self.onMouseUp(sender, 0, 0)

class RemoteHandler:
    def __init__(self, game):
        self.game = game
        
    def onRemoteResponse(self, response, request_info):
        if request_info.method == 'get_scores':
            self.game.toppers = response
            self.load_top_scores()
    
    def load_top_scores(self):
        html = "<p>These are the top MineSweepers.<p>"
        html += "<table class='scores_table'>"
        html += "<tr><th> %s </th><th> %s </th><th> %s </th></tr>" % \
                ('Beginner', 'Intermediate', 'Expert')
        html += "<tr>"
        for score in self.game.toppers:
            html += "<td><table class='individual_table'>"
            html += "<tr><th class='name'> MineSweepers </th>" \
                    "<th class='time'> Time </th></tr>"
            for player, time in score:
                html += "<tr><td class='name'> %s </td>" \
                        "<td class='time'> %s </td></tr>" % (player, time)
            html += "</table></td>"
        html += "</tr></table>"
        SCORES.setHTML(html)
    
    def onRemoteError(self, code, message, request_info):
        LOG.setHTML(str(message))
        Timer(5000, lambda: LOG.setHTML(''))

class RemainingMineHandler:
    """handler for counter, only active when counter is 000"""
    def __init__(self, game):
        self.game = game
    
    def onClick(self, sender):
        self.game.counter.setStyleName('digit counter')
        
        bomb_explodes_on = [one for one in self.game.bombed_cells \
                                                            if one.state != 1]
        if bomb_explodes_on:
            self.game.show_all_bombs(bomb_explodes_on)
            # the above method will set game.started == False, so set it True
            self.game.started = True
        
        for one in self.game.get_all_cells():
            if not self.game.started:
                break
            elif one.state in (0, 2) and one.count != -1:
                self.game.grid.onClick(one)
        
        self.game.started = False
        if bomb_explodes_on:
            self.game.face.setStyleName('facedead')

class Cell(SimplePanel):
    def __init__(self, x, y, grid):
        super(Cell, self).__init__()
        self.x = x
        self.y = y
        self.grid = grid
        
        self.count = 0  # count of surr bombs. -1 if it contains bomb
        self.state = 0  # 0 = blank, 1 = flagged, 2 = qmarked, 3 = opened
        
        # mock self.element as if it were td associated with this cell.
        # because we won't be creating div inside td.
        self.element = grid.cellFormatter.getElement(x, y)
        self.setStyleName('blank')

class CustomGrid(Grid):
    def __init__(self, game, row, column):
        super(CustomGrid, self).__init__(row, column, StyleName='grid')
        self.sinkEvents(Event.ONCONTEXTMENU)
        self.sinkEvents(Event.ONMOUSEDOWN | Event.ONMOUSEUP | Event.ONMOUSEOUT)
        self.game = game
        
        self.cells = []
        for i in xrange(row):
            self.cells.append([])
            for j in xrange(column):
                self.cells[-1].append(Cell(i, j, self))
    
    def getCell(self, row, column):
        return self.cells[row][column]
    
    def onBrowserEvent(self, event):
        DOM.eventPreventDefault(event)
        if not self.game.started:
            return
        td = self.getEventTargetCell(event)
        if not td:
            return
        tr = DOM.getParent(td)
        table = DOM.getParent(tr)
        row = DOM.getChildIndex(table, tr)
        column = DOM.getChildIndex(tr, td)
        target_cell = self.getCell(row, column)
        
        type = DOM.eventGetType(event)
        event_mapper = {'click': 'onClick',
                        'contextmenu': 'onRightClick',
                        'mousedown': 'onMouseDown',
                        'mouseup': 'onMouseUp',
                        'mouseout': 'onMouseLeave'}
        event_handler = event_mapper.get(type)
        if event_handler:
            getattr(self, event_handler)(target_cell)
    
    def onClick(self, target):
        if target.state == 1:
            return
        if target.state == 3 and target.count:
            self.game.open_if_satisfies(target)
            return
        target.setStyleName('opened')
        target.state = 3
        self.game.count_opened_cells += 1
        
        if self.game.first_click:
            self.game.first_click = False
            self.game.onTimer(target)
            if target.count == -1:
                self.game.move_to_extra_mine(target)
        
        if target.count == -1:
            self.game.show_all_bombs([target])
            return
        elif target.count == 0:
            self.game.open_neighboring_cells(target)
        else:
            setColorfulHTML(target.getElement(), target.count)
        
        self.game.check_win()
    
    def onRightClick(self, target):
        if target.state == 3:
            return
        if self.game.first_click:
            self.game.first_click = False
            self.game.onTimer(target)
        if target.state == 0:
            target.setStyleName('bombflagged')
            target.state = 1
            self.game.flagged_cells.append(target)
        elif target.state == 1:
            target.setStyleName('bombquestion')
            target.state = 2
            self.game.flagged_cells.remove(target)
        elif target.state == 2:
            target.setStyleName('blank')
            target.state = 0
        
        self.game.set_counter()
        self.game.check_win()
    
    def onMouseDown(self, target):
        if target.state == 0:
            target.addStyleName('pressed')
            self.game.to_be_released = [target]
        if target.state == 3 and target.count:
            self.game.press_neighbor_cells(target)
        self.game.face.setStyleName('faceooh')
        self.game.no_of_click += 1
    
    def onMouseUp(self, target):
        for one in self.game.to_be_released:
            one.removeStyleName('pressed')
        self.game.to_be_released = []
        self.game.face.setStyleName('facesmile')
    
    def onMouseLeave(self, target):
        self.onMouseUp(target)

class Game(VerticalPanel):
    def __init__(self, row, column=0):
        super(Game, self).__init__(StyleName='game')
        self.sinkEvents(Event.ONCONTEXTMENU)  # to disable right click
        
        self.row = row
        self.column = column or row
        self.level = 1
        self.toppers = [[], [], []]  # storage for top scorers for 3 levels.
        self.remote = DataService()
        self.remote_handler = RemoteHandler(self)
        self.remote.get_scores(self.remote_handler)
        
        # contents of Game
        menubar = MineMenuBar(self)
        score_board = HorizontalPanel(StyleName='score-board')
        self.grid_panel = SimplePanel(StyleName='grid-panel')
        
        self.add(menubar)
        self.add(score_board)
        self.add(self.grid_panel)
        
        # contents of score_board
        self.counter = Label('000', StyleName='digit counter')
        self.face = Smiley(self)
        self.timer = Label('000', StyleName='digit timer')
        
        for one in (self.counter, self.face, self.timer):
            score_board.add(one)
        score_board.setCellWidth(self.face, '100%')
        
        self.create_grid()
        self.start()
    
    def onBrowserEvent(self, event):
        # prevent right click context menu as well as all the other events.
        DOM.eventPreventDefault(event)
    
    def create_grid(self):
        # contents of self.grid_panel
        self.grid = CustomGrid(self, self.row, self.column)
        self.grid_panel.add(self.grid)
    
    def start(self, no_of_bomb=0):
        self.time = -1
        self.started = True
        self.first_click = True
        
        self.bombed_cells = []
        self.flagged_cells = []
        self.to_be_released = []  # cells to be released after being pressed
        self.count_opened_cells = 0
        self.no_of_click = 0
        
        self.squares = self.row * self.column
        self.no_of_bomb = no_of_bomb or int((self.squares * 10) / 64)
        self.no_of_safe_zones = self.squares - self.no_of_bomb
        
        self.set_counter()
        self.timer.setText('000')
        
        self.generate_bombs()
        self.face.setStyleName('facesmile')
    
    def get_all_cells(self):
        for i in xrange(self.row):
            for j in xrange(self.column):
                one = self.grid.getCell(i, j)
                yield one
    
    def get_neighbors(self, cell):
        x = cell.x
        y = cell.y
        row, column = self.row, self.column
        for i in xrange(x-1, x+2):
            if 0 <= i < row:
                for j in xrange(y-1, y+2):
                    if 0 <= j < column:
                        if (i,j) != (x, y):
                            one = self.grid.getCell(i, j)
                            yield one
    
    def set_counter(self):
        next_value = self.no_of_bomb - len(self.flagged_cells)
        
        if next_value == 0 and self.started:
            self.counter.setStyleName('digit counter-blue')
            self.counter.addClickListener(RemainingMineHandler(self))
        else:
            self.counter.setStyleName('digit counter')
            self.counter._clickListeners = []
        
        if next_value < 0:
            template = '-00'
            next_value = abs(next_value)
        else:
            template = '000'
        value = str(next_value)
        value = template[:-len(value)] + value
        self.counter.setText(value)
    
    def onTimer(self, target):
        if not self.started or self.first_click:
            return
        Timer(1000, self)
        self.time += 1
        if self.time <= 999:
            str_time = str(self.time)
            str_time = '000'[:-len(str_time)] + str_time
            self.timer.setText(str_time)
        else:
            self.started = False
            self.face.setStyleName('faceclock')
    
    def sample(self, population, k):
        # pyjamas doesn't support random.sample but random.choice
        seq = list(population)
        s = []
        for i in xrange(k):
            pick = random.choice(seq)
            seq.remove(pick)
            s.append(pick)
        return s
    
    def generate_bombs(self):
        # generate 1 extra mine so that if user's first click is bomb, move that
        bombs = self.sample(xrange(self.squares), self.no_of_bomb+1)
        row, column = self.row, self.column
        for i,bomb in enumerate(bombs):
            x = bomb // column
            y = bomb % column
            mine = self.grid.getCell(x, y)
            if i == 0:
                self.extra_mine = mine
                continue
            #DOM.setInnerHTML(mine.getElement(),'b');mine.addStyleName('debug')
            self.bombed_cells.append(mine)
            mine.count = -1
            for one in self.get_neighbors(mine):
                if one.count != -1:
                    one.count += 1
    
    def move_to_extra_mine(self, to_be_moved):
        to_be_moved.count = 0
        self.bombed_cells.remove(to_be_moved)
        for one in self.get_neighbors(to_be_moved):
            if one.count == -1:
                to_be_moved.count += 1
            else:
                one.count -= 1
        
        self.extra_mine.count = -1
        self.bombed_cells.append(self.extra_mine)
        for one in self.get_neighbors(self.extra_mine):
            if one.count != -1:
                one.count += 1
    
    def press_neighbor_cells(self, cell):
        self.count_flags = 0
        self.bomb_explodes_on = []
        self.to_be_released = []
        for one in self.get_neighbors(cell):
            if one.state == 3:
                continue
            one.addStyleName('pressed')
            self.to_be_released.append(one)
            if one.state == 1:
                self.count_flags += 1
            else:
                if one.count == -1:
                    self.bomb_explodes_on.append(one)
    
    def open_if_satisfies(self, cell):
        if self.count_flags == cell.count:
            if self.bomb_explodes_on:
                self.show_all_bombs(self.bomb_explodes_on)
            else:
                self.open_neighboring_cells(cell)
    
    def open_neighboring_cells(self, cell):
        if not self.started:
            return
        for one in self.get_neighbors(cell):
            if one.state in (0, 2) and one.count != -1:
                one.setStyleName('opened')
                one.state = 3
                self.count_opened_cells += 1
                if one.count == 0:
                    self.open_neighboring_cells(one)
                else:
                    setColorfulHTML(one.getElement(), one.count)
        self.check_win()
    
    def check_win(self):
        if not self.started:
            return
        if self.count_opened_cells == self.no_of_safe_zones:
            for one in self.bombed_cells:
                if one.state != 1:
                    one.setStyleName('cell bombflagged')
                    self.flagged_cells.append(one)
            self.started = False
            self.set_counter()
            self.face.setStyleName('facewin')
            name = Window.prompt("You've done it !\n\
                                Game Time: %s seconds\n\
                                Number of Clicks: %s\n"
                                "What's ur name ?" % (self.time, self.no_of_click))
            if name and self.level in (1, 2, 3):
                self.remote.add_score(name, self.level, self.time, \
                                      self.no_of_click, self.remote_handler)
                self.add_player_to_toppers(name)
    
    def add_player_to_toppers(self, name):
        current_level = self.level - 1
        toppers_in_this_level = self.toppers[current_level]
        toppers_in_this_level.append(('<b>%s</b>' % name, self.time))
        self.toppers[current_level] = sorted(toppers_in_this_level, \
                                             key=lambda score: score[1])
        self.remote_handler.load_top_scores()
        
    def show_all_bombs(self, bomb_explodes_on=[]):
        self.started = False
        self.face.setStyleName('facedead')
        
        for one in self.bombed_cells:
            if one.state != 1:
                one.setStyleName('cell bombrevealed')
        for one in self.flagged_cells:
            if one.count != -1:
                one.setStyleName('cell bombmisflagged')
        
        for one in bomb_explodes_on:
            one.setStyleName('cell bombdeath')
    
    def next_game(self, level=None, no_of_bomb=0):
        current_level = (self.row, self.column)
        if not level or level == (0,0) or level == current_level:
            self.restart(no_of_bomb)
        else:
            self.row, self.column = level
            if level[0] <= current_level[0] and level[1] <= current_level[1]:
                self.grid.resize(*level)
                self.restart(no_of_bomb)
            else:
                self.grid_panel.remove(self.grid)
                self.create_grid()
                self.start(no_of_bomb)
    
    def restart(self, no_of_bomb=0):
        for one in self.get_all_cells():
            one.count = 0
            one.state = 0
            one.setStyleName('blank')
            DOM.setInnerHTML(one.getElement(), '')
        self.start(no_of_bomb)

if __name__ == '__main__':
    pyjd.setup("./public/minesweeper.html")
    LOG = HTMLPanel('', StyleName='log')
    SCORES = HTMLPanel('', StyleName='scores')
    game = Game(8, 8)
    
    RootPanel('content').add(game)
    RootPanel('content').add(SCORES)
    RootPanel('content').add(LOG)

    pyjd.run()
