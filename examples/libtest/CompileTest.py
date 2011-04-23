"""
This module does no actual work. It simply consists of some tests which may
cause compile to fail. When you find a new compiler bug, first add the test
here, in commented-out form and add self.fail() with issue number.
When you've patched the bug, remove the comments.
"""

import UnitTest
class CompileTest(UnitTest.UnitTest):
    def test_issue_432(self):
        #issue 432
        x, y = 1, 2
        del x, y
     
    def test_issue_433(self):
        #issue 433
        for x in [1, 2] + [3, 4]:
            pass

    def test_slice_span(self):
        """
        self.assertEqual([1,2,3,4][::2], [1,3])
        """
        self.fail("Slice span, #364, #434, #577, #582")


    def test_discard_expressions(self):
        """
        (1, 2)
        x = 10
        x
        "some string"
        """
        self.fail("ast.Discard nodes, #584")
        
    def test_callfunc_expressions(self):
        """
        s = "123"
        x = ('a' + 'b').strip()
        ("    " + s).rstrip()
        """
        self.fail("Callfunc over expressions, #591")
    
    def test_deep_tuple_unpacking(self):
        """
        x = ((1, 2), 3, (4, 5))
        (a, b), c, (d, e) = x
        """
        self.fail("Bug #527 Tuple unpacking not supported for more than one level")

    def test_subscript_tuple(self):
        """
        d = {}
        d[(1,2)] = 3
        x = d[1,2]
        """
        self.fail("Tuple subscripts issue #496")

    def test_bad_import(self):
        try: import _nonexistentmodule
        except: pass

        try: import _importtimeerror
        except: pass
        
        """
        try: import _badsyntaxmodule
        except: pass
        """
        self.fail("try: import badcode/except does not catch SyntaxError, #592")

        """
        try: import _untranslatablemodule
        except: pass
        """
        self.fail("try: import badcode/except does not catch TranslationError, #592")
            
