import UnitTest
from StringIO import StringIO
import sys

class StringIOModuleTest(UnitTest.UnitTest):
    def test_write(self):
        data = StringIO()
        data.write('hi')
        self.assertEqual(data.getvalue(), 'hi')

    def test_print(self):
        orig_stdout = sys.stdout
        try:
            sys.stdout = StringIO()
            print 'hi'
            self.assertEqual(sys.stdout.getvalue(), 'hi\n')
        finally:
            sys.stdout = orig_stdout
