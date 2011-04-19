from pyjamas.gears import Factory
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas.ui.Grid import Grid
from pyjamas.ui.TextBox import TextBox
from pyjamas.ui.Button import Button
from pyjamas.Window import alert
from time import time

class DbTest():

    def __init__(self):

        self.tb = TextBox()
        self.b = Button("add")
        self.g = Grid()
        self.g.resize(4, 2)

        RootPanel().add(HTML("Add Phrase.  Press Button."))
        RootPanel().add(self.tb)
        RootPanel().add(self.b)
        RootPanel().add(self.g)
        self.b.addClickListener(self)

        try:
            self.db = Factory.createDatabase()
            self.db.open('database-demo')
            self.db.execute('create table if not exists Demo' +
                       ' (Phrase varchar(255), Timestamp int)')
        except:
            alert("Could not create database.\nDo you have the google gears extension installed?")

    def onClick(self, sender):
        phrase = self.tb.getText()
        currTime = time()
        self.db.execute('insert into Demo values (?, ?)', phrase, currTime);

        rs = self.db.execute('select * from Demo order by Timestamp desc');
        index = 0
        while rs.isValidRow():
            if index <4:
                self.g.setHTML(index, 0, rs.field(0))
                self.g.setHTML(index, 1, rs.field(1))
            else:
                self.db.execute('delete from Demo where Timestamp=?', rs.field(1));
            index += 1

            rs.next()
        rs.close()
            
if __name__ == '__main__':
    app = DbTest()

