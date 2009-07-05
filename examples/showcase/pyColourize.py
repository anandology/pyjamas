######################################################################
# PySourceColor
# A hacked up version of the MoinMoin python parser that 
# was originally submitted / written by Jurgen Hermann to ASPN.
# This does not create w3c valid html, but it works on every 
# browser i've tried so far.(I.E.,Mozilla/Firefox,Opera,wxHTML).
# After experimenting with diffrent html vs CSS + html
# I settled on plain old html because it works!
# Too bad CSS is not supported everywhere yet.
# Hacked by M.E.Farmer Jr. 2004
# Python license
######################################################################

import keyword, os, sys
import cgi, string, cStringIO
import token, tokenize, glob
import getopt, webbrowser, time

__title__ = 'PySourceColor'
__version__ = "ver.1"
__date__ = '2 August 2004'
__author__ = "M.E.Farmer Jr."
__credits__ = '''This was originally submitted / written by Jurgen Hermann 
to ASPN python recipes. I found it in 2003 and integrated it into an editor.
Recent refactoring led me to seperate it. I decided to polish it up a little
and release it in the hope it would be useful.
Python license     M.E.Farmer 2004
'''
# Testing raw and unicode strings
# We do nothing with the value just look at colorizing
_ = (r'raw',r'''raw''',r"raw",r"""raw""")##Raw test
_ = (u'uni',u'''uni''',u"uni",u"""uni""")##Unicode test

# Do not edit
_DOUBLECOMMENT = token.NT_OFFSET + 1   
_CLASS = token.NT_OFFSET + 2
_DEF = token.NT_OFFSET + 3           
_TEXT = token.NT_OFFSET + 4           
_KEYWORD = token.NT_OFFSET + 5      
_SINGLEQUOTE = token.NT_OFFSET + 6    
_DOUBLEQUOTE = token.NT_OFFSET + 7     
_TRIPLESINGLEQUOTE = token.NT_OFFSET + 8
_TRIPLEDOUBLEQUOTE = token.NT_OFFSET + 9
_BACKGROUND = token.NT_OFFSET + 10

######################################################################
# Edit colors and styles to taste
# Create your own scheme, just copy one below , rename and edit.
# Styles are optional: b = bold, i = italic, u = underline
# Color is rgb hex and must be specified. sss#RRGGBB
# Colorscheme names must start with an underscore: _MyColor
######################################################################

_Null = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#000000',# no edit 
    _TEXT:                '#000000',# no edit
    token.NAME:           '#000000',# All Text
    token.NUMBER:        'b#000000',# 0->10
    token.OP:            'b#000000',# ()<>=!.:;^>%, etc...
    tokenize.COMMENT:    'i#000000',# There are 2 types of comment
    _DOUBLECOMMENT:       '#000000',## Like this 
    _CLASS:             'bu#000000',# Class name
    _DEF:                'b#000000',# Def name
    _KEYWORD:            'b#000000',# Python keywords
    _SINGLEQUOTE:         '#000000',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#000000',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#000000',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:  'i#000000',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#FFFFFF',# Page background color
    }

_Dark = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#FFFFFF',# no edit 
    _TEXT:                '#000000',# no edit
    token.NAME:           '#ffffff',# All Text
    token.NUMBER:         '#FF0000',# 0->10
    token.OP:            'b#FAF785',# Operators ()<>=!.:;^>%, etc...
    tokenize.COMMENT:    'i#45FCA0',# There are 2 types of comment
    _DOUBLECOMMENT:       '#A7C7A9',## Like this 
    _CLASS:              'b#B599FD',# Class name
    _DEF:                'b#EBAE5C',# Def name
    _KEYWORD:            'b#8680FF',# Python keywords
    _SINGLEQUOTE:         '#F8BAFE',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#FF80C0',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#FF9595',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:   '#B3FFFF',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#000000',# Page background color
    }

 
_Lite = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#000000',# no edit 
    _TEXT:                '#000000',# no edit
    token.NAME:           '#000000',# All Text
    token.NUMBER:         '#FF2200',# 0->10
    token.OP:            'b#303000',# Operators ()<>=!.:;^>%, etc...
    tokenize.COMMENT:     '#007F00',# There are 2 types of comment
    _DOUBLECOMMENT:       '#606060',## Like this 
    _CLASS:               '#0000FF',# Class name
    _DEF:                'b#BF9B00',# Def name
    _KEYWORD:            'b#0000AF',# Python keywords
    _SINGLEQUOTE:         '#600080',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#A0008A',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#4488BB',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:   '#2299BB',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#FFFFFF',# Page background color
    }

_Idle = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#000000',# no edit 
    _TEXT:                '#000000',# no edit
    token.NAME:           '#000000',# All Text
    token.NUMBER:         '#000000',# 0->10
    token.OP:             '#000000',# Operators ()<>=!.:;^>%, etc...
    tokenize.COMMENT:     '#DD0000',# There are 2 types of comment
    _DOUBLECOMMENT:       '#DD0000',## Like this 
    _CLASS:               '#0000FF',# Class name
    _DEF:                 '#0000FF',# Def name
    _KEYWORD:             '#FF7700',# Python keywords
    _SINGLEQUOTE:         '#00AA00',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#00AA00',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#00AA00',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:   '#00AA00',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#FFFFFF',# Page background color
    }

_PythonWin = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#000000',# no edit
    _TEXT:                '#000000',# no edit
    token.NAME:           '#303030',# All Text
    token.NUMBER:         '#008080',# 0->10
    token.OP:             '#000000',# ()<>=!.:;^>%, etc...
    tokenize.COMMENT:     '#007F00',# There are 2 types of comment
    _DOUBLECOMMENT:       '#7F7F7F',## Like this 
    _CLASS:              'b#0000FF',# Class name
    _DEF:                'b#007F7F',# Def name
    _KEYWORD:            'b#000080',# Python keywords
    _SINGLEQUOTE:         '#808000',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#808000',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#808000',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:   '#808000',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#FFFFFF',# Page background color
    }

_Eriks_Style = {
    token.ERRORTOKEN:     '#FF8080',# no edit
    token.STRING:         '#000000',# no edit 
    _TEXT:                '#000000',# no edit
    token.NAME:           '#000000',# All Text
    token.NUMBER:         '#FF2200',# 0->10
    token.OP:            'b#303000',# Operators ()<>=!.:;^>%, etc...
    tokenize.COMMENT:     '#007F00',# There are 2 types of comment
    _DOUBLECOMMENT:       '#606060',## Like this 
    _CLASS:               '#0000FF',# Class name
    _DEF:                 '#0000FF',# Def name
    _KEYWORD:            'b#0000AF',# Python keywords
    _SINGLEQUOTE:         '#600080',# 'SINGLEQUOTE'
    _DOUBLEQUOTE:         '#A0008A',# "DOUBLEQUOTE"
    _TRIPLESINGLEQUOTE:   '#4488BB',# '''TRIPLESINGLEQUOTE'''
    _TRIPLEDOUBLEQUOTE:   '#2299BB',# """TRIPLEDOUBLEQUOTE"""
    _BACKGROUND:          '#FFFFFF',# Page background color
    }

##################################################################################

def Usage():
    print"""
_______________________________________________________________________________
Example usage:
  # To colorize all .py,.pyw files in cwdir you can also use: . or _
 python PySourceColor.py -i .
  # Using long options w/ =
 python PySourceColor.py --in=c:/myDir/my.py --out=c:/myDir --color=Lite --show
  # Using short options w/out =
 python PySourceColor.py -i c:/myDir/  -c Idle
  # Using any mix 
 python PySourceColor.py --in _ -o=c:/myDir --show
-------------------------------------------------------------------------------
This module is designed to colorize python source code.
It is a hacked version of MoinMoin python parser recipe.
    -h or --help
        Display this help message.
    -i or --in 
        Input file or dir. (Use any of these for the cwdir . , _ , this)
    -o or --out
        Optional, output dir for the colorized source
            default: output dir is input dir.
    -c or --color
        Optional. Null, Dark, Lite, Idle, Pythonwin, create your own!

            default: Dark
    -s or --show
        Optional, Show webpage after creation.
            default: no show
_______________________________________________________________________________
"""

def Main():
    '''This code gathers the command line arguments 
       and tries to do something reasonable with them
    '''
    try:
        # try to get command line args 
        opts, args = getopt.getopt(sys.argv[1:],
                     "hsi:o:c:", ["help", "show", "input=", "out=", "color="])
    except getopt.GetoptError:
        # on error print help information and exit:
        Usage()
        sys.exit(2)
    # init some names
    input = None
    output = None
    scheme = None

    # if we have args then process them
    for o, a in opts:
        if o in ("-h", "--help"):
            Usage()
            sys.exit()
        if o in ("-o", "--out"):
            output = a
        if o in ("-i", "--input"):
            input = a
            if input in('.','_'):
                input = os.getcwd()
        if o  in ("-s", "--show"):
            show = 1
        else:
            show = 0
        if o in ("-c", "--color"):
            try:
               scheme = eval('_%s'%a)
            except:
               scheme = None

    if input is None:
        # if there was no input specified then we try to
        # parse ourselves and do it in diffrent flavors.
        WebIt(sys.argv[0], '/MyDir/null', _Null, 1)
        WebIt(sys.argv[0], '/MyDir/dark', _Dark, 1)
        WebIt(sys.argv[0], '/MyDir/lite', _Lite, 1)
        WebIt(sys.argv[0], '/MyDir/idle', _Idle, 1)
        WebIt(sys.argv[0], '/MyDir/pythonwin', _PythonWin, 1)
    else:
        # if there was at least an input given we can proceed
        WebAll(input, output, scheme, show)

def WebAll(sourcePath, outdir=None, colors=None, show=0):
    ''' Converts all python source in the given directory to html
    '''
    c=0
     # If it is a filename then WebIt
    if not os.path.isdir(sourcePath):
        if os.path.isfile(sourcePath):
            c+=1
            WebIt(sourcePath, outdir, colors, show)
    # If we pass in a dir we need to walkdir for files.
    # Then we need to colorize them with WebIt
    else:
        fileList = WalkDir(sourcePath)
        if fileList is not None:
            for i in fileList:
                c+=1
                WebIt(i, outdir, colors, show)
    print'Completed colorizing %s source files.'% str(c)

def WebIt(sourcePath, outdir=None, colors=None, show=0):
    ''' Converts python source to html.
    '''
    print" Converting %s into HTML" % sourcePath                
    if colors is None:
        # Default colorscheme
        colors = _Dark
    # If no outdir is given we use the sourcePath
    if outdir is None:
        htmlPath = sourcePath + '.html'
    else:
        # If we do give an outdir, and it does
        # not exist , it will be created.
        if not os.path.isdir(outdir):
            os.makedirs(outdir)
        sourceName = os.path.basename(sourcePath)
        htmlPath = os.path.join(outdir,sourceName)+'.html'
        print "  Output to %s"%htmlPath
    # Open the text and do the parsing.
    source = open(sourcePath).read()
    Parser(source, colors, sourcePath, open(htmlPath, 'wt')).format(None, None)
    if show:
        # load HTML page into the default web browser.
        # slower than os.startfile or os.system, but more universal
        try:
            webbrowser.open_new(htmlPath)
        except:
            pass
    return htmlPath

def WalkDir(dir):
    '''Return a list of .py and .pyw files from a given directory.
    '''
    # Get a list of files that match *.py*
    GLOB_PATTERN = os.path.join(dir, "*.[p][y]*")
    pathlist = glob.glob(GLOB_PATTERN)
    # Now filter out all but py and pyw
    filterlist = [x for x in pathlist 
                        if x.endswith('.py')
                        or x.endswith('.pyw')]
    if filterlist != []:
        # if we have a list send it
        return filterlist
    else:
        return None

class Parser:
    """ MoinMoin python parser heavily chopped :)
    """
    def __init__(self, raw, colors, title, out = sys.stdout):
        ''' Store the source text.
        '''
        self.raw = string.strip(string.expandtabs(raw))
        self.out = out
        self.title = os.path.basename(title)
        self.ClassFlag = 0
        self.DefFlag = 0
        self.colors = colors
        # Name: Date stamp top
        self.header = 0
        # Name: Date stamp bottom
        self.footer = 0

    def format(self, formatter, form):
        ''' Parse and send the colored source.
        '''
        # Store line offsets in self.lines
        self.lines = [0, 0]
        pos = 0

        # Gather lines
        while 1:
            pos = string.find(self.raw, '\n', pos) + 1
            if not pos: break
            self.lines.append(pos)
        self.lines.append(len(self.raw))

        # Wrap text in a filelike object
        self.pos = 0
        text = cStringIO.StringIO(self.raw)

        # Html start
        self.doPageStart()

        # Parse the source.
        ## Tokenize calls the __call__ 
        ## function for each token till done.
        try:
            tokenize.tokenize(text.readline, self)
        except tokenize.TokenError, ex:
            msg = ex[0]
            line = ex[1][0]
            self.out.write("<h3>ERROR: %s</h3>%s\n" % (
                msg, self.raw[self.lines[line]:]))

        # Html end
        self.doPageEnd()


    def __call__(self, toktype, toktext, (srow,scol), (erow,ecol), line):
        ''' Token handler.
        '''
        style = ''
        # calculate new positions
        oldpos = self.pos
        newpos = self.lines[srow] + scol
        self.pos = newpos + len(toktext)

        # handle newlines
        if toktype in [token.NEWLINE, tokenize.NL]:
            self.out.write('\n')
            return

        # send the original whitespace, if needed
        if newpos > oldpos:
            self.out.write(self.raw[oldpos:newpos])

        # skip indenting tokens
        if toktype in [token.INDENT, token.DEDENT]:
            self.pos = newpos
            return

        # map token type to a color group
        if token.LPAR <= toktype and toktype <= token.OP:
            toktype = token.OP
        elif toktype == token.NAME and keyword.iskeyword(toktext):
            toktype = _KEYWORD

        # If the keyword is class or def then we set a flag
        # the next word gets set to the class/def name color.
        if self.ClassFlag or self.DefFlag:
            # Sets the color if it was a class or def name
            if self.ClassFlag:
                toktype = _CLASS
                self.ClassFlag = 0 
            elif self.DefFlag:
                toktype = _DEF
                self.DefFlag = 0
        else:
            # Sets a flag if it was a class or def
            # next token will be colored.
            if toktext =='class':
                self.ClassFlag = 1
            elif toktext == 'def':
                self.DefFlag = 1

        # Extended to seperate the diffrent string types..
        # plus raw and unicode types
        if toktype == token.STRING:
            if (toktext[:3] == "'''") or (
                toktext[:4] == "r'''") or (
                toktext[:4] == "u'''"):
                toktype = _TRIPLESINGLEQUOTE
            elif (toktext[:3] == '"""') or (
                   toktext[:4] == 'r"""') or (
                   toktext[:4] == 'u"""'):
                toktype = _TRIPLEDOUBLEQUOTE
            elif (toktext[:1] == '"') or (
                   toktext[:2] == 'r"') or (
                   toktext[:2] == 'u"'):
                toktype = _DOUBLEQUOTE
            elif (toktext[:1] == "'") or (
                   toktext[:2] == "r'") or (
                   toktext[:2] == "u'"):
                toktype = _SINGLEQUOTE

        # Exetended to seperate the diffrent comment types
        elif toktype == tokenize.COMMENT:
            if toktext[:2] == "##":
                toktype = _DOUBLECOMMENT

        # Get the colors from the dictionary for the standard tokens
        color = self.colors.get(toktype, self.colors[_TEXT])
        otherstart = ''
        otherend = ''
        splitpoint = color.find('#')
        tags = color[:splitpoint].lower()
        color = color[splitpoint:]
        
        # Check for styles and set them if needed..(b=bold, i=italics)
        if 'b' in tags:
            otherstart += '<b>'
            otherend += '</b>'
        if 'i' in tags:
            otherstart += '<i>'
            otherend += '</i>'
        if 'u' in tags:
            otherstart += '<u>'
            otherend += '</u>'

        # Error tokenizing ..red boxes
        if toktype == token.ERRORTOKEN:
            style = ' style="border: solid 1.5pt #FF0000;"'

        # send text
        self.out.write('<font color="%s"%s>%s' % (color, style, otherstart))
        self.out.write(cgi.escape(toktext))
        self.out.write('%s</font>'% (otherend,))
        return

    def doPageStart(self):
        self.out.write('<!DOCTYPE HTML PUBLIC "-//W3C//DTD \
                          HTML 3.2 Final//EN"\n')
        self.out.write('<html><head><title>%s</title>\n'% (self.title))
        self.out.write('<!--This document created by %s %s on: %s-->\n'%
                                        (__title__,__version__,time.ctime()))
        self.out.write('<meta http-equiv="Content-Type" \
                         content="text/html;charset=iso-8859-1" />\n')
        # Get background color and check for styles and ignore all but b,i,u
        color = self.colors.get(_BACKGROUND, self.colors[_TEXT])
        color = color[color.find('#'):]
        if color[:1] != '#': 
            self.out.write('</head><body bgcolor="#000000">\n')
        else:
            self.out.write('</head><body bgcolor="%s">\n'% color)
        # Write a little info at the top.
        if self.header:
            self.doPageHeader()
        self.out.write('<pre><font face="Lucida Console, Courier New">\n')
        #self.out.write('<pre>\n')

    def doPageHeader(self):
            color = self.colors.get(token.NAME, self.colors[_TEXT])
            color = color[color.find('#'):]
            self.out.write(' <b><u><font color="%s">%s    %s</font></u></b>\n'%
                                            (color, self.title, time.ctime()))
    def doPageFooter(self):
            color = self.colors.get(token.NAME, self.colors[_TEXT])
            color = color[color.find('#'):]
            self.out.write(' <b><u><font color="%s">%s    %s</font></u></b>\n'%
                                              (color, self.title,time.ctime()))
    def doPageEnd(self):
        self.out.write('</pre>\n')
        # Write a little info at the bottom
        if self.footer:
            self.doPageFooter()
        # Write a little info in the web page source
        self.out.write('<!--This document created by %s ver.%s on: %s-->\n'%
                                        (__title__,__version__,time.ctime()))
        self.out.write('</body></html>\n')

if __name__ == '__main__':
    Main()

