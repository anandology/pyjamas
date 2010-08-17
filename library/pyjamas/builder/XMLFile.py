#
# Copyright 2010 ZX www.zx.nl
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
#

import re

class XMLFileError(RuntimeError):
    pass

class XMLFile(object):
    re_xml = re.compile('''<[?]xml([^?]*)[?]>''')
    re_comment = re.compile('''<!--(-*)''')
    re_tag = re.compile('''<\s*([^/]\S*)(.*)>''')
    re_tag_close = re.compile('''</\s*(\S+)\s*>''')
    #re_attr = re.compile('''(\S+)="([^"]*)"''') # Bug in pyjamas re module
    re_attr = re.compile('''\S+="[^"]*"''')

    def __init__(self, lines):
        if isinstance(lines, str):
            lines = lines.split("\n")
        self.lines = lines
        self.lineno = 0
        self.xmlAttrs = None

    def error(self, msg):
        raise XMLFileError("Line %s: %s" % (self.lineno, msg))

    def parseValue(self, v, unpackStr=False):
        vlower =  v.lower()
        if vlower in ["null", "none"]:
            return None
        if vlower == "true":
            return True
        if vlower == "false":
            return False
        try:
            v = int(v)
            return v
        except:
            pass
        try:
            v = float(v)
            return v
        except:
            pass
        if len(v) > 1:
            if v[0] == v[-1]:
                if unpackStr and v[0] in ["'", '"']:
                    return v[1:-1]
            elif v[0] == '(' and v[-1] == ')':
                values = []
                try:
                    for value in v[1:-1].split(','):
                        value = self.parseValue(value.strip(), True)
                        values.append(value)
                    return tuple(values)
                except:
                    pass
            if len(v) > 2:
                if v[:2] == "u'" and v[-1] == "'":
                    return v[2:-1]
                if v[:2] == 'u"' and v[-1] == '"':
                    return v[2:-1]
        return v

    def getAttrs(self, line):
        attrs = {}
        #for k, v in self.re_attr.findall(line):
        #    attrs[k] = self.parseValue(v)
        for kv in self.re_attr.findall(line):
            k, v = kv.split("=", 1)
            k = k.strip()
            v = v.replace("%22;", '"')
            v = v.replace("%0A;", "\n")
            v = v.strip()[1:-1]
            attrs[k] = self.parseValue(v)
        return attrs

    def getTag(self, line, requiredTags=None):
        mTag = self.re_tag.match(line)
        if ( not mTag 
             or ( requiredTags is not None 
                 and mTag.group(1) not in requiredTags
                )
           ):
            if requiredTags is not None:
                self.error("Expected tag %s" % ",".join(requiredTags))
            else:
                self.error("Expected a tag")
        tagName = mTag.group(1)
        tagAttrs = mTag.group(2)
        if tagAttrs and tagAttrs[-1] == "/":
            tagAttrs = tagAttrs[:-1]
            tagClose = True
        else:
            tagClose = False
        return (tagName, tagClose, self.getAttrs(tagAttrs))

    def getTagClose(self, line, tag=None):
        mTag = self.re_tag_close.match(line)
        if not mTag or (tag is not None and mTag.group(1) != tag):
            if tag is not None:
                self.error("Expected closing tag '%s'" % tag)
            else:
                self.error("Expected a closing tag")
        return (
            mTag.group(1),
        )

    def currentLine(self):
        if self.lineno > len(self.lines):
            return None
        line = self.lines[self.lineno].strip()
        startlineno = self.lineno
        mComment = self.re_comment.search(line)
        while mComment:
            start = '<!--%s' % mComment.group(1)
            end = '%s-->' % mComment.group(1)
            left = line.find(start) + len(start)
            right = line.find(end, left)
            if right >= left:
                right += len(end)
                line = line[:left - len(start)] + line[right + len(end):]
                mComment = self.re_comment.search(line)
            elif self.lineno == len(self.lines):
                self.error(
                    "Unterminated comment starting at line %s" % startlineno,
                )
            else:
                self.lineno += 1
                line = line[:left] + self.lines[self.lineno].strip()
        return line

    def nextLine(self):
        if self.lineno > len(self.lines):
            return None
        line = self.currentLine()
        self.lineno += 1
        return line

    def isTagClose(self, tagName):
        line = self.currentLine()
        mTag = self.re_tag_close.match(line)
        if mTag and mTag.group(1) == tagName:
            return True
        return False

    def nextTag(self, requiredTags):
        line = self.nextLine()
        tag = self.getTag(line, requiredTags)
        if self.isTagClose(tag[0]):
            line = self.nextLine()
            tag = (tag[0], True) + tag[2:]
        tagFunc = "tag_%s" % tag[0]
        if hasattr(self, tagFunc):
            return getattr(self, tagFunc)(tag)
        self.error("Unknown tag '%s'" % tag[0])

    def parse(self):
        line = self.currentLine()
        mXML = self.re_xml.match(line)
        if mXML:
            xmlAttrs = mXML.group(1)
            self.xmlAttrs = self.getAttrs(xmlAttrs)
            line = self.nextLine()
        rootTag = None
        properties = self.nextTag(["pyjsglade", "properties", "components"])
        if properties[0] == 'pyjsglade':
            rootTag = properties[0]
            properties = self.nextTag(["properties", "components"])
        if properties[0] == 'properties':
            properties = properties[2]
            components = self.nextTag(["components"])[1]
        else:
             components = properties[1]
             properties = {}
        if rootTag is not None:
            line = self.nextLine()
            self.getTagClose(line, rootTag)
        return properties, components

    def tag_pyjsglade(self, tag):
        return tag

    def tag_components(self, tag):
        tags = []
        tagName, tagClosed, tagAttrs = tag
        if not tagClosed:
            while not self.isTagClose(tagName):
                tags.append(self.nextTag(["component"]))
            line = self.nextLine()
            self.getTagClose(line, tagName)
        components = []
        for tag in tags:
            components.append((tag[1]["index"], tag[1:]))
            components.sort()
        return tagName, [c[1] for c in components]

    def tag_component(self, tag):
        tags = []
        tagName, tagClosed, tagAttrs = tag
        if not tagClosed:
            while not self.isTagClose(tagName):
                tags.append(self.nextTag(["properties", "components"]))
            line = self.nextLine()
            self.getTagClose(line, tagName)
        props = {}
        childs = []
        for tag in tags:
            if tag[0] == 'properties':
                name = tag[1]["name"]
                if not name in props:
                    props[name] = {}
                props[name].update(tag[2])
            elif tag[0] == 'components':
                childs += tag[1]
            else:
                assert("Unknown tag found: %s" % repr(tag[0]))
        return tagName, tagAttrs, props, childs

    def tag_properties(self, tag):
        tags = []
        tagName, tagClosed, tagAttrs = tag
        if not tagClosed:
            while not self.isTagClose(tagName):
                tags.append(self.nextTag(["properties", "property"]))
            line = self.nextLine()
            self.getTagClose(line, tagName)

        props = {}
        for tag in tags:
            if tag[0] == "properties":
                props[tag[1]["name"]] = tag[2]
            else:
                props.update(tag[1])
        return tagName, tagAttrs, props

    def tag_property(self, tag):
        tags = []
        tagName, tagClosed, tagAttrs = tag
        if not tagClosed:
            line = self.nextLine()
            self.getTagClose(line, tagName)
        return tagName, {tag[2]["name"]: tag[2]["value"]}


if __name__ == '__main__':
    import sys
    lines = open(sys.argv[1]).read()
    xmlFile = XMLFile(lines)
    tagName, components = xmlFile.parse()

    def dump(component):
        print "component:", component[0], component[1]
        for c in component[2]:
            dump(c)
    for component in components:
        print "Frame:", component[0], component[1]
        for c in component[2]:
            dump(c)
