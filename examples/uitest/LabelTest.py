from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label

from UnitTest import UnitTest

from __pyjamas__ import doc

class LabelTest(UnitTest):

    def testLabelAdd(self):
        self.l = Label("Hello World (label)", StyleName='teststyle')
        RootPanel().add(self.l)
        ht = doc().body.innerHTML
        self.write_test_output(ht, 'addlabel')

        if not RootPanel().remove(self.l):
            self.fail("Label added but apparently not owned by RootPanel()")
        ht = doc().body.innerHTML
        self.write_test_output(ht, 'removelabel')

