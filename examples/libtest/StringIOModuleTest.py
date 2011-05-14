import UnitTest
from StringIO import StringIO
import sys

class StringIOModuleTest(UnitTest.UnitTest):
    def test_write(self):
        data = StringIO()
        data.write('straight')
        self.assertEqual(data.getvalue(), 'straight')

    def test_print(self):
        orig_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            print 'stdout'
            self.assertEqual(sys.stdout.getvalue(), 'stdout\n')
        finally:
            sys.stdout = orig_stdout
