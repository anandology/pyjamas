# Testing md5 module

import sys
import UnitTest

# XXX unfortunately this doesn't work when compiled via build.sh
# because hashlib doesn't exist as a JavaScript support module
# try:
#     from hashlib import md5
# except ImportError:
#     from md5 import md5
from md5 import md5

if sys.platform in ['mozilla', 'ie6', 'opera', 'oldmoz',
                    'safari', 'spidermonkey', 'pyv8']:
    from __pyjamas__ import JS

    def hexstr(s):
        h = '0123456789abcdef'
        r = ''
        i = None
        for x in range(16):
            JS("i = s[x];")
            r = r + h[(i >> 4) & 0xF] + h[i & 0xF]
        return r

else:

    def hexstr(s):
        h = '0123456789abcdef'
        r = ''
        for c in s:
            i = ord(c)
            r = r + h[(i >> 4) & 0xF] + h[i & 0xF]
        return r


class MD5Test(UnitTest.UnitTest):

    def md5test(self, s, expected):
        self.assertEqual(hexstr(md5(s).digest()), expected)
        self.assertEqual(md5(s).hexdigest(), expected)

    def test_basics(self):
        self.md5test('', 'd41d8cd98f00b204e9800998ecf8427e')
        self.md5test('a', '0cc175b9c0f1b6a831c399e269772661')
        self.md5test('abc', '900150983cd24fb0d6963f7d28e17f72')
        self.md5test('message digest', 'f96b697d7cb7938d525a2f31aaf161d0')
        self.md5test('abcdefghijklmnopqrstuvwxyz', 'c3fcd3d76192e4007dfb496cca67e13b')
        self.md5test('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789',
           'd174ab98d277d9f5a5611c2c9f419d9f')
        self.md5test('12345678901234567890123456789012345678901234567890123456789012345678901234567890',
           '57edf4a22be3c955ac49da2e2107b67a')

    def test_hexdigest(self):
        m = md5('testing the hexdigest method')
        h = m.hexdigest()
        self.assertEqual(hexstr(m.digest()), h)

    def test_large_update(self):
        #aas = 'a' * 64
        #bees = 'b' * 64
        #cees = 'c' * 64

        aas = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
        bs = 'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb'
        cs = 'cccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc'

        m1 = md5()
        m1.update(aas)
        m1.update(bs)
        m1.update(cs)

        m2 = md5()
        m2.update(aas + bs + cs)
        self.assertEqual(hexstr(m1.digest()), hexstr(m2.digest()))

