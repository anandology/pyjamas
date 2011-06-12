from UnitTest import UnitTest
import RunTests
import os
import sys

sys.path[0:0] = [os.path.dirname(os.path.dirname(os.path.abspath(__file__)))]

import pyjspath
from pyjspath import realpath, abspath, dirname, basename

class PyjsPathTest(UnitTest):
    def test_commonprefix(self):
        commonprefix = pyjspath.commonprefix
        self.assertEqual(
            commonprefix([]),
            ""
        )
        self.assertEqual(
            commonprefix(["/home/swenson/spam", "/home/swen/spam"]),
            "/home/swen"
        )
        self.assertEqual(
            commonprefix(["/home/swen/spam", "/home/swen/eggs"]),
            "/home/swen/"
        )
        self.assertEqual(
            commonprefix(["/home/swen/spam", "/home/swen/spam"]),
            "/home/swen/spam"
        )
        self.assertEqual(
            commonprefix(["home:swenson:spam", "home:swen:spam"]),
            "home:swen"
        )

    def test_join(self):
        self.assertEqual(pyjspath.join("/foo", "bar", "/bar", "baz"), "/bar/baz")
        self.assertEqual(pyjspath.join("/foo", "bar", "baz"), "/foo/bar/baz")
        self.assertEqual(pyjspath.join("/foo/", "bar/", "baz/"), "/foo/bar/baz/")

    def test_split(self):
        self.assertEqual(pyjspath.split("/foo/bar"), ("/foo", "bar"))
        self.assertEqual(pyjspath.split("/"), ("/", ""))
        self.assertEqual(pyjspath.split("foo"), ("", "foo"))
        self.assertEqual(pyjspath.split("////foo"), ("////", "foo"))
        self.assertEqual(pyjspath.split("//foo//bar"), ("//foo", "bar"))

    def splitextTest(self, path, filename, ext):
        self.assertEqual(pyjspath.splitext(path), (filename, ext))
        self.assertEqual(pyjspath.splitext("/" + path), ("/" + filename, ext))
        self.assertEqual(pyjspath.splitext("abc/" + path), ("abc/" + filename, ext))
        self.assertEqual(pyjspath.splitext("abc.def/" + path), ("abc.def/" + filename, ext))
        self.assertEqual(pyjspath.splitext("/abc.def/" + path), ("/abc.def/" + filename, ext))
        self.assertEqual(pyjspath.splitext(path + "/"), (filename + ext + "/", ""))

    def test_splitext(self):
        self.splitextTest("foo.bar", "foo", ".bar")
        self.splitextTest("foo.boo.bar", "foo.boo", ".bar")
        self.splitextTest("foo.boo.biff.bar", "foo.boo.biff", ".bar")
        self.splitextTest(".csh.rc", ".csh", ".rc")
        self.splitextTest("nodots", "nodots", "")
        self.splitextTest(".cshrc", ".cshrc", "")
        self.splitextTest("...manydots", "...manydots", "")
        self.splitextTest("...manydots.ext", "...manydots", ".ext")
        self.splitextTest(".", ".", "")
        self.splitextTest("..", "..", "")
        self.splitextTest("........", "........", "")
        self.splitextTest("", "", "")

    def test_isabs(self):
        self.assertEqual(pyjspath.isabs(""), False)
        self.assertEqual(pyjspath.isabs("/"), True)
        self.assertEqual(pyjspath.isabs("/foo"), True)
        self.assertEqual(pyjspath.isabs("/foo/bar"), True)
        self.assertEqual(pyjspath.isabs("foo/bar"), False)

    def test_basename(self):
        self.assertEqual(pyjspath.basename("/foo/bar"), "bar")
        self.assertEqual(pyjspath.basename("/"), "")
        self.assertEqual(pyjspath.basename("foo"), "foo")
        self.assertEqual(pyjspath.basename("////foo"), "foo")
        self.assertEqual(pyjspath.basename("//foo//bar"), "bar")

    def test_dirname(self):
        self.assertEqual(pyjspath.dirname("/foo/bar"), "/foo")
        self.assertEqual(pyjspath.dirname("/"), "/")
        self.assertEqual(pyjspath.dirname("foo"), "")
        self.assertEqual(pyjspath.dirname("////foo"), "////")
        self.assertEqual(pyjspath.dirname("//foo//bar"), "//foo")

    def test_normpath(self):
        self.assertEqual(pyjspath.normpath(""), ".")
        self.assertEqual(pyjspath.normpath("/"), "/")
        self.assertEqual(pyjspath.normpath("//"), "//")
        self.assertEqual(pyjspath.normpath("///"), "/")
        self.assertEqual(pyjspath.normpath("///foo/.//bar//"), "/foo/bar")
        self.assertEqual(pyjspath.normpath("///foo/.//bar//.//..//.//baz"), "/foo/baz")
        self.assertEqual(pyjspath.normpath("///..//./foo/.//bar"), "/foo/bar")

def test_main():
    t = RunTests.RunTests()
    t.add(PyjsPathTest)
    t.start_test()

if __name__=="__main__":
    test_main()
