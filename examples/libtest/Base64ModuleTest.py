# Testing time module

import sys
import UnitTest
import base64


class Base64ModuleTest(UnitTest.UnitTest):

    def testBase64(self):
        text = "Pyjamas is fun"

        encodetext = base64.encodestring(text)
        self.assertEqual(encodetext, 'UHlqYW1hcyBpcyBmdW4=\n')
        decodetext = base64.decodestring(encodetext)
        self.assertEqual(decodetext, text)

        encodetext = base64.b64encode(text)
        self.assertEqual(encodetext, 'UHlqYW1hcyBpcyBmdW4=')
        decodetext = base64.b64decode(encodetext)
        self.assertEqual(decodetext, text)

        encodetext = base64.standard_b64encode(text)
        self.assertEqual(encodetext, 'UHlqYW1hcyBpcyBmdW4=')
        decodetext = base64.standard_b64decode(encodetext)
        self.assertEqual(decodetext, text)

        encodetext = base64.urlsafe_b64encode(text)
        self.assertEqual(encodetext, 'UHlqYW1hcyBpcyBmdW4=')
        decodetext = base64.urlsafe_b64decode(encodetext)
        self.assertEqual(decodetext, text)

    def testBase32(self):
        text = "Pyjamas is fun"
        
        encodetext = base64.b32encode(text)
        self.assertEqual(encodetext, 'KB4WUYLNMFZSA2LTEBTHK3Q=')
        decodetext = base64.b32decode(encodetext)
        self.assertEqual(decodetext, text)

    def testBase16(self):
        text = "Pyjamas is fun"
        
        encodetext = base64.b16encode(text)
        self.assertEqual(encodetext, '50796A616D61732069732066756E')
        decodetext = base64.b16decode(encodetext)
        self.assertEqual(decodetext, text)


