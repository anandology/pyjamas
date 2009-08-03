# auto-generated using idlparser mshtml.idl - do not edit!
import sys
from comtypes.client import GetModule
if not hasattr(sys, 'frozen'):
    GetModule('atl.dll')
    GetModule('shdocvw.dll')
from comtypes.gen import SHDocVw
from comtypes.gen import MSHTML

wrapperClasses = {}
coWrapperClasses = {}
backWrapperClasses = {}
def unwrap(item):
    if item is None:
        return None
    kls = item.__class__
    if not backWrapperClasses.has_key(kls):
        return item
    return item.__instance__
def wrap(item):
    if item is None:
        return None
    if not hasattr(item, '_iid_'):
        return item
    kls = str(item._iid_)
    if coWrapperClasses.has_key(kls):
        return coWrapperClasses[kls](item)
    if not wrapperClasses.has_key(kls):
        return item
    return wrapperClasses[kls](item)


##############################
# IHTMLFiltersCollection
#
class IHTMLFiltersCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFiltersCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F3EE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFiltersCollection
backWrapperClasses[IHTMLFiltersCollection] = '{3050F3EE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle
#
class IHTMLStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle
		return self.__instance__.QueryInterface(kls)
	#font
	def _get_font(self):
		return wrap(self.__get_instance().font)
	def _set_font(self, value):
		self.__get_instance().font = unwrap(value)
	font = property(_get_font, _set_font)

	#borderTop
	def _get_borderTop(self):
		return wrap(self.__get_instance().borderTop)
	def _set_borderTop(self, value):
		self.__get_instance().borderTop = unwrap(value)
	borderTop = property(_get_borderTop, _set_borderTop)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#posTop
	def _get_posTop(self):
		return wrap(self.__get_instance().posTop)
	def _set_posTop(self, value):
		self.__get_instance().posTop = unwrap(value)
	posTop = property(_get_posTop, _set_posTop)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#background
	def _get_background(self):
		return wrap(self.__get_instance().background)
	def _set_background(self, value):
		self.__get_instance().background = unwrap(value)
	background = property(_get_background, _set_background)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#textDecorationLineThrough
	def _get_textDecorationLineThrough(self):
		return wrap(self.__get_instance().textDecorationLineThrough)
	def _set_textDecorationLineThrough(self, value):
		self.__get_instance().textDecorationLineThrough = unwrap(value)
	textDecorationLineThrough = property(_get_textDecorationLineThrough, _set_textDecorationLineThrough)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance().cssText)
	def _set_cssText(self, value):
		self.__get_instance().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

	#posHeight
	def _get_posHeight(self):
		return wrap(self.__get_instance().posHeight)
	def _set_posHeight(self, value):
		self.__get_instance().posHeight = unwrap(value)
	posHeight = property(_get_posHeight, _set_posHeight)

	#pixelWidth
	def _get_pixelWidth(self):
		return wrap(self.__get_instance().pixelWidth)
	def _set_pixelWidth(self, value):
		self.__get_instance().pixelWidth = unwrap(value)
	pixelWidth = property(_get_pixelWidth, _set_pixelWidth)

	#posLeft
	def _get_posLeft(self):
		return wrap(self.__get_instance().posLeft)
	def _set_posLeft(self, value):
		self.__get_instance().posLeft = unwrap(value)
	posLeft = property(_get_posLeft, _set_posLeft)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance().filter)
	def _set_filter(self, value):
		self.__get_instance().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#borderRight
	def _get_borderRight(self):
		return wrap(self.__get_instance().borderRight)
	def _set_borderRight(self, value):
		self.__get_instance().borderRight = unwrap(value)
	borderRight = property(_get_borderRight, _set_borderRight)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#color
	def _get_color(self):
		return wrap(self.__get_instance().color)
	def _set_color(self, value):
		self.__get_instance().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#borderBottom
	def _get_borderBottom(self):
		return wrap(self.__get_instance().borderBottom)
	def _set_borderBottom(self, value):
		self.__get_instance().borderBottom = unwrap(value)
	borderBottom = property(_get_borderBottom, _set_borderBottom)

	#backgroundPosition
	def _get_backgroundPosition(self):
		return wrap(self.__get_instance().backgroundPosition)
	def _set_backgroundPosition(self, value):
		self.__get_instance().backgroundPosition = unwrap(value)
	backgroundPosition = property(_get_backgroundPosition, _set_backgroundPosition)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#top
	def _get_top(self):
		return wrap(self.__get_instance().top)
	def _set_top(self, value):
		self.__get_instance().top = unwrap(value)
	top = property(_get_top, _set_top)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#pixelLeft
	def _get_pixelLeft(self):
		return wrap(self.__get_instance().pixelLeft)
	def _set_pixelLeft(self, value):
		self.__get_instance().pixelLeft = unwrap(value)
	pixelLeft = property(_get_pixelLeft, _set_pixelLeft)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance().visibility)
	def _set_visibility(self, value):
		self.__get_instance().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#textDecorationNone
	def _get_textDecorationNone(self):
		return wrap(self.__get_instance().textDecorationNone)
	def _set_textDecorationNone(self, value):
		self.__get_instance().textDecorationNone = unwrap(value)
	textDecorationNone = property(_get_textDecorationNone, _set_textDecorationNone)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance().padding)
	def _set_padding(self, value):
		self.__get_instance().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#textDecorationOverline
	def _get_textDecorationOverline(self):
		return wrap(self.__get_instance().textDecorationOverline)
	def _set_textDecorationOverline(self, value):
		self.__get_instance().textDecorationOverline = unwrap(value)
	textDecorationOverline = property(_get_textDecorationOverline, _set_textDecorationOverline)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance().overflow)
	def _set_overflow(self, value):
		self.__get_instance().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance().cursor)
	def _set_cursor(self, value):
		self.__get_instance().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance().margin)
	def _set_margin(self, value):
		self.__get_instance().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance().display)
	def _set_display(self, value):
		self.__get_instance().display = unwrap(value)
	display = property(_get_display, _set_display)

	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#clip
	def _get_clip(self):
		return wrap(self.__get_instance().clip)
	def _set_clip(self, value):
		self.__get_instance().clip = unwrap(value)
	clip = property(_get_clip, _set_clip)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderLeft
	def _get_borderLeft(self):
		return wrap(self.__get_instance().borderLeft)
	def _set_borderLeft(self, value):
		self.__get_instance().borderLeft = unwrap(value)
	borderLeft = property(_get_borderLeft, _set_borderLeft)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#pixelHeight
	def _get_pixelHeight(self):
		return wrap(self.__get_instance().pixelHeight)
	def _set_pixelHeight(self, value):
		self.__get_instance().pixelHeight = unwrap(value)
	pixelHeight = property(_get_pixelHeight, _set_pixelHeight)

	#posWidth
	def _get_posWidth(self):
		return wrap(self.__get_instance().posWidth)
	def _set_posWidth(self, value):
		self.__get_instance().posWidth = unwrap(value)
	posWidth = property(_get_posWidth, _set_posWidth)

	#textDecorationBlink
	def _get_textDecorationBlink(self):
		return wrap(self.__get_instance().textDecorationBlink)
	def _set_textDecorationBlink(self, value):
		self.__get_instance().textDecorationBlink = unwrap(value)
	textDecorationBlink = property(_get_textDecorationBlink, _set_textDecorationBlink)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#pixelTop
	def _get_pixelTop(self):
		return wrap(self.__get_instance().pixelTop)
	def _set_pixelTop(self, value):
		self.__get_instance().pixelTop = unwrap(value)
	pixelTop = property(_get_pixelTop, _set_pixelTop)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance().clear)
	def _set_clear(self, value):
		self.__get_instance().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#textDecorationUnderline
	def _get_textDecorationUnderline(self):
		return wrap(self.__get_instance().textDecorationUnderline)
	def _set_textDecorationUnderline(self, value):
		self.__get_instance().textDecorationUnderline = unwrap(value)
	textDecorationUnderline = property(_get_textDecorationUnderline, _set_textDecorationUnderline)

	#listStyle
	def _get_listStyle(self):
		return wrap(self.__get_instance().listStyle)
	def _set_listStyle(self, value):
		self.__get_instance().listStyle = unwrap(value)
	listStyle = property(_get_listStyle, _set_listStyle)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#left
	def _get_left(self):
		return wrap(self.__get_instance().left)
	def _set_left(self, value):
		self.__get_instance().left = unwrap(value)
	left = property(_get_left, _set_left)

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttribute(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setAttribute(*args))

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeAttribute(*args))

wrapperClasses['{3050F25E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle
backWrapperClasses[IHTMLStyle] = '{3050F25E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle2
#
class IHTMLStyle2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle2
		return self.__instance__.QueryInterface(kls)
	#textJustifyTrim
	def _get_textJustifyTrim(self):
		return wrap(self.__get_instance().textJustifyTrim)
	def _set_textJustifyTrim(self, value):
		self.__get_instance().textJustifyTrim = unwrap(value)
	textJustifyTrim = property(_get_textJustifyTrim, _set_textJustifyTrim)

	#right
	def _get_right(self):
		return wrap(self.__get_instance().right)
	def _set_right(self, value):
		self.__get_instance().right = unwrap(value)
	right = property(_get_right, _set_right)

	#pixelRight
	def _get_pixelRight(self):
		return wrap(self.__get_instance().pixelRight)
	def _set_pixelRight(self, value):
		self.__get_instance().pixelRight = unwrap(value)
	pixelRight = property(_get_pixelRight, _set_pixelRight)

	#accelerator
	def _get_accelerator(self):
		return wrap(self.__get_instance().accelerator)
	def _set_accelerator(self, value):
		self.__get_instance().accelerator = unwrap(value)
	accelerator = property(_get_accelerator, _set_accelerator)

	#pixelBottom
	def _get_pixelBottom(self):
		return wrap(self.__get_instance().pixelBottom)
	def _set_pixelBottom(self, value):
		self.__get_instance().pixelBottom = unwrap(value)
	pixelBottom = property(_get_pixelBottom, _set_pixelBottom)

	#layoutGridLine
	def _get_layoutGridLine(self):
		return wrap(self.__get_instance().layoutGridLine)
	def _set_layoutGridLine(self, value):
		self.__get_instance().layoutGridLine = unwrap(value)
	layoutGridLine = property(_get_layoutGridLine, _set_layoutGridLine)

	#tableLayout
	def _get_tableLayout(self):
		return wrap(self.__get_instance().tableLayout)
	def _set_tableLayout(self, value):
		self.__get_instance().tableLayout = unwrap(value)
	tableLayout = property(_get_tableLayout, _set_tableLayout)

	#layoutGridType
	def _get_layoutGridType(self):
		return wrap(self.__get_instance().layoutGridType)
	def _set_layoutGridType(self, value):
		self.__get_instance().layoutGridType = unwrap(value)
	layoutGridType = property(_get_layoutGridType, _set_layoutGridType)

	#borderCollapse
	def _get_borderCollapse(self):
		return wrap(self.__get_instance().borderCollapse)
	def _set_borderCollapse(self, value):
		self.__get_instance().borderCollapse = unwrap(value)
	borderCollapse = property(_get_borderCollapse, _set_borderCollapse)

	#overflowY
	def _get_overflowY(self):
		return wrap(self.__get_instance().overflowY)
	def _set_overflowY(self, value):
		self.__get_instance().overflowY = unwrap(value)
	overflowY = property(_get_overflowY, _set_overflowY)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance().bottom)
	def _set_bottom(self, value):
		self.__get_instance().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#rubyAlign
	def _get_rubyAlign(self):
		return wrap(self.__get_instance().rubyAlign)
	def _set_rubyAlign(self, value):
		self.__get_instance().rubyAlign = unwrap(value)
	rubyAlign = property(_get_rubyAlign, _set_rubyAlign)

	#imeMode
	def _get_imeMode(self):
		return wrap(self.__get_instance().imeMode)
	def _set_imeMode(self, value):
		self.__get_instance().imeMode = unwrap(value)
	imeMode = property(_get_imeMode, _set_imeMode)

	#rubyOverhang
	def _get_rubyOverhang(self):
		return wrap(self.__get_instance().rubyOverhang)
	def _set_rubyOverhang(self, value):
		self.__get_instance().rubyOverhang = unwrap(value)
	rubyOverhang = property(_get_rubyOverhang, _set_rubyOverhang)

	#textKashida
	def _get_textKashida(self):
		return wrap(self.__get_instance().textKashida)
	def _set_textKashida(self, value):
		self.__get_instance().textKashida = unwrap(value)
	textKashida = property(_get_textKashida, _set_textKashida)

	#rubyPosition
	def _get_rubyPosition(self):
		return wrap(self.__get_instance().rubyPosition)
	def _set_rubyPosition(self, value):
		self.__get_instance().rubyPosition = unwrap(value)
	rubyPosition = property(_get_rubyPosition, _set_rubyPosition)

	#unicodeBidi
	def _get_unicodeBidi(self):
		return wrap(self.__get_instance().unicodeBidi)
	def _set_unicodeBidi(self, value):
		self.__get_instance().unicodeBidi = unwrap(value)
	unicodeBidi = property(_get_unicodeBidi, _set_unicodeBidi)

	#direction
	def _get_direction(self):
		return wrap(self.__get_instance().direction)
	def _set_direction(self, value):
		self.__get_instance().direction = unwrap(value)
	direction = property(_get_direction, _set_direction)

	#layoutGridChar
	def _get_layoutGridChar(self):
		return wrap(self.__get_instance().layoutGridChar)
	def _set_layoutGridChar(self, value):
		self.__get_instance().layoutGridChar = unwrap(value)
	layoutGridChar = property(_get_layoutGridChar, _set_layoutGridChar)

	#position
	def _get_position(self):
		return wrap(self.__get_instance().position)
	def _set_position(self, value):
		self.__get_instance().position = unwrap(value)
	position = property(_get_position, _set_position)

	#textJustify
	def _get_textJustify(self):
		return wrap(self.__get_instance().textJustify)
	def _set_textJustify(self, value):
		self.__get_instance().textJustify = unwrap(value)
	textJustify = property(_get_textJustify, _set_textJustify)

	#wordBreak
	def _get_wordBreak(self):
		return wrap(self.__get_instance().wordBreak)
	def _set_wordBreak(self, value):
		self.__get_instance().wordBreak = unwrap(value)
	wordBreak = property(_get_wordBreak, _set_wordBreak)

	#layoutGrid
	def _get_layoutGrid(self):
		return wrap(self.__get_instance().layoutGrid)
	def _set_layoutGrid(self, value):
		self.__get_instance().layoutGrid = unwrap(value)
	layoutGrid = property(_get_layoutGrid, _set_layoutGrid)

	#lineBreak
	def _get_lineBreak(self):
		return wrap(self.__get_instance().lineBreak)
	def _set_lineBreak(self, value):
		self.__get_instance().lineBreak = unwrap(value)
	lineBreak = property(_get_lineBreak, _set_lineBreak)

	#textAutospace
	def _get_textAutospace(self):
		return wrap(self.__get_instance().textAutospace)
	def _set_textAutospace(self, value):
		self.__get_instance().textAutospace = unwrap(value)
	textAutospace = property(_get_textAutospace, _set_textAutospace)

	#posBottom
	def _get_posBottom(self):
		return wrap(self.__get_instance().posBottom)
	def _set_posBottom(self, value):
		self.__get_instance().posBottom = unwrap(value)
	posBottom = property(_get_posBottom, _set_posBottom)

	#overflowX
	def _get_overflowX(self):
		return wrap(self.__get_instance().overflowX)
	def _set_overflowX(self, value):
		self.__get_instance().overflowX = unwrap(value)
	overflowX = property(_get_overflowX, _set_overflowX)

	#posRight
	def _get_posRight(self):
		return wrap(self.__get_instance().posRight)
	def _set_posRight(self, value):
		self.__get_instance().posRight = unwrap(value)
	posRight = property(_get_posRight, _set_posRight)

	#behavior
	def _get_behavior(self):
		return wrap(self.__get_instance().behavior)
	def _set_behavior(self, value):
		self.__get_instance().behavior = unwrap(value)
	behavior = property(_get_behavior, _set_behavior)

	#layoutGridMode
	def _get_layoutGridMode(self):
		return wrap(self.__get_instance().layoutGridMode)
	def _set_layoutGridMode(self, value):
		self.__get_instance().layoutGridMode = unwrap(value)
	layoutGridMode = property(_get_layoutGridMode, _set_layoutGridMode)

	#setExpression
	def setExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setExpression(*args))

	#removeExpression
	def removeExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeExpression(*args))

	#getExpression
	def getExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getExpression(*args))

wrapperClasses['{3050F4A2-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle2
backWrapperClasses[IHTMLStyle2] = '{3050F4A2-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRuleStyle
#
class IHTMLRuleStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRuleStyle
		return self.__instance__.QueryInterface(kls)
	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#clip
	def _get_clip(self):
		return wrap(self.__get_instance().clip)
	def _set_clip(self, value):
		self.__get_instance().clip = unwrap(value)
	clip = property(_get_clip, _set_clip)

	#color
	def _get_color(self):
		return wrap(self.__get_instance().color)
	def _set_color(self, value):
		self.__get_instance().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderBottom
	def _get_borderBottom(self):
		return wrap(self.__get_instance().borderBottom)
	def _set_borderBottom(self, value):
		self.__get_instance().borderBottom = unwrap(value)
	borderBottom = property(_get_borderBottom, _set_borderBottom)

	#backgroundPosition
	def _get_backgroundPosition(self):
		return wrap(self.__get_instance().backgroundPosition)
	def _set_backgroundPosition(self, value):
		self.__get_instance().backgroundPosition = unwrap(value)
	backgroundPosition = property(_get_backgroundPosition, _set_backgroundPosition)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderLeft
	def _get_borderLeft(self):
		return wrap(self.__get_instance().borderLeft)
	def _set_borderLeft(self, value):
		self.__get_instance().borderLeft = unwrap(value)
	borderLeft = property(_get_borderLeft, _set_borderLeft)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#font
	def _get_font(self):
		return wrap(self.__get_instance().font)
	def _set_font(self, value):
		self.__get_instance().font = unwrap(value)
	font = property(_get_font, _set_font)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance().overflow)
	def _set_overflow(self, value):
		self.__get_instance().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#textDecorationLineThrough
	def _get_textDecorationLineThrough(self):
		return wrap(self.__get_instance().textDecorationLineThrough)
	def _set_textDecorationLineThrough(self, value):
		self.__get_instance().textDecorationLineThrough = unwrap(value)
	textDecorationLineThrough = property(_get_textDecorationLineThrough, _set_textDecorationLineThrough)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance().cssText)
	def _set_cssText(self, value):
		self.__get_instance().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#top
	def _get_top(self):
		return wrap(self.__get_instance().top)
	def _set_top(self, value):
		self.__get_instance().top = unwrap(value)
	top = property(_get_top, _set_top)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance().filter)
	def _set_filter(self, value):
		self.__get_instance().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textDecorationBlink
	def _get_textDecorationBlink(self):
		return wrap(self.__get_instance().textDecorationBlink)
	def _set_textDecorationBlink(self, value):
		self.__get_instance().textDecorationBlink = unwrap(value)
	textDecorationBlink = property(_get_textDecorationBlink, _set_textDecorationBlink)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance().visibility)
	def _set_visibility(self, value):
		self.__get_instance().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#textDecorationNone
	def _get_textDecorationNone(self):
		return wrap(self.__get_instance().textDecorationNone)
	def _set_textDecorationNone(self, value):
		self.__get_instance().textDecorationNone = unwrap(value)
	textDecorationNone = property(_get_textDecorationNone, _set_textDecorationNone)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance().padding)
	def _set_padding(self, value):
		self.__get_instance().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#textDecorationOverline
	def _get_textDecorationOverline(self):
		return wrap(self.__get_instance().textDecorationOverline)
	def _set_textDecorationOverline(self, value):
		self.__get_instance().textDecorationOverline = unwrap(value)
	textDecorationOverline = property(_get_textDecorationOverline, _set_textDecorationOverline)

	#background
	def _get_background(self):
		return wrap(self.__get_instance().background)
	def _set_background(self, value):
		self.__get_instance().background = unwrap(value)
	background = property(_get_background, _set_background)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderTop
	def _get_borderTop(self):
		return wrap(self.__get_instance().borderTop)
	def _set_borderTop(self, value):
		self.__get_instance().borderTop = unwrap(value)
	borderTop = property(_get_borderTop, _set_borderTop)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#left
	def _get_left(self):
		return wrap(self.__get_instance().left)
	def _set_left(self, value):
		self.__get_instance().left = unwrap(value)
	left = property(_get_left, _set_left)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance().clear)
	def _set_clear(self, value):
		self.__get_instance().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance().cursor)
	def _set_cursor(self, value):
		self.__get_instance().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#listStyle
	def _get_listStyle(self):
		return wrap(self.__get_instance().listStyle)
	def _set_listStyle(self, value):
		self.__get_instance().listStyle = unwrap(value)
	listStyle = property(_get_listStyle, _set_listStyle)

	#borderRight
	def _get_borderRight(self):
		return wrap(self.__get_instance().borderRight)
	def _set_borderRight(self, value):
		self.__get_instance().borderRight = unwrap(value)
	borderRight = property(_get_borderRight, _set_borderRight)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#position
	def _get_position(self):
		return wrap(self.__get_instance().position)
	def _set_position(self, value):
		self.__get_instance().position = unwrap(value)
	position = property(_get_position, _set_position)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance().margin)
	def _set_margin(self, value):
		self.__get_instance().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance().display)
	def _set_display(self, value):
		self.__get_instance().display = unwrap(value)
	display = property(_get_display, _set_display)

	#textDecorationUnderline
	def _get_textDecorationUnderline(self):
		return wrap(self.__get_instance().textDecorationUnderline)
	def _set_textDecorationUnderline(self, value):
		self.__get_instance().textDecorationUnderline = unwrap(value)
	textDecorationUnderline = property(_get_textDecorationUnderline, _set_textDecorationUnderline)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttribute(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setAttribute(*args))

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeAttribute(*args))

wrapperClasses['{3050F3CF-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRuleStyle
backWrapperClasses[IHTMLRuleStyle] = '{3050F3CF-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLStyle
#
class DispHTMLStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLStyle
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F55A-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLStyle
backWrapperClasses[DispHTMLStyle] = '{3050F55A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle3
#
class IHTMLStyle3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle3
		return self.__instance__.QueryInterface(kls)
	#scrollbarHighlightColor
	def _get_scrollbarHighlightColor(self):
		return wrap(self.__get_instance().scrollbarHighlightColor)
	def _set_scrollbarHighlightColor(self, value):
		self.__get_instance().scrollbarHighlightColor = unwrap(value)
	scrollbarHighlightColor = property(_get_scrollbarHighlightColor, _set_scrollbarHighlightColor)

	#scrollbar3dLightColor
	def _get_scrollbar3dLightColor(self):
		return wrap(self.__get_instance().scrollbar3dLightColor)
	def _set_scrollbar3dLightColor(self, value):
		self.__get_instance().scrollbar3dLightColor = unwrap(value)
	scrollbar3dLightColor = property(_get_scrollbar3dLightColor, _set_scrollbar3dLightColor)

	#scrollbarDarkShadowColor
	def _get_scrollbarDarkShadowColor(self):
		return wrap(self.__get_instance().scrollbarDarkShadowColor)
	def _set_scrollbarDarkShadowColor(self, value):
		self.__get_instance().scrollbarDarkShadowColor = unwrap(value)
	scrollbarDarkShadowColor = property(_get_scrollbarDarkShadowColor, _set_scrollbarDarkShadowColor)

	#zoom
	def _get_zoom(self):
		return wrap(self.__get_instance().zoom)
	def _set_zoom(self, value):
		self.__get_instance().zoom = unwrap(value)
	zoom = property(_get_zoom, _set_zoom)

	#scrollbarShadowColor
	def _get_scrollbarShadowColor(self):
		return wrap(self.__get_instance().scrollbarShadowColor)
	def _set_scrollbarShadowColor(self, value):
		self.__get_instance().scrollbarShadowColor = unwrap(value)
	scrollbarShadowColor = property(_get_scrollbarShadowColor, _set_scrollbarShadowColor)

	#scrollbarFaceColor
	def _get_scrollbarFaceColor(self):
		return wrap(self.__get_instance().scrollbarFaceColor)
	def _set_scrollbarFaceColor(self, value):
		self.__get_instance().scrollbarFaceColor = unwrap(value)
	scrollbarFaceColor = property(_get_scrollbarFaceColor, _set_scrollbarFaceColor)

	#writingMode
	def _get_writingMode(self):
		return wrap(self.__get_instance().writingMode)
	def _set_writingMode(self, value):
		self.__get_instance().writingMode = unwrap(value)
	writingMode = property(_get_writingMode, _set_writingMode)

	#scrollbarTrackColor
	def _get_scrollbarTrackColor(self):
		return wrap(self.__get_instance().scrollbarTrackColor)
	def _set_scrollbarTrackColor(self, value):
		self.__get_instance().scrollbarTrackColor = unwrap(value)
	scrollbarTrackColor = property(_get_scrollbarTrackColor, _set_scrollbarTrackColor)

	#scrollbarBaseColor
	def _get_scrollbarBaseColor(self):
		return wrap(self.__get_instance().scrollbarBaseColor)
	def _set_scrollbarBaseColor(self, value):
		self.__get_instance().scrollbarBaseColor = unwrap(value)
	scrollbarBaseColor = property(_get_scrollbarBaseColor, _set_scrollbarBaseColor)

	#scrollbarArrowColor
	def _get_scrollbarArrowColor(self):
		return wrap(self.__get_instance().scrollbarArrowColor)
	def _set_scrollbarArrowColor(self, value):
		self.__get_instance().scrollbarArrowColor = unwrap(value)
	scrollbarArrowColor = property(_get_scrollbarArrowColor, _set_scrollbarArrowColor)

	#textAlignLast
	def _get_textAlignLast(self):
		return wrap(self.__get_instance().textAlignLast)
	def _set_textAlignLast(self, value):
		self.__get_instance().textAlignLast = unwrap(value)
	textAlignLast = property(_get_textAlignLast, _set_textAlignLast)

	#wordWrap
	def _get_wordWrap(self):
		return wrap(self.__get_instance().wordWrap)
	def _set_wordWrap(self, value):
		self.__get_instance().wordWrap = unwrap(value)
	wordWrap = property(_get_wordWrap, _set_wordWrap)

	#textKashidaSpace
	def _get_textKashidaSpace(self):
		return wrap(self.__get_instance().textKashidaSpace)
	def _set_textKashidaSpace(self, value):
		self.__get_instance().textKashidaSpace = unwrap(value)
	textKashidaSpace = property(_get_textKashidaSpace, _set_textKashidaSpace)

	#layoutFlow
	def _get_layoutFlow(self):
		return wrap(self.__get_instance().layoutFlow)
	def _set_layoutFlow(self, value):
		self.__get_instance().layoutFlow = unwrap(value)
	layoutFlow = property(_get_layoutFlow, _set_layoutFlow)

	#textUnderlinePosition
	def _get_textUnderlinePosition(self):
		return wrap(self.__get_instance().textUnderlinePosition)
	def _set_textUnderlinePosition(self, value):
		self.__get_instance().textUnderlinePosition = unwrap(value)
	textUnderlinePosition = property(_get_textUnderlinePosition, _set_textUnderlinePosition)

wrapperClasses['{3050F656-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle3
backWrapperClasses[IHTMLStyle3] = '{3050F656-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle4
#
class IHTMLStyle4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle4
		return self.__instance__.QueryInterface(kls)
	#textOverflow
	def _get_textOverflow(self):
		return wrap(self.__get_instance().textOverflow)
	def _set_textOverflow(self, value):
		self.__get_instance().textOverflow = unwrap(value)
	textOverflow = property(_get_textOverflow, _set_textOverflow)

	#minHeight
	def _get_minHeight(self):
		return wrap(self.__get_instance().minHeight)
	def _set_minHeight(self, value):
		self.__get_instance().minHeight = unwrap(value)
	minHeight = property(_get_minHeight, _set_minHeight)

wrapperClasses['{3050F816-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle4
backWrapperClasses[IHTMLStyle4] = '{3050F816-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRenderStyle
#
class IHTMLRenderStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRenderStyle
		return self.__instance__.QueryInterface(kls)
	#renderingPriority
	def _get_renderingPriority(self):
		return wrap(self.__get_instance().renderingPriority)
	def _set_renderingPriority(self, value):
		self.__get_instance().renderingPriority = unwrap(value)
	renderingPriority = property(_get_renderingPriority, _set_renderingPriority)

	#defaultTextSelection
	def _get_defaultTextSelection(self):
		return wrap(self.__get_instance().defaultTextSelection)
	def _set_defaultTextSelection(self, value):
		self.__get_instance().defaultTextSelection = unwrap(value)
	defaultTextSelection = property(_get_defaultTextSelection, _set_defaultTextSelection)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#textEffect
	def _get_textEffect(self):
		return wrap(self.__get_instance().textEffect)
	def _set_textEffect(self, value):
		self.__get_instance().textEffect = unwrap(value)
	textEffect = property(_get_textEffect, _set_textEffect)

	#textBackgroundColor
	def _get_textBackgroundColor(self):
		return wrap(self.__get_instance().textBackgroundColor)
	def _set_textBackgroundColor(self, value):
		self.__get_instance().textBackgroundColor = unwrap(value)
	textBackgroundColor = property(_get_textBackgroundColor, _set_textBackgroundColor)

	#textLineThroughStyle
	def _get_textLineThroughStyle(self):
		return wrap(self.__get_instance().textLineThroughStyle)
	def _set_textLineThroughStyle(self, value):
		self.__get_instance().textLineThroughStyle = unwrap(value)
	textLineThroughStyle = property(_get_textLineThroughStyle, _set_textLineThroughStyle)

	#textColor
	def _get_textColor(self):
		return wrap(self.__get_instance().textColor)
	def _set_textColor(self, value):
		self.__get_instance().textColor = unwrap(value)
	textColor = property(_get_textColor, _set_textColor)

	#textUnderlineStyle
	def _get_textUnderlineStyle(self):
		return wrap(self.__get_instance().textUnderlineStyle)
	def _set_textUnderlineStyle(self, value):
		self.__get_instance().textUnderlineStyle = unwrap(value)
	textUnderlineStyle = property(_get_textUnderlineStyle, _set_textUnderlineStyle)

	#textDecorationColor
	def _get_textDecorationColor(self):
		return wrap(self.__get_instance().textDecorationColor)
	def _set_textDecorationColor(self, value):
		self.__get_instance().textDecorationColor = unwrap(value)
	textDecorationColor = property(_get_textDecorationColor, _set_textDecorationColor)

wrapperClasses['{3050F6AE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRenderStyle
backWrapperClasses[IHTMLRenderStyle] = '{3050F6AE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle
#
class IHTMLCurrentStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle
		return self.__instance__.QueryInterface(kls)
	#layoutGridType
	def _get_layoutGridType(self):
		return wrap(self.__get_instance().layoutGridType)
	def _set_layoutGridType(self, value):
		self.__get_instance().layoutGridType = unwrap(value)
	layoutGridType = property(_get_layoutGridType, _set_layoutGridType)

	#tableLayout
	def _get_tableLayout(self):
		return wrap(self.__get_instance().tableLayout)
	def _set_tableLayout(self, value):
		self.__get_instance().tableLayout = unwrap(value)
	tableLayout = property(_get_tableLayout, _set_tableLayout)

	#left
	def _get_left(self):
		return wrap(self.__get_instance().left)
	def _set_left(self, value):
		self.__get_instance().left = unwrap(value)
	left = property(_get_left, _set_left)

	#borderCollapse
	def _get_borderCollapse(self):
		return wrap(self.__get_instance().borderCollapse)
	def _set_borderCollapse(self, value):
		self.__get_instance().borderCollapse = unwrap(value)
	borderCollapse = property(_get_borderCollapse, _set_borderCollapse)

	#overflowY
	def _get_overflowY(self):
		return wrap(self.__get_instance().overflowY)
	def _set_overflowY(self, value):
		self.__get_instance().overflowY = unwrap(value)
	overflowY = property(_get_overflowY, _set_overflowY)

	#overflowX
	def _get_overflowX(self):
		return wrap(self.__get_instance().overflowX)
	def _set_overflowX(self, value):
		self.__get_instance().overflowX = unwrap(value)
	overflowX = property(_get_overflowX, _set_overflowX)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#imeMode
	def _get_imeMode(self):
		return wrap(self.__get_instance().imeMode)
	def _set_imeMode(self, value):
		self.__get_instance().imeMode = unwrap(value)
	imeMode = property(_get_imeMode, _set_imeMode)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#textJustify
	def _get_textJustify(self):
		return wrap(self.__get_instance().textJustify)
	def _set_textJustify(self, value):
		self.__get_instance().textJustify = unwrap(value)
	textJustify = property(_get_textJustify, _set_textJustify)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#layoutGridLine
	def _get_layoutGridLine(self):
		return wrap(self.__get_instance().layoutGridLine)
	def _set_layoutGridLine(self, value):
		self.__get_instance().layoutGridLine = unwrap(value)
	layoutGridLine = property(_get_layoutGridLine, _set_layoutGridLine)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#layoutGridMode
	def _get_layoutGridMode(self):
		return wrap(self.__get_instance().layoutGridMode)
	def _set_layoutGridMode(self, value):
		self.__get_instance().layoutGridMode = unwrap(value)
	layoutGridMode = property(_get_layoutGridMode, _set_layoutGridMode)

	#right
	def _get_right(self):
		return wrap(self.__get_instance().right)
	def _set_right(self, value):
		self.__get_instance().right = unwrap(value)
	right = property(_get_right, _set_right)

	#accelerator
	def _get_accelerator(self):
		return wrap(self.__get_instance().accelerator)
	def _set_accelerator(self, value):
		self.__get_instance().accelerator = unwrap(value)
	accelerator = property(_get_accelerator, _set_accelerator)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#clipRight
	def _get_clipRight(self):
		return wrap(self.__get_instance().clipRight)
	def _set_clipRight(self, value):
		self.__get_instance().clipRight = unwrap(value)
	clipRight = property(_get_clipRight, _set_clipRight)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance().bottom)
	def _set_bottom(self, value):
		self.__get_instance().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#clipBottom
	def _get_clipBottom(self):
		return wrap(self.__get_instance().clipBottom)
	def _set_clipBottom(self, value):
		self.__get_instance().clipBottom = unwrap(value)
	clipBottom = property(_get_clipBottom, _set_clipBottom)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#unicodeBidi
	def _get_unicodeBidi(self):
		return wrap(self.__get_instance().unicodeBidi)
	def _set_unicodeBidi(self, value):
		self.__get_instance().unicodeBidi = unwrap(value)
	unicodeBidi = property(_get_unicodeBidi, _set_unicodeBidi)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#layoutGridChar
	def _get_layoutGridChar(self):
		return wrap(self.__get_instance().layoutGridChar)
	def _set_layoutGridChar(self, value):
		self.__get_instance().layoutGridChar = unwrap(value)
	layoutGridChar = property(_get_layoutGridChar, _set_layoutGridChar)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#textAutospace
	def _get_textAutospace(self):
		return wrap(self.__get_instance().textAutospace)
	def _set_textAutospace(self, value):
		self.__get_instance().textAutospace = unwrap(value)
	textAutospace = property(_get_textAutospace, _set_textAutospace)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#clipTop
	def _get_clipTop(self):
		return wrap(self.__get_instance().clipTop)
	def _set_clipTop(self, value):
		self.__get_instance().clipTop = unwrap(value)
	clipTop = property(_get_clipTop, _set_clipTop)

	#textJustifyTrim
	def _get_textJustifyTrim(self):
		return wrap(self.__get_instance().textJustifyTrim)
	def _set_textJustifyTrim(self, value):
		self.__get_instance().textJustifyTrim = unwrap(value)
	textJustifyTrim = property(_get_textJustifyTrim, _set_textJustifyTrim)

	#color
	def _get_color(self):
		return wrap(self.__get_instance().color)
	def _set_color(self, value):
		self.__get_instance().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#top
	def _get_top(self):
		return wrap(self.__get_instance().top)
	def _set_top(self, value):
		self.__get_instance().top = unwrap(value)
	top = property(_get_top, _set_top)

	#rubyAlign
	def _get_rubyAlign(self):
		return wrap(self.__get_instance().rubyAlign)
	def _set_rubyAlign(self, value):
		self.__get_instance().rubyAlign = unwrap(value)
	rubyAlign = property(_get_rubyAlign, _set_rubyAlign)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#textKashida
	def _get_textKashida(self):
		return wrap(self.__get_instance().textKashida)
	def _set_textKashida(self, value):
		self.__get_instance().textKashida = unwrap(value)
	textKashida = property(_get_textKashida, _set_textKashida)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#direction
	def _get_direction(self):
		return wrap(self.__get_instance().direction)
	def _set_direction(self, value):
		self.__get_instance().direction = unwrap(value)
	direction = property(_get_direction, _set_direction)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance().visibility)
	def _set_visibility(self, value):
		self.__get_instance().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance().padding)
	def _set_padding(self, value):
		self.__get_instance().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance().overflow)
	def _set_overflow(self, value):
		self.__get_instance().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#wordBreak
	def _get_wordBreak(self):
		return wrap(self.__get_instance().wordBreak)
	def _set_wordBreak(self, value):
		self.__get_instance().wordBreak = unwrap(value)
	wordBreak = property(_get_wordBreak, _set_wordBreak)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance().cursor)
	def _set_cursor(self, value):
		self.__get_instance().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#behavior
	def _get_behavior(self):
		return wrap(self.__get_instance().behavior)
	def _set_behavior(self, value):
		self.__get_instance().behavior = unwrap(value)
	behavior = property(_get_behavior, _set_behavior)

	#clipLeft
	def _get_clipLeft(self):
		return wrap(self.__get_instance().clipLeft)
	def _set_clipLeft(self, value):
		self.__get_instance().clipLeft = unwrap(value)
	clipLeft = property(_get_clipLeft, _set_clipLeft)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance().margin)
	def _set_margin(self, value):
		self.__get_instance().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance().display)
	def _set_display(self, value):
		self.__get_instance().display = unwrap(value)
	display = property(_get_display, _set_display)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#rubyOverhang
	def _get_rubyOverhang(self):
		return wrap(self.__get_instance().rubyOverhang)
	def _set_rubyOverhang(self, value):
		self.__get_instance().rubyOverhang = unwrap(value)
	rubyOverhang = property(_get_rubyOverhang, _set_rubyOverhang)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#rubyPosition
	def _get_rubyPosition(self):
		return wrap(self.__get_instance().rubyPosition)
	def _set_rubyPosition(self, value):
		self.__get_instance().rubyPosition = unwrap(value)
	rubyPosition = property(_get_rubyPosition, _set_rubyPosition)

	#blockDirection
	def _get_blockDirection(self):
		return wrap(self.__get_instance().blockDirection)
	def _set_blockDirection(self, value):
		self.__get_instance().blockDirection = unwrap(value)
	blockDirection = property(_get_blockDirection, _set_blockDirection)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#lineBreak
	def _get_lineBreak(self):
		return wrap(self.__get_instance().lineBreak)
	def _set_lineBreak(self, value):
		self.__get_instance().lineBreak = unwrap(value)
	lineBreak = property(_get_lineBreak, _set_lineBreak)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance().clear)
	def _set_clear(self, value):
		self.__get_instance().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#position
	def _get_position(self):
		return wrap(self.__get_instance().position)
	def _set_position(self, value):
		self.__get_instance().position = unwrap(value)
	position = property(_get_position, _set_position)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttribute(*args))

wrapperClasses['{3050F3DB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle
backWrapperClasses[IHTMLCurrentStyle] = '{3050F3DB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle2
#
class IHTMLCurrentStyle2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle2
		return self.__instance__.QueryInterface(kls)
	#scrollbarHighlightColor
	def _get_scrollbarHighlightColor(self):
		return wrap(self.__get_instance().scrollbarHighlightColor)
	def _set_scrollbarHighlightColor(self, value):
		self.__get_instance().scrollbarHighlightColor = unwrap(value)
	scrollbarHighlightColor = property(_get_scrollbarHighlightColor, _set_scrollbarHighlightColor)

	#isBlock
	def _get_isBlock(self):
		return wrap(self.__get_instance().isBlock)
	def _set_isBlock(self, value):
		self.__get_instance().isBlock = unwrap(value)
	isBlock = property(_get_isBlock, _set_isBlock)

	#hasLayout
	def _get_hasLayout(self):
		return wrap(self.__get_instance().hasLayout)
	def _set_hasLayout(self, value):
		self.__get_instance().hasLayout = unwrap(value)
	hasLayout = property(_get_hasLayout, _set_hasLayout)

	#zoom
	def _get_zoom(self):
		return wrap(self.__get_instance().zoom)
	def _set_zoom(self, value):
		self.__get_instance().zoom = unwrap(value)
	zoom = property(_get_zoom, _set_zoom)

	#scrollbarDarkShadowColor
	def _get_scrollbarDarkShadowColor(self):
		return wrap(self.__get_instance().scrollbarDarkShadowColor)
	def _set_scrollbarDarkShadowColor(self, value):
		self.__get_instance().scrollbarDarkShadowColor = unwrap(value)
	scrollbarDarkShadowColor = property(_get_scrollbarDarkShadowColor, _set_scrollbarDarkShadowColor)

	#writingMode
	def _get_writingMode(self):
		return wrap(self.__get_instance().writingMode)
	def _set_writingMode(self, value):
		self.__get_instance().writingMode = unwrap(value)
	writingMode = property(_get_writingMode, _set_writingMode)

	#scrollbarShadowColor
	def _get_scrollbarShadowColor(self):
		return wrap(self.__get_instance().scrollbarShadowColor)
	def _set_scrollbarShadowColor(self, value):
		self.__get_instance().scrollbarShadowColor = unwrap(value)
	scrollbarShadowColor = property(_get_scrollbarShadowColor, _set_scrollbarShadowColor)

	#scrollbarFaceColor
	def _get_scrollbarFaceColor(self):
		return wrap(self.__get_instance().scrollbarFaceColor)
	def _set_scrollbarFaceColor(self, value):
		self.__get_instance().scrollbarFaceColor = unwrap(value)
	scrollbarFaceColor = property(_get_scrollbarFaceColor, _set_scrollbarFaceColor)

	#scrollbarTrackColor
	def _get_scrollbarTrackColor(self):
		return wrap(self.__get_instance().scrollbarTrackColor)
	def _set_scrollbarTrackColor(self, value):
		self.__get_instance().scrollbarTrackColor = unwrap(value)
	scrollbarTrackColor = property(_get_scrollbarTrackColor, _set_scrollbarTrackColor)

	#scrollbar3dLightColor
	def _get_scrollbar3dLightColor(self):
		return wrap(self.__get_instance().scrollbar3dLightColor)
	def _set_scrollbar3dLightColor(self, value):
		self.__get_instance().scrollbar3dLightColor = unwrap(value)
	scrollbar3dLightColor = property(_get_scrollbar3dLightColor, _set_scrollbar3dLightColor)

	#scrollbarBaseColor
	def _get_scrollbarBaseColor(self):
		return wrap(self.__get_instance().scrollbarBaseColor)
	def _set_scrollbarBaseColor(self, value):
		self.__get_instance().scrollbarBaseColor = unwrap(value)
	scrollbarBaseColor = property(_get_scrollbarBaseColor, _set_scrollbarBaseColor)

	#scrollbarArrowColor
	def _get_scrollbarArrowColor(self):
		return wrap(self.__get_instance().scrollbarArrowColor)
	def _set_scrollbarArrowColor(self, value):
		self.__get_instance().scrollbarArrowColor = unwrap(value)
	scrollbarArrowColor = property(_get_scrollbarArrowColor, _set_scrollbarArrowColor)

	#textAlignLast
	def _get_textAlignLast(self):
		return wrap(self.__get_instance().textAlignLast)
	def _set_textAlignLast(self, value):
		self.__get_instance().textAlignLast = unwrap(value)
	textAlignLast = property(_get_textAlignLast, _set_textAlignLast)

	#wordWrap
	def _get_wordWrap(self):
		return wrap(self.__get_instance().wordWrap)
	def _set_wordWrap(self, value):
		self.__get_instance().wordWrap = unwrap(value)
	wordWrap = property(_get_wordWrap, _set_wordWrap)

	#textKashidaSpace
	def _get_textKashidaSpace(self):
		return wrap(self.__get_instance().textKashidaSpace)
	def _set_textKashidaSpace(self, value):
		self.__get_instance().textKashidaSpace = unwrap(value)
	textKashidaSpace = property(_get_textKashidaSpace, _set_textKashidaSpace)

	#layoutFlow
	def _get_layoutFlow(self):
		return wrap(self.__get_instance().layoutFlow)
	def _set_layoutFlow(self, value):
		self.__get_instance().layoutFlow = unwrap(value)
	layoutFlow = property(_get_layoutFlow, _set_layoutFlow)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance().filter)
	def _set_filter(self, value):
		self.__get_instance().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textUnderlinePosition
	def _get_textUnderlinePosition(self):
		return wrap(self.__get_instance().textUnderlinePosition)
	def _set_textUnderlinePosition(self, value):
		self.__get_instance().textUnderlinePosition = unwrap(value)
	textUnderlinePosition = property(_get_textUnderlinePosition, _set_textUnderlinePosition)

wrapperClasses['{3050F658-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle2
backWrapperClasses[IHTMLCurrentStyle2] = '{3050F658-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle3
#
class IHTMLCurrentStyle3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle3
		return self.__instance__.QueryInterface(kls)
	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#textOverflow
	def _get_textOverflow(self):
		return wrap(self.__get_instance().textOverflow)
	def _set_textOverflow(self, value):
		self.__get_instance().textOverflow = unwrap(value)
	textOverflow = property(_get_textOverflow, _set_textOverflow)

	#minHeight
	def _get_minHeight(self):
		return wrap(self.__get_instance().minHeight)
	def _set_minHeight(self, value):
		self.__get_instance().minHeight = unwrap(value)
	minHeight = property(_get_minHeight, _set_minHeight)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

wrapperClasses['{3050F818-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle3
backWrapperClasses[IHTMLCurrentStyle3] = '{3050F818-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle4
#
class IHTMLCurrentStyle4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle4
		return self.__instance__.QueryInterface(kls)
	#msInterpolationMode
	def _get_msInterpolationMode(self):
		return wrap(self.__get_instance().msInterpolationMode)
	def _set_msInterpolationMode(self, value):
		self.__get_instance().msInterpolationMode = unwrap(value)
	msInterpolationMode = property(_get_msInterpolationMode, _set_msInterpolationMode)

	#minWidth
	def _get_minWidth(self):
		return wrap(self.__get_instance().minWidth)
	def _set_minWidth(self, value):
		self.__get_instance().minWidth = unwrap(value)
	minWidth = property(_get_minWidth, _set_minWidth)

	#maxWidth
	def _get_maxWidth(self):
		return wrap(self.__get_instance().maxWidth)
	def _set_maxWidth(self, value):
		self.__get_instance().maxWidth = unwrap(value)
	maxWidth = property(_get_maxWidth, _set_maxWidth)

	#maxHeight
	def _get_maxHeight(self):
		return wrap(self.__get_instance().maxHeight)
	def _set_maxHeight(self, value):
		self.__get_instance().maxHeight = unwrap(value)
	maxHeight = property(_get_maxHeight, _set_maxHeight)

wrapperClasses['{3050F33B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle4
backWrapperClasses[IHTMLCurrentStyle4] = '{3050F33B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLCurrentStyle
#
class DispHTMLCurrentStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLCurrentStyle
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F557-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLCurrentStyle
backWrapperClasses[DispHTMLCurrentStyle] = '{3050F557-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRect
#
class IHTMLRect(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRect
		return self.__instance__.QueryInterface(kls)
	#top
	def _get_top(self):
		return wrap(self.__get_instance().top)
	def _set_top(self, value):
		self.__get_instance().top = unwrap(value)
	top = property(_get_top, _set_top)

	#right
	def _get_right(self):
		return wrap(self.__get_instance().right)
	def _set_right(self, value):
		self.__get_instance().right = unwrap(value)
	right = property(_get_right, _set_right)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance().bottom)
	def _set_bottom(self, value):
		self.__get_instance().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#left
	def _get_left(self):
		return wrap(self.__get_instance().left)
	def _set_left(self, value):
		self.__get_instance().left = unwrap(value)
	left = property(_get_left, _set_left)

wrapperClasses['{3050F4A3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRect
backWrapperClasses[IHTMLRect] = '{3050F4A3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRectCollection
#
class IHTMLRectCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRectCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F4A4-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRectCollection
backWrapperClasses[IHTMLRectCollection] = '{3050F4A4-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMNode
#
class IHTMLDOMNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMNode
		return self.__instance__.QueryInterface(kls)
	#lastChild
	def _get_lastChild(self):
		return wrap(self.__get_instance().lastChild)
	def _set_lastChild(self, value):
		self.__get_instance().lastChild = unwrap(value)
	lastChild = property(_get_lastChild, _set_lastChild)

	#nodeType
	def _get_nodeType(self):
		return wrap(self.__get_instance().nodeType)
	def _set_nodeType(self, value):
		self.__get_instance().nodeType = unwrap(value)
	nodeType = property(_get_nodeType, _set_nodeType)

	#nodeName
	def _get_nodeName(self):
		return wrap(self.__get_instance().nodeName)
	def _set_nodeName(self, value):
		self.__get_instance().nodeName = unwrap(value)
	nodeName = property(_get_nodeName, _set_nodeName)

	#nextSibling
	def _get_nextSibling(self):
		return wrap(self.__get_instance().nextSibling)
	def _set_nextSibling(self, value):
		self.__get_instance().nextSibling = unwrap(value)
	nextSibling = property(_get_nextSibling, _set_nextSibling)

	#nodeValue
	def _get_nodeValue(self):
		return wrap(self.__get_instance().nodeValue)
	def _set_nodeValue(self, value):
		self.__get_instance().nodeValue = unwrap(value)
	nodeValue = property(_get_nodeValue, _set_nodeValue)

	#firstChild
	def _get_firstChild(self):
		return wrap(self.__get_instance().firstChild)
	def _set_firstChild(self, value):
		self.__get_instance().firstChild = unwrap(value)
	firstChild = property(_get_firstChild, _set_firstChild)

	#parentNode
	def _get_parentNode(self):
		return wrap(self.__get_instance().parentNode)
	def _set_parentNode(self, value):
		self.__get_instance().parentNode = unwrap(value)
	parentNode = property(_get_parentNode, _set_parentNode)

	#attributes
	def _get_attributes(self):
		return wrap(self.__get_instance().attributes)
	def _set_attributes(self, value):
		self.__get_instance().attributes = unwrap(value)
	attributes = property(_get_attributes, _set_attributes)

	#childNodes
	def _get_childNodes(self):
		return wrap(self.__get_instance().childNodes)
	def _set_childNodes(self, value):
		self.__get_instance().childNodes = unwrap(value)
	childNodes = property(_get_childNodes, _set_childNodes)

	#previousSibling
	def _get_previousSibling(self):
		return wrap(self.__get_instance().previousSibling)
	def _set_previousSibling(self, value):
		self.__get_instance().previousSibling = unwrap(value)
	previousSibling = property(_get_previousSibling, _set_previousSibling)

	#appendChild
	def appendChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().appendChild(*args))

	#insertBefore
	def insertBefore(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertBefore(*args))

	#removeNode
	def removeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeNode(*args))

	#replaceNode
	def replaceNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replaceNode(*args))

	#swapNode
	def swapNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().swapNode(*args))

	#cloneNode
	def cloneNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().cloneNode(*args))

	#removeChild
	def removeChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeChild(*args))

	#hasChildNodes
	def hasChildNodes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().hasChildNodes(*args))

	#replaceChild
	def replaceChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replaceChild(*args))

wrapperClasses['{3050F5DA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMNode
backWrapperClasses[IHTMLDOMNode] = '{3050F5DA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMNode2
#
class IHTMLDOMNode2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMNode2
		return self.__instance__.QueryInterface(kls)
	#ownerDocument
	def _get_ownerDocument(self):
		return wrap(self.__get_instance().ownerDocument)
	def _set_ownerDocument(self, value):
		self.__get_instance().ownerDocument = unwrap(value)
	ownerDocument = property(_get_ownerDocument, _set_ownerDocument)

wrapperClasses['{3050F80B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMNode2
backWrapperClasses[IHTMLDOMNode2] = '{3050F80B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMAttribute
#
class IHTMLDOMAttribute(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMAttribute
		return self.__instance__.QueryInterface(kls)
	#nodeName
	def _get_nodeName(self):
		return wrap(self.__get_instance().nodeName)
	def _set_nodeName(self, value):
		self.__get_instance().nodeName = unwrap(value)
	nodeName = property(_get_nodeName, _set_nodeName)

	#nodeValue
	def _get_nodeValue(self):
		return wrap(self.__get_instance().nodeValue)
	def _set_nodeValue(self, value):
		self.__get_instance().nodeValue = unwrap(value)
	nodeValue = property(_get_nodeValue, _set_nodeValue)

	#specified
	def _get_specified(self):
		return wrap(self.__get_instance().specified)
	def _set_specified(self, value):
		self.__get_instance().specified = unwrap(value)
	specified = property(_get_specified, _set_specified)

wrapperClasses['{3050F4B0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMAttribute
backWrapperClasses[IHTMLDOMAttribute] = '{3050F4B0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMTextNode
#
class IHTMLDOMTextNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMTextNode
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#data
	def _get_data(self):
		return wrap(self.__get_instance().data)
	def _set_data(self, value):
		self.__get_instance().data = unwrap(value)
	data = property(_get_data, _set_data)

	#splitText
	def splitText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().splitText(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

wrapperClasses['{3050F4B1-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMTextNode
backWrapperClasses[IHTMLDOMTextNode] = '{3050F4B1-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMTextNode2
#
class IHTMLDOMTextNode2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMTextNode2
		return self.__instance__.QueryInterface(kls)
	#appendData
	def appendData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().appendData(*args))

	#deleteData
	def deleteData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteData(*args))

	#substringData
	def substringData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().substringData(*args))

	#insertData
	def insertData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertData(*args))

	#replaceData
	def replaceData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replaceData(*args))

wrapperClasses['{3050F809-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMTextNode2
backWrapperClasses[IHTMLDOMTextNode2] = '{3050F809-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMImplementation
#
class IHTMLDOMImplementation(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMImplementation
		return self.__instance__.QueryInterface(kls)
	#hasFeature
	def hasFeature(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().hasFeature(*args))

wrapperClasses['{3050F80D-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMImplementation
backWrapperClasses[IHTMLDOMImplementation] = '{3050F80D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLDOMTextNode
#
class DispHTMLDOMTextNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLDOMTextNode
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F565-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLDOMTextNode
backWrapperClasses[DispHTMLDOMTextNode] = '{3050F565-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMChildrenCollection
#
class IHTMLDOMChildrenCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMChildrenCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F5AB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMChildrenCollection
backWrapperClasses[IHTMLDOMChildrenCollection] = '{3050F5AB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispDOMChildrenCollection
#
class DispDOMChildrenCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispDOMChildrenCollection
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F577-98B5-11CF-BB82-00AA00BDCE0B}'] = DispDOMChildrenCollection
backWrapperClasses[DispDOMChildrenCollection] = '{3050F577-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement
#
class IHTMLElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement
		return self.__instance__.QueryInterface(kls)
	#all
	def _get_all(self):
		return wrap(self.__get_instance().all)
	def _set_all(self, value):
		self.__get_instance().all = unwrap(value)
	all = property(_get_all, _set_all)

	#onrowexit
	def _get_onrowexit(self):
		return wrap(self.__get_instance().onrowexit)
	def _set_onrowexit(self, value):
		self.__get_instance().onrowexit = unwrap(value)
	onrowexit = property(_get_onrowexit, _set_onrowexit)

	#parentElement
	def _get_parentElement(self):
		return wrap(self.__get_instance().parentElement)
	def _set_parentElement(self, value):
		self.__get_instance().parentElement = unwrap(value)
	parentElement = property(_get_parentElement, _set_parentElement)

	#onafterupdate
	def _get_onafterupdate(self):
		return wrap(self.__get_instance().onafterupdate)
	def _set_onafterupdate(self, value):
		self.__get_instance().onafterupdate = unwrap(value)
	onafterupdate = property(_get_onafterupdate, _set_onafterupdate)

	#innerHTML
	def _get_innerHTML(self):
		return wrap(self.__get_instance().innerHTML)
	def _set_innerHTML(self, value):
		self.__get_instance().innerHTML = unwrap(value)
	innerHTML = property(_get_innerHTML, _set_innerHTML)

	#onmousedown
	def _get_onmousedown(self):
		return wrap(self.__get_instance().onmousedown)
	def _set_onmousedown(self, value):
		self.__get_instance().onmousedown = unwrap(value)
	onmousedown = property(_get_onmousedown, _set_onmousedown)

	#outerHTML
	def _get_outerHTML(self):
		return wrap(self.__get_instance().outerHTML)
	def _set_outerHTML(self, value):
		self.__get_instance().outerHTML = unwrap(value)
	outerHTML = property(_get_outerHTML, _set_outerHTML)

	#tagName
	def _get_tagName(self):
		return wrap(self.__get_instance().tagName)
	def _set_tagName(self, value):
		self.__get_instance().tagName = unwrap(value)
	tagName = property(_get_tagName, _set_tagName)

	#offsetHeight
	def _get_offsetHeight(self):
		return wrap(self.__get_instance().offsetHeight)
	def _set_offsetHeight(self, value):
		self.__get_instance().offsetHeight = unwrap(value)
	offsetHeight = property(_get_offsetHeight, _set_offsetHeight)

	#onerrorupdate
	def _get_onerrorupdate(self):
		return wrap(self.__get_instance().onerrorupdate)
	def _set_onerrorupdate(self, value):
		self.__get_instance().onerrorupdate = unwrap(value)
	onerrorupdate = property(_get_onerrorupdate, _set_onerrorupdate)

	#onfilterchange
	def _get_onfilterchange(self):
		return wrap(self.__get_instance().onfilterchange)
	def _set_onfilterchange(self, value):
		self.__get_instance().onfilterchange = unwrap(value)
	onfilterchange = property(_get_onfilterchange, _set_onfilterchange)

	#id
	def _get_id(self):
		return wrap(self.__get_instance().id)
	def _set_id(self, value):
		self.__get_instance().id = unwrap(value)
	id = property(_get_id, _set_id)

	#offsetParent
	def _get_offsetParent(self):
		return wrap(self.__get_instance().offsetParent)
	def _set_offsetParent(self, value):
		self.__get_instance().offsetParent = unwrap(value)
	offsetParent = property(_get_offsetParent, _set_offsetParent)

	#style
	def _get_style(self):
		return wrap(self.__get_instance().style)
	def _set_style(self, value):
		self.__get_instance().style = unwrap(value)
	style = property(_get_style, _set_style)

	#ondataavailable
	def _get_ondataavailable(self):
		return wrap(self.__get_instance().ondataavailable)
	def _set_ondataavailable(self, value):
		self.__get_instance().ondataavailable = unwrap(value)
	ondataavailable = property(_get_ondataavailable, _set_ondataavailable)

	#title
	def _get_title(self):
		return wrap(self.__get_instance().title)
	def _set_title(self, value):
		self.__get_instance().title = unwrap(value)
	title = property(_get_title, _set_title)

	#filters
	def _get_filters(self):
		return wrap(self.__get_instance().filters)
	def _set_filters(self, value):
		self.__get_instance().filters = unwrap(value)
	filters = property(_get_filters, _set_filters)

	#isTextEdit
	def _get_isTextEdit(self):
		return wrap(self.__get_instance().isTextEdit)
	def _set_isTextEdit(self, value):
		self.__get_instance().isTextEdit = unwrap(value)
	isTextEdit = property(_get_isTextEdit, _set_isTextEdit)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#children
	def _get_children(self):
		return wrap(self.__get_instance().children)
	def _set_children(self, value):
		self.__get_instance().children = unwrap(value)
	children = property(_get_children, _set_children)

	#onmousemove
	def _get_onmousemove(self):
		return wrap(self.__get_instance().onmousemove)
	def _set_onmousemove(self, value):
		self.__get_instance().onmousemove = unwrap(value)
	onmousemove = property(_get_onmousemove, _set_onmousemove)

	#ondatasetcomplete
	def _get_ondatasetcomplete(self):
		return wrap(self.__get_instance().ondatasetcomplete)
	def _set_ondatasetcomplete(self, value):
		self.__get_instance().ondatasetcomplete = unwrap(value)
	ondatasetcomplete = property(_get_ondatasetcomplete, _set_ondatasetcomplete)

	#onclick
	def _get_onclick(self):
		return wrap(self.__get_instance().onclick)
	def _set_onclick(self, value):
		self.__get_instance().onclick = unwrap(value)
	onclick = property(_get_onclick, _set_onclick)

	#offsetTop
	def _get_offsetTop(self):
		return wrap(self.__get_instance().offsetTop)
	def _set_offsetTop(self, value):
		self.__get_instance().offsetTop = unwrap(value)
	offsetTop = property(_get_offsetTop, _set_offsetTop)

	#offsetLeft
	def _get_offsetLeft(self):
		return wrap(self.__get_instance().offsetLeft)
	def _set_offsetLeft(self, value):
		self.__get_instance().offsetLeft = unwrap(value)
	offsetLeft = property(_get_offsetLeft, _set_offsetLeft)

	#document
	def _get_document(self):
		return wrap(self.__get_instance().document)
	def _set_document(self, value):
		self.__get_instance().document = unwrap(value)
	document = property(_get_document, _set_document)

	#ondragstart
	def _get_ondragstart(self):
		return wrap(self.__get_instance().ondragstart)
	def _set_ondragstart(self, value):
		self.__get_instance().ondragstart = unwrap(value)
	ondragstart = property(_get_ondragstart, _set_ondragstart)

	#onmouseup
	def _get_onmouseup(self):
		return wrap(self.__get_instance().onmouseup)
	def _set_onmouseup(self, value):
		self.__get_instance().onmouseup = unwrap(value)
	onmouseup = property(_get_onmouseup, _set_onmouseup)

	#onmouseout
	def _get_onmouseout(self):
		return wrap(self.__get_instance().onmouseout)
	def _set_onmouseout(self, value):
		self.__get_instance().onmouseout = unwrap(value)
	onmouseout = property(_get_onmouseout, _set_onmouseout)

	#onkeypress
	def _get_onkeypress(self):
		return wrap(self.__get_instance().onkeypress)
	def _set_onkeypress(self, value):
		self.__get_instance().onkeypress = unwrap(value)
	onkeypress = property(_get_onkeypress, _set_onkeypress)

	#onbeforeupdate
	def _get_onbeforeupdate(self):
		return wrap(self.__get_instance().onbeforeupdate)
	def _set_onbeforeupdate(self, value):
		self.__get_instance().onbeforeupdate = unwrap(value)
	onbeforeupdate = property(_get_onbeforeupdate, _set_onbeforeupdate)

	#onkeydown
	def _get_onkeydown(self):
		return wrap(self.__get_instance().onkeydown)
	def _set_onkeydown(self, value):
		self.__get_instance().onkeydown = unwrap(value)
	onkeydown = property(_get_onkeydown, _set_onkeydown)

	#onmouseover
	def _get_onmouseover(self):
		return wrap(self.__get_instance().onmouseover)
	def _set_onmouseover(self, value):
		self.__get_instance().onmouseover = unwrap(value)
	onmouseover = property(_get_onmouseover, _set_onmouseover)

	#parentTextEdit
	def _get_parentTextEdit(self):
		return wrap(self.__get_instance().parentTextEdit)
	def _set_parentTextEdit(self, value):
		self.__get_instance().parentTextEdit = unwrap(value)
	parentTextEdit = property(_get_parentTextEdit, _set_parentTextEdit)

	#recordNumber
	def _get_recordNumber(self):
		return wrap(self.__get_instance().recordNumber)
	def _set_recordNumber(self, value):
		self.__get_instance().recordNumber = unwrap(value)
	recordNumber = property(_get_recordNumber, _set_recordNumber)

	#lang
	def _get_lang(self):
		return wrap(self.__get_instance().lang)
	def _set_lang(self, value):
		self.__get_instance().lang = unwrap(value)
	lang = property(_get_lang, _set_lang)

	#onrowenter
	def _get_onrowenter(self):
		return wrap(self.__get_instance().onrowenter)
	def _set_onrowenter(self, value):
		self.__get_instance().onrowenter = unwrap(value)
	onrowenter = property(_get_onrowenter, _set_onrowenter)

	#language
	def _get_language(self):
		return wrap(self.__get_instance().language)
	def _set_language(self, value):
		self.__get_instance().language = unwrap(value)
	language = property(_get_language, _set_language)

	#offsetWidth
	def _get_offsetWidth(self):
		return wrap(self.__get_instance().offsetWidth)
	def _set_offsetWidth(self, value):
		self.__get_instance().offsetWidth = unwrap(value)
	offsetWidth = property(_get_offsetWidth, _set_offsetWidth)

	#ondatasetchanged
	def _get_ondatasetchanged(self):
		return wrap(self.__get_instance().ondatasetchanged)
	def _set_ondatasetchanged(self, value):
		self.__get_instance().ondatasetchanged = unwrap(value)
	ondatasetchanged = property(_get_ondatasetchanged, _set_ondatasetchanged)

	#className
	def _get_className(self):
		return wrap(self.__get_instance().className)
	def _set_className(self, value):
		self.__get_instance().className = unwrap(value)
	className = property(_get_className, _set_className)

	#sourceIndex
	def _get_sourceIndex(self):
		return wrap(self.__get_instance().sourceIndex)
	def _set_sourceIndex(self, value):
		self.__get_instance().sourceIndex = unwrap(value)
	sourceIndex = property(_get_sourceIndex, _set_sourceIndex)

	#innerText
	def _get_innerText(self):
		return wrap(self.__get_instance().innerText)
	def _set_innerText(self, value):
		self.__get_instance().innerText = unwrap(value)
	innerText = property(_get_innerText, _set_innerText)

	#onkeyup
	def _get_onkeyup(self):
		return wrap(self.__get_instance().onkeyup)
	def _set_onkeyup(self, value):
		self.__get_instance().onkeyup = unwrap(value)
	onkeyup = property(_get_onkeyup, _set_onkeyup)

	#ondblclick
	def _get_ondblclick(self):
		return wrap(self.__get_instance().ondblclick)
	def _set_ondblclick(self, value):
		self.__get_instance().ondblclick = unwrap(value)
	ondblclick = property(_get_ondblclick, _set_ondblclick)

	#onselectstart
	def _get_onselectstart(self):
		return wrap(self.__get_instance().onselectstart)
	def _set_onselectstart(self, value):
		self.__get_instance().onselectstart = unwrap(value)
	onselectstart = property(_get_onselectstart, _set_onselectstart)

	#outerText
	def _get_outerText(self):
		return wrap(self.__get_instance().outerText)
	def _set_outerText(self, value):
		self.__get_instance().outerText = unwrap(value)
	outerText = property(_get_outerText, _set_outerText)

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeAttribute(*args))

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttribute(*args))

	#insertAdjacentText
	def insertAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertAdjacentText(*args))

	#contains
	def contains(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().contains(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setAttribute(*args))

	#scrollIntoView
	def scrollIntoView(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().scrollIntoView(*args))

	#insertAdjacentHTML
	def insertAdjacentHTML(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertAdjacentHTML(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#click
	def click(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().click(*args))

wrapperClasses['{3050F1FF-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement
backWrapperClasses[IHTMLElement] = '{3050F1FF-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement2
#
class IHTMLElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement2
		return self.__instance__.QueryInterface(kls)
	#behaviorUrns
	def _get_behaviorUrns(self):
		return wrap(self.__get_instance().behaviorUrns)
	def _set_behaviorUrns(self, value):
		self.__get_instance().behaviorUrns = unwrap(value)
	behaviorUrns = property(_get_behaviorUrns, _set_behaviorUrns)

	#clientHeight
	def _get_clientHeight(self):
		return wrap(self.__get_instance().clientHeight)
	def _set_clientHeight(self, value):
		self.__get_instance().clientHeight = unwrap(value)
	clientHeight = property(_get_clientHeight, _set_clientHeight)

	#ondragenter
	def _get_ondragenter(self):
		return wrap(self.__get_instance().ondragenter)
	def _set_ondragenter(self, value):
		self.__get_instance().ondragenter = unwrap(value)
	ondragenter = property(_get_ondragenter, _set_ondragenter)

	#onrowsinserted
	def _get_onrowsinserted(self):
		return wrap(self.__get_instance().onrowsinserted)
	def _set_onrowsinserted(self, value):
		self.__get_instance().onrowsinserted = unwrap(value)
	onrowsinserted = property(_get_onrowsinserted, _set_onrowsinserted)

	#onbeforecut
	def _get_onbeforecut(self):
		return wrap(self.__get_instance().onbeforecut)
	def _set_onbeforecut(self, value):
		self.__get_instance().onbeforecut = unwrap(value)
	onbeforecut = property(_get_onbeforecut, _set_onbeforecut)

	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#clientTop
	def _get_clientTop(self):
		return wrap(self.__get_instance().clientTop)
	def _set_clientTop(self, value):
		self.__get_instance().clientTop = unwrap(value)
	clientTop = property(_get_clientTop, _set_clientTop)

	#oncopy
	def _get_oncopy(self):
		return wrap(self.__get_instance().oncopy)
	def _set_oncopy(self, value):
		self.__get_instance().oncopy = unwrap(value)
	oncopy = property(_get_oncopy, _set_oncopy)

	#onbeforepaste
	def _get_onbeforepaste(self):
		return wrap(self.__get_instance().onbeforepaste)
	def _set_onbeforepaste(self, value):
		self.__get_instance().onbeforepaste = unwrap(value)
	onbeforepaste = property(_get_onbeforepaste, _set_onbeforepaste)

	#runtimeStyle
	def _get_runtimeStyle(self):
		return wrap(self.__get_instance().runtimeStyle)
	def _set_runtimeStyle(self, value):
		self.__get_instance().runtimeStyle = unwrap(value)
	runtimeStyle = property(_get_runtimeStyle, _set_runtimeStyle)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#scrollWidth
	def _get_scrollWidth(self):
		return wrap(self.__get_instance().scrollWidth)
	def _set_scrollWidth(self, value):
		self.__get_instance().scrollWidth = unwrap(value)
	scrollWidth = property(_get_scrollWidth, _set_scrollWidth)

	#ondragover
	def _get_ondragover(self):
		return wrap(self.__get_instance().ondragover)
	def _set_ondragover(self, value):
		self.__get_instance().ondragover = unwrap(value)
	ondragover = property(_get_ondragover, _set_ondragover)

	#clientLeft
	def _get_clientLeft(self):
		return wrap(self.__get_instance().clientLeft)
	def _set_clientLeft(self, value):
		self.__get_instance().clientLeft = unwrap(value)
	clientLeft = property(_get_clientLeft, _set_clientLeft)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#oncellchange
	def _get_oncellchange(self):
		return wrap(self.__get_instance().oncellchange)
	def _set_oncellchange(self, value):
		self.__get_instance().oncellchange = unwrap(value)
	oncellchange = property(_get_oncellchange, _set_oncellchange)

	#ondragleave
	def _get_ondragleave(self):
		return wrap(self.__get_instance().ondragleave)
	def _set_ondragleave(self, value):
		self.__get_instance().ondragleave = unwrap(value)
	ondragleave = property(_get_ondragleave, _set_ondragleave)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance().onresize)
	def _set_onresize(self, value):
		self.__get_instance().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#ondrag
	def _get_ondrag(self):
		return wrap(self.__get_instance().ondrag)
	def _set_ondrag(self, value):
		self.__get_instance().ondrag = unwrap(value)
	ondrag = property(_get_ondrag, _set_ondrag)

	#currentStyle
	def _get_currentStyle(self):
		return wrap(self.__get_instance().currentStyle)
	def _set_currentStyle(self, value):
		self.__get_instance().currentStyle = unwrap(value)
	currentStyle = property(_get_currentStyle, _set_currentStyle)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance().onblur)
	def _set_onblur(self, value):
		self.__get_instance().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#ondrop
	def _get_ondrop(self):
		return wrap(self.__get_instance().ondrop)
	def _set_ondrop(self, value):
		self.__get_instance().ondrop = unwrap(value)
	ondrop = property(_get_ondrop, _set_ondrop)

	#onrowsdelete
	def _get_onrowsdelete(self):
		return wrap(self.__get_instance().onrowsdelete)
	def _set_onrowsdelete(self, value):
		self.__get_instance().onrowsdelete = unwrap(value)
	onrowsdelete = property(_get_onrowsdelete, _set_onrowsdelete)

	#onpropertychange
	def _get_onpropertychange(self):
		return wrap(self.__get_instance().onpropertychange)
	def _set_onpropertychange(self, value):
		self.__get_instance().onpropertychange = unwrap(value)
	onpropertychange = property(_get_onpropertychange, _set_onpropertychange)

	#scrollLeft
	def _get_scrollLeft(self):
		return wrap(self.__get_instance().scrollLeft)
	def _set_scrollLeft(self, value):
		self.__get_instance().scrollLeft = unwrap(value)
	scrollLeft = property(_get_scrollLeft, _set_scrollLeft)

	#onbeforeeditfocus
	def _get_onbeforeeditfocus(self):
		return wrap(self.__get_instance().onbeforeeditfocus)
	def _set_onbeforeeditfocus(self, value):
		self.__get_instance().onbeforeeditfocus = unwrap(value)
	onbeforeeditfocus = property(_get_onbeforeeditfocus, _set_onbeforeeditfocus)

	#onbeforecopy
	def _get_onbeforecopy(self):
		return wrap(self.__get_instance().onbeforecopy)
	def _set_onbeforecopy(self, value):
		self.__get_instance().onbeforecopy = unwrap(value)
	onbeforecopy = property(_get_onbeforecopy, _set_onbeforecopy)

	#onpaste
	def _get_onpaste(self):
		return wrap(self.__get_instance().onpaste)
	def _set_onpaste(self, value):
		self.__get_instance().onpaste = unwrap(value)
	onpaste = property(_get_onpaste, _set_onpaste)

	#scrollHeight
	def _get_scrollHeight(self):
		return wrap(self.__get_instance().scrollHeight)
	def _set_scrollHeight(self, value):
		self.__get_instance().scrollHeight = unwrap(value)
	scrollHeight = property(_get_scrollHeight, _set_scrollHeight)

	#oncontextmenu
	def _get_oncontextmenu(self):
		return wrap(self.__get_instance().oncontextmenu)
	def _set_oncontextmenu(self, value):
		self.__get_instance().oncontextmenu = unwrap(value)
	oncontextmenu = property(_get_oncontextmenu, _set_oncontextmenu)

	#clientWidth
	def _get_clientWidth(self):
		return wrap(self.__get_instance().clientWidth)
	def _set_clientWidth(self, value):
		self.__get_instance().clientWidth = unwrap(value)
	clientWidth = property(_get_clientWidth, _set_clientWidth)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#ondragend
	def _get_ondragend(self):
		return wrap(self.__get_instance().ondragend)
	def _set_ondragend(self, value):
		self.__get_instance().ondragend = unwrap(value)
	ondragend = property(_get_ondragend, _set_ondragend)

	#scopeName
	def _get_scopeName(self):
		return wrap(self.__get_instance().scopeName)
	def _set_scopeName(self, value):
		self.__get_instance().scopeName = unwrap(value)
	scopeName = property(_get_scopeName, _set_scopeName)

	#onlosecapture
	def _get_onlosecapture(self):
		return wrap(self.__get_instance().onlosecapture)
	def _set_onlosecapture(self, value):
		self.__get_instance().onlosecapture = unwrap(value)
	onlosecapture = property(_get_onlosecapture, _set_onlosecapture)

	#oncut
	def _get_oncut(self):
		return wrap(self.__get_instance().oncut)
	def _set_oncut(self, value):
		self.__get_instance().oncut = unwrap(value)
	oncut = property(_get_oncut, _set_oncut)

	#canHaveChildren
	def _get_canHaveChildren(self):
		return wrap(self.__get_instance().canHaveChildren)
	def _set_canHaveChildren(self, value):
		self.__get_instance().canHaveChildren = unwrap(value)
	canHaveChildren = property(_get_canHaveChildren, _set_canHaveChildren)

	#scrollTop
	def _get_scrollTop(self):
		return wrap(self.__get_instance().scrollTop)
	def _set_scrollTop(self, value):
		self.__get_instance().scrollTop = unwrap(value)
	scrollTop = property(_get_scrollTop, _set_scrollTop)

	#readyStateValue
	def _get_readyStateValue(self):
		return wrap(self.__get_instance().readyStateValue)
	def _set_readyStateValue(self, value):
		self.__get_instance().readyStateValue = unwrap(value)
	readyStateValue = property(_get_readyStateValue, _set_readyStateValue)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance().dir)
	def _set_dir(self, value):
		self.__get_instance().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#tagUrn
	def _get_tagUrn(self):
		return wrap(self.__get_instance().tagUrn)
	def _set_tagUrn(self, value):
		self.__get_instance().tagUrn = unwrap(value)
	tagUrn = property(_get_tagUrn, _set_tagUrn)

	#setCapture
	def setCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setCapture(*args))

	#releaseCapture
	def releaseCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().releaseCapture(*args))

	#replaceAdjacentText
	def replaceAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replaceAdjacentText(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().attachEvent(*args))

	#createControlRange
	def createControlRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createControlRange(*args))

	#getExpression
	def getExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getExpression(*args))

	#getBoundingClientRect
	def getBoundingClientRect(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getBoundingClientRect(*args))

	#removeExpression
	def removeExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeExpression(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().blur(*args))

	#getAdjacentText
	def getAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAdjacentText(*args))

	#clearAttributes
	def clearAttributes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clearAttributes(*args))

	#addBehavior
	def addBehavior(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addBehavior(*args))

	#getClientRects
	def getClientRects(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getClientRects(*args))

	#applyElement
	def applyElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().applyElement(*args))

	#getElementsByTagName
	def getElementsByTagName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getElementsByTagName(*args))

	#insertAdjacentElement
	def insertAdjacentElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertAdjacentElement(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().focus(*args))

	#doScroll
	def doScroll(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().doScroll(*args))

	#removeBehavior
	def removeBehavior(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeBehavior(*args))

	#setExpression
	def setExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setExpression(*args))

	#mergeAttributes
	def mergeAttributes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().mergeAttributes(*args))

	#componentFromPoint
	def componentFromPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().componentFromPoint(*args))

	#addFilter
	def addFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addFilter(*args))

	#removeFilter
	def removeFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeFilter(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().detachEvent(*args))

wrapperClasses['{3050F434-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement2
backWrapperClasses[IHTMLElement2] = '{3050F434-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement3
#
class IHTMLElement3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement3
		return self.__instance__.QueryInterface(kls)
	#contentEditable
	def _get_contentEditable(self):
		return wrap(self.__get_instance().contentEditable)
	def _set_contentEditable(self, value):
		self.__get_instance().contentEditable = unwrap(value)
	contentEditable = property(_get_contentEditable, _set_contentEditable)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#onresizestart
	def _get_onresizestart(self):
		return wrap(self.__get_instance().onresizestart)
	def _set_onresizestart(self, value):
		self.__get_instance().onresizestart = unwrap(value)
	onresizestart = property(_get_onresizestart, _set_onresizestart)

	#ondeactivate
	def _get_ondeactivate(self):
		return wrap(self.__get_instance().ondeactivate)
	def _set_ondeactivate(self, value):
		self.__get_instance().ondeactivate = unwrap(value)
	ondeactivate = property(_get_ondeactivate, _set_ondeactivate)

	#onpage
	def _get_onpage(self):
		return wrap(self.__get_instance().onpage)
	def _set_onpage(self, value):
		self.__get_instance().onpage = unwrap(value)
	onpage = property(_get_onpage, _set_onpage)

	#isDisabled
	def _get_isDisabled(self):
		return wrap(self.__get_instance().isDisabled)
	def _set_isDisabled(self, value):
		self.__get_instance().isDisabled = unwrap(value)
	isDisabled = property(_get_isDisabled, _set_isDisabled)

	#glyphMode
	def _get_glyphMode(self):
		return wrap(self.__get_instance().glyphMode)
	def _set_glyphMode(self, value):
		self.__get_instance().glyphMode = unwrap(value)
	glyphMode = property(_get_glyphMode, _set_glyphMode)

	#oncontrolselect
	def _get_oncontrolselect(self):
		return wrap(self.__get_instance().oncontrolselect)
	def _set_oncontrolselect(self, value):
		self.__get_instance().oncontrolselect = unwrap(value)
	oncontrolselect = property(_get_oncontrolselect, _set_oncontrolselect)

	#onresizeend
	def _get_onresizeend(self):
		return wrap(self.__get_instance().onresizeend)
	def _set_onresizeend(self, value):
		self.__get_instance().onresizeend = unwrap(value)
	onresizeend = property(_get_onresizeend, _set_onresizeend)

	#onmoveend
	def _get_onmoveend(self):
		return wrap(self.__get_instance().onmoveend)
	def _set_onmoveend(self, value):
		self.__get_instance().onmoveend = unwrap(value)
	onmoveend = property(_get_onmoveend, _set_onmoveend)

	#isMultiLine
	def _get_isMultiLine(self):
		return wrap(self.__get_instance().isMultiLine)
	def _set_isMultiLine(self, value):
		self.__get_instance().isMultiLine = unwrap(value)
	isMultiLine = property(_get_isMultiLine, _set_isMultiLine)

	#hideFocus
	def _get_hideFocus(self):
		return wrap(self.__get_instance().hideFocus)
	def _set_hideFocus(self, value):
		self.__get_instance().hideFocus = unwrap(value)
	hideFocus = property(_get_hideFocus, _set_hideFocus)

	#isContentEditable
	def _get_isContentEditable(self):
		return wrap(self.__get_instance().isContentEditable)
	def _set_isContentEditable(self, value):
		self.__get_instance().isContentEditable = unwrap(value)
	isContentEditable = property(_get_isContentEditable, _set_isContentEditable)

	#onactivate
	def _get_onactivate(self):
		return wrap(self.__get_instance().onactivate)
	def _set_onactivate(self, value):
		self.__get_instance().onactivate = unwrap(value)
	onactivate = property(_get_onactivate, _set_onactivate)

	#onmouseleave
	def _get_onmouseleave(self):
		return wrap(self.__get_instance().onmouseleave)
	def _set_onmouseleave(self, value):
		self.__get_instance().onmouseleave = unwrap(value)
	onmouseleave = property(_get_onmouseleave, _set_onmouseleave)

	#inflateBlock
	def _get_inflateBlock(self):
		return wrap(self.__get_instance().inflateBlock)
	def _set_inflateBlock(self, value):
		self.__get_instance().inflateBlock = unwrap(value)
	inflateBlock = property(_get_inflateBlock, _set_inflateBlock)

	#canHaveHTML
	def _get_canHaveHTML(self):
		return wrap(self.__get_instance().canHaveHTML)
	def _set_canHaveHTML(self, value):
		self.__get_instance().canHaveHTML = unwrap(value)
	canHaveHTML = property(_get_canHaveHTML, _set_canHaveHTML)

	#onmouseenter
	def _get_onmouseenter(self):
		return wrap(self.__get_instance().onmouseenter)
	def _set_onmouseenter(self, value):
		self.__get_instance().onmouseenter = unwrap(value)
	onmouseenter = property(_get_onmouseenter, _set_onmouseenter)

	#onlayoutcomplete
	def _get_onlayoutcomplete(self):
		return wrap(self.__get_instance().onlayoutcomplete)
	def _set_onlayoutcomplete(self, value):
		self.__get_instance().onlayoutcomplete = unwrap(value)
	onlayoutcomplete = property(_get_onlayoutcomplete, _set_onlayoutcomplete)

	#onbeforedeactivate
	def _get_onbeforedeactivate(self):
		return wrap(self.__get_instance().onbeforedeactivate)
	def _set_onbeforedeactivate(self, value):
		self.__get_instance().onbeforedeactivate = unwrap(value)
	onbeforedeactivate = property(_get_onbeforedeactivate, _set_onbeforedeactivate)

	#onmovestart
	def _get_onmovestart(self):
		return wrap(self.__get_instance().onmovestart)
	def _set_onmovestart(self, value):
		self.__get_instance().onmovestart = unwrap(value)
	onmovestart = property(_get_onmovestart, _set_onmovestart)

	#onmove
	def _get_onmove(self):
		return wrap(self.__get_instance().onmove)
	def _set_onmove(self, value):
		self.__get_instance().onmove = unwrap(value)
	onmove = property(_get_onmove, _set_onmove)

	#fireEvent
	def fireEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().fireEvent(*args))

wrapperClasses['{3050F673-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement3
backWrapperClasses[IHTMLElement3] = '{3050F673-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement4
#
class IHTMLElement4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement4
		return self.__instance__.QueryInterface(kls)
	#onfocusout
	def _get_onfocusout(self):
		return wrap(self.__get_instance().onfocusout)
	def _set_onfocusout(self, value):
		self.__get_instance().onfocusout = unwrap(value)
	onfocusout = property(_get_onfocusout, _set_onfocusout)

	#onmousewheel
	def _get_onmousewheel(self):
		return wrap(self.__get_instance().onmousewheel)
	def _set_onmousewheel(self, value):
		self.__get_instance().onmousewheel = unwrap(value)
	onmousewheel = property(_get_onmousewheel, _set_onmousewheel)

	#onfocusin
	def _get_onfocusin(self):
		return wrap(self.__get_instance().onfocusin)
	def _set_onfocusin(self, value):
		self.__get_instance().onfocusin = unwrap(value)
	onfocusin = property(_get_onfocusin, _set_onfocusin)

	#onbeforeactivate
	def _get_onbeforeactivate(self):
		return wrap(self.__get_instance().onbeforeactivate)
	def _set_onbeforeactivate(self, value):
		self.__get_instance().onbeforeactivate = unwrap(value)
	onbeforeactivate = property(_get_onbeforeactivate, _set_onbeforeactivate)

	#normalize
	def normalize(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().normalize(*args))

	#getAttributeNode
	def getAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttributeNode(*args))

	#setAttributeNode
	def setAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setAttributeNode(*args))

	#removeAttributeNode
	def removeAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeAttributeNode(*args))

wrapperClasses['{3050F80F-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement4
backWrapperClasses[IHTMLElement4] = '{3050F80F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLGenericElement
#
class IHTMLGenericElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLGenericElement
		return self.__instance__.QueryInterface(kls)
	#recordset
	def _get_recordset(self):
		return wrap(self.__get_instance().recordset)
	def _set_recordset(self, value):
		self.__get_instance().recordset = unwrap(value)
	recordset = property(_get_recordset, _set_recordset)

	#namedRecordset
	def namedRecordset(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().namedRecordset(*args))

wrapperClasses['{3050F4B7-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLGenericElement
backWrapperClasses[IHTMLGenericElement] = '{3050F4B7-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLGenericElement
#
class DispHTMLGenericElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLGenericElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F563-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLGenericElement
backWrapperClasses[DispHTMLGenericElement] = '{3050F563-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetRule
#
class IHTMLStyleSheetRule(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetRule
		return self.__instance__.QueryInterface(kls)
	#style
	def _get_style(self):
		return wrap(self.__get_instance().style)
	def _set_style(self, value):
		self.__get_instance().style = unwrap(value)
	style = property(_get_style, _set_style)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#selectorText
	def _get_selectorText(self):
		return wrap(self.__get_instance().selectorText)
	def _set_selectorText(self, value):
		self.__get_instance().selectorText = unwrap(value)
	selectorText = property(_get_selectorText, _set_selectorText)

wrapperClasses['{3050F357-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetRule
backWrapperClasses[IHTMLStyleSheetRule] = '{3050F357-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetRulesCollection
#
class IHTMLStyleSheetRulesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetRulesCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F2E5-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetRulesCollection
backWrapperClasses[IHTMLStyleSheetRulesCollection] = '{3050F2E5-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetPage
#
class IHTMLStyleSheetPage(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetPage
		return self.__instance__.QueryInterface(kls)
	#pseudoClass
	def _get_pseudoClass(self):
		return wrap(self.__get_instance().pseudoClass)
	def _set_pseudoClass(self, value):
		self.__get_instance().pseudoClass = unwrap(value)
	pseudoClass = property(_get_pseudoClass, _set_pseudoClass)

	#selector
	def _get_selector(self):
		return wrap(self.__get_instance().selector)
	def _set_selector(self, value):
		self.__get_instance().selector = unwrap(value)
	selector = property(_get_selector, _set_selector)

wrapperClasses['{3050F7EE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetPage
backWrapperClasses[IHTMLStyleSheetPage] = '{3050F7EE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetPagesCollection
#
class IHTMLStyleSheetPagesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetPagesCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F7F0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetPagesCollection
backWrapperClasses[IHTMLStyleSheetPagesCollection] = '{3050F7F0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheet
#
class IHTMLStyleSheet(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheet
		return self.__instance__.QueryInterface(kls)
	#title
	def _get_title(self):
		return wrap(self.__get_instance().title)
	def _set_title(self, value):
		self.__get_instance().title = unwrap(value)
	title = property(_get_title, _set_title)

	#parentStyleSheet
	def _get_parentStyleSheet(self):
		return wrap(self.__get_instance().parentStyleSheet)
	def _set_parentStyleSheet(self, value):
		self.__get_instance().parentStyleSheet = unwrap(value)
	parentStyleSheet = property(_get_parentStyleSheet, _set_parentStyleSheet)

	#imports
	def _get_imports(self):
		return wrap(self.__get_instance().imports)
	def _set_imports(self, value):
		self.__get_instance().imports = unwrap(value)
	imports = property(_get_imports, _set_imports)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance().cssText)
	def _set_cssText(self, value):
		self.__get_instance().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#owningElement
	def _get_owningElement(self):
		return wrap(self.__get_instance().owningElement)
	def _set_owningElement(self, value):
		self.__get_instance().owningElement = unwrap(value)
	owningElement = property(_get_owningElement, _set_owningElement)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#rules
	def _get_rules(self):
		return wrap(self.__get_instance().rules)
	def _set_rules(self, value):
		self.__get_instance().rules = unwrap(value)
	rules = property(_get_rules, _set_rules)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#href
	def _get_href(self):
		return wrap(self.__get_instance().href)
	def _set_href(self, value):
		self.__get_instance().href = unwrap(value)
	href = property(_get_href, _set_href)

	#media
	def _get_media(self):
		return wrap(self.__get_instance().media)
	def _set_media(self, value):
		self.__get_instance().media = unwrap(value)
	media = property(_get_media, _set_media)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#id
	def _get_id(self):
		return wrap(self.__get_instance().id)
	def _set_id(self, value):
		self.__get_instance().id = unwrap(value)
	id = property(_get_id, _set_id)

	#addRule
	def addRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addRule(*args))

	#removeRule
	def removeRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeRule(*args))

	#removeImport
	def removeImport(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeImport(*args))

	#addImport
	def addImport(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addImport(*args))

wrapperClasses['{3050F2E3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheet
backWrapperClasses[IHTMLStyleSheet] = '{3050F2E3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheet2
#
class IHTMLStyleSheet2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheet2
		return self.__instance__.QueryInterface(kls)
	#pages
	def _get_pages(self):
		return wrap(self.__get_instance().pages)
	def _set_pages(self, value):
		self.__get_instance().pages = unwrap(value)
	pages = property(_get_pages, _set_pages)

	#addPageRule
	def addPageRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addPageRule(*args))

wrapperClasses['{3050F3D1-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheet2
backWrapperClasses[IHTMLStyleSheet2] = '{3050F3D1-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLStyleSheet
#
class DispHTMLStyleSheet(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLStyleSheet
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F58D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLStyleSheet
backWrapperClasses[DispHTMLStyleSheet] = '{3050F58D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetsCollection
#
class IHTMLStyleSheetsCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetsCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F37E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetsCollection
backWrapperClasses[IHTMLStyleSheetsCollection] = '{3050F37E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTxtRange
#
class IHTMLTxtRange(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTxtRange
		return self.__instance__.QueryInterface(kls)
	#text
	def _get_text(self):
		return wrap(self.__get_instance().text)
	def _set_text(self, value):
		self.__get_instance().text = unwrap(value)
	text = property(_get_text, _set_text)

	#htmlText
	def _get_htmlText(self):
		return wrap(self.__get_instance().htmlText)
	def _set_htmlText(self, value):
		self.__get_instance().htmlText = unwrap(value)
	htmlText = property(_get_htmlText, _set_htmlText)

	#moveStart
	def moveStart(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveStart(*args))

	#parentElement
	def parentElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().parentElement(*args))

	#move
	def move(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().move(*args))

	#findText
	def findText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().findText(*args))

	#getBookmark
	def getBookmark(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getBookmark(*args))

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().select(*args))

	#setEndPoint
	def setEndPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setEndPoint(*args))

	#moveEnd
	def moveEnd(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveEnd(*args))

	#execCommandShowHelp
	def execCommandShowHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().execCommandShowHelp(*args))

	#duplicate
	def duplicate(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().duplicate(*args))

	#expand
	def expand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().expand(*args))

	#inRange
	def inRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().inRange(*args))

	#queryCommandIndeterm
	def queryCommandIndeterm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandIndeterm(*args))

	#pasteHTML
	def pasteHTML(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().pasteHTML(*args))

	#collapse
	def collapse(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().collapse(*args))

	#compareEndPoints
	def compareEndPoints(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().compareEndPoints(*args))

	#queryCommandState
	def queryCommandState(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandState(*args))

	#moveToPoint
	def moveToPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveToPoint(*args))

	#moveToBookmark
	def moveToBookmark(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveToBookmark(*args))

	#queryCommandValue
	def queryCommandValue(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandValue(*args))

	#queryCommandSupported
	def queryCommandSupported(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandSupported(*args))

	#scrollIntoView
	def scrollIntoView(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().scrollIntoView(*args))

	#execCommand
	def execCommand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().execCommand(*args))

	#queryCommandText
	def queryCommandText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandText(*args))

	#moveToElementText
	def moveToElementText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveToElementText(*args))

	#queryCommandEnabled
	def queryCommandEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandEnabled(*args))

	#isEqual
	def isEqual(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().isEqual(*args))

wrapperClasses['{3050F220-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTxtRange
backWrapperClasses[IHTMLTxtRange] = '{3050F220-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFormElement
#
class IHTMLFormElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFormElement
		return self.__instance__.QueryInterface(kls)
	#elements
	def _get_elements(self):
		return wrap(self.__get_instance().elements)
	def _set_elements(self, value):
		self.__get_instance().elements = unwrap(value)
	elements = property(_get_elements, _set_elements)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#target
	def _get_target(self):
		return wrap(self.__get_instance().target)
	def _set_target(self, value):
		self.__get_instance().target = unwrap(value)
	target = property(_get_target, _set_target)

	#encoding
	def _get_encoding(self):
		return wrap(self.__get_instance().encoding)
	def _set_encoding(self, value):
		self.__get_instance().encoding = unwrap(value)
	encoding = property(_get_encoding, _set_encoding)

	#onreset
	def _get_onreset(self):
		return wrap(self.__get_instance().onreset)
	def _set_onreset(self, value):
		self.__get_instance().onreset = unwrap(value)
	onreset = property(_get_onreset, _set_onreset)

	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#onsubmit
	def _get_onsubmit(self):
		return wrap(self.__get_instance().onsubmit)
	def _set_onsubmit(self, value):
		self.__get_instance().onsubmit = unwrap(value)
	onsubmit = property(_get_onsubmit, _set_onsubmit)

	#action
	def _get_action(self):
		return wrap(self.__get_instance().action)
	def _set_action(self, value):
		self.__get_instance().action = unwrap(value)
	action = property(_get_action, _set_action)

	#method
	def _get_method(self):
		return wrap(self.__get_instance().method)
	def _set_method(self, value):
		self.__get_instance().method = unwrap(value)
	method = property(_get_method, _set_method)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance().dir)
	def _set_dir(self, value):
		self.__get_instance().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#reset
	def reset(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().reset(*args))

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

	#submit
	def submit(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().submit(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().tags(*args))

wrapperClasses['{3050F1F7-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFormElement
backWrapperClasses[IHTMLFormElement] = '{3050F1F7-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTextContainer
#
class IHTMLTextContainer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTextContainer
		return self.__instance__.QueryInterface(kls)
	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#scrollTop
	def _get_scrollTop(self):
		return wrap(self.__get_instance().scrollTop)
	def _set_scrollTop(self, value):
		self.__get_instance().scrollTop = unwrap(value)
	scrollTop = property(_get_scrollTop, _set_scrollTop)

	#scrollWidth
	def _get_scrollWidth(self):
		return wrap(self.__get_instance().scrollWidth)
	def _set_scrollWidth(self, value):
		self.__get_instance().scrollWidth = unwrap(value)
	scrollWidth = property(_get_scrollWidth, _set_scrollWidth)

	#scrollLeft
	def _get_scrollLeft(self):
		return wrap(self.__get_instance().scrollLeft)
	def _set_scrollLeft(self, value):
		self.__get_instance().scrollLeft = unwrap(value)
	scrollLeft = property(_get_scrollLeft, _set_scrollLeft)

	#scrollHeight
	def _get_scrollHeight(self):
		return wrap(self.__get_instance().scrollHeight)
	def _set_scrollHeight(self, value):
		self.__get_instance().scrollHeight = unwrap(value)
	scrollHeight = property(_get_scrollHeight, _set_scrollHeight)

	#createControlRange
	def createControlRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createControlRange(*args))

wrapperClasses['{3050F230-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTextContainer
backWrapperClasses[IHTMLTextContainer] = '{3050F230-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLImgElement
#
class IHTMLImgElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLImgElement
		return self.__instance__.QueryInterface(kls)
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance().protocol)
	def _set_protocol(self, value):
		self.__get_instance().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance().onerror)
	def _set_onerror(self, value):
		self.__get_instance().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#fileCreatedDate
	def _get_fileCreatedDate(self):
		return wrap(self.__get_instance().fileCreatedDate)
	def _set_fileCreatedDate(self, value):
		self.__get_instance().fileCreatedDate = unwrap(value)
	fileCreatedDate = property(_get_fileCreatedDate, _set_fileCreatedDate)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#href
	def _get_href(self):
		return wrap(self.__get_instance().href)
	def _set_href(self, value):
		self.__get_instance().href = unwrap(value)
	href = property(_get_href, _set_href)

	#alt
	def _get_alt(self):
		return wrap(self.__get_instance().alt)
	def _set_alt(self, value):
		self.__get_instance().alt = unwrap(value)
	alt = property(_get_alt, _set_alt)

	#fileModifiedDate
	def _get_fileModifiedDate(self):
		return wrap(self.__get_instance().fileModifiedDate)
	def _set_fileModifiedDate(self, value):
		self.__get_instance().fileModifiedDate = unwrap(value)
	fileModifiedDate = property(_get_fileModifiedDate, _set_fileModifiedDate)

	#hspace
	def _get_hspace(self):
		return wrap(self.__get_instance().hspace)
	def _set_hspace(self, value):
		self.__get_instance().hspace = unwrap(value)
	hspace = property(_get_hspace, _set_hspace)

	#onabort
	def _get_onabort(self):
		return wrap(self.__get_instance().onabort)
	def _set_onabort(self, value):
		self.__get_instance().onabort = unwrap(value)
	onabort = property(_get_onabort, _set_onabort)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance().onload)
	def _set_onload(self, value):
		self.__get_instance().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#start
	def _get_start(self):
		return wrap(self.__get_instance().start)
	def _set_start(self, value):
		self.__get_instance().start = unwrap(value)
	start = property(_get_start, _set_start)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#vspace
	def _get_vspace(self):
		return wrap(self.__get_instance().vspace)
	def _set_vspace(self, value):
		self.__get_instance().vspace = unwrap(value)
	vspace = property(_get_vspace, _set_vspace)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#useMap
	def _get_useMap(self):
		return wrap(self.__get_instance().useMap)
	def _set_useMap(self, value):
		self.__get_instance().useMap = unwrap(value)
	useMap = property(_get_useMap, _set_useMap)

	#vrml
	def _get_vrml(self):
		return wrap(self.__get_instance().vrml)
	def _set_vrml(self, value):
		self.__get_instance().vrml = unwrap(value)
	vrml = property(_get_vrml, _set_vrml)

	#fileUpdatedDate
	def _get_fileUpdatedDate(self):
		return wrap(self.__get_instance().fileUpdatedDate)
	def _set_fileUpdatedDate(self, value):
		self.__get_instance().fileUpdatedDate = unwrap(value)
	fileUpdatedDate = property(_get_fileUpdatedDate, _set_fileUpdatedDate)

	#complete
	def _get_complete(self):
		return wrap(self.__get_instance().complete)
	def _set_complete(self, value):
		self.__get_instance().complete = unwrap(value)
	complete = property(_get_complete, _set_complete)

	#fileSize
	def _get_fileSize(self):
		return wrap(self.__get_instance().fileSize)
	def _set_fileSize(self, value):
		self.__get_instance().fileSize = unwrap(value)
	fileSize = property(_get_fileSize, _set_fileSize)

	#src
	def _get_src(self):
		return wrap(self.__get_instance().src)
	def _set_src(self, value):
		self.__get_instance().src = unwrap(value)
	src = property(_get_src, _set_src)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#lowsrc
	def _get_lowsrc(self):
		return wrap(self.__get_instance().lowsrc)
	def _set_lowsrc(self, value):
		self.__get_instance().lowsrc = unwrap(value)
	lowsrc = property(_get_lowsrc, _set_lowsrc)

	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#isMap
	def _get_isMap(self):
		return wrap(self.__get_instance().isMap)
	def _set_isMap(self, value):
		self.__get_instance().isMap = unwrap(value)
	isMap = property(_get_isMap, _set_isMap)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#dynsrc
	def _get_dynsrc(self):
		return wrap(self.__get_instance().dynsrc)
	def _set_dynsrc(self, value):
		self.__get_instance().dynsrc = unwrap(value)
	dynsrc = property(_get_dynsrc, _set_dynsrc)

	#loop
	def _get_loop(self):
		return wrap(self.__get_instance().loop)
	def _set_loop(self, value):
		self.__get_instance().loop = unwrap(value)
	loop = property(_get_loop, _set_loop)

wrapperClasses['{3050F240-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLImgElement
backWrapperClasses[IHTMLImgElement] = '{3050F240-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLImageElementFactory
#
class IHTMLImageElementFactory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLImageElementFactory
		return self.__instance__.QueryInterface(kls)
	#create
	def create(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().create(*args))

wrapperClasses['{3050F38E-98B5-11CF-BB82-00AAA0BDCE0B}'] = IHTMLImageElementFactory
backWrapperClasses[IHTMLImageElementFactory] = '{3050F38E-98B5-11CF-BB82-00AAA0BDCE0B}'

##############################
# DispHTMLImg
#
class DispHTMLImg(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLImg
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F51C-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLImg
backWrapperClasses[DispHTMLImg] = '{3050F51C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLUniqueName
#
class IHTMLUniqueName(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLUniqueName
		return self.__instance__.QueryInterface(kls)
	#uniqueID
	def _get_uniqueID(self):
		return wrap(self.__get_instance().uniqueID)
	def _set_uniqueID(self, value):
		self.__get_instance().uniqueID = unwrap(value)
	uniqueID = property(_get_uniqueID, _set_uniqueID)

	#uniqueNumber
	def _get_uniqueNumber(self):
		return wrap(self.__get_instance().uniqueNumber)
	def _set_uniqueNumber(self, value):
		self.__get_instance().uniqueNumber = unwrap(value)
	uniqueNumber = property(_get_uniqueNumber, _set_uniqueNumber)

wrapperClasses['{3050F4D0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLUniqueName
backWrapperClasses[IHTMLUniqueName] = '{3050F4D0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLControlElement
#
class IHTMLControlElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLControlElement
		return self.__instance__.QueryInterface(kls)
	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance().onblur)
	def _set_onblur(self, value):
		self.__get_instance().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#clientLeft
	def _get_clientLeft(self):
		return wrap(self.__get_instance().clientLeft)
	def _set_clientLeft(self, value):
		self.__get_instance().clientLeft = unwrap(value)
	clientLeft = property(_get_clientLeft, _set_clientLeft)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#clientHeight
	def _get_clientHeight(self):
		return wrap(self.__get_instance().clientHeight)
	def _set_clientHeight(self, value):
		self.__get_instance().clientHeight = unwrap(value)
	clientHeight = property(_get_clientHeight, _set_clientHeight)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance().onresize)
	def _set_onresize(self, value):
		self.__get_instance().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#clientWidth
	def _get_clientWidth(self):
		return wrap(self.__get_instance().clientWidth)
	def _set_clientWidth(self, value):
		self.__get_instance().clientWidth = unwrap(value)
	clientWidth = property(_get_clientWidth, _set_clientWidth)

	#clientTop
	def _get_clientTop(self):
		return wrap(self.__get_instance().clientTop)
	def _set_clientTop(self, value):
		self.__get_instance().clientTop = unwrap(value)
	clientTop = property(_get_clientTop, _set_clientTop)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#removeFilter
	def removeFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().removeFilter(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().focus(*args))

	#addFilter
	def addFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addFilter(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().blur(*args))

wrapperClasses['{3050F4E9-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLControlElement
backWrapperClasses[IHTMLControlElement] = '{3050F4E9-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLBodyElement
#
class IHTMLBodyElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBodyElement
		return self.__instance__.QueryInterface(kls)
	#onload
	def _get_onload(self):
		return wrap(self.__get_instance().onload)
	def _set_onload(self, value):
		self.__get_instance().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#onunload
	def _get_onunload(self):
		return wrap(self.__get_instance().onunload)
	def _set_onunload(self, value):
		self.__get_instance().onunload = unwrap(value)
	onunload = property(_get_onunload, _set_onunload)

	#noWrap
	def _get_noWrap(self):
		return wrap(self.__get_instance().noWrap)
	def _set_noWrap(self, value):
		self.__get_instance().noWrap = unwrap(value)
	noWrap = property(_get_noWrap, _set_noWrap)

	#vLink
	def _get_vLink(self):
		return wrap(self.__get_instance().vLink)
	def _set_vLink(self, value):
		self.__get_instance().vLink = unwrap(value)
	vLink = property(_get_vLink, _set_vLink)

	#topMargin
	def _get_topMargin(self):
		return wrap(self.__get_instance().topMargin)
	def _set_topMargin(self, value):
		self.__get_instance().topMargin = unwrap(value)
	topMargin = property(_get_topMargin, _set_topMargin)

	#rightMargin
	def _get_rightMargin(self):
		return wrap(self.__get_instance().rightMargin)
	def _set_rightMargin(self, value):
		self.__get_instance().rightMargin = unwrap(value)
	rightMargin = property(_get_rightMargin, _set_rightMargin)

	#aLink
	def _get_aLink(self):
		return wrap(self.__get_instance().aLink)
	def _set_aLink(self, value):
		self.__get_instance().aLink = unwrap(value)
	aLink = property(_get_aLink, _set_aLink)

	#text
	def _get_text(self):
		return wrap(self.__get_instance().text)
	def _set_text(self, value):
		self.__get_instance().text = unwrap(value)
	text = property(_get_text, _set_text)

	#onbeforeunload
	def _get_onbeforeunload(self):
		return wrap(self.__get_instance().onbeforeunload)
	def _set_onbeforeunload(self, value):
		self.__get_instance().onbeforeunload = unwrap(value)
	onbeforeunload = property(_get_onbeforeunload, _set_onbeforeunload)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#bgProperties
	def _get_bgProperties(self):
		return wrap(self.__get_instance().bgProperties)
	def _set_bgProperties(self, value):
		self.__get_instance().bgProperties = unwrap(value)
	bgProperties = property(_get_bgProperties, _set_bgProperties)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance().onselect)
	def _set_onselect(self, value):
		self.__get_instance().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#link
	def _get_link(self):
		return wrap(self.__get_instance().link)
	def _set_link(self, value):
		self.__get_instance().link = unwrap(value)
	link = property(_get_link, _set_link)

	#background
	def _get_background(self):
		return wrap(self.__get_instance().background)
	def _set_background(self, value):
		self.__get_instance().background = unwrap(value)
	background = property(_get_background, _set_background)

	#bottomMargin
	def _get_bottomMargin(self):
		return wrap(self.__get_instance().bottomMargin)
	def _set_bottomMargin(self, value):
		self.__get_instance().bottomMargin = unwrap(value)
	bottomMargin = property(_get_bottomMargin, _set_bottomMargin)

	#scroll
	def _get_scroll(self):
		return wrap(self.__get_instance().scroll)
	def _set_scroll(self, value):
		self.__get_instance().scroll = unwrap(value)
	scroll = property(_get_scroll, _set_scroll)

	#leftMargin
	def _get_leftMargin(self):
		return wrap(self.__get_instance().leftMargin)
	def _set_leftMargin(self, value):
		self.__get_instance().leftMargin = unwrap(value)
	leftMargin = property(_get_leftMargin, _set_leftMargin)

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTextRange(*args))

wrapperClasses['{3050F1D8-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBodyElement
backWrapperClasses[IHTMLBodyElement] = '{3050F1D8-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLBodyElement2
#
class IHTMLBodyElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBodyElement2
		return self.__instance__.QueryInterface(kls)
	#onbeforeprint
	def _get_onbeforeprint(self):
		return wrap(self.__get_instance().onbeforeprint)
	def _set_onbeforeprint(self, value):
		self.__get_instance().onbeforeprint = unwrap(value)
	onbeforeprint = property(_get_onbeforeprint, _set_onbeforeprint)

	#onafterprint
	def _get_onafterprint(self):
		return wrap(self.__get_instance().onafterprint)
	def _set_onafterprint(self, value):
		self.__get_instance().onafterprint = unwrap(value)
	onafterprint = property(_get_onafterprint, _set_onafterprint)

wrapperClasses['{3050F5C5-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBodyElement2
backWrapperClasses[IHTMLBodyElement2] = '{3050F5C5-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLBody
#
class DispHTMLBody(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLBody
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F507-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLBody
backWrapperClasses[DispHTMLBody] = '{3050F507-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLAnchorElement
#
class IHTMLAnchorElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLAnchorElement
		return self.__instance__.QueryInterface(kls)
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#search
	def _get_search(self):
		return wrap(self.__get_instance().search)
	def _set_search(self, value):
		self.__get_instance().search = unwrap(value)
	search = property(_get_search, _set_search)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance().protocol)
	def _set_protocol(self, value):
		self.__get_instance().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#target
	def _get_target(self):
		return wrap(self.__get_instance().target)
	def _set_target(self, value):
		self.__get_instance().target = unwrap(value)
	target = property(_get_target, _set_target)

	#urn
	def _get_urn(self):
		return wrap(self.__get_instance().urn)
	def _set_urn(self, value):
		self.__get_instance().urn = unwrap(value)
	urn = property(_get_urn, _set_urn)

	#hostname
	def _get_hostname(self):
		return wrap(self.__get_instance().hostname)
	def _set_hostname(self, value):
		self.__get_instance().hostname = unwrap(value)
	hostname = property(_get_hostname, _set_hostname)

	#rev
	def _get_rev(self):
		return wrap(self.__get_instance().rev)
	def _set_rev(self, value):
		self.__get_instance().rev = unwrap(value)
	rev = property(_get_rev, _set_rev)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance().onblur)
	def _set_onblur(self, value):
		self.__get_instance().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#host
	def _get_host(self):
		return wrap(self.__get_instance().host)
	def _set_host(self, value):
		self.__get_instance().host = unwrap(value)
	host = property(_get_host, _set_host)

	#href
	def _get_href(self):
		return wrap(self.__get_instance().href)
	def _set_href(self, value):
		self.__get_instance().href = unwrap(value)
	href = property(_get_href, _set_href)

	#pathname
	def _get_pathname(self):
		return wrap(self.__get_instance().pathname)
	def _set_pathname(self, value):
		self.__get_instance().pathname = unwrap(value)
	pathname = property(_get_pathname, _set_pathname)

	#rel
	def _get_rel(self):
		return wrap(self.__get_instance().rel)
	def _set_rel(self, value):
		self.__get_instance().rel = unwrap(value)
	rel = property(_get_rel, _set_rel)

	#protocolLong
	def _get_protocolLong(self):
		return wrap(self.__get_instance().protocolLong)
	def _set_protocolLong(self, value):
		self.__get_instance().protocolLong = unwrap(value)
	protocolLong = property(_get_protocolLong, _set_protocolLong)

	#hash
	def _get_hash(self):
		return wrap(self.__get_instance().hash)
	def _set_hash(self, value):
		self.__get_instance().hash = unwrap(value)
	hash = property(_get_hash, _set_hash)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#port
	def _get_port(self):
		return wrap(self.__get_instance().port)
	def _set_port(self, value):
		self.__get_instance().port = unwrap(value)
	port = property(_get_port, _set_port)

	#Methods
	def _get_Methods(self):
		return wrap(self.__get_instance().Methods)
	def _set_Methods(self, value):
		self.__get_instance().Methods = unwrap(value)
	Methods = property(_get_Methods, _set_Methods)

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().focus(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().blur(*args))

wrapperClasses['{3050F1DA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLAnchorElement
backWrapperClasses[IHTMLAnchorElement] = '{3050F1DA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElementCollection
#
class IHTMLElementCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElementCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().tags(*args))

wrapperClasses['{3050F21F-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElementCollection
backWrapperClasses[IHTMLElementCollection] = '{3050F21F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLElementCollection
#
class DispHTMLElementCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLElementCollection
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F56B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLElementCollection
backWrapperClasses[DispHTMLElementCollection] = '{3050F56B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLSelectElement
#
class IHTMLSelectElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLSelectElement
		return self.__instance__.QueryInterface(kls)
	#multiple
	def _get_multiple(self):
		return wrap(self.__get_instance().multiple)
	def _set_multiple(self, value):
		self.__get_instance().multiple = unwrap(value)
	multiple = property(_get_multiple, _set_multiple)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance().form)
	def _set_form(self, value):
		self.__get_instance().form = unwrap(value)
	form = property(_get_form, _set_form)

	#value
	def _get_value(self):
		return wrap(self.__get_instance().value)
	def _set_value(self, value):
		self.__get_instance().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#selectedIndex
	def _get_selectedIndex(self):
		return wrap(self.__get_instance().selectedIndex)
	def _set_selectedIndex(self, value):
		self.__get_instance().selectedIndex = unwrap(value)
	selectedIndex = property(_get_selectedIndex, _set_selectedIndex)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance().onchange)
	def _set_onchange(self, value):
		self.__get_instance().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#options
	def _get_options(self):
		return wrap(self.__get_instance().options)
	def _set_options(self, value):
		self.__get_instance().options = unwrap(value)
	options = property(_get_options, _set_options)

	#size
	def _get_size(self):
		return wrap(self.__get_instance().size)
	def _set_size(self, value):
		self.__get_instance().size = unwrap(value)
	size = property(_get_size, _set_size)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

	#add
	def add(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().add(*args))

	#remove
	def remove(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().remove(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().tags(*args))

wrapperClasses['{3050F244-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLSelectElement
backWrapperClasses[IHTMLSelectElement] = '{3050F244-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLSelectElement
#
class DispHTMLSelectElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLSelectElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F531-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLSelectElement
backWrapperClasses[DispHTMLSelectElement] = '{3050F531-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLSelectionObject
#
class IHTMLSelectionObject(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLSelectionObject
		return self.__instance__.QueryInterface(kls)
	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#createRange
	def createRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createRange(*args))

	#clear
	def clear(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clear(*args))

	#empty
	def empty(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().empty(*args))

wrapperClasses['{3050F25A-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLSelectionObject
backWrapperClasses[IHTMLSelectionObject] = '{3050F25A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOptionElement
#
class IHTMLOptionElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOptionElement
		return self.__instance__.QueryInterface(kls)
	#index
	def _get_index(self):
		return wrap(self.__get_instance().index)
	def _set_index(self, value):
		self.__get_instance().index = unwrap(value)
	index = property(_get_index, _set_index)

	#selected
	def _get_selected(self):
		return wrap(self.__get_instance().selected)
	def _set_selected(self, value):
		self.__get_instance().selected = unwrap(value)
	selected = property(_get_selected, _set_selected)

	#form
	def _get_form(self):
		return wrap(self.__get_instance().form)
	def _set_form(self, value):
		self.__get_instance().form = unwrap(value)
	form = property(_get_form, _set_form)

	#text
	def _get_text(self):
		return wrap(self.__get_instance().text)
	def _set_text(self, value):
		self.__get_instance().text = unwrap(value)
	text = property(_get_text, _set_text)

	#defaultSelected
	def _get_defaultSelected(self):
		return wrap(self.__get_instance().defaultSelected)
	def _set_defaultSelected(self, value):
		self.__get_instance().defaultSelected = unwrap(value)
	defaultSelected = property(_get_defaultSelected, _set_defaultSelected)

	#value
	def _get_value(self):
		return wrap(self.__get_instance().value)
	def _set_value(self, value):
		self.__get_instance().value = unwrap(value)
	value = property(_get_value, _set_value)

wrapperClasses['{3050F211-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOptionElement
backWrapperClasses[IHTMLOptionElement] = '{3050F211-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOptionElementFactory
#
class IHTMLOptionElementFactory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOptionElementFactory
		return self.__instance__.QueryInterface(kls)
	#create
	def create(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().create(*args))

wrapperClasses['{3050F38C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOptionElementFactory
backWrapperClasses[IHTMLOptionElementFactory] = '{3050F38C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLOptionElement
#
class DispHTMLOptionElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLOptionElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F52B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLOptionElement
backWrapperClasses[DispHTMLOptionElement] = '{3050F52B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLInputElement
#
class IHTMLInputElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLInputElement
		return self.__instance__.QueryInterface(kls)
	#defaultChecked
	def _get_defaultChecked(self):
		return wrap(self.__get_instance().defaultChecked)
	def _set_defaultChecked(self, value):
		self.__get_instance().defaultChecked = unwrap(value)
	defaultChecked = property(_get_defaultChecked, _set_defaultChecked)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance().onerror)
	def _set_onerror(self, value):
		self.__get_instance().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#alt
	def _get_alt(self):
		return wrap(self.__get_instance().alt)
	def _set_alt(self, value):
		self.__get_instance().alt = unwrap(value)
	alt = property(_get_alt, _set_alt)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance().onchange)
	def _set_onchange(self, value):
		self.__get_instance().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#size
	def _get_size(self):
		return wrap(self.__get_instance().size)
	def _set_size(self, value):
		self.__get_instance().size = unwrap(value)
	size = property(_get_size, _set_size)

	#onabort
	def _get_onabort(self):
		return wrap(self.__get_instance().onabort)
	def _set_onabort(self, value):
		self.__get_instance().onabort = unwrap(value)
	onabort = property(_get_onabort, _set_onabort)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance().onload)
	def _set_onload(self, value):
		self.__get_instance().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#checked
	def _get_checked(self):
		return wrap(self.__get_instance().checked)
	def _set_checked(self, value):
		self.__get_instance().checked = unwrap(value)
	checked = property(_get_checked, _set_checked)

	#start
	def _get_start(self):
		return wrap(self.__get_instance().start)
	def _set_start(self, value):
		self.__get_instance().start = unwrap(value)
	start = property(_get_start, _set_start)

	#hspace
	def _get_hspace(self):
		return wrap(self.__get_instance().hspace)
	def _set_hspace(self, value):
		self.__get_instance().hspace = unwrap(value)
	hspace = property(_get_hspace, _set_hspace)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#indeterminate
	def _get_indeterminate(self):
		return wrap(self.__get_instance().indeterminate)
	def _set_indeterminate(self, value):
		self.__get_instance().indeterminate = unwrap(value)
	indeterminate = property(_get_indeterminate, _set_indeterminate)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance().onselect)
	def _set_onselect(self, value):
		self.__get_instance().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#vrml
	def _get_vrml(self):
		return wrap(self.__get_instance().vrml)
	def _set_vrml(self, value):
		self.__get_instance().vrml = unwrap(value)
	vrml = property(_get_vrml, _set_vrml)

	#status
	def _get_status(self):
		return wrap(self.__get_instance().status)
	def _set_status(self, value):
		self.__get_instance().status = unwrap(value)
	status = property(_get_status, _set_status)

	#complete
	def _get_complete(self):
		return wrap(self.__get_instance().complete)
	def _set_complete(self, value):
		self.__get_instance().complete = unwrap(value)
	complete = property(_get_complete, _set_complete)

	#form
	def _get_form(self):
		return wrap(self.__get_instance().form)
	def _set_form(self, value):
		self.__get_instance().form = unwrap(value)
	form = property(_get_form, _set_form)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#maxLength
	def _get_maxLength(self):
		return wrap(self.__get_instance().maxLength)
	def _set_maxLength(self, value):
		self.__get_instance().maxLength = unwrap(value)
	maxLength = property(_get_maxLength, _set_maxLength)

	#src
	def _get_src(self):
		return wrap(self.__get_instance().src)
	def _set_src(self, value):
		self.__get_instance().src = unwrap(value)
	src = property(_get_src, _set_src)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#lowsrc
	def _get_lowsrc(self):
		return wrap(self.__get_instance().lowsrc)
	def _set_lowsrc(self, value):
		self.__get_instance().lowsrc = unwrap(value)
	lowsrc = property(_get_lowsrc, _set_lowsrc)

	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#value
	def _get_value(self):
		return wrap(self.__get_instance().value)
	def _set_value(self, value):
		self.__get_instance().value = unwrap(value)
	value = property(_get_value, _set_value)

	#vspace
	def _get_vspace(self):
		return wrap(self.__get_instance().vspace)
	def _set_vspace(self, value):
		self.__get_instance().vspace = unwrap(value)
	vspace = property(_get_vspace, _set_vspace)

	#dynsrc
	def _get_dynsrc(self):
		return wrap(self.__get_instance().dynsrc)
	def _set_dynsrc(self, value):
		self.__get_instance().dynsrc = unwrap(value)
	dynsrc = property(_get_dynsrc, _set_dynsrc)

	#loop
	def _get_loop(self):
		return wrap(self.__get_instance().loop)
	def _set_loop(self, value):
		self.__get_instance().loop = unwrap(value)
	loop = property(_get_loop, _set_loop)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTextRange(*args))

wrapperClasses['{3050F5D2-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLInputElement
backWrapperClasses[IHTMLInputElement] = '{3050F5D2-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLInputTextElement
#
class IHTMLInputTextElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLInputTextElement
		return self.__instance__.QueryInterface(kls)
	#status
	def _get_status(self):
		return wrap(self.__get_instance().status)
	def _set_status(self, value):
		self.__get_instance().status = unwrap(value)
	status = property(_get_status, _set_status)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance().form)
	def _set_form(self, value):
		self.__get_instance().form = unwrap(value)
	form = property(_get_form, _set_form)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#value
	def _get_value(self):
		return wrap(self.__get_instance().value)
	def _set_value(self, value):
		self.__get_instance().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance().onselect)
	def _set_onselect(self, value):
		self.__get_instance().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#maxLength
	def _get_maxLength(self):
		return wrap(self.__get_instance().maxLength)
	def _set_maxLength(self, value):
		self.__get_instance().maxLength = unwrap(value)
	maxLength = property(_get_maxLength, _set_maxLength)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance().onchange)
	def _set_onchange(self, value):
		self.__get_instance().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#size
	def _get_size(self):
		return wrap(self.__get_instance().size)
	def _set_size(self, value):
		self.__get_instance().size = unwrap(value)
	size = property(_get_size, _set_size)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTextRange(*args))

wrapperClasses['{3050F2A6-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLInputTextElement
backWrapperClasses[IHTMLInputTextElement] = '{3050F2A6-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLInputElement
#
class DispHTMLInputElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLInputElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F57D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLInputElement
backWrapperClasses[DispHTMLInputElement] = '{3050F57D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTextAreaElement
#
class IHTMLTextAreaElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTextAreaElement
		return self.__instance__.QueryInterface(kls)
	#status
	def _get_status(self):
		return wrap(self.__get_instance().status)
	def _set_status(self, value):
		self.__get_instance().status = unwrap(value)
	status = property(_get_status, _set_status)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance().rows)
	def _set_rows(self, value):
		self.__get_instance().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance().form)
	def _set_form(self, value):
		self.__get_instance().form = unwrap(value)
	form = property(_get_form, _set_form)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#cols
	def _get_cols(self):
		return wrap(self.__get_instance().cols)
	def _set_cols(self, value):
		self.__get_instance().cols = unwrap(value)
	cols = property(_get_cols, _set_cols)

	#value
	def _get_value(self):
		return wrap(self.__get_instance().value)
	def _set_value(self, value):
		self.__get_instance().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance().disabled)
	def _set_disabled(self, value):
		self.__get_instance().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance().onselect)
	def _set_onselect(self, value):
		self.__get_instance().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#wrap
	def _get_wrap(self):
		return wrap(self.__get_instance().wrap)
	def _set_wrap(self, value):
		self.__get_instance().wrap = unwrap(value)
	wrap = property(_get_wrap, _set_wrap)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance().onchange)
	def _set_onchange(self, value):
		self.__get_instance().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTextRange(*args))

wrapperClasses['{3050F2AA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTextAreaElement
backWrapperClasses[IHTMLTextAreaElement] = '{3050F2AA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLUnknownElement
#
class DispHTMLUnknownElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLUnknownElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F539-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLUnknownElement
backWrapperClasses[DispHTMLUnknownElement] = '{3050F539-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IOmHistory
#
class IOmHistory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IOmHistory
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#forward
	def forward(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().forward(*args))

	#go
	def go(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().go(*args))

	#back
	def back(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().back(*args))

wrapperClasses['{FECEAAA2-8405-11CF-8BA1-00AA00476DA6}'] = IOmHistory
backWrapperClasses[IOmHistory] = '{FECEAAA2-8405-11CF-8BA1-00AA00476DA6}'

##############################
# IHTMLMimeTypesCollection
#
class IHTMLMimeTypesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLMimeTypesCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

wrapperClasses['{3050F3FC-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLMimeTypesCollection
backWrapperClasses[IHTMLMimeTypesCollection] = '{3050F3FC-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLPluginsCollection
#
class IHTMLPluginsCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLPluginsCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#refresh
	def refresh(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().refresh(*args))

wrapperClasses['{3050F3FD-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLPluginsCollection
backWrapperClasses[IHTMLPluginsCollection] = '{3050F3FD-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOpsProfile
#
class IHTMLOpsProfile(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOpsProfile
		return self.__instance__.QueryInterface(kls)
	#doRequest
	def doRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().doRequest(*args))

	#addReadRequest
	def addReadRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addReadRequest(*args))

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getAttribute(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setAttribute(*args))

	#clearRequest
	def clearRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clearRequest(*args))

	#doWriteRequest
	def doWriteRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().doWriteRequest(*args))

	#doReadRequest
	def doReadRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().doReadRequest(*args))

	#commitChanges
	def commitChanges(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().commitChanges(*args))

	#addRequest
	def addRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().addRequest(*args))

wrapperClasses['{3050F401-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOpsProfile
backWrapperClasses[IHTMLOpsProfile] = '{3050F401-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IOmNavigator
#
class IOmNavigator(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IOmNavigator
		return self.__instance__.QueryInterface(kls)
	#mimeTypes
	def _get_mimeTypes(self):
		return wrap(self.__get_instance().mimeTypes)
	def _set_mimeTypes(self, value):
		self.__get_instance().mimeTypes = unwrap(value)
	mimeTypes = property(_get_mimeTypes, _set_mimeTypes)

	#userProfile
	def _get_userProfile(self):
		return wrap(self.__get_instance().userProfile)
	def _set_userProfile(self, value):
		self.__get_instance().userProfile = unwrap(value)
	userProfile = property(_get_userProfile, _set_userProfile)

	#appName
	def _get_appName(self):
		return wrap(self.__get_instance().appName)
	def _set_appName(self, value):
		self.__get_instance().appName = unwrap(value)
	appName = property(_get_appName, _set_appName)

	#appCodeName
	def _get_appCodeName(self):
		return wrap(self.__get_instance().appCodeName)
	def _set_appCodeName(self, value):
		self.__get_instance().appCodeName = unwrap(value)
	appCodeName = property(_get_appCodeName, _set_appCodeName)

	#opsProfile
	def _get_opsProfile(self):
		return wrap(self.__get_instance().opsProfile)
	def _set_opsProfile(self, value):
		self.__get_instance().opsProfile = unwrap(value)
	opsProfile = property(_get_opsProfile, _set_opsProfile)

	#onLine
	def _get_onLine(self):
		return wrap(self.__get_instance().onLine)
	def _set_onLine(self, value):
		self.__get_instance().onLine = unwrap(value)
	onLine = property(_get_onLine, _set_onLine)

	#cookieEnabled
	def _get_cookieEnabled(self):
		return wrap(self.__get_instance().cookieEnabled)
	def _set_cookieEnabled(self, value):
		self.__get_instance().cookieEnabled = unwrap(value)
	cookieEnabled = property(_get_cookieEnabled, _set_cookieEnabled)

	#appVersion
	def _get_appVersion(self):
		return wrap(self.__get_instance().appVersion)
	def _set_appVersion(self, value):
		self.__get_instance().appVersion = unwrap(value)
	appVersion = property(_get_appVersion, _set_appVersion)

	#connectionSpeed
	def _get_connectionSpeed(self):
		return wrap(self.__get_instance().connectionSpeed)
	def _set_connectionSpeed(self, value):
		self.__get_instance().connectionSpeed = unwrap(value)
	connectionSpeed = property(_get_connectionSpeed, _set_connectionSpeed)

	#appMinorVersion
	def _get_appMinorVersion(self):
		return wrap(self.__get_instance().appMinorVersion)
	def _set_appMinorVersion(self, value):
		self.__get_instance().appMinorVersion = unwrap(value)
	appMinorVersion = property(_get_appMinorVersion, _set_appMinorVersion)

	#platform
	def _get_platform(self):
		return wrap(self.__get_instance().platform)
	def _set_platform(self, value):
		self.__get_instance().platform = unwrap(value)
	platform = property(_get_platform, _set_platform)

	#systemLanguage
	def _get_systemLanguage(self):
		return wrap(self.__get_instance().systemLanguage)
	def _set_systemLanguage(self, value):
		self.__get_instance().systemLanguage = unwrap(value)
	systemLanguage = property(_get_systemLanguage, _set_systemLanguage)

	#cpuClass
	def _get_cpuClass(self):
		return wrap(self.__get_instance().cpuClass)
	def _set_cpuClass(self, value):
		self.__get_instance().cpuClass = unwrap(value)
	cpuClass = property(_get_cpuClass, _set_cpuClass)

	#plugins
	def _get_plugins(self):
		return wrap(self.__get_instance().plugins)
	def _set_plugins(self, value):
		self.__get_instance().plugins = unwrap(value)
	plugins = property(_get_plugins, _set_plugins)

	#userAgent
	def _get_userAgent(self):
		return wrap(self.__get_instance().userAgent)
	def _set_userAgent(self, value):
		self.__get_instance().userAgent = unwrap(value)
	userAgent = property(_get_userAgent, _set_userAgent)

	#userLanguage
	def _get_userLanguage(self):
		return wrap(self.__get_instance().userLanguage)
	def _set_userLanguage(self, value):
		self.__get_instance().userLanguage = unwrap(value)
	userLanguage = property(_get_userLanguage, _set_userLanguage)

	#browserLanguage
	def _get_browserLanguage(self):
		return wrap(self.__get_instance().browserLanguage)
	def _set_browserLanguage(self, value):
		self.__get_instance().browserLanguage = unwrap(value)
	browserLanguage = property(_get_browserLanguage, _set_browserLanguage)

	#javaEnabled
	def javaEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().javaEnabled(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#taintEnabled
	def taintEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().taintEnabled(*args))

wrapperClasses['{FECEAAA5-8405-11CF-8BA1-00AA00476DA6}'] = IOmNavigator
backWrapperClasses[IOmNavigator] = '{FECEAAA5-8405-11CF-8BA1-00AA00476DA6}'

##############################
# IHTMLLocation
#
class IHTMLLocation(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLLocation
		return self.__instance__.QueryInterface(kls)
	#search
	def _get_search(self):
		return wrap(self.__get_instance().search)
	def _set_search(self, value):
		self.__get_instance().search = unwrap(value)
	search = property(_get_search, _set_search)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance().protocol)
	def _set_protocol(self, value):
		self.__get_instance().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#hostname
	def _get_hostname(self):
		return wrap(self.__get_instance().hostname)
	def _set_hostname(self, value):
		self.__get_instance().hostname = unwrap(value)
	hostname = property(_get_hostname, _set_hostname)

	#host
	def _get_host(self):
		return wrap(self.__get_instance().host)
	def _set_host(self, value):
		self.__get_instance().host = unwrap(value)
	host = property(_get_host, _set_host)

	#href
	def _get_href(self):
		return wrap(self.__get_instance().href)
	def _set_href(self, value):
		self.__get_instance().href = unwrap(value)
	href = property(_get_href, _set_href)

	#pathname
	def _get_pathname(self):
		return wrap(self.__get_instance().pathname)
	def _set_pathname(self, value):
		self.__get_instance().pathname = unwrap(value)
	pathname = property(_get_pathname, _set_pathname)

	#hash
	def _get_hash(self):
		return wrap(self.__get_instance().hash)
	def _set_hash(self, value):
		self.__get_instance().hash = unwrap(value)
	hash = property(_get_hash, _set_hash)

	#port
	def _get_port(self):
		return wrap(self.__get_instance().port)
	def _set_port(self, value):
		self.__get_instance().port = unwrap(value)
	port = property(_get_port, _set_port)

	#reload
	def reload(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().reload(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#assign
	def assign(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().assign(*args))

	#replace
	def replace(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replace(*args))

wrapperClasses['{163BB1E0-6E00-11CF-837A-48DC04C10000}'] = IHTMLLocation
backWrapperClasses[IHTMLLocation] = '{163BB1E0-6E00-11CF-837A-48DC04C10000}'

##############################
# IHTMLBookmarkCollection
#
class IHTMLBookmarkCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBookmarkCollection
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{3050F4CE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBookmarkCollection
backWrapperClasses[IHTMLBookmarkCollection] = '{3050F4CE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDataTransfer
#
class IHTMLDataTransfer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDataTransfer
		return self.__instance__.QueryInterface(kls)
	#effectAllowed
	def _get_effectAllowed(self):
		return wrap(self.__get_instance().effectAllowed)
	def _set_effectAllowed(self, value):
		self.__get_instance().effectAllowed = unwrap(value)
	effectAllowed = property(_get_effectAllowed, _set_effectAllowed)

	#dropEffect
	def _get_dropEffect(self):
		return wrap(self.__get_instance().dropEffect)
	def _set_dropEffect(self, value):
		self.__get_instance().dropEffect = unwrap(value)
	dropEffect = property(_get_dropEffect, _set_dropEffect)

	#getData
	def getData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getData(*args))

	#clearData
	def clearData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clearData(*args))

	#setData
	def setData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setData(*args))

wrapperClasses['{3050F4B3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDataTransfer
backWrapperClasses[IHTMLDataTransfer] = '{3050F4B3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEventObj
#
class IHTMLEventObj(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEventObj
		return self.__instance__.QueryInterface(kls)
	#returnValue
	def _get_returnValue(self):
		return wrap(self.__get_instance().returnValue)
	def _set_returnValue(self, value):
		self.__get_instance().returnValue = unwrap(value)
	returnValue = property(_get_returnValue, _set_returnValue)

	#ctrlKey
	def _get_ctrlKey(self):
		return wrap(self.__get_instance().ctrlKey)
	def _set_ctrlKey(self, value):
		self.__get_instance().ctrlKey = unwrap(value)
	ctrlKey = property(_get_ctrlKey, _set_ctrlKey)

	#fromElement
	def _get_fromElement(self):
		return wrap(self.__get_instance().fromElement)
	def _set_fromElement(self, value):
		self.__get_instance().fromElement = unwrap(value)
	fromElement = property(_get_fromElement, _set_fromElement)

	#screenY
	def _get_screenY(self):
		return wrap(self.__get_instance().screenY)
	def _set_screenY(self, value):
		self.__get_instance().screenY = unwrap(value)
	screenY = property(_get_screenY, _set_screenY)

	#screenX
	def _get_screenX(self):
		return wrap(self.__get_instance().screenX)
	def _set_screenX(self, value):
		self.__get_instance().screenX = unwrap(value)
	screenX = property(_get_screenX, _set_screenX)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#clientX
	def _get_clientX(self):
		return wrap(self.__get_instance().clientX)
	def _set_clientX(self, value):
		self.__get_instance().clientX = unwrap(value)
	clientX = property(_get_clientX, _set_clientX)

	#clientY
	def _get_clientY(self):
		return wrap(self.__get_instance().clientY)
	def _set_clientY(self, value):
		self.__get_instance().clientY = unwrap(value)
	clientY = property(_get_clientY, _set_clientY)

	#qualifier
	def _get_qualifier(self):
		return wrap(self.__get_instance().qualifier)
	def _set_qualifier(self, value):
		self.__get_instance().qualifier = unwrap(value)
	qualifier = property(_get_qualifier, _set_qualifier)

	#altKey
	def _get_altKey(self):
		return wrap(self.__get_instance().altKey)
	def _set_altKey(self, value):
		self.__get_instance().altKey = unwrap(value)
	altKey = property(_get_altKey, _set_altKey)

	#reason
	def _get_reason(self):
		return wrap(self.__get_instance().reason)
	def _set_reason(self, value):
		self.__get_instance().reason = unwrap(value)
	reason = property(_get_reason, _set_reason)

	#x
	def _get_x(self):
		return wrap(self.__get_instance().x)
	def _set_x(self, value):
		self.__get_instance().x = unwrap(value)
	x = property(_get_x, _set_x)

	#cancelBubble
	def _get_cancelBubble(self):
		return wrap(self.__get_instance().cancelBubble)
	def _set_cancelBubble(self, value):
		self.__get_instance().cancelBubble = unwrap(value)
	cancelBubble = property(_get_cancelBubble, _set_cancelBubble)

	#toElement
	def _get_toElement(self):
		return wrap(self.__get_instance().toElement)
	def _set_toElement(self, value):
		self.__get_instance().toElement = unwrap(value)
	toElement = property(_get_toElement, _set_toElement)

	#srcElement
	def _get_srcElement(self):
		return wrap(self.__get_instance().srcElement)
	def _set_srcElement(self, value):
		self.__get_instance().srcElement = unwrap(value)
	srcElement = property(_get_srcElement, _set_srcElement)

	#shiftKey
	def _get_shiftKey(self):
		return wrap(self.__get_instance().shiftKey)
	def _set_shiftKey(self, value):
		self.__get_instance().shiftKey = unwrap(value)
	shiftKey = property(_get_shiftKey, _set_shiftKey)

	#button
	def _get_button(self):
		return wrap(self.__get_instance().button)
	def _set_button(self, value):
		self.__get_instance().button = unwrap(value)
	button = property(_get_button, _set_button)

	#offsetX
	def _get_offsetX(self):
		return wrap(self.__get_instance().offsetX)
	def _set_offsetX(self, value):
		self.__get_instance().offsetX = unwrap(value)
	offsetX = property(_get_offsetX, _set_offsetX)

	#offsetY
	def _get_offsetY(self):
		return wrap(self.__get_instance().offsetY)
	def _set_offsetY(self, value):
		self.__get_instance().offsetY = unwrap(value)
	offsetY = property(_get_offsetY, _set_offsetY)

	#y
	def _get_y(self):
		return wrap(self.__get_instance().y)
	def _set_y(self, value):
		self.__get_instance().y = unwrap(value)
	y = property(_get_y, _set_y)

	#srcFilter
	def _get_srcFilter(self):
		return wrap(self.__get_instance().srcFilter)
	def _set_srcFilter(self, value):
		self.__get_instance().srcFilter = unwrap(value)
	srcFilter = property(_get_srcFilter, _set_srcFilter)

	#keyCode
	def _get_keyCode(self):
		return wrap(self.__get_instance().keyCode)
	def _set_keyCode(self, value):
		self.__get_instance().keyCode = unwrap(value)
	keyCode = property(_get_keyCode, _set_keyCode)

wrapperClasses['{3050F32D-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLEventObj
backWrapperClasses[IHTMLEventObj] = '{3050F32D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispCEventObj
#
class DispCEventObj(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispCEventObj
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F558-98B5-11CF-BB82-00AA00BDCE0B}'] = DispCEventObj
backWrapperClasses[DispCEventObj] = '{3050F558-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFramesCollection2
#
class IHTMLFramesCollection2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFramesCollection2
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().item(*args))

wrapperClasses['{332C4426-26CB-11D0-B483-00C04FD90119}'] = IHTMLFramesCollection2
backWrapperClasses[IHTMLFramesCollection2] = '{332C4426-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLScreen
#
class IHTMLScreen(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScreen
		return self.__instance__.QueryInterface(kls)
	#availWidth
	def _get_availWidth(self):
		return wrap(self.__get_instance().availWidth)
	def _set_availWidth(self, value):
		self.__get_instance().availWidth = unwrap(value)
	availWidth = property(_get_availWidth, _set_availWidth)

	#bufferDepth
	def _get_bufferDepth(self):
		return wrap(self.__get_instance().bufferDepth)
	def _set_bufferDepth(self, value):
		self.__get_instance().bufferDepth = unwrap(value)
	bufferDepth = property(_get_bufferDepth, _set_bufferDepth)

	#availHeight
	def _get_availHeight(self):
		return wrap(self.__get_instance().availHeight)
	def _set_availHeight(self, value):
		self.__get_instance().availHeight = unwrap(value)
	availHeight = property(_get_availHeight, _set_availHeight)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#fontSmoothingEnabled
	def _get_fontSmoothingEnabled(self):
		return wrap(self.__get_instance().fontSmoothingEnabled)
	def _set_fontSmoothingEnabled(self, value):
		self.__get_instance().fontSmoothingEnabled = unwrap(value)
	fontSmoothingEnabled = property(_get_fontSmoothingEnabled, _set_fontSmoothingEnabled)

	#colorDepth
	def _get_colorDepth(self):
		return wrap(self.__get_instance().colorDepth)
	def _set_colorDepth(self, value):
		self.__get_instance().colorDepth = unwrap(value)
	colorDepth = property(_get_colorDepth, _set_colorDepth)

	#updateInterval
	def _get_updateInterval(self):
		return wrap(self.__get_instance().updateInterval)
	def _set_updateInterval(self, value):
		self.__get_instance().updateInterval = unwrap(value)
	updateInterval = property(_get_updateInterval, _set_updateInterval)

wrapperClasses['{3050F35C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScreen
backWrapperClasses[IHTMLScreen] = '{3050F35C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLWindow2
#
class IHTMLWindow2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLWindow2
		return self.__instance__.QueryInterface(kls)
	#defaultStatus
	def _get_defaultStatus(self):
		return wrap(self.__get_instance().defaultStatus)
	def _set_defaultStatus(self, value):
		self.__get_instance().defaultStatus = unwrap(value)
	defaultStatus = property(_get_defaultStatus, _set_defaultStatus)

	#clientInformation
	def _get_clientInformation(self):
		return wrap(self.__get_instance().clientInformation)
	def _set_clientInformation(self, value):
		self.__get_instance().clientInformation = unwrap(value)
	clientInformation = property(_get_clientInformation, _set_clientInformation)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance().onerror)
	def _set_onerror(self, value):
		self.__get_instance().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#frames
	def _get_frames(self):
		return wrap(self.__get_instance().frames)
	def _set_frames(self, value):
		self.__get_instance().frames = unwrap(value)
	frames = property(_get_frames, _set_frames)

	#navigator
	def _get_navigator(self):
		return wrap(self.__get_instance().navigator)
	def _set_navigator(self, value):
		self.__get_instance().navigator = unwrap(value)
	navigator = property(_get_navigator, _set_navigator)

	#event
	def _get_event(self):
		return wrap(self.__get_instance().event)
	def _set_event(self, value):
		self.__get_instance().event = unwrap(value)
	event = property(_get_event, _set_event)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance().onload)
	def _set_onload(self, value):
		self.__get_instance().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#Option
	def _get_Option(self):
		return wrap(self.__get_instance().Option)
	def _set_Option(self, value):
		self.__get_instance().Option = unwrap(value)
	Option = property(_get_Option, _set_Option)

	#top
	def _get_top(self):
		return wrap(self.__get_instance().top)
	def _set_top(self, value):
		self.__get_instance().top = unwrap(value)
	top = property(_get_top, _set_top)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance().onresize)
	def _set_onresize(self, value):
		self.__get_instance().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#window
	def _get_window(self):
		return wrap(self.__get_instance().window)
	def _set_window(self, value):
		self.__get_instance().window = unwrap(value)
	window = property(_get_window, _set_window)

	#opener
	def _get_opener(self):
		return wrap(self.__get_instance().opener)
	def _set_opener(self, value):
		self.__get_instance().opener = unwrap(value)
	opener = property(_get_opener, _set_opener)

	#location
	def _get_location(self):
		return wrap(self.__get_instance().location)
	def _set_location(self, value):
		self.__get_instance().location = unwrap(value)
	location = property(_get_location, _set_location)

	#closed
	def _get_closed(self):
		return wrap(self.__get_instance().closed)
	def _set_closed(self, value):
		self.__get_instance().closed = unwrap(value)
	closed = property(_get_closed, _set_closed)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#document
	def _get_document(self):
		return wrap(self.__get_instance().document)
	def _set_document(self, value):
		self.__get_instance().document = unwrap(value)
	document = property(_get_document, _set_document)

	#status
	def _get_status(self):
		return wrap(self.__get_instance().status)
	def _set_status(self, value):
		self.__get_instance().status = unwrap(value)
	status = property(_get_status, _set_status)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance().onblur)
	def _set_onblur(self, value):
		self.__get_instance().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#parent
	def _get_parent(self):
		return wrap(self.__get_instance().parent)
	def _set_parent(self, value):
		self.__get_instance().parent = unwrap(value)
	parent = property(_get_parent, _set_parent)

	#screen
	def _get_screen(self):
		return wrap(self.__get_instance().screen)
	def _set_screen(self, value):
		self.__get_instance().screen = unwrap(value)
	screen = property(_get_screen, _set_screen)

	#external
	def _get_external(self):
		return wrap(self.__get_instance().external)
	def _set_external(self, value):
		self.__get_instance().external = unwrap(value)
	external = property(_get_external, _set_external)

	#offscreenBuffering
	def _get_offscreenBuffering(self):
		return wrap(self.__get_instance().offscreenBuffering)
	def _set_offscreenBuffering(self, value):
		self.__get_instance().offscreenBuffering = unwrap(value)
	offscreenBuffering = property(_get_offscreenBuffering, _set_offscreenBuffering)

	#onunload
	def _get_onunload(self):
		return wrap(self.__get_instance().onunload)
	def _set_onunload(self, value):
		self.__get_instance().onunload = unwrap(value)
	onunload = property(_get_onunload, _set_onunload)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#Image
	def _get_Image(self):
		return wrap(self.__get_instance().Image)
	def _set_Image(self, value):
		self.__get_instance().Image = unwrap(value)
	Image = property(_get_Image, _set_Image)

	#onbeforeunload
	def _get_onbeforeunload(self):
		return wrap(self.__get_instance().onbeforeunload)
	def _set_onbeforeunload(self, value):
		self.__get_instance().onbeforeunload = unwrap(value)
	onbeforeunload = property(_get_onbeforeunload, _set_onbeforeunload)

	#self
	def _get_self(self):
		return wrap(self.__get_instance().self)
	def _set_self(self, value):
		self.__get_instance().self = unwrap(value)
	self = property(_get_self, _set_self)

	#history
	def _get_history(self):
		return wrap(self.__get_instance().history)
	def _set_history(self, value):
		self.__get_instance().history = unwrap(value)
	history = property(_get_history, _set_history)

	#moveTo
	def moveTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveTo(*args))

	#prompt
	def prompt(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().prompt(*args))

	#scrollTo
	def scrollTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().scrollTo(*args))

	#navigate
	def navigate(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().navigate(*args))

	#clearInterval
	def clearInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clearInterval(*args))

	#close
	def close(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().close(*args))

	#open
	def open(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().open(*args))

	#showHelp
	def showHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().showHelp(*args))

	#setTimeout
	def setTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setTimeout(*args))

	#confirm
	def confirm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().confirm(*args))

	#clearTimeout
	def clearTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clearTimeout(*args))

	#resizeBy
	def resizeBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().resizeBy(*args))

	#execScript
	def execScript(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().execScript(*args))

	#moveBy
	def moveBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().moveBy(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().blur(*args))

	#setInterval
	def setInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setInterval(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().focus(*args))

	#alert
	def alert(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().alert(*args))

	#showModalDialog
	def showModalDialog(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().showModalDialog(*args))

	#scrollBy
	def scrollBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().scrollBy(*args))

	#resizeTo
	def resizeTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().resizeTo(*args))

	#scroll
	def scroll(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().scroll(*args))

wrapperClasses['{332C4427-26CB-11D0-B483-00C04FD90119}'] = IHTMLWindow2
backWrapperClasses[IHTMLWindow2] = '{332C4427-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLWindow3
#
class IHTMLWindow3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLWindow3
		return self.__instance__.QueryInterface(kls)
	#onafterprint
	def _get_onafterprint(self):
		return wrap(self.__get_instance().onafterprint)
	def _set_onafterprint(self, value):
		self.__get_instance().onafterprint = unwrap(value)
	onafterprint = property(_get_onafterprint, _set_onafterprint)

	#onbeforeprint
	def _get_onbeforeprint(self):
		return wrap(self.__get_instance().onbeforeprint)
	def _set_onbeforeprint(self, value):
		self.__get_instance().onbeforeprint = unwrap(value)
	onbeforeprint = property(_get_onbeforeprint, _set_onbeforeprint)

	#screenTop
	def _get_screenTop(self):
		return wrap(self.__get_instance().screenTop)
	def _set_screenTop(self, value):
		self.__get_instance().screenTop = unwrap(value)
	screenTop = property(_get_screenTop, _set_screenTop)

	#screenLeft
	def _get_screenLeft(self):
		return wrap(self.__get_instance().screenLeft)
	def _set_screenLeft(self, value):
		self.__get_instance().screenLeft = unwrap(value)
	screenLeft = property(_get_screenLeft, _set_screenLeft)

	#clipboardData
	def _get_clipboardData(self):
		return wrap(self.__get_instance().clipboardData)
	def _set_clipboardData(self, value):
		self.__get_instance().clipboardData = unwrap(value)
	clipboardData = property(_get_clipboardData, _set_clipboardData)

	#setInterval
	def setInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setInterval(*args))

	#showModelessDialog
	def showModelessDialog(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().showModelessDialog(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().attachEvent(*args))

	#print_
	def print_(self, *args):
		args = map(unwrap, args)
		fn = getattr('print', self.__get_instance())
		return wrap(fn(*args))

	#setTimeout
	def setTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().setTimeout(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().detachEvent(*args))

wrapperClasses['{3050F4AE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLWindow3
backWrapperClasses[IHTMLWindow3] = '{3050F4AE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLWindow2
#
class DispHTMLWindow2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLWindow2
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F55D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLWindow2
backWrapperClasses[DispHTMLWindow2] = '{3050F55D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLDocumentEvents2
#
class HTMLDocumentEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLDocumentEvents2
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F613-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDocumentEvents2
backWrapperClasses[HTMLDocumentEvents2] = '{3050F613-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLDocumentEvents
#
class HTMLDocumentEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLDocumentEvents
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F260-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDocumentEvents
backWrapperClasses[HTMLDocumentEvents] = '{3050F260-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLTextContainerEvents
#
class HTMLTextContainerEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTextContainerEvents
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{1FF6AA72-5842-11CF-A707-00AA00C0098D}'] = HTMLTextContainerEvents
backWrapperClasses[HTMLTextContainerEvents] = '{1FF6AA72-5842-11CF-A707-00AA00C0098D}'

##############################
# HTMLTextContainerEvents2
#
class HTMLTextContainerEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTextContainerEvents2
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F624-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLTextContainerEvents2
backWrapperClasses[HTMLTextContainerEvents2] = '{3050F624-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument
#
class IHTMLDocument(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument
		return self.__instance__.QueryInterface(kls)
	#Script
	def _get_Script(self):
		return wrap(self.__get_instance().Script)
	def _set_Script(self, value):
		self.__get_instance().Script = unwrap(value)
	Script = property(_get_Script, _set_Script)

wrapperClasses['{626FC520-A41E-11CF-A731-00A0C9082637}'] = IHTMLDocument
backWrapperClasses[IHTMLDocument] = '{626FC520-A41E-11CF-A731-00A0C9082637}'

##############################
# IHTMLDocument2
#
class IHTMLDocument2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument2
		return self.__instance__.QueryInterface(kls)
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#fileUpdatedDate
	def _get_fileUpdatedDate(self):
		return wrap(self.__get_instance().fileUpdatedDate)
	def _set_fileUpdatedDate(self, value):
		self.__get_instance().fileUpdatedDate = unwrap(value)
	fileUpdatedDate = property(_get_fileUpdatedDate, _set_fileUpdatedDate)

	#all
	def _get_all(self):
		return wrap(self.__get_instance().all)
	def _set_all(self, value):
		self.__get_instance().all = unwrap(value)
	all = property(_get_all, _set_all)

	#selection
	def _get_selection(self):
		return wrap(self.__get_instance().selection)
	def _set_selection(self, value):
		self.__get_instance().selection = unwrap(value)
	selection = property(_get_selection, _set_selection)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance().protocol)
	def _set_protocol(self, value):
		self.__get_instance().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#links
	def _get_links(self):
		return wrap(self.__get_instance().links)
	def _set_links(self, value):
		self.__get_instance().links = unwrap(value)
	links = property(_get_links, _set_links)

	#onafterupdate
	def _get_onafterupdate(self):
		return wrap(self.__get_instance().onafterupdate)
	def _set_onafterupdate(self, value):
		self.__get_instance().onafterupdate = unwrap(value)
	onafterupdate = property(_get_onafterupdate, _set_onafterupdate)

	#domain
	def _get_domain(self):
		return wrap(self.__get_instance().domain)
	def _set_domain(self, value):
		self.__get_instance().domain = unwrap(value)
	domain = property(_get_domain, _set_domain)

	#onmousedown
	def _get_onmousedown(self):
		return wrap(self.__get_instance().onmousedown)
	def _set_onmousedown(self, value):
		self.__get_instance().onmousedown = unwrap(value)
	onmousedown = property(_get_onmousedown, _set_onmousedown)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#designMode
	def _get_designMode(self):
		return wrap(self.__get_instance().designMode)
	def _set_designMode(self, value):
		self.__get_instance().designMode = unwrap(value)
	designMode = property(_get_designMode, _set_designMode)

	#plugins
	def _get_plugins(self):
		return wrap(self.__get_instance().plugins)
	def _set_plugins(self, value):
		self.__get_instance().plugins = unwrap(value)
	plugins = property(_get_plugins, _set_plugins)

	#frames
	def _get_frames(self):
		return wrap(self.__get_instance().frames)
	def _set_frames(self, value):
		self.__get_instance().frames = unwrap(value)
	frames = property(_get_frames, _set_frames)

	#onrowexit
	def _get_onrowexit(self):
		return wrap(self.__get_instance().onrowexit)
	def _set_onrowexit(self, value):
		self.__get_instance().onrowexit = unwrap(value)
	onrowexit = property(_get_onrowexit, _set_onrowexit)

	#fileModifiedDate
	def _get_fileModifiedDate(self):
		return wrap(self.__get_instance().fileModifiedDate)
	def _set_fileModifiedDate(self, value):
		self.__get_instance().fileModifiedDate = unwrap(value)
	fileModifiedDate = property(_get_fileModifiedDate, _set_fileModifiedDate)

	#title
	def _get_title(self):
		return wrap(self.__get_instance().title)
	def _set_title(self, value):
		self.__get_instance().title = unwrap(value)
	title = property(_get_title, _set_title)

	#applets
	def _get_applets(self):
		return wrap(self.__get_instance().applets)
	def _set_applets(self, value):
		self.__get_instance().applets = unwrap(value)
	applets = property(_get_applets, _set_applets)

	#charset
	def _get_charset(self):
		return wrap(self.__get_instance().charset)
	def _set_charset(self, value):
		self.__get_instance().charset = unwrap(value)
	charset = property(_get_charset, _set_charset)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#forms
	def _get_forms(self):
		return wrap(self.__get_instance().forms)
	def _set_forms(self, value):
		self.__get_instance().forms = unwrap(value)
	forms = property(_get_forms, _set_forms)

	#URL
	def _get_URL(self):
		return wrap(self.__get_instance().URL)
	def _set_URL(self, value):
		self.__get_instance().URL = unwrap(value)
	URL = property(_get_URL, _set_URL)

	#onmouseup
	def _get_onmouseup(self):
		return wrap(self.__get_instance().onmouseup)
	def _set_onmouseup(self, value):
		self.__get_instance().onmouseup = unwrap(value)
	onmouseup = property(_get_onmouseup, _set_onmouseup)

	#linkColor
	def _get_linkColor(self):
		return wrap(self.__get_instance().linkColor)
	def _set_linkColor(self, value):
		self.__get_instance().linkColor = unwrap(value)
	linkColor = property(_get_linkColor, _set_linkColor)

	#vlinkColor
	def _get_vlinkColor(self):
		return wrap(self.__get_instance().vlinkColor)
	def _set_vlinkColor(self, value):
		self.__get_instance().vlinkColor = unwrap(value)
	vlinkColor = property(_get_vlinkColor, _set_vlinkColor)

	#onclick
	def _get_onclick(self):
		return wrap(self.__get_instance().onclick)
	def _set_onclick(self, value):
		self.__get_instance().onclick = unwrap(value)
	onclick = property(_get_onclick, _set_onclick)

	#onbeforeupdate
	def _get_onbeforeupdate(self):
		return wrap(self.__get_instance().onbeforeupdate)
	def _set_onbeforeupdate(self, value):
		self.__get_instance().onbeforeupdate = unwrap(value)
	onbeforeupdate = property(_get_onbeforeupdate, _set_onbeforeupdate)

	#onmousemove
	def _get_onmousemove(self):
		return wrap(self.__get_instance().onmousemove)
	def _set_onmousemove(self, value):
		self.__get_instance().onmousemove = unwrap(value)
	onmousemove = property(_get_onmousemove, _set_onmousemove)

	#onrowenter
	def _get_onrowenter(self):
		return wrap(self.__get_instance().onrowenter)
	def _set_onrowenter(self, value):
		self.__get_instance().onrowenter = unwrap(value)
	onrowenter = property(_get_onrowenter, _set_onrowenter)

	#location
	def _get_location(self):
		return wrap(self.__get_instance().location)
	def _set_location(self, value):
		self.__get_instance().location = unwrap(value)
	location = property(_get_location, _set_location)

	#body
	def _get_body(self):
		return wrap(self.__get_instance(MSHTML.DispHTMLBody).body)
	def _set_body(self, value):
		self.__get_instance().body = unwrap(value)
	body = property(_get_body, _set_body)

	#ondragstart
	def _get_ondragstart(self):
		return wrap(self.__get_instance().ondragstart)
	def _set_ondragstart(self, value):
		self.__get_instance().ondragstart = unwrap(value)
	ondragstart = property(_get_ondragstart, _set_ondragstart)

	#anchors
	def _get_anchors(self):
		return wrap(self.__get_instance().anchors)
	def _set_anchors(self, value):
		self.__get_instance().anchors = unwrap(value)
	anchors = property(_get_anchors, _set_anchors)

	#onmouseout
	def _get_onmouseout(self):
		return wrap(self.__get_instance().onmouseout)
	def _set_onmouseout(self, value):
		self.__get_instance().onmouseout = unwrap(value)
	onmouseout = property(_get_onmouseout, _set_onmouseout)

	#onkeypress
	def _get_onkeypress(self):
		return wrap(self.__get_instance().onkeypress)
	def _set_onkeypress(self, value):
		self.__get_instance().onkeypress = unwrap(value)
	onkeypress = property(_get_onkeypress, _set_onkeypress)

	#embeds
	def _get_embeds(self):
		return wrap(self.__get_instance().embeds)
	def _set_embeds(self, value):
		self.__get_instance().embeds = unwrap(value)
	embeds = property(_get_embeds, _set_embeds)

	#images
	def _get_images(self):
		return wrap(self.__get_instance().images)
	def _set_images(self, value):
		self.__get_instance().images = unwrap(value)
	images = property(_get_images, _set_images)

	#onerrorupdate
	def _get_onerrorupdate(self):
		return wrap(self.__get_instance().onerrorupdate)
	def _set_onerrorupdate(self, value):
		self.__get_instance().onerrorupdate = unwrap(value)
	onerrorupdate = property(_get_onerrorupdate, _set_onerrorupdate)

	#onkeydown
	def _get_onkeydown(self):
		return wrap(self.__get_instance().onkeydown)
	def _set_onkeydown(self, value):
		self.__get_instance().onkeydown = unwrap(value)
	onkeydown = property(_get_onkeydown, _set_onkeydown)

	#fileCreatedDate
	def _get_fileCreatedDate(self):
		return wrap(self.__get_instance().fileCreatedDate)
	def _set_fileCreatedDate(self, value):
		self.__get_instance().fileCreatedDate = unwrap(value)
	fileCreatedDate = property(_get_fileCreatedDate, _set_fileCreatedDate)

	#onkeyup
	def _get_onkeyup(self):
		return wrap(self.__get_instance().onkeyup)
	def _set_onkeyup(self, value):
		self.__get_instance().onkeyup = unwrap(value)
	onkeyup = property(_get_onkeyup, _set_onkeyup)

	#cookie
	def _get_cookie(self):
		return wrap(self.__get_instance().cookie)
	def _set_cookie(self, value):
		self.__get_instance().cookie = unwrap(value)
	cookie = property(_get_cookie, _set_cookie)

	#fileSize
	def _get_fileSize(self):
		return wrap(self.__get_instance().fileSize)
	def _set_fileSize(self, value):
		self.__get_instance().fileSize = unwrap(value)
	fileSize = property(_get_fileSize, _set_fileSize)

	#scripts
	def _get_scripts(self):
		return wrap(self.__get_instance().scripts)
	def _set_scripts(self, value):
		self.__get_instance().scripts = unwrap(value)
	scripts = property(_get_scripts, _set_scripts)

	#parentWindow
	def _get_parentWindow(self):
		return wrap(self.__get_instance().parentWindow)
	def _set_parentWindow(self, value):
		self.__get_instance().parentWindow = unwrap(value)
	parentWindow = property(_get_parentWindow, _set_parentWindow)

	#activeElement
	def _get_activeElement(self):
		return wrap(self.__get_instance().activeElement)
	def _set_activeElement(self, value):
		self.__get_instance().activeElement = unwrap(value)
	activeElement = property(_get_activeElement, _set_activeElement)

	#expando
	def _get_expando(self):
		return wrap(self.__get_instance().expando)
	def _set_expando(self, value):
		self.__get_instance().expando = unwrap(value)
	expando = property(_get_expando, _set_expando)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#referrer
	def _get_referrer(self):
		return wrap(self.__get_instance().referrer)
	def _set_referrer(self, value):
		self.__get_instance().referrer = unwrap(value)
	referrer = property(_get_referrer, _set_referrer)

	#onmouseover
	def _get_onmouseover(self):
		return wrap(self.__get_instance().onmouseover)
	def _set_onmouseover(self, value):
		self.__get_instance().onmouseover = unwrap(value)
	onmouseover = property(_get_onmouseover, _set_onmouseover)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#styleSheets
	def _get_styleSheets(self):
		return wrap(self.__get_instance().styleSheets)
	def _set_styleSheets(self, value):
		self.__get_instance().styleSheets = unwrap(value)
	styleSheets = property(_get_styleSheets, _set_styleSheets)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#lastModified
	def _get_lastModified(self):
		return wrap(self.__get_instance().lastModified)
	def _set_lastModified(self, value):
		self.__get_instance().lastModified = unwrap(value)
	lastModified = property(_get_lastModified, _set_lastModified)

	#alinkColor
	def _get_alinkColor(self):
		return wrap(self.__get_instance().alinkColor)
	def _set_alinkColor(self, value):
		self.__get_instance().alinkColor = unwrap(value)
	alinkColor = property(_get_alinkColor, _set_alinkColor)

	#security
	def _get_security(self):
		return wrap(self.__get_instance().security)
	def _set_security(self, value):
		self.__get_instance().security = unwrap(value)
	security = property(_get_security, _set_security)

	#ondblclick
	def _get_ondblclick(self):
		return wrap(self.__get_instance().ondblclick)
	def _set_ondblclick(self, value):
		self.__get_instance().ondblclick = unwrap(value)
	ondblclick = property(_get_ondblclick, _set_ondblclick)

	#onselectstart
	def _get_onselectstart(self):
		return wrap(self.__get_instance().onselectstart)
	def _set_onselectstart(self, value):
		self.__get_instance().onselectstart = unwrap(value)
	onselectstart = property(_get_onselectstart, _set_onselectstart)

	#fgColor
	def _get_fgColor(self):
		return wrap(self.__get_instance().fgColor)
	def _set_fgColor(self, value):
		self.__get_instance().fgColor = unwrap(value)
	fgColor = property(_get_fgColor, _set_fgColor)

	#defaultCharset
	def _get_defaultCharset(self):
		return wrap(self.__get_instance().defaultCharset)
	def _set_defaultCharset(self, value):
		self.__get_instance().defaultCharset = unwrap(value)
	defaultCharset = property(_get_defaultCharset, _set_defaultCharset)

	#writeln
	def writeln(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().writeln(*args))

	#execCommandShowHelp
	def execCommandShowHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().execCommandShowHelp(*args))

	#execCommand
	def execCommand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().execCommand(*args))

	#clear
	def clear(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().clear(*args))

	#queryCommandState
	def queryCommandState(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandState(*args))

	#createStyleSheet
	def createStyleSheet(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createStyleSheet(*args))

	#createElement
	def createElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createElement(*args))

	#write
	def write(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().write(*args))

	#queryCommandEnabled
	def queryCommandEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandEnabled(*args))

	#queryCommandText
	def queryCommandText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandText(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().toString(*args))

	#queryCommandIndeterm
	def queryCommandIndeterm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandIndeterm(*args))

	#queryCommandValue
	def queryCommandValue(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandValue(*args))

	#close
	def close(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().close(*args))

	#elementFromPoint
	def elementFromPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().elementFromPoint(*args))

	#open
	def open(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().open(*args))

	#queryCommandSupported
	def queryCommandSupported(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().queryCommandSupported(*args))

wrapperClasses['{332C4425-26CB-11D0-B483-00C04FD90119}'] = IHTMLDocument2
backWrapperClasses[IHTMLDocument2] = '{332C4425-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLDocument3
#
class IHTMLDocument3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument3
		return self.__instance__.QueryInterface(kls)
	#oncontextmenu
	def _get_oncontextmenu(self):
		return wrap(self.__get_instance().oncontextmenu)
	def _set_oncontextmenu(self, value):
		self.__get_instance().oncontextmenu = unwrap(value)
	oncontextmenu = property(_get_oncontextmenu, _set_oncontextmenu)

	#onrowsdelete
	def _get_onrowsdelete(self):
		return wrap(self.__get_instance().onrowsdelete)
	def _set_onrowsdelete(self, value):
		self.__get_instance().onrowsdelete = unwrap(value)
	onrowsdelete = property(_get_onrowsdelete, _set_onrowsdelete)

	#ondataavailable
	def _get_ondataavailable(self):
		return wrap(self.__get_instance().ondataavailable)
	def _set_ondataavailable(self, value):
		self.__get_instance().ondataavailable = unwrap(value)
	ondataavailable = property(_get_ondataavailable, _set_ondataavailable)

	#documentElement
	def _get_documentElement(self):
		return wrap(self.__get_instance().documentElement)
	def _set_documentElement(self, value):
		self.__get_instance().documentElement = unwrap(value)
	documentElement = property(_get_documentElement, _set_documentElement)

	#oncellchange
	def _get_oncellchange(self):
		return wrap(self.__get_instance().oncellchange)
	def _set_oncellchange(self, value):
		self.__get_instance().oncellchange = unwrap(value)
	oncellchange = property(_get_oncellchange, _set_oncellchange)

	#enableDownload
	def _get_enableDownload(self):
		return wrap(self.__get_instance().enableDownload)
	def _set_enableDownload(self, value):
		self.__get_instance().enableDownload = unwrap(value)
	enableDownload = property(_get_enableDownload, _set_enableDownload)

	#onpropertychange
	def _get_onpropertychange(self):
		return wrap(self.__get_instance().onpropertychange)
	def _set_onpropertychange(self, value):
		self.__get_instance().onpropertychange = unwrap(value)
	onpropertychange = property(_get_onpropertychange, _set_onpropertychange)

	#baseUrl
	def _get_baseUrl(self):
		return wrap(self.__get_instance().baseUrl)
	def _set_baseUrl(self, value):
		self.__get_instance().baseUrl = unwrap(value)
	baseUrl = property(_get_baseUrl, _set_baseUrl)

	#onrowsinserted
	def _get_onrowsinserted(self):
		return wrap(self.__get_instance().onrowsinserted)
	def _set_onrowsinserted(self, value):
		self.__get_instance().onrowsinserted = unwrap(value)
	onrowsinserted = property(_get_onrowsinserted, _set_onrowsinserted)

	#ondatasetchanged
	def _get_ondatasetchanged(self):
		return wrap(self.__get_instance().ondatasetchanged)
	def _set_ondatasetchanged(self, value):
		self.__get_instance().ondatasetchanged = unwrap(value)
	ondatasetchanged = property(_get_ondatasetchanged, _set_ondatasetchanged)

	#onbeforeeditfocus
	def _get_onbeforeeditfocus(self):
		return wrap(self.__get_instance().onbeforeeditfocus)
	def _set_onbeforeeditfocus(self, value):
		self.__get_instance().onbeforeeditfocus = unwrap(value)
	onbeforeeditfocus = property(_get_onbeforeeditfocus, _set_onbeforeeditfocus)

	#ondatasetcomplete
	def _get_ondatasetcomplete(self):
		return wrap(self.__get_instance().ondatasetcomplete)
	def _set_ondatasetcomplete(self, value):
		self.__get_instance().ondatasetcomplete = unwrap(value)
	ondatasetcomplete = property(_get_ondatasetcomplete, _set_ondatasetcomplete)

	#uniqueID
	def _get_uniqueID(self):
		return wrap(self.__get_instance().uniqueID)
	def _set_uniqueID(self, value):
		self.__get_instance().uniqueID = unwrap(value)
	uniqueID = property(_get_uniqueID, _set_uniqueID)

	#inheritStyleSheets
	def _get_inheritStyleSheets(self):
		return wrap(self.__get_instance().inheritStyleSheets)
	def _set_inheritStyleSheets(self, value):
		self.__get_instance().inheritStyleSheets = unwrap(value)
	inheritStyleSheets = property(_get_inheritStyleSheets, _set_inheritStyleSheets)

	#childNodes
	def _get_childNodes(self):
		return wrap(self.__get_instance().childNodes)
	def _set_childNodes(self, value):
		self.__get_instance().childNodes = unwrap(value)
	childNodes = property(_get_childNodes, _set_childNodes)

	#parentDocument
	def _get_parentDocument(self):
		return wrap(self.__get_instance().parentDocument)
	def _set_parentDocument(self, value):
		self.__get_instance().parentDocument = unwrap(value)
	parentDocument = property(_get_parentDocument, _set_parentDocument)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance().dir)
	def _set_dir(self, value):
		self.__get_instance().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#onstop
	def _get_onstop(self):
		return wrap(self.__get_instance().onstop)
	def _set_onstop(self, value):
		self.__get_instance().onstop = unwrap(value)
	onstop = property(_get_onstop, _set_onstop)

	#getElementsByName
	def getElementsByName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getElementsByName(*args))

	#recalc
	def recalc(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().recalc(*args))

	#getElementsByTagName
	def getElementsByTagName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getElementsByTagName(*args))

	#releaseCapture
	def releaseCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().releaseCapture(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().attachEvent(*args))

	#getElementById
	def getElementById(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().getElementById(*args))

	#createDocumentFragment
	def createDocumentFragment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createDocumentFragment(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().detachEvent(*args))

	#createTextNode
	def createTextNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTextNode(*args))

wrapperClasses['{3050F485-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument3
backWrapperClasses[IHTMLDocument3] = '{3050F485-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument4
#
class IHTMLDocument4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument4
		return self.__instance__.QueryInterface(kls)
	#media
	def _get_media(self):
		return wrap(self.__get_instance().media)
	def _set_media(self, value):
		self.__get_instance().media = unwrap(value)
	media = property(_get_media, _set_media)

	#onselectionchange
	def _get_onselectionchange(self):
		return wrap(self.__get_instance().onselectionchange)
	def _set_onselectionchange(self, value):
		self.__get_instance().onselectionchange = unwrap(value)
	onselectionchange = property(_get_onselectionchange, _set_onselectionchange)

	#URLUnencoded
	def _get_URLUnencoded(self):
		return wrap(self.__get_instance().URLUnencoded)
	def _set_URLUnencoded(self, value):
		self.__get_instance().URLUnencoded = unwrap(value)
	URLUnencoded = property(_get_URLUnencoded, _set_URLUnencoded)

	#namespaces
	def _get_namespaces(self):
		return wrap(self.__get_instance().namespaces)
	def _set_namespaces(self, value):
		self.__get_instance().namespaces = unwrap(value)
	namespaces = property(_get_namespaces, _set_namespaces)

	#oncontrolselect
	def _get_oncontrolselect(self):
		return wrap(self.__get_instance().oncontrolselect)
	def _set_oncontrolselect(self, value):
		self.__get_instance().oncontrolselect = unwrap(value)
	oncontrolselect = property(_get_oncontrolselect, _set_oncontrolselect)

	#hasFocus
	def hasFocus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().hasFocus(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().focus(*args))

	#createDocumentFromUrl
	def createDocumentFromUrl(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createDocumentFromUrl(*args))

	#createRenderStyle
	def createRenderStyle(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createRenderStyle(*args))

	#createEventObject
	def createEventObject(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createEventObject(*args))

	#fireEvent
	def fireEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().fireEvent(*args))

wrapperClasses['{3050F69A-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument4
backWrapperClasses[IHTMLDocument4] = '{3050F69A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument5
#
class IHTMLDocument5(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument5
		return self.__instance__.QueryInterface(kls)
	#ondeactivate
	def _get_ondeactivate(self):
		return wrap(self.__get_instance().ondeactivate)
	def _set_ondeactivate(self, value):
		self.__get_instance().ondeactivate = unwrap(value)
	ondeactivate = property(_get_ondeactivate, _set_ondeactivate)

	#implementation
	def _get_implementation(self):
		return wrap(self.__get_instance().implementation)
	def _set_implementation(self, value):
		self.__get_instance().implementation = unwrap(value)
	implementation = property(_get_implementation, _set_implementation)

	#onfocusout
	def _get_onfocusout(self):
		return wrap(self.__get_instance().onfocusout)
	def _set_onfocusout(self, value):
		self.__get_instance().onfocusout = unwrap(value)
	onfocusout = property(_get_onfocusout, _set_onfocusout)

	#doctype
	def _get_doctype(self):
		return wrap(self.__get_instance().doctype)
	def _set_doctype(self, value):
		self.__get_instance().doctype = unwrap(value)
	doctype = property(_get_doctype, _set_doctype)

	#onbeforeactivate
	def _get_onbeforeactivate(self):
		return wrap(self.__get_instance().onbeforeactivate)
	def _set_onbeforeactivate(self, value):
		self.__get_instance().onbeforeactivate = unwrap(value)
	onbeforeactivate = property(_get_onbeforeactivate, _set_onbeforeactivate)

	#onbeforedeactivate
	def _get_onbeforedeactivate(self):
		return wrap(self.__get_instance().onbeforedeactivate)
	def _set_onbeforedeactivate(self, value):
		self.__get_instance().onbeforedeactivate = unwrap(value)
	onbeforedeactivate = property(_get_onbeforedeactivate, _set_onbeforedeactivate)

	#onactivate
	def _get_onactivate(self):
		return wrap(self.__get_instance().onactivate)
	def _set_onactivate(self, value):
		self.__get_instance().onactivate = unwrap(value)
	onactivate = property(_get_onactivate, _set_onactivate)

	#compatMode
	def _get_compatMode(self):
		return wrap(self.__get_instance().compatMode)
	def _set_compatMode(self, value):
		self.__get_instance().compatMode = unwrap(value)
	compatMode = property(_get_compatMode, _set_compatMode)

	#onmousewheel
	def _get_onmousewheel(self):
		return wrap(self.__get_instance().onmousewheel)
	def _set_onmousewheel(self, value):
		self.__get_instance().onmousewheel = unwrap(value)
	onmousewheel = property(_get_onmousewheel, _set_onmousewheel)

	#onfocusin
	def _get_onfocusin(self):
		return wrap(self.__get_instance().onfocusin)
	def _set_onfocusin(self, value):
		self.__get_instance().onfocusin = unwrap(value)
	onfocusin = property(_get_onfocusin, _set_onfocusin)

	#createAttribute
	def createAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createAttribute(*args))

	#createComment
	def createComment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createComment(*args))

wrapperClasses['{3050F80C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument5
backWrapperClasses[IHTMLDocument5] = '{3050F80C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLDocument
#
class DispHTMLDocument(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLDocument
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F55F-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLDocument
backWrapperClasses[DispHTMLDocument] = '{3050F55F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCommentElement
#
class IHTMLCommentElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCommentElement
		return self.__instance__.QueryInterface(kls)
	#text
	def _get_text(self):
		return wrap(self.__get_instance().text)
	def _set_text(self, value):
		self.__get_instance().text = unwrap(value)
	text = property(_get_text, _set_text)

	#atomic
	def _get_atomic(self):
		return wrap(self.__get_instance().atomic)
	def _set_atomic(self, value):
		self.__get_instance().atomic = unwrap(value)
	atomic = property(_get_atomic, _set_atomic)

wrapperClasses['{3050F20C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCommentElement
backWrapperClasses[IHTMLCommentElement] = '{3050F20C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCommentElement2
#
class IHTMLCommentElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCommentElement2
		return self.__instance__.QueryInterface(kls)
	#length
	def _get_length(self):
		return wrap(self.__get_instance().length)
	def _set_length(self, value):
		self.__get_instance().length = unwrap(value)
	length = property(_get_length, _set_length)

	#data
	def _get_data(self):
		return wrap(self.__get_instance().data)
	def _set_data(self, value):
		self.__get_instance().data = unwrap(value)
	data = property(_get_data, _set_data)

	#appendData
	def appendData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().appendData(*args))

	#deleteData
	def deleteData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteData(*args))

	#substringData
	def substringData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().substringData(*args))

	#insertData
	def insertData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertData(*args))

	#replaceData
	def replaceData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().replaceData(*args))

wrapperClasses['{3050F813-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCommentElement2
backWrapperClasses[IHTMLCommentElement2] = '{3050F813-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLCommentElement
#
class DispHTMLCommentElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLCommentElement
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F50A-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLCommentElement
backWrapperClasses[DispHTMLCommentElement] = '{3050F50A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLElementEvents2
#
class HTMLElementEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLElementEvents2
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F60F-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLElementEvents2
backWrapperClasses[HTMLElementEvents2] = '{3050F60F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLElementEvents
#
class HTMLElementEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLElementEvents
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F33C-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLElementEvents
backWrapperClasses[HTMLElementEvents] = '{3050F33C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLTableEvents
#
class HTMLTableEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTableEvents
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F407-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLTableEvents
backWrapperClasses[HTMLTableEvents] = '{3050F407-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableCaption
#
class IHTMLTableCaption(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableCaption
		return self.__instance__.QueryInterface(kls)
	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

wrapperClasses['{3050F2EB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableCaption
backWrapperClasses[IHTMLTableCaption] = '{3050F2EB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTable
#
class IHTMLTable(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTable
		return self.__instance__.QueryInterface(kls)
	#frame
	def _get_frame(self):
		return wrap(self.__get_instance().frame)
	def _set_frame(self, value):
		self.__get_instance().frame = unwrap(value)
	frame = property(_get_frame, _set_frame)

	#borderColorDark
	def _get_borderColorDark(self):
		return wrap(self.__get_instance().borderColorDark)
	def _set_borderColorDark(self, value):
		self.__get_instance().borderColorDark = unwrap(value)
	borderColorDark = property(_get_borderColorDark, _set_borderColorDark)

	#cols
	def _get_cols(self):
		return wrap(self.__get_instance().cols)
	def _set_cols(self, value):
		self.__get_instance().cols = unwrap(value)
	cols = property(_get_cols, _set_cols)

	#height
	def _get_height(self):
		return wrap(self.__get_instance().height)
	def _set_height(self, value):
		self.__get_instance().height = unwrap(value)
	height = property(_get_height, _set_height)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#tFoot
	def _get_tFoot(self):
		return wrap(self.__get_instance().tFoot)
	def _set_tFoot(self, value):
		self.__get_instance().tFoot = unwrap(value)
	tFoot = property(_get_tFoot, _set_tFoot)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#tHead
	def _get_tHead(self):
		return wrap(self.__get_instance().tHead)
	def _set_tHead(self, value):
		self.__get_instance().tHead = unwrap(value)
	tHead = property(_get_tHead, _set_tHead)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance().rows)
	def _set_rows(self, value):
		self.__get_instance().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#cellSpacing
	def _get_cellSpacing(self):
		return wrap(self.__get_instance().cellSpacing)
	def _set_cellSpacing(self, value):
		self.__get_instance().cellSpacing = unwrap(value)
	cellSpacing = property(_get_cellSpacing, _set_cellSpacing)

	#dataPageSize
	def _get_dataPageSize(self):
		return wrap(self.__get_instance().dataPageSize)
	def _set_dataPageSize(self, value):
		self.__get_instance().dataPageSize = unwrap(value)
	dataPageSize = property(_get_dataPageSize, _set_dataPageSize)

	#width
	def _get_width(self):
		return wrap(self.__get_instance().width)
	def _set_width(self, value):
		self.__get_instance().width = unwrap(value)
	width = property(_get_width, _set_width)

	#tBodies
	def _get_tBodies(self):
		return wrap(self.__get_instance().tBodies)
	def _set_tBodies(self, value):
		self.__get_instance().tBodies = unwrap(value)
	tBodies = property(_get_tBodies, _set_tBodies)

	#rules
	def _get_rules(self):
		return wrap(self.__get_instance().rules)
	def _set_rules(self, value):
		self.__get_instance().rules = unwrap(value)
	rules = property(_get_rules, _set_rules)

	#borderColorLight
	def _get_borderColorLight(self):
		return wrap(self.__get_instance().borderColorLight)
	def _set_borderColorLight(self, value):
		self.__get_instance().borderColorLight = unwrap(value)
	borderColorLight = property(_get_borderColorLight, _set_borderColorLight)

	#background
	def _get_background(self):
		return wrap(self.__get_instance().background)
	def _set_background(self, value):
		self.__get_instance().background = unwrap(value)
	background = property(_get_background, _set_background)

	#cellPadding
	def _get_cellPadding(self):
		return wrap(self.__get_instance().cellPadding)
	def _set_cellPadding(self, value):
		self.__get_instance().cellPadding = unwrap(value)
	cellPadding = property(_get_cellPadding, _set_cellPadding)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#caption
	def _get_caption(self):
		return wrap(self.__get_instance().caption)
	def _set_caption(self, value):
		self.__get_instance().caption = unwrap(value)
	caption = property(_get_caption, _set_caption)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#deleteTFoot
	def deleteTFoot(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteTFoot(*args))

	#deleteTHead
	def deleteTHead(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteTHead(*args))

	#createTFoot
	def createTFoot(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTFoot(*args))

	#refresh
	def refresh(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().refresh(*args))

	#createCaption
	def createCaption(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createCaption(*args))

	#insertRow
	def insertRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertRow(*args))

	#deleteRow
	def deleteRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteRow(*args))

	#deleteCaption
	def deleteCaption(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteCaption(*args))

	#nextPage
	def nextPage(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().nextPage(*args))

	#createTHead
	def createTHead(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().createTHead(*args))

	#previousPage
	def previousPage(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().previousPage(*args))

wrapperClasses['{3050F21E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTable
backWrapperClasses[IHTMLTable] = '{3050F21E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableSection
#
class IHTMLTableSection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableSection
		return self.__instance__.QueryInterface(kls)
	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance().rows)
	def _set_rows(self, value):
		self.__get_instance().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

	#insertRow
	def insertRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertRow(*args))

	#deleteRow
	def deleteRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteRow(*args))

wrapperClasses['{3050F23B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableSection
backWrapperClasses[IHTMLTableSection] = '{3050F23B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableRow
#
class IHTMLTableRow(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableRow
		return self.__instance__.QueryInterface(kls)
	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#sectionRowIndex
	def _get_sectionRowIndex(self):
		return wrap(self.__get_instance().sectionRowIndex)
	def _set_sectionRowIndex(self, value):
		self.__get_instance().sectionRowIndex = unwrap(value)
	sectionRowIndex = property(_get_sectionRowIndex, _set_sectionRowIndex)

	#rowIndex
	def _get_rowIndex(self):
		return wrap(self.__get_instance().rowIndex)
	def _set_rowIndex(self, value):
		self.__get_instance().rowIndex = unwrap(value)
	rowIndex = property(_get_rowIndex, _set_rowIndex)

	#borderColorLight
	def _get_borderColorLight(self):
		return wrap(self.__get_instance().borderColorLight)
	def _set_borderColorLight(self, value):
		self.__get_instance().borderColorLight = unwrap(value)
	borderColorLight = property(_get_borderColorLight, _set_borderColorLight)

	#align
	def _get_align(self):
		return wrap(self.__get_instance().align)
	def _set_align(self, value):
		self.__get_instance().align = unwrap(value)
	align = property(_get_align, _set_align)

	#borderColorDark
	def _get_borderColorDark(self):
		return wrap(self.__get_instance().borderColorDark)
	def _set_borderColorDark(self, value):
		self.__get_instance().borderColorDark = unwrap(value)
	borderColorDark = property(_get_borderColorDark, _set_borderColorDark)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

	#cells
	def _get_cells(self):
		return wrap(self.__get_instance().cells)
	def _set_cells(self, value):
		self.__get_instance().cells = unwrap(value)
	cells = property(_get_cells, _set_cells)

	#insertCell
	def insertCell(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().insertCell(*args))

	#deleteCell
	def deleteCell(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().deleteCell(*args))

wrapperClasses['{3050F23C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableRow
backWrapperClasses[IHTMLTableRow] = '{3050F23C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLTable
#
class DispHTMLTable(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLTable
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F532-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLTable
backWrapperClasses[DispHTMLTable] = '{3050F532-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLTableRow
#
class DispHTMLTableRow(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLTableRow
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F535-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLTableRow
backWrapperClasses[DispHTMLTableRow] = '{3050F535-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLScriptElement
#
class IHTMLScriptElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScriptElement
		return self.__instance__.QueryInterface(kls)
	#defer
	def _get_defer(self):
		return wrap(self.__get_instance().defer)
	def _set_defer(self, value):
		self.__get_instance().defer = unwrap(value)
	defer = property(_get_defer, _set_defer)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#src
	def _get_src(self):
		return wrap(self.__get_instance().src)
	def _set_src(self, value):
		self.__get_instance().src = unwrap(value)
	src = property(_get_src, _set_src)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance().onerror)
	def _set_onerror(self, value):
		self.__get_instance().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#text
	def _get_text(self):
		return wrap(self.__get_instance().text)
	def _set_text(self, value):
		self.__get_instance().text = unwrap(value)
	text = property(_get_text, _set_text)

	#htmlFor
	def _get_htmlFor(self):
		return wrap(self.__get_instance().htmlFor)
	def _set_htmlFor(self, value):
		self.__get_instance().htmlFor = unwrap(value)
	htmlFor = property(_get_htmlFor, _set_htmlFor)

	#type
	def _get_type(self):
		return wrap(self.__get_instance().type)
	def _set_type(self, value):
		self.__get_instance().type = unwrap(value)
	type = property(_get_type, _set_type)

	#event
	def _get_event(self):
		return wrap(self.__get_instance().event)
	def _set_event(self, value):
		self.__get_instance().event = unwrap(value)
	event = property(_get_event, _set_event)

wrapperClasses['{3050F28B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScriptElement
backWrapperClasses[IHTMLScriptElement] = '{3050F28B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLScriptElement2
#
class IHTMLScriptElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScriptElement2
		return self.__instance__.QueryInterface(kls)
	#charset
	def _get_charset(self):
		return wrap(self.__get_instance().charset)
	def _set_charset(self, value):
		self.__get_instance().charset = unwrap(value)
	charset = property(_get_charset, _set_charset)

wrapperClasses['{3050F828-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScriptElement2
backWrapperClasses[IHTMLScriptElement2] = '{3050F828-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFrameBase
#
class IHTMLFrameBase(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFrameBase
		return self.__instance__.QueryInterface(kls)
	#src
	def _get_src(self):
		return wrap(self.__get_instance().src)
	def _set_src(self, value):
		self.__get_instance().src = unwrap(value)
	src = property(_get_src, _set_src)

	#name
	def _get_name(self):
		return wrap(self.__get_instance().name)
	def _set_name(self, value):
		self.__get_instance().name = unwrap(value)
	name = property(_get_name, _set_name)

	#scrolling
	def _get_scrolling(self):
		return wrap(self.__get_instance().scrolling)
	def _set_scrolling(self, value):
		self.__get_instance().scrolling = unwrap(value)
	scrolling = property(_get_scrolling, _set_scrolling)

	#frameSpacing
	def _get_frameSpacing(self):
		return wrap(self.__get_instance().frameSpacing)
	def _set_frameSpacing(self, value):
		self.__get_instance().frameSpacing = unwrap(value)
	frameSpacing = property(_get_frameSpacing, _set_frameSpacing)

	#marginWidth
	def _get_marginWidth(self):
		return wrap(self.__get_instance().marginWidth)
	def _set_marginWidth(self, value):
		self.__get_instance().marginWidth = unwrap(value)
	marginWidth = property(_get_marginWidth, _set_marginWidth)

	#marginHeight
	def _get_marginHeight(self):
		return wrap(self.__get_instance().marginHeight)
	def _set_marginHeight(self, value):
		self.__get_instance().marginHeight = unwrap(value)
	marginHeight = property(_get_marginHeight, _set_marginHeight)

	#border
	def _get_border(self):
		return wrap(self.__get_instance().border)
	def _set_border(self, value):
		self.__get_instance().border = unwrap(value)
	border = property(_get_border, _set_border)

	#frameBorder
	def _get_frameBorder(self):
		return wrap(self.__get_instance().frameBorder)
	def _set_frameBorder(self, value):
		self.__get_instance().frameBorder = unwrap(value)
	frameBorder = property(_get_frameBorder, _set_frameBorder)

	#noResize
	def _get_noResize(self):
		return wrap(self.__get_instance().noResize)
	def _set_noResize(self, value):
		self.__get_instance().noResize = unwrap(value)
	noResize = property(_get_noResize, _set_noResize)

wrapperClasses['{3050F311-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFrameBase
backWrapperClasses[IHTMLFrameBase] = '{3050F311-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFrameBase2
#
class IHTMLFrameBase2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFrameBase2
		return self.__instance__.QueryInterface(kls)
	#allowTransparency
	def _get_allowTransparency(self):
		return wrap(self.__get_instance().allowTransparency)
	def _set_allowTransparency(self, value):
		self.__get_instance().allowTransparency = unwrap(value)
	allowTransparency = property(_get_allowTransparency, _set_allowTransparency)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance().onload)
	def _set_onload(self, value):
		self.__get_instance().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#contentWindow
	def _get_contentWindow(self):
		return wrap(self.__get_instance().contentWindow)
	def _set_contentWindow(self, value):
		self.__get_instance().contentWindow = unwrap(value)
	contentWindow = property(_get_contentWindow, _set_contentWindow)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance().readyState)
	def _set_readyState(self, value):
		self.__get_instance().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

wrapperClasses['{3050F6DB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFrameBase2
backWrapperClasses[IHTMLFrameBase2] = '{3050F6DB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLIFrame
#
class DispHTMLIFrame(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLIFrame
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F51B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLIFrame
backWrapperClasses[DispHTMLIFrame] = '{3050F51B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IMarkupContainer
#
class IMarkupContainer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IMarkupContainer
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F5F9-98B5-11CF-BB82-00AA00BDCE0B}'] = IMarkupContainer
backWrapperClasses[IMarkupContainer] = '{3050F5F9-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IMarkupPointer
#
class IMarkupPointer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IMarkupPointer
		return self.__instance__.QueryInterface(kls)
	#Right
	def Right(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().Right(*args))

	#IsRightOfOrEqualTo
	def IsRightOfOrEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().IsRightOfOrEqualTo(*args))

	#IsEqualTo
	def IsEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().IsEqualTo(*args))

	#MoveUnit
	def MoveUnit(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().MoveUnit(*args))

	#IsRightOf
	def IsRightOf(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().IsRightOf(*args))

	#IsLeftOfOrEqualTo
	def IsLeftOfOrEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().IsLeftOfOrEqualTo(*args))

	#CurrentScope
	def CurrentScope(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().CurrentScope(*args))

	#MoveToPointer
	def MoveToPointer(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().MoveToPointer(*args))

	#Left
	def Left(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().Left(*args))

wrapperClasses['{3050F49F-98B5-11CF-BB82-00AA00BDCE0B}'] = IMarkupPointer
backWrapperClasses[IMarkupPointer] = '{3050F49F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISegment
#
class ISegment(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.ISegment
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F683-98B5-11CF-BB82-00AA00BDCE0B}'] = ISegment
backWrapperClasses[ISegment] = '{3050F683-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IElementSegment
#
class IElementSegment(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IElementSegment
		return self.__instance__.QueryInterface(kls)
wrapperClasses['{3050F68F-98B5-11CF-BB82-00AA00BDCE0B}'] = IElementSegment
backWrapperClasses[IElementSegment] = '{3050F68F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISelectionServicesListener
#
class ISelectionServicesListener(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.ISelectionServicesListener
		return self.__instance__.QueryInterface(kls)
	#GetTypeDetail
	def GetTypeDetail(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().GetTypeDetail(*args))

	#OnChangeType
	def OnChangeType(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().OnChangeType(*args))

wrapperClasses['{3050F699-98B5-11CF-BB82-00AA00BDCE0B}'] = ISelectionServicesListener
backWrapperClasses[ISelectionServicesListener] = '{3050F699-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISelectionServices
#
class ISelectionServices(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.ISelectionServices
		return self.__instance__.QueryInterface(kls)
	#AddElementSegment
	def AddElementSegment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().AddElementSegment(*args))

	#RemoveSegment
	def RemoveSegment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().RemoveSegment(*args))

	#GetMarkupContainer
	def GetMarkupContainer(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().GetMarkupContainer(*args))

wrapperClasses['{3050F684-98B5-11CF-BB82-00AA00BDCE0B}'] = ISelectionServices
backWrapperClasses[ISelectionServices] = '{3050F684-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEditDesigner
#
class IHTMLEditDesigner(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEditDesigner
		return self.__instance__.QueryInterface(kls)
	#PostHandleEvent
	def PostHandleEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().PostHandleEvent(*args))

	#PostEditorEventNotify
	def PostEditorEventNotify(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().PostEditorEventNotify(*args))

	#TranslateAccelerator
	def TranslateAccelerator(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().TranslateAccelerator(*args))

wrapperClasses['{3050F662-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLEditDesigner
backWrapperClasses[IHTMLEditDesigner] = '{3050F662-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEditServices
#
class IHTMLEditServices(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEditServices
		return self.__instance__.QueryInterface(kls)
	#MoveToSelectionAnchor
	def MoveToSelectionAnchor(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance().MoveToSelectionAnchor(*args))

wrapperClasses['{3050F663-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLEditServices
backWrapperClasses[IHTMLEditServices] = '{3050F663-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLDocument
#
class HTMLDocument(IHTMLDOMNode2,
			IHTMLDOMNode,
			IHTMLDocument5,
			IHTMLDocument4,
			IHTMLDocument3,
			IHTMLDocument2,
			HTMLDocumentEvents2,
			HTMLDocumentEvents,
			DispHTMLDocument):
	def __init__(self, item):
		DispHTMLDocument.__init__(self, item)

coWrapperClasses['{3050F55F-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDocument

##############################
# COpsProfile
#
class COpsProfile(IHTMLOpsProfile):
	def __init__(self, item):
		IHTMLOpsProfile.__init__(self, item)

coWrapperClasses['{3050F401-98B5-11CF-BB82-00AA00BDCE0B}'] = COpsProfile

##############################
# HTMLStyleSheet
#
class HTMLStyleSheet(IHTMLStyleSheet2,
			IHTMLStyleSheet,
			DispHTMLStyleSheet):
	def __init__(self, item):
		DispHTMLStyleSheet.__init__(self, item)

coWrapperClasses['{3050F58D-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLStyleSheet

##############################
# HTMLDOMTextNode
#
class HTMLDOMTextNode(IHTMLDOMNode2,
			IHTMLDOMNode,
			IHTMLDOMTextNode2,
			IHTMLDOMTextNode,
			DispHTMLDOMTextNode):
	def __init__(self, item):
		DispHTMLDOMTextNode.__init__(self, item)

coWrapperClasses['{3050F565-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDOMTextNode

##############################
# HTMLLocation
#
class HTMLLocation(IHTMLLocation):
	def __init__(self, item):
		IHTMLLocation.__init__(self, item)

coWrapperClasses['{163BB1E0-6E00-11CF-837A-48DC04C10000}'] = HTMLLocation

##############################
# HTMLNavigator
#
class HTMLNavigator(IOmNavigator):
	def __init__(self, item):
		IOmNavigator.__init__(self, item)

coWrapperClasses['{FECEAAA5-8405-11CF-8BA1-00AA00476DA6}'] = HTMLNavigator

##############################
# HTMLBody
#
class HTMLBody(IHTMLBodyElement2,
			IHTMLBodyElement,
			IHTMLTextContainer,
			IHTMLControlElement,
			IHTMLDOMNode2,
			IHTMLDOMNode,
			IHTMLUniqueName,
			IHTMLElement4,
			IHTMLElement3,
			IHTMLElement2,
			IHTMLElement,
			HTMLTextContainerEvents2,
			HTMLTextContainerEvents,
			DispHTMLBody):
	def __init__(self, item):
		DispHTMLBody.__init__(self, item)

coWrapperClasses['{3050F507-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLBody

##############################
# HTMLCommentElement
#
class HTMLCommentElement(IHTMLCommentElement2,
			IHTMLCommentElement,
			IHTMLDOMNode2,
			IHTMLDOMNode,
			IHTMLUniqueName,
			IHTMLElement4,
			IHTMLElement3,
			IHTMLElement2,
			IHTMLElement,
			HTMLElementEvents2,
			HTMLElementEvents,
			DispHTMLCommentElement):
	def __init__(self, item):
		DispHTMLCommentElement.__init__(self, item)

coWrapperClasses['{3050F50A-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLCommentElement

##############################
# HTMLStyleSheetsCollection
#
class HTMLStyleSheetsCollection(IHTMLStyleSheetsCollection):
	def __init__(self, item):
		IHTMLStyleSheetsCollection.__init__(self, item)

coWrapperClasses['{3050F37E-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLStyleSheetsCollection

##############################
# HTMLCurrentStyle
#
class HTMLCurrentStyle(IHTMLCurrentStyle4,
			IHTMLCurrentStyle3,
			IHTMLCurrentStyle2,
			IHTMLCurrentStyle,
			DispHTMLCurrentStyle):
	def __init__(self, item):
		DispHTMLCurrentStyle.__init__(self, item)

coWrapperClasses['{3050F557-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLCurrentStyle

##############################
# CMimeTypes
#
class CMimeTypes(IHTMLMimeTypesCollection):
	def __init__(self, item):
		IHTMLMimeTypesCollection.__init__(self, item)

coWrapperClasses['{3050F3FC-98B5-11CF-BB82-00AA00BDCE0B}'] = CMimeTypes

##############################
# HTMLStyle
#
class HTMLStyle(IHTMLStyle4,
			IHTMLStyle3,
			IHTMLStyle2,
			IHTMLStyle,
			DispHTMLStyle):
	def __init__(self, item):
		DispHTMLStyle.__init__(self, item)

coWrapperClasses['{3050F55A-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLStyle

##############################
# HTMLHistory
#
class HTMLHistory(IOmHistory):
	def __init__(self, item):
		IOmHistory.__init__(self, item)

coWrapperClasses['{FECEAAA2-8405-11CF-8BA1-00AA00476DA6}'] = HTMLHistory

##############################
# CPlugins
#
class CPlugins(IHTMLPluginsCollection):
	def __init__(self, item):
		IHTMLPluginsCollection.__init__(self, item)

coWrapperClasses['{3050F3FD-98B5-11CF-BB82-00AA00BDCE0B}'] = CPlugins

