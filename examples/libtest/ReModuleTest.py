# Testing time module

import sys
import UnitTest
import re

#from __pyjamas__ import debugger

class ReModuleTest(UnitTest.UnitTest):

    def matchTest(self, msg, pat, flags, string, groups, span):
        r = re.compile(pat, flags)
        m = r.match(string)
        if groups is None:
            self.assertTrue(m is None, "%s: None expected" % msg)
            return
        self.assertTrue(m is not None, "%s: Unexpected None" % msg)
        self.assertTrue(len(m.groups()) == len(groups)-1, "%s: len(m.groups()) = %s != %s" % (msg, len(m.groups()), len(groups)-1))
        for i in range(len(groups)):
            self.assertEqual(m.group(i), groups[i], "%s: m.group(%d) = '%s' != groups[%d] = '%s'" % (msg, i, m.group(i), i, groups[i]))
        self.assertEqual(m.start(), span[0], "%s: start = %d != %d" % (msg, m.start(), span[0]))
        self.assertEqual(m.end(), span[1], "%s: end = %d != %d" % (msg, m.end(), span[1]))
        self.assertTrue(m.span() == span, "%s: span = %r != %r" % (msg, m.span(), span[1]))

    def searchTest(self, msg, pat, flags, string, groups, span):
        r = re.compile(pat, flags)
        m = r.search(string)
        if groups is None:
            self.assertTrue(m is None, "%s: None expected" % msg)
            return
        self.assertTrue(m is not None, "%s: Unexpected None" % msg)
        self.assertTrue(len(m.groups()) == len(groups)-1, "%s: len(m.groups()) = %s != %s" % (msg, len(m.groups()), len(groups)-1))
        for i in range(len(groups)):
            self.assertEqual(m.group(i), groups[i], "%s: m.group(%d) = '%s' != groups[%d] = '%s'" % (msg, i, m.group(i), i, groups[i]))
        self.assertEqual(m.start(), span[0], "%s: start = %d != %d" % (msg, m.start(), span[0]))
        self.assertEqual(m.end(), span[1], "%s: end = %d != %d" % (msg, m.end(), span[1]))
        self.assertTrue(m.span() == span, "%s: span = %r != %r" % (msg, m.span(), span[1]))


    def testMatchBasics(self):
        self.matchTest('test 1', 'Ab.cd', 0, 'AbXcd', ['AbXcd'], (0,5))
        self.matchTest('test 2', 'Ab.cd', 0, 'abXcd', None, (0,5))
        self.matchTest('test 3a', 'Ab.cd', re.I, 'abXcd', ['abXcd'], (0,5))
        self.matchTest('test 3b', '(?i)Ab.cd', 0, 'abXcd', ['abXcd'], (0,5))
        self.matchTest('test 4', 'Ab.cd', 0, 'ab\ncd', None, (0,5))
        self.matchTest('test 5a', 'Ab.cd', re.S, 'Ab\ncd', ['Ab\ncd'], (0,5))
        self.matchTest('test 5b', '(?s)Ab.cd', 0, 'Ab\ncd', ['Ab\ncd'], (0,5))
        # bug #288: even re.compile on these two tests puts webkit/chrome into
        # an infinite CPU loop.
        self.matchTest('test 6a', 'A(b).(c)d', re.I | re.S, 'ab\ncd', ['ab\ncd', 'b', 'c'], (0,5))
        self.matchTest('test 6b', '(?is)A(b).(c)d', 0, 'ab\ncd', ['ab\ncd', 'b', 'c'], (0,5))

        m = re.match("1..4", "1234")
        self.assertFalse(m is None, """re.match("1..4", "1234")""")
 
    def testSearchBasics(self):
        self.searchTest('test 1', 'Ab.cd', 0, 'AbXcd', ['AbXcd'], (0,5))
        self.searchTest('test 2', 'Ab.cd', 0, 'abXcd', None, (0,5))
        self.searchTest('test 3a', 'Ab.cd', re.I, 'abXcd', ['abXcd'], (0,5))
        self.searchTest('test 3b', '(?i)Ab.cd', 0, 'abXcd', ['abXcd'], (0,5))
        self.searchTest('test 4', 'Ab.cd', 0, 'ab\ncd', None, (0,5))
        self.searchTest('test 5a', 'Ab.cd', re.S, 'Ab\ncd', ['Ab\ncd'], (0,5))
        self.searchTest('test 5b', 'Ab.cd(?s)', 0, 'Ab\ncd', ['Ab\ncd'], (0,5))
        self.searchTest('test 6a', 'A(b).(c)d', re.I | re.S, 'ab\ncd', ['ab\ncd', 'b', 'c'], (0,5))
        self.searchTest('test 6b', 'A(b)(?is).(c)d', 0, 'ab\ncd', ['ab\ncd', 'b', 'c'], (0,5))
        self.searchTest('test 7', 'Ab.cd', 0, 'AAAbXcd', ['AbXcd'], (2,7))
        self.searchTest('test 8', ' ', 0, 'Spaces in a sentence', [' '], (6,7))

        m = re.search("ab", "dab abba a b")
        self.assertFalse(m is None, """re.search("ab", "dab abba a b")""")

    # bug #258 - this is throwing a javascript syntax error in FF2
    def testFindallBasics(self):
        e = re.compile("e").findall("Where are all these eees")
        self.assertEqual(len(e), 8)

    def testSubBasics(self):
        matches = []
        def fn(m):
            matches.append(m)
            return "%s" % len(matches)
        r = re.compile('e')
        s = "Where are all these eees"
        self.assertEqual(r.sub("Q", s), "WhQrQ arQ all thQsQ QQQs")
        self.assertEqual(r.sub(fn, s), "Wh1r2 ar3 all th4s5 678s")
        self.assertEqual(r.sub("Q", s, 4), "WhQrQ arQ all thQse eees")
        matches = []
        self.assertEqual(r.sub(fn, s, 5), "Wh1r2 ar3 all th4s5 eees")

        self.assertEqual(r.subn("Q", s), ("WhQrQ arQ all thQsQ QQQs", 8))


    def testSplitBasics(self):
        r = re.compile('e')
        s = "Where are all these eees"

        self.assertEqual(r.split(s), ['Wh', 'r', ' ar', ' all th', 's', ' ', '', '', 's'])


    def testMatchExtended(self):
        r = re.compile("ed")
        m = r.match("ed ed", 0)
        self.assertEqual(m.group(0), "ed")

        m = r.match("ed ed", 1)
        self.assertTrue(m is None, """match("ed ed", 1)""")

        m = r.match("ed ed", 3)
        self.assertEqual(m.group(0), "ed")

        r = re.compile("^a.*$", re.M)
        m = r.match("a  ")
        self.assertEqual(m.group(0), "a  ")

        m = r.match("a1\na2")
        self.assertEqual(m.group(0), "a1")

        m = r.match("a1\na2", 2)
        self.assertTrue(m is None, """match("a1\na2", 2)""")

        m = r.match("a1\na2", 3)
        self.assertEqual(m.group(0), "a2")

        m = r.match("a1\na2", 3, 4)
        self.assertEqual(m.group(0), "a")

        r = re.compile("([+])?(\d{1,})?")
        m = r.match("1")
        g = m.groups("")
        self.assertEqual(g, ("", "1"))

    def testBackReferences(self):
        B_re = re.compile(r'\*\*(.*?)\*\*', re.DOTALL)
        EM_re = re.compile(r'\*(.*?)\*', re.DOTALL)
        s = '''Text between *single asterisks* is emphasized.<br>Text between **double asterisks** is bolded.<br>You **can *even* embed** them!'''
        expected = '''Text between <EM>single asterisks</EM> is emphasized.<br>Text between <STRONG>double asterisks</STRONG> is bolded.<br>You <STRONG>can <EM>even</EM> embed</STRONG> them!'''

        s = B_re.sub(r'<STRONG>\1</STRONG>', s)
        s = EM_re.sub(r'<EM>\1</EM>', s)
        self.assertEqual(s, expected, 'Bug #495')
