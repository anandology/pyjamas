from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Label import Label

from UnitTest import UnitTest

from __pyjamas__ import doc

class LabelTest(UnitTest):

    def testLabelAdd(self):
        self.l = Label("Hello World (label)", StyleName='teststyle')
        RootPanel('tests').add(self.l)
        self.write_test_output('addlabel')

        if not RootPanel('tests').remove(self.l):
            self.fail("Label added but apparently not owned by RootPanel()")
        self.write_test_output('removelabel')

