# Copyright (C) 2010 Jim Washington
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

class UnicodeCodecError(Exception):
    pass

def encode(unicode_string):
    """
    Unicode encoder: Given an arbitrary unicode string, returns a string
    of characters with code points in range 0x00 - 0xFF corresponding to
    the bytes of the utf-8 representation of those characters.
    """
    return unicode_string.encode('utf8')

def decode(bytes):
    """
    Unicode decoder: Given a string of characters with code points in
    range 0x00 - 0xFF, which, when interpreted as bytes, are valid UTF-8,
    returns the corresponding Unicode string, along with the number of
    bytes in the input string which were successfully parsed.

    Unlike most JavaScript utf-8 encode/decode implementations, properly
    deals with partial multi-byte characters at the end of the byte string.
    """

    return bytes.decode('utf8')
