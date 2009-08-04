# auto-generated using idlparser mshtml.idl - do not edit!
import sys
from comtypes.client import GetModule
if not hasattr(sys, 'frozen'):
    GetModule('atl.dll')
    GetModule('shdocvw.dll')
from comtypes.gen import SHDocVw
from comtypes.gen import MSHTML
from comtypes.client.dynamic import Dispatch, _Dispatch

wrapperClasses = {}
coWrapperClasses = {}
backWrapperClasses = {}
def unwrap(item):
    if item is None:
        return None
    kls = item.__class__
    if not backWrapperClasses.has_key(kls):
        return item
    inst = item.__instance__
    if inst.__dict__.has_key('_comobj'):
        inst = inst.__dict__['_comobj']
    return inst
def wrap(item, override=None):
    if override: # easier to pass in class than GUID
        override = backWrapperClasses[override]
    if item is None:
        return None
    if not hasattr(item, '_iid_'):
        return item
    if override:
        kls = override
    else:
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

	def __get_instance_IHTMLFiltersCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFiltersCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLFiltersCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLFiltersCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLFiltersCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLFiltersCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFiltersCollection().item(*args))

wrapperClasses['{3050F3EE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFiltersCollection
backWrapperClasses[IHTMLFiltersCollection] = '{3050F3EE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle
#
class IHTMLStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
	#font
	def _get_font(self):
		return wrap(self.__get_instance_IHTMLStyle().font)
	def _set_font(self, value):
		self.__get_instance_IHTMLStyle().font = unwrap(value)
	font = property(_get_font, _set_font)

	#borderTop
	def _get_borderTop(self):
		return wrap(self.__get_instance_IHTMLStyle().borderTop)
	def _set_borderTop(self, value):
		self.__get_instance_IHTMLStyle().borderTop = unwrap(value)
	borderTop = property(_get_borderTop, _set_borderTop)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance_IHTMLStyle().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance_IHTMLStyle().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance_IHTMLStyle().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance_IHTMLStyle().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance_IHTMLStyle().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance_IHTMLStyle().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#posTop
	def _get_posTop(self):
		return wrap(self.__get_instance_IHTMLStyle().posTop)
	def _set_posTop(self, value):
		self.__get_instance_IHTMLStyle().posTop = unwrap(value)
	posTop = property(_get_posTop, _set_posTop)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance_IHTMLStyle().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance_IHTMLStyle().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance_IHTMLStyle().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance_IHTMLStyle().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#background
	def _get_background(self):
		return wrap(self.__get_instance_IHTMLStyle().background)
	def _set_background(self, value):
		self.__get_instance_IHTMLStyle().background = unwrap(value)
	background = property(_get_background, _set_background)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLStyle().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLStyle().height = unwrap(value)
	height = property(_get_height, _set_height)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance_IHTMLStyle().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance_IHTMLStyle().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance_IHTMLStyle().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance_IHTMLStyle().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance_IHTMLStyle().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance_IHTMLStyle().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance_IHTMLStyle().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance_IHTMLStyle().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance_IHTMLStyle().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance_IHTMLStyle().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#textDecorationLineThrough
	def _get_textDecorationLineThrough(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecorationLineThrough)
	def _set_textDecorationLineThrough(self, value):
		self.__get_instance_IHTMLStyle().textDecorationLineThrough = unwrap(value)
	textDecorationLineThrough = property(_get_textDecorationLineThrough, _set_textDecorationLineThrough)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance_IHTMLStyle().cssText)
	def _set_cssText(self, value):
		self.__get_instance_IHTMLStyle().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance_IHTMLStyle().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance_IHTMLStyle().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance_IHTMLStyle().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance_IHTMLStyle().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance_IHTMLStyle().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance_IHTMLStyle().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance_IHTMLStyle().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance_IHTMLStyle().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance_IHTMLStyle().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

	#posHeight
	def _get_posHeight(self):
		return wrap(self.__get_instance_IHTMLStyle().posHeight)
	def _set_posHeight(self, value):
		self.__get_instance_IHTMLStyle().posHeight = unwrap(value)
	posHeight = property(_get_posHeight, _set_posHeight)

	#pixelWidth
	def _get_pixelWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().pixelWidth)
	def _set_pixelWidth(self, value):
		self.__get_instance_IHTMLStyle().pixelWidth = unwrap(value)
	pixelWidth = property(_get_pixelWidth, _set_pixelWidth)

	#posLeft
	def _get_posLeft(self):
		return wrap(self.__get_instance_IHTMLStyle().posLeft)
	def _set_posLeft(self, value):
		self.__get_instance_IHTMLStyle().posLeft = unwrap(value)
	posLeft = property(_get_posLeft, _set_posLeft)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance_IHTMLStyle().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance_IHTMLStyle().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance_IHTMLStyle().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance_IHTMLStyle().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance_IHTMLStyle().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance_IHTMLStyle().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance_IHTMLStyle().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance_IHTMLStyle().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance_IHTMLStyle().filter)
	def _set_filter(self, value):
		self.__get_instance_IHTMLStyle().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance_IHTMLStyle().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance_IHTMLStyle().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#borderRight
	def _get_borderRight(self):
		return wrap(self.__get_instance_IHTMLStyle().borderRight)
	def _set_borderRight(self, value):
		self.__get_instance_IHTMLStyle().borderRight = unwrap(value)
	borderRight = property(_get_borderRight, _set_borderRight)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance_IHTMLStyle().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance_IHTMLStyle().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance_IHTMLStyle().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance_IHTMLStyle().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance_IHTMLStyle().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance_IHTMLStyle().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#color
	def _get_color(self):
		return wrap(self.__get_instance_IHTMLStyle().color)
	def _set_color(self, value):
		self.__get_instance_IHTMLStyle().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance_IHTMLStyle().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance_IHTMLStyle().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#borderBottom
	def _get_borderBottom(self):
		return wrap(self.__get_instance_IHTMLStyle().borderBottom)
	def _set_borderBottom(self, value):
		self.__get_instance_IHTMLStyle().borderBottom = unwrap(value)
	borderBottom = property(_get_borderBottom, _set_borderBottom)

	#backgroundPosition
	def _get_backgroundPosition(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundPosition)
	def _set_backgroundPosition(self, value):
		self.__get_instance_IHTMLStyle().backgroundPosition = unwrap(value)
	backgroundPosition = property(_get_backgroundPosition, _set_backgroundPosition)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance_IHTMLStyle().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance_IHTMLStyle().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance_IHTMLStyle().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance_IHTMLStyle().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance_IHTMLStyle().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance_IHTMLStyle().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#top
	def _get_top(self):
		return wrap(self.__get_instance_IHTMLStyle().top)
	def _set_top(self, value):
		self.__get_instance_IHTMLStyle().top = unwrap(value)
	top = property(_get_top, _set_top)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLStyle().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLStyle().width = unwrap(value)
	width = property(_get_width, _set_width)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance_IHTMLStyle().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance_IHTMLStyle().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#pixelLeft
	def _get_pixelLeft(self):
		return wrap(self.__get_instance_IHTMLStyle().pixelLeft)
	def _set_pixelLeft(self, value):
		self.__get_instance_IHTMLStyle().pixelLeft = unwrap(value)
	pixelLeft = property(_get_pixelLeft, _set_pixelLeft)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance_IHTMLStyle().visibility)
	def _set_visibility(self, value):
		self.__get_instance_IHTMLStyle().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#textDecorationNone
	def _get_textDecorationNone(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecorationNone)
	def _set_textDecorationNone(self, value):
		self.__get_instance_IHTMLStyle().textDecorationNone = unwrap(value)
	textDecorationNone = property(_get_textDecorationNone, _set_textDecorationNone)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance_IHTMLStyle().padding)
	def _set_padding(self, value):
		self.__get_instance_IHTMLStyle().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#textDecorationOverline
	def _get_textDecorationOverline(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecorationOverline)
	def _set_textDecorationOverline(self, value):
		self.__get_instance_IHTMLStyle().textDecorationOverline = unwrap(value)
	textDecorationOverline = property(_get_textDecorationOverline, _set_textDecorationOverline)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance_IHTMLStyle().overflow)
	def _set_overflow(self, value):
		self.__get_instance_IHTMLStyle().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance_IHTMLStyle().cursor)
	def _set_cursor(self, value):
		self.__get_instance_IHTMLStyle().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance_IHTMLStyle().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance_IHTMLStyle().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance_IHTMLStyle().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance_IHTMLStyle().margin)
	def _set_margin(self, value):
		self.__get_instance_IHTMLStyle().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance_IHTMLStyle().display)
	def _set_display(self, value):
		self.__get_instance_IHTMLStyle().display = unwrap(value)
	display = property(_get_display, _set_display)

	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance_IHTMLStyle().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance_IHTMLStyle().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#clip
	def _get_clip(self):
		return wrap(self.__get_instance_IHTMLStyle().clip)
	def _set_clip(self, value):
		self.__get_instance_IHTMLStyle().clip = unwrap(value)
	clip = property(_get_clip, _set_clip)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance_IHTMLStyle().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance_IHTMLStyle().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance_IHTMLStyle().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance_IHTMLStyle().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance_IHTMLStyle().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderLeft
	def _get_borderLeft(self):
		return wrap(self.__get_instance_IHTMLStyle().borderLeft)
	def _set_borderLeft(self, value):
		self.__get_instance_IHTMLStyle().borderLeft = unwrap(value)
	borderLeft = property(_get_borderLeft, _set_borderLeft)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance_IHTMLStyle().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance_IHTMLStyle().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance_IHTMLStyle().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance_IHTMLStyle().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance_IHTMLStyle().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLStyle().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLStyle().border = unwrap(value)
	border = property(_get_border, _set_border)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance_IHTMLStyle().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance_IHTMLStyle().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance_IHTMLStyle().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance_IHTMLStyle().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#pixelHeight
	def _get_pixelHeight(self):
		return wrap(self.__get_instance_IHTMLStyle().pixelHeight)
	def _set_pixelHeight(self, value):
		self.__get_instance_IHTMLStyle().pixelHeight = unwrap(value)
	pixelHeight = property(_get_pixelHeight, _set_pixelHeight)

	#posWidth
	def _get_posWidth(self):
		return wrap(self.__get_instance_IHTMLStyle().posWidth)
	def _set_posWidth(self, value):
		self.__get_instance_IHTMLStyle().posWidth = unwrap(value)
	posWidth = property(_get_posWidth, _set_posWidth)

	#textDecorationBlink
	def _get_textDecorationBlink(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecorationBlink)
	def _set_textDecorationBlink(self, value):
		self.__get_instance_IHTMLStyle().textDecorationBlink = unwrap(value)
	textDecorationBlink = property(_get_textDecorationBlink, _set_textDecorationBlink)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance_IHTMLStyle().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance_IHTMLStyle().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance_IHTMLStyle().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance_IHTMLStyle().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#pixelTop
	def _get_pixelTop(self):
		return wrap(self.__get_instance_IHTMLStyle().pixelTop)
	def _set_pixelTop(self, value):
		self.__get_instance_IHTMLStyle().pixelTop = unwrap(value)
	pixelTop = property(_get_pixelTop, _set_pixelTop)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance_IHTMLStyle().clear)
	def _set_clear(self, value):
		self.__get_instance_IHTMLStyle().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance_IHTMLStyle().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#textDecorationUnderline
	def _get_textDecorationUnderline(self):
		return wrap(self.__get_instance_IHTMLStyle().textDecorationUnderline)
	def _set_textDecorationUnderline(self, value):
		self.__get_instance_IHTMLStyle().textDecorationUnderline = unwrap(value)
	textDecorationUnderline = property(_get_textDecorationUnderline, _set_textDecorationUnderline)

	#listStyle
	def _get_listStyle(self):
		return wrap(self.__get_instance_IHTMLStyle().listStyle)
	def _set_listStyle(self, value):
		self.__get_instance_IHTMLStyle().listStyle = unwrap(value)
	listStyle = property(_get_listStyle, _set_listStyle)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance_IHTMLStyle().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance_IHTMLStyle().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance_IHTMLStyle().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance_IHTMLStyle().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#left
	def _get_left(self):
		return wrap(self.__get_instance_IHTMLStyle().left)
	def _set_left(self, value):
		self.__get_instance_IHTMLStyle().left = unwrap(value)
	left = property(_get_left, _set_left)

	#getProperty
	def getProperty(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle().getAttribute(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle().toString(*args))

	#setProperty
	def setProperty(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle().setAttribute(*args))

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle().removeAttribute(*args))

wrapperClasses['{3050F25E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle
backWrapperClasses[IHTMLStyle] = '{3050F25E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle2
#
class IHTMLStyle2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyle2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#textJustifyTrim
	def _get_textJustifyTrim(self):
		return wrap(self.__get_instance_IHTMLStyle2().textJustifyTrim)
	def _set_textJustifyTrim(self, value):
		self.__get_instance_IHTMLStyle2().textJustifyTrim = unwrap(value)
	textJustifyTrim = property(_get_textJustifyTrim, _set_textJustifyTrim)

	#right
	def _get_right(self):
		return wrap(self.__get_instance_IHTMLStyle2().right)
	def _set_right(self, value):
		self.__get_instance_IHTMLStyle2().right = unwrap(value)
	right = property(_get_right, _set_right)

	#pixelRight
	def _get_pixelRight(self):
		return wrap(self.__get_instance_IHTMLStyle2().pixelRight)
	def _set_pixelRight(self, value):
		self.__get_instance_IHTMLStyle2().pixelRight = unwrap(value)
	pixelRight = property(_get_pixelRight, _set_pixelRight)

	#accelerator
	def _get_accelerator(self):
		return wrap(self.__get_instance_IHTMLStyle2().accelerator)
	def _set_accelerator(self, value):
		self.__get_instance_IHTMLStyle2().accelerator = unwrap(value)
	accelerator = property(_get_accelerator, _set_accelerator)

	#pixelBottom
	def _get_pixelBottom(self):
		return wrap(self.__get_instance_IHTMLStyle2().pixelBottom)
	def _set_pixelBottom(self, value):
		self.__get_instance_IHTMLStyle2().pixelBottom = unwrap(value)
	pixelBottom = property(_get_pixelBottom, _set_pixelBottom)

	#layoutGridLine
	def _get_layoutGridLine(self):
		return wrap(self.__get_instance_IHTMLStyle2().layoutGridLine)
	def _set_layoutGridLine(self, value):
		self.__get_instance_IHTMLStyle2().layoutGridLine = unwrap(value)
	layoutGridLine = property(_get_layoutGridLine, _set_layoutGridLine)

	#tableLayout
	def _get_tableLayout(self):
		return wrap(self.__get_instance_IHTMLStyle2().tableLayout)
	def _set_tableLayout(self, value):
		self.__get_instance_IHTMLStyle2().tableLayout = unwrap(value)
	tableLayout = property(_get_tableLayout, _set_tableLayout)

	#layoutGridType
	def _get_layoutGridType(self):
		return wrap(self.__get_instance_IHTMLStyle2().layoutGridType)
	def _set_layoutGridType(self, value):
		self.__get_instance_IHTMLStyle2().layoutGridType = unwrap(value)
	layoutGridType = property(_get_layoutGridType, _set_layoutGridType)

	#borderCollapse
	def _get_borderCollapse(self):
		return wrap(self.__get_instance_IHTMLStyle2().borderCollapse)
	def _set_borderCollapse(self, value):
		self.__get_instance_IHTMLStyle2().borderCollapse = unwrap(value)
	borderCollapse = property(_get_borderCollapse, _set_borderCollapse)

	#overflowY
	def _get_overflowY(self):
		return wrap(self.__get_instance_IHTMLStyle2().overflowY)
	def _set_overflowY(self, value):
		self.__get_instance_IHTMLStyle2().overflowY = unwrap(value)
	overflowY = property(_get_overflowY, _set_overflowY)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance_IHTMLStyle2().bottom)
	def _set_bottom(self, value):
		self.__get_instance_IHTMLStyle2().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#rubyAlign
	def _get_rubyAlign(self):
		return wrap(self.__get_instance_IHTMLStyle2().rubyAlign)
	def _set_rubyAlign(self, value):
		self.__get_instance_IHTMLStyle2().rubyAlign = unwrap(value)
	rubyAlign = property(_get_rubyAlign, _set_rubyAlign)

	#imeMode
	def _get_imeMode(self):
		return wrap(self.__get_instance_IHTMLStyle2().imeMode)
	def _set_imeMode(self, value):
		self.__get_instance_IHTMLStyle2().imeMode = unwrap(value)
	imeMode = property(_get_imeMode, _set_imeMode)

	#rubyOverhang
	def _get_rubyOverhang(self):
		return wrap(self.__get_instance_IHTMLStyle2().rubyOverhang)
	def _set_rubyOverhang(self, value):
		self.__get_instance_IHTMLStyle2().rubyOverhang = unwrap(value)
	rubyOverhang = property(_get_rubyOverhang, _set_rubyOverhang)

	#textKashida
	def _get_textKashida(self):
		return wrap(self.__get_instance_IHTMLStyle2().textKashida)
	def _set_textKashida(self, value):
		self.__get_instance_IHTMLStyle2().textKashida = unwrap(value)
	textKashida = property(_get_textKashida, _set_textKashida)

	#rubyPosition
	def _get_rubyPosition(self):
		return wrap(self.__get_instance_IHTMLStyle2().rubyPosition)
	def _set_rubyPosition(self, value):
		self.__get_instance_IHTMLStyle2().rubyPosition = unwrap(value)
	rubyPosition = property(_get_rubyPosition, _set_rubyPosition)

	#unicodeBidi
	def _get_unicodeBidi(self):
		return wrap(self.__get_instance_IHTMLStyle2().unicodeBidi)
	def _set_unicodeBidi(self, value):
		self.__get_instance_IHTMLStyle2().unicodeBidi = unwrap(value)
	unicodeBidi = property(_get_unicodeBidi, _set_unicodeBidi)

	#direction
	def _get_direction(self):
		return wrap(self.__get_instance_IHTMLStyle2().direction)
	def _set_direction(self, value):
		self.__get_instance_IHTMLStyle2().direction = unwrap(value)
	direction = property(_get_direction, _set_direction)

	#layoutGridChar
	def _get_layoutGridChar(self):
		return wrap(self.__get_instance_IHTMLStyle2().layoutGridChar)
	def _set_layoutGridChar(self, value):
		self.__get_instance_IHTMLStyle2().layoutGridChar = unwrap(value)
	layoutGridChar = property(_get_layoutGridChar, _set_layoutGridChar)

	#position
	def _get_position(self):
		return wrap(self.__get_instance_IHTMLStyle2().position)
	def _set_position(self, value):
		self.__get_instance_IHTMLStyle2().position = unwrap(value)
	position = property(_get_position, _set_position)

	#textJustify
	def _get_textJustify(self):
		return wrap(self.__get_instance_IHTMLStyle2().textJustify)
	def _set_textJustify(self, value):
		self.__get_instance_IHTMLStyle2().textJustify = unwrap(value)
	textJustify = property(_get_textJustify, _set_textJustify)

	#wordBreak
	def _get_wordBreak(self):
		return wrap(self.__get_instance_IHTMLStyle2().wordBreak)
	def _set_wordBreak(self, value):
		self.__get_instance_IHTMLStyle2().wordBreak = unwrap(value)
	wordBreak = property(_get_wordBreak, _set_wordBreak)

	#layoutGrid
	def _get_layoutGrid(self):
		return wrap(self.__get_instance_IHTMLStyle2().layoutGrid)
	def _set_layoutGrid(self, value):
		self.__get_instance_IHTMLStyle2().layoutGrid = unwrap(value)
	layoutGrid = property(_get_layoutGrid, _set_layoutGrid)

	#lineBreak
	def _get_lineBreak(self):
		return wrap(self.__get_instance_IHTMLStyle2().lineBreak)
	def _set_lineBreak(self, value):
		self.__get_instance_IHTMLStyle2().lineBreak = unwrap(value)
	lineBreak = property(_get_lineBreak, _set_lineBreak)

	#textAutospace
	def _get_textAutospace(self):
		return wrap(self.__get_instance_IHTMLStyle2().textAutospace)
	def _set_textAutospace(self, value):
		self.__get_instance_IHTMLStyle2().textAutospace = unwrap(value)
	textAutospace = property(_get_textAutospace, _set_textAutospace)

	#posBottom
	def _get_posBottom(self):
		return wrap(self.__get_instance_IHTMLStyle2().posBottom)
	def _set_posBottom(self, value):
		self.__get_instance_IHTMLStyle2().posBottom = unwrap(value)
	posBottom = property(_get_posBottom, _set_posBottom)

	#overflowX
	def _get_overflowX(self):
		return wrap(self.__get_instance_IHTMLStyle2().overflowX)
	def _set_overflowX(self, value):
		self.__get_instance_IHTMLStyle2().overflowX = unwrap(value)
	overflowX = property(_get_overflowX, _set_overflowX)

	#posRight
	def _get_posRight(self):
		return wrap(self.__get_instance_IHTMLStyle2().posRight)
	def _set_posRight(self, value):
		self.__get_instance_IHTMLStyle2().posRight = unwrap(value)
	posRight = property(_get_posRight, _set_posRight)

	#behavior
	def _get_behavior(self):
		return wrap(self.__get_instance_IHTMLStyle2().behavior)
	def _set_behavior(self, value):
		self.__get_instance_IHTMLStyle2().behavior = unwrap(value)
	behavior = property(_get_behavior, _set_behavior)

	#layoutGridMode
	def _get_layoutGridMode(self):
		return wrap(self.__get_instance_IHTMLStyle2().layoutGridMode)
	def _set_layoutGridMode(self, value):
		self.__get_instance_IHTMLStyle2().layoutGridMode = unwrap(value)
	layoutGridMode = property(_get_layoutGridMode, _set_layoutGridMode)

	#setExpression
	def setExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle2().setExpression(*args))

	#removeExpression
	def removeExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle2().removeExpression(*args))

	#getExpression
	def getExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyle2().getExpression(*args))

wrapperClasses['{3050F4A2-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle2
backWrapperClasses[IHTMLStyle2] = '{3050F4A2-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRuleStyle
#
class IHTMLRuleStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLRuleStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRuleStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance_IHTMLRuleStyle().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance_IHTMLRuleStyle().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#clip
	def _get_clip(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().clip)
	def _set_clip(self, value):
		self.__get_instance_IHTMLRuleStyle().clip = unwrap(value)
	clip = property(_get_clip, _set_clip)

	#color
	def _get_color(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().color)
	def _set_color(self, value):
		self.__get_instance_IHTMLRuleStyle().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance_IHTMLRuleStyle().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance_IHTMLRuleStyle().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderBottom
	def _get_borderBottom(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderBottom)
	def _set_borderBottom(self, value):
		self.__get_instance_IHTMLRuleStyle().borderBottom = unwrap(value)
	borderBottom = property(_get_borderBottom, _set_borderBottom)

	#backgroundPosition
	def _get_backgroundPosition(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundPosition)
	def _set_backgroundPosition(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundPosition = unwrap(value)
	backgroundPosition = property(_get_backgroundPosition, _set_backgroundPosition)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance_IHTMLRuleStyle().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance_IHTMLRuleStyle().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderLeft
	def _get_borderLeft(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderLeft)
	def _set_borderLeft(self, value):
		self.__get_instance_IHTMLRuleStyle().borderLeft = unwrap(value)
	borderLeft = property(_get_borderLeft, _set_borderLeft)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance_IHTMLRuleStyle().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance_IHTMLRuleStyle().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance_IHTMLRuleStyle().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#font
	def _get_font(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().font)
	def _set_font(self, value):
		self.__get_instance_IHTMLRuleStyle().font = unwrap(value)
	font = property(_get_font, _set_font)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLRuleStyle().border = unwrap(value)
	border = property(_get_border, _set_border)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().overflow)
	def _set_overflow(self, value):
		self.__get_instance_IHTMLRuleStyle().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance_IHTMLRuleStyle().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance_IHTMLRuleStyle().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#textDecorationLineThrough
	def _get_textDecorationLineThrough(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecorationLineThrough)
	def _set_textDecorationLineThrough(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecorationLineThrough = unwrap(value)
	textDecorationLineThrough = property(_get_textDecorationLineThrough, _set_textDecorationLineThrough)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance_IHTMLRuleStyle().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().cssText)
	def _set_cssText(self, value):
		self.__get_instance_IHTMLRuleStyle().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#top
	def _get_top(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().top)
	def _set_top(self, value):
		self.__get_instance_IHTMLRuleStyle().top = unwrap(value)
	top = property(_get_top, _set_top)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance_IHTMLRuleStyle().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance_IHTMLRuleStyle().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance_IHTMLRuleStyle().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance_IHTMLRuleStyle().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance_IHTMLRuleStyle().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLRuleStyle().width = unwrap(value)
	width = property(_get_width, _set_width)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance_IHTMLRuleStyle().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance_IHTMLRuleStyle().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance_IHTMLRuleStyle().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance_IHTMLRuleStyle().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance_IHTMLRuleStyle().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance_IHTMLRuleStyle().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance_IHTMLRuleStyle().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().filter)
	def _set_filter(self, value):
		self.__get_instance_IHTMLRuleStyle().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textDecorationBlink
	def _get_textDecorationBlink(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecorationBlink)
	def _set_textDecorationBlink(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecorationBlink = unwrap(value)
	textDecorationBlink = property(_get_textDecorationBlink, _set_textDecorationBlink)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().visibility)
	def _set_visibility(self, value):
		self.__get_instance_IHTMLRuleStyle().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#textDecorationNone
	def _get_textDecorationNone(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecorationNone)
	def _set_textDecorationNone(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecorationNone = unwrap(value)
	textDecorationNone = property(_get_textDecorationNone, _set_textDecorationNone)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().padding)
	def _set_padding(self, value):
		self.__get_instance_IHTMLRuleStyle().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance_IHTMLRuleStyle().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance_IHTMLRuleStyle().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#textDecorationOverline
	def _get_textDecorationOverline(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecorationOverline)
	def _set_textDecorationOverline(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecorationOverline = unwrap(value)
	textDecorationOverline = property(_get_textDecorationOverline, _set_textDecorationOverline)

	#background
	def _get_background(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().background)
	def _set_background(self, value):
		self.__get_instance_IHTMLRuleStyle().background = unwrap(value)
	background = property(_get_background, _set_background)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance_IHTMLRuleStyle().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderTop
	def _get_borderTop(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderTop)
	def _set_borderTop(self, value):
		self.__get_instance_IHTMLRuleStyle().borderTop = unwrap(value)
	borderTop = property(_get_borderTop, _set_borderTop)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLRuleStyle().height = unwrap(value)
	height = property(_get_height, _set_height)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance_IHTMLRuleStyle().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance_IHTMLRuleStyle().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance_IHTMLRuleStyle().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#left
	def _get_left(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().left)
	def _set_left(self, value):
		self.__get_instance_IHTMLRuleStyle().left = unwrap(value)
	left = property(_get_left, _set_left)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance_IHTMLRuleStyle().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance_IHTMLRuleStyle().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().clear)
	def _set_clear(self, value):
		self.__get_instance_IHTMLRuleStyle().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance_IHTMLRuleStyle().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().cursor)
	def _set_cursor(self, value):
		self.__get_instance_IHTMLRuleStyle().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance_IHTMLRuleStyle().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#listStyle
	def _get_listStyle(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().listStyle)
	def _set_listStyle(self, value):
		self.__get_instance_IHTMLRuleStyle().listStyle = unwrap(value)
	listStyle = property(_get_listStyle, _set_listStyle)

	#borderRight
	def _get_borderRight(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().borderRight)
	def _set_borderRight(self, value):
		self.__get_instance_IHTMLRuleStyle().borderRight = unwrap(value)
	borderRight = property(_get_borderRight, _set_borderRight)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance_IHTMLRuleStyle().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#position
	def _get_position(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().position)
	def _set_position(self, value):
		self.__get_instance_IHTMLRuleStyle().position = unwrap(value)
	position = property(_get_position, _set_position)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance_IHTMLRuleStyle().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance_IHTMLRuleStyle().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().margin)
	def _set_margin(self, value):
		self.__get_instance_IHTMLRuleStyle().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().display)
	def _set_display(self, value):
		self.__get_instance_IHTMLRuleStyle().display = unwrap(value)
	display = property(_get_display, _set_display)

	#textDecorationUnderline
	def _get_textDecorationUnderline(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().textDecorationUnderline)
	def _set_textDecorationUnderline(self, value):
		self.__get_instance_IHTMLRuleStyle().textDecorationUnderline = unwrap(value)
	textDecorationUnderline = property(_get_textDecorationUnderline, _set_textDecorationUnderline)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance_IHTMLRuleStyle().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance_IHTMLRuleStyle().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLRuleStyle().getAttribute(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLRuleStyle().setAttribute(*args))

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLRuleStyle().removeAttribute(*args))

wrapperClasses['{3050F3CF-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRuleStyle
backWrapperClasses[IHTMLRuleStyle] = '{3050F3CF-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLStyle
#
class DispHTMLStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F55A-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLStyle
backWrapperClasses[DispHTMLStyle] = '{3050F55A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle3
#
class IHTMLStyle3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyle3(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle3
		return Dispatch(self.__instance__.QueryInterface(kls))
	#scrollbarHighlightColor
	def _get_scrollbarHighlightColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarHighlightColor)
	def _set_scrollbarHighlightColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarHighlightColor = unwrap(value)
	scrollbarHighlightColor = property(_get_scrollbarHighlightColor, _set_scrollbarHighlightColor)

	#scrollbar3dLightColor
	def _get_scrollbar3dLightColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbar3dLightColor)
	def _set_scrollbar3dLightColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbar3dLightColor = unwrap(value)
	scrollbar3dLightColor = property(_get_scrollbar3dLightColor, _set_scrollbar3dLightColor)

	#scrollbarDarkShadowColor
	def _get_scrollbarDarkShadowColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarDarkShadowColor)
	def _set_scrollbarDarkShadowColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarDarkShadowColor = unwrap(value)
	scrollbarDarkShadowColor = property(_get_scrollbarDarkShadowColor, _set_scrollbarDarkShadowColor)

	#zoom
	def _get_zoom(self):
		return wrap(self.__get_instance_IHTMLStyle3().zoom)
	def _set_zoom(self, value):
		self.__get_instance_IHTMLStyle3().zoom = unwrap(value)
	zoom = property(_get_zoom, _set_zoom)

	#scrollbarShadowColor
	def _get_scrollbarShadowColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarShadowColor)
	def _set_scrollbarShadowColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarShadowColor = unwrap(value)
	scrollbarShadowColor = property(_get_scrollbarShadowColor, _set_scrollbarShadowColor)

	#scrollbarFaceColor
	def _get_scrollbarFaceColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarFaceColor)
	def _set_scrollbarFaceColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarFaceColor = unwrap(value)
	scrollbarFaceColor = property(_get_scrollbarFaceColor, _set_scrollbarFaceColor)

	#writingMode
	def _get_writingMode(self):
		return wrap(self.__get_instance_IHTMLStyle3().writingMode)
	def _set_writingMode(self, value):
		self.__get_instance_IHTMLStyle3().writingMode = unwrap(value)
	writingMode = property(_get_writingMode, _set_writingMode)

	#scrollbarTrackColor
	def _get_scrollbarTrackColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarTrackColor)
	def _set_scrollbarTrackColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarTrackColor = unwrap(value)
	scrollbarTrackColor = property(_get_scrollbarTrackColor, _set_scrollbarTrackColor)

	#scrollbarBaseColor
	def _get_scrollbarBaseColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarBaseColor)
	def _set_scrollbarBaseColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarBaseColor = unwrap(value)
	scrollbarBaseColor = property(_get_scrollbarBaseColor, _set_scrollbarBaseColor)

	#scrollbarArrowColor
	def _get_scrollbarArrowColor(self):
		return wrap(self.__get_instance_IHTMLStyle3().scrollbarArrowColor)
	def _set_scrollbarArrowColor(self, value):
		self.__get_instance_IHTMLStyle3().scrollbarArrowColor = unwrap(value)
	scrollbarArrowColor = property(_get_scrollbarArrowColor, _set_scrollbarArrowColor)

	#textAlignLast
	def _get_textAlignLast(self):
		return wrap(self.__get_instance_IHTMLStyle3().textAlignLast)
	def _set_textAlignLast(self, value):
		self.__get_instance_IHTMLStyle3().textAlignLast = unwrap(value)
	textAlignLast = property(_get_textAlignLast, _set_textAlignLast)

	#wordWrap
	def _get_wordWrap(self):
		return wrap(self.__get_instance_IHTMLStyle3().wordWrap)
	def _set_wordWrap(self, value):
		self.__get_instance_IHTMLStyle3().wordWrap = unwrap(value)
	wordWrap = property(_get_wordWrap, _set_wordWrap)

	#textKashidaSpace
	def _get_textKashidaSpace(self):
		return wrap(self.__get_instance_IHTMLStyle3().textKashidaSpace)
	def _set_textKashidaSpace(self, value):
		self.__get_instance_IHTMLStyle3().textKashidaSpace = unwrap(value)
	textKashidaSpace = property(_get_textKashidaSpace, _set_textKashidaSpace)

	#layoutFlow
	def _get_layoutFlow(self):
		return wrap(self.__get_instance_IHTMLStyle3().layoutFlow)
	def _set_layoutFlow(self, value):
		self.__get_instance_IHTMLStyle3().layoutFlow = unwrap(value)
	layoutFlow = property(_get_layoutFlow, _set_layoutFlow)

	#textUnderlinePosition
	def _get_textUnderlinePosition(self):
		return wrap(self.__get_instance_IHTMLStyle3().textUnderlinePosition)
	def _set_textUnderlinePosition(self, value):
		self.__get_instance_IHTMLStyle3().textUnderlinePosition = unwrap(value)
	textUnderlinePosition = property(_get_textUnderlinePosition, _set_textUnderlinePosition)

wrapperClasses['{3050F656-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle3
backWrapperClasses[IHTMLStyle3] = '{3050F656-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyle4
#
class IHTMLStyle4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyle4(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyle4
		return Dispatch(self.__instance__.QueryInterface(kls))
	#textOverflow
	def _get_textOverflow(self):
		return wrap(self.__get_instance_IHTMLStyle4().textOverflow)
	def _set_textOverflow(self, value):
		self.__get_instance_IHTMLStyle4().textOverflow = unwrap(value)
	textOverflow = property(_get_textOverflow, _set_textOverflow)

	#minHeight
	def _get_minHeight(self):
		return wrap(self.__get_instance_IHTMLStyle4().minHeight)
	def _set_minHeight(self, value):
		self.__get_instance_IHTMLStyle4().minHeight = unwrap(value)
	minHeight = property(_get_minHeight, _set_minHeight)

wrapperClasses['{3050F816-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyle4
backWrapperClasses[IHTMLStyle4] = '{3050F816-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRenderStyle
#
class IHTMLRenderStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLRenderStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRenderStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
	#renderingPriority
	def _get_renderingPriority(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().renderingPriority)
	def _set_renderingPriority(self, value):
		self.__get_instance_IHTMLRenderStyle().renderingPriority = unwrap(value)
	renderingPriority = property(_get_renderingPriority, _set_renderingPriority)

	#defaultTextSelection
	def _get_defaultTextSelection(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().defaultTextSelection)
	def _set_defaultTextSelection(self, value):
		self.__get_instance_IHTMLRenderStyle().defaultTextSelection = unwrap(value)
	defaultTextSelection = property(_get_defaultTextSelection, _set_defaultTextSelection)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance_IHTMLRenderStyle().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#textEffect
	def _get_textEffect(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textEffect)
	def _set_textEffect(self, value):
		self.__get_instance_IHTMLRenderStyle().textEffect = unwrap(value)
	textEffect = property(_get_textEffect, _set_textEffect)

	#textBackgroundColor
	def _get_textBackgroundColor(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textBackgroundColor)
	def _set_textBackgroundColor(self, value):
		self.__get_instance_IHTMLRenderStyle().textBackgroundColor = unwrap(value)
	textBackgroundColor = property(_get_textBackgroundColor, _set_textBackgroundColor)

	#textLineThroughStyle
	def _get_textLineThroughStyle(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textLineThroughStyle)
	def _set_textLineThroughStyle(self, value):
		self.__get_instance_IHTMLRenderStyle().textLineThroughStyle = unwrap(value)
	textLineThroughStyle = property(_get_textLineThroughStyle, _set_textLineThroughStyle)

	#textColor
	def _get_textColor(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textColor)
	def _set_textColor(self, value):
		self.__get_instance_IHTMLRenderStyle().textColor = unwrap(value)
	textColor = property(_get_textColor, _set_textColor)

	#textUnderlineStyle
	def _get_textUnderlineStyle(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textUnderlineStyle)
	def _set_textUnderlineStyle(self, value):
		self.__get_instance_IHTMLRenderStyle().textUnderlineStyle = unwrap(value)
	textUnderlineStyle = property(_get_textUnderlineStyle, _set_textUnderlineStyle)

	#textDecorationColor
	def _get_textDecorationColor(self):
		return wrap(self.__get_instance_IHTMLRenderStyle().textDecorationColor)
	def _set_textDecorationColor(self, value):
		self.__get_instance_IHTMLRenderStyle().textDecorationColor = unwrap(value)
	textDecorationColor = property(_get_textDecorationColor, _set_textDecorationColor)

wrapperClasses['{3050F6AE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRenderStyle
backWrapperClasses[IHTMLRenderStyle] = '{3050F6AE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle
#
class IHTMLCurrentStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCurrentStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
	#layoutGridType
	def _get_layoutGridType(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().layoutGridType)
	def _set_layoutGridType(self, value):
		self.__get_instance_IHTMLCurrentStyle().layoutGridType = unwrap(value)
	layoutGridType = property(_get_layoutGridType, _set_layoutGridType)

	#tableLayout
	def _get_tableLayout(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().tableLayout)
	def _set_tableLayout(self, value):
		self.__get_instance_IHTMLCurrentStyle().tableLayout = unwrap(value)
	tableLayout = property(_get_tableLayout, _set_tableLayout)

	#left
	def _get_left(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().left)
	def _set_left(self, value):
		self.__get_instance_IHTMLCurrentStyle().left = unwrap(value)
	left = property(_get_left, _set_left)

	#borderCollapse
	def _get_borderCollapse(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderCollapse)
	def _set_borderCollapse(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderCollapse = unwrap(value)
	borderCollapse = property(_get_borderCollapse, _set_borderCollapse)

	#overflowY
	def _get_overflowY(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().overflowY)
	def _set_overflowY(self, value):
		self.__get_instance_IHTMLCurrentStyle().overflowY = unwrap(value)
	overflowY = property(_get_overflowY, _set_overflowY)

	#overflowX
	def _get_overflowX(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().overflowX)
	def _set_overflowX(self, value):
		self.__get_instance_IHTMLCurrentStyle().overflowX = unwrap(value)
	overflowX = property(_get_overflowX, _set_overflowX)

	#marginBottom
	def _get_marginBottom(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().marginBottom)
	def _set_marginBottom(self, value):
		self.__get_instance_IHTMLCurrentStyle().marginBottom = unwrap(value)
	marginBottom = property(_get_marginBottom, _set_marginBottom)

	#styleFloat
	def _get_styleFloat(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().styleFloat)
	def _set_styleFloat(self, value):
		self.__get_instance_IHTMLCurrentStyle().styleFloat = unwrap(value)
	styleFloat = property(_get_styleFloat, _set_styleFloat)

	#borderRightWidth
	def _get_borderRightWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderRightWidth)
	def _set_borderRightWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderRightWidth = unwrap(value)
	borderRightWidth = property(_get_borderRightWidth, _set_borderRightWidth)

	#imeMode
	def _get_imeMode(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().imeMode)
	def _set_imeMode(self, value):
		self.__get_instance_IHTMLCurrentStyle().imeMode = unwrap(value)
	imeMode = property(_get_imeMode, _set_imeMode)

	#lineHeight
	def _get_lineHeight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().lineHeight)
	def _set_lineHeight(self, value):
		self.__get_instance_IHTMLCurrentStyle().lineHeight = unwrap(value)
	lineHeight = property(_get_lineHeight, _set_lineHeight)

	#borderLeftWidth
	def _get_borderLeftWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderLeftWidth)
	def _set_borderLeftWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderLeftWidth = unwrap(value)
	borderLeftWidth = property(_get_borderLeftWidth, _set_borderLeftWidth)

	#borderBottomStyle
	def _get_borderBottomStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderBottomStyle)
	def _set_borderBottomStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderBottomStyle = unwrap(value)
	borderBottomStyle = property(_get_borderBottomStyle, _set_borderBottomStyle)

	#textJustify
	def _get_textJustify(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textJustify)
	def _set_textJustify(self, value):
		self.__get_instance_IHTMLCurrentStyle().textJustify = unwrap(value)
	textJustify = property(_get_textJustify, _set_textJustify)

	#textAlign
	def _get_textAlign(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textAlign)
	def _set_textAlign(self, value):
		self.__get_instance_IHTMLCurrentStyle().textAlign = unwrap(value)
	textAlign = property(_get_textAlign, _set_textAlign)

	#borderLeftColor
	def _get_borderLeftColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderLeftColor)
	def _set_borderLeftColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderLeftColor = unwrap(value)
	borderLeftColor = property(_get_borderLeftColor, _set_borderLeftColor)

	#layoutGridLine
	def _get_layoutGridLine(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().layoutGridLine)
	def _set_layoutGridLine(self, value):
		self.__get_instance_IHTMLCurrentStyle().layoutGridLine = unwrap(value)
	layoutGridLine = property(_get_layoutGridLine, _set_layoutGridLine)

	#borderWidth
	def _get_borderWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderWidth)
	def _set_borderWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderWidth = unwrap(value)
	borderWidth = property(_get_borderWidth, _set_borderWidth)

	#layoutGridMode
	def _get_layoutGridMode(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().layoutGridMode)
	def _set_layoutGridMode(self, value):
		self.__get_instance_IHTMLCurrentStyle().layoutGridMode = unwrap(value)
	layoutGridMode = property(_get_layoutGridMode, _set_layoutGridMode)

	#right
	def _get_right(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().right)
	def _set_right(self, value):
		self.__get_instance_IHTMLCurrentStyle().right = unwrap(value)
	right = property(_get_right, _set_right)

	#accelerator
	def _get_accelerator(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().accelerator)
	def _set_accelerator(self, value):
		self.__get_instance_IHTMLCurrentStyle().accelerator = unwrap(value)
	accelerator = property(_get_accelerator, _set_accelerator)

	#fontVariant
	def _get_fontVariant(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().fontVariant)
	def _set_fontVariant(self, value):
		self.__get_instance_IHTMLCurrentStyle().fontVariant = unwrap(value)
	fontVariant = property(_get_fontVariant, _set_fontVariant)

	#pageBreakBefore
	def _get_pageBreakBefore(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().pageBreakBefore)
	def _set_pageBreakBefore(self, value):
		self.__get_instance_IHTMLCurrentStyle().pageBreakBefore = unwrap(value)
	pageBreakBefore = property(_get_pageBreakBefore, _set_pageBreakBefore)

	#clipRight
	def _get_clipRight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().clipRight)
	def _set_clipRight(self, value):
		self.__get_instance_IHTMLCurrentStyle().clipRight = unwrap(value)
	clipRight = property(_get_clipRight, _set_clipRight)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().bottom)
	def _set_bottom(self, value):
		self.__get_instance_IHTMLCurrentStyle().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#backgroundRepeat
	def _get_backgroundRepeat(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundRepeat)
	def _set_backgroundRepeat(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundRepeat = unwrap(value)
	backgroundRepeat = property(_get_backgroundRepeat, _set_backgroundRepeat)

	#paddingTop
	def _get_paddingTop(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().paddingTop)
	def _set_paddingTop(self, value):
		self.__get_instance_IHTMLCurrentStyle().paddingTop = unwrap(value)
	paddingTop = property(_get_paddingTop, _set_paddingTop)

	#fontSize
	def _get_fontSize(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().fontSize)
	def _set_fontSize(self, value):
		self.__get_instance_IHTMLCurrentStyle().fontSize = unwrap(value)
	fontSize = property(_get_fontSize, _set_fontSize)

	#clipBottom
	def _get_clipBottom(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().clipBottom)
	def _set_clipBottom(self, value):
		self.__get_instance_IHTMLCurrentStyle().clipBottom = unwrap(value)
	clipBottom = property(_get_clipBottom, _set_clipBottom)

	#backgroundColor
	def _get_backgroundColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundColor)
	def _set_backgroundColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundColor = unwrap(value)
	backgroundColor = property(_get_backgroundColor, _set_backgroundColor)

	#unicodeBidi
	def _get_unicodeBidi(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().unicodeBidi)
	def _set_unicodeBidi(self, value):
		self.__get_instance_IHTMLCurrentStyle().unicodeBidi = unwrap(value)
	unicodeBidi = property(_get_unicodeBidi, _set_unicodeBidi)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#layoutGridChar
	def _get_layoutGridChar(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().layoutGridChar)
	def _set_layoutGridChar(self, value):
		self.__get_instance_IHTMLCurrentStyle().layoutGridChar = unwrap(value)
	layoutGridChar = property(_get_layoutGridChar, _set_layoutGridChar)

	#letterSpacing
	def _get_letterSpacing(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().letterSpacing)
	def _set_letterSpacing(self, value):
		self.__get_instance_IHTMLCurrentStyle().letterSpacing = unwrap(value)
	letterSpacing = property(_get_letterSpacing, _set_letterSpacing)

	#backgroundPositionX
	def _get_backgroundPositionX(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundPositionX)
	def _set_backgroundPositionX(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundPositionX = unwrap(value)
	backgroundPositionX = property(_get_backgroundPositionX, _set_backgroundPositionX)

	#backgroundPositionY
	def _get_backgroundPositionY(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundPositionY)
	def _set_backgroundPositionY(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundPositionY = unwrap(value)
	backgroundPositionY = property(_get_backgroundPositionY, _set_backgroundPositionY)

	#textDecoration
	def _get_textDecoration(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textDecoration)
	def _set_textDecoration(self, value):
		self.__get_instance_IHTMLCurrentStyle().textDecoration = unwrap(value)
	textDecoration = property(_get_textDecoration, _set_textDecoration)

	#textAutospace
	def _get_textAutospace(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textAutospace)
	def _set_textAutospace(self, value):
		self.__get_instance_IHTMLCurrentStyle().textAutospace = unwrap(value)
	textAutospace = property(_get_textAutospace, _set_textAutospace)

	#verticalAlign
	def _get_verticalAlign(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().verticalAlign)
	def _set_verticalAlign(self, value):
		self.__get_instance_IHTMLCurrentStyle().verticalAlign = unwrap(value)
	verticalAlign = property(_get_verticalAlign, _set_verticalAlign)

	#paddingLeft
	def _get_paddingLeft(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().paddingLeft)
	def _set_paddingLeft(self, value):
		self.__get_instance_IHTMLCurrentStyle().paddingLeft = unwrap(value)
	paddingLeft = property(_get_paddingLeft, _set_paddingLeft)

	#textIndent
	def _get_textIndent(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textIndent)
	def _set_textIndent(self, value):
		self.__get_instance_IHTMLCurrentStyle().textIndent = unwrap(value)
	textIndent = property(_get_textIndent, _set_textIndent)

	#listStyleImage
	def _get_listStyleImage(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().listStyleImage)
	def _set_listStyleImage(self, value):
		self.__get_instance_IHTMLCurrentStyle().listStyleImage = unwrap(value)
	listStyleImage = property(_get_listStyleImage, _set_listStyleImage)

	#marginTop
	def _get_marginTop(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().marginTop)
	def _set_marginTop(self, value):
		self.__get_instance_IHTMLCurrentStyle().marginTop = unwrap(value)
	marginTop = property(_get_marginTop, _set_marginTop)

	#clipTop
	def _get_clipTop(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().clipTop)
	def _set_clipTop(self, value):
		self.__get_instance_IHTMLCurrentStyle().clipTop = unwrap(value)
	clipTop = property(_get_clipTop, _set_clipTop)

	#textJustifyTrim
	def _get_textJustifyTrim(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textJustifyTrim)
	def _set_textJustifyTrim(self, value):
		self.__get_instance_IHTMLCurrentStyle().textJustifyTrim = unwrap(value)
	textJustifyTrim = property(_get_textJustifyTrim, _set_textJustifyTrim)

	#color
	def _get_color(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().color)
	def _set_color(self, value):
		self.__get_instance_IHTMLCurrentStyle().color = unwrap(value)
	color = property(_get_color, _set_color)

	#borderRightColor
	def _get_borderRightColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderRightColor)
	def _set_borderRightColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderRightColor = unwrap(value)
	borderRightColor = property(_get_borderRightColor, _set_borderRightColor)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLCurrentStyle().height = unwrap(value)
	height = property(_get_height, _set_height)

	#pageBreakAfter
	def _get_pageBreakAfter(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().pageBreakAfter)
	def _set_pageBreakAfter(self, value):
		self.__get_instance_IHTMLCurrentStyle().pageBreakAfter = unwrap(value)
	pageBreakAfter = property(_get_pageBreakAfter, _set_pageBreakAfter)

	#borderTopStyle
	def _get_borderTopStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderTopStyle)
	def _set_borderTopStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderTopStyle = unwrap(value)
	borderTopStyle = property(_get_borderTopStyle, _set_borderTopStyle)

	#paddingBottom
	def _get_paddingBottom(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().paddingBottom)
	def _set_paddingBottom(self, value):
		self.__get_instance_IHTMLCurrentStyle().paddingBottom = unwrap(value)
	paddingBottom = property(_get_paddingBottom, _set_paddingBottom)

	#top
	def _get_top(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().top)
	def _set_top(self, value):
		self.__get_instance_IHTMLCurrentStyle().top = unwrap(value)
	top = property(_get_top, _set_top)

	#rubyAlign
	def _get_rubyAlign(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().rubyAlign)
	def _set_rubyAlign(self, value):
		self.__get_instance_IHTMLCurrentStyle().rubyAlign = unwrap(value)
	rubyAlign = property(_get_rubyAlign, _set_rubyAlign)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLCurrentStyle().width = unwrap(value)
	width = property(_get_width, _set_width)

	#textKashida
	def _get_textKashida(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textKashida)
	def _set_textKashida(self, value):
		self.__get_instance_IHTMLCurrentStyle().textKashida = unwrap(value)
	textKashida = property(_get_textKashida, _set_textKashida)

	#borderTopWidth
	def _get_borderTopWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderTopWidth)
	def _set_borderTopWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderTopWidth = unwrap(value)
	borderTopWidth = property(_get_borderTopWidth, _set_borderTopWidth)

	#direction
	def _get_direction(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().direction)
	def _set_direction(self, value):
		self.__get_instance_IHTMLCurrentStyle().direction = unwrap(value)
	direction = property(_get_direction, _set_direction)

	#listStylePosition
	def _get_listStylePosition(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().listStylePosition)
	def _set_listStylePosition(self, value):
		self.__get_instance_IHTMLCurrentStyle().listStylePosition = unwrap(value)
	listStylePosition = property(_get_listStylePosition, _set_listStylePosition)

	#visibility
	def _get_visibility(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().visibility)
	def _set_visibility(self, value):
		self.__get_instance_IHTMLCurrentStyle().visibility = unwrap(value)
	visibility = property(_get_visibility, _set_visibility)

	#padding
	def _get_padding(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().padding)
	def _set_padding(self, value):
		self.__get_instance_IHTMLCurrentStyle().padding = unwrap(value)
	padding = property(_get_padding, _set_padding)

	#fontStyle
	def _get_fontStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().fontStyle)
	def _set_fontStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().fontStyle = unwrap(value)
	fontStyle = property(_get_fontStyle, _set_fontStyle)

	#overflow
	def _get_overflow(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().overflow)
	def _set_overflow(self, value):
		self.__get_instance_IHTMLCurrentStyle().overflow = unwrap(value)
	overflow = property(_get_overflow, _set_overflow)

	#wordBreak
	def _get_wordBreak(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().wordBreak)
	def _set_wordBreak(self, value):
		self.__get_instance_IHTMLCurrentStyle().wordBreak = unwrap(value)
	wordBreak = property(_get_wordBreak, _set_wordBreak)

	#cursor
	def _get_cursor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().cursor)
	def _set_cursor(self, value):
		self.__get_instance_IHTMLCurrentStyle().cursor = unwrap(value)
	cursor = property(_get_cursor, _set_cursor)

	#behavior
	def _get_behavior(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().behavior)
	def _set_behavior(self, value):
		self.__get_instance_IHTMLCurrentStyle().behavior = unwrap(value)
	behavior = property(_get_behavior, _set_behavior)

	#clipLeft
	def _get_clipLeft(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().clipLeft)
	def _set_clipLeft(self, value):
		self.__get_instance_IHTMLCurrentStyle().clipLeft = unwrap(value)
	clipLeft = property(_get_clipLeft, _set_clipLeft)

	#borderStyle
	def _get_borderStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderStyle)
	def _set_borderStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderStyle = unwrap(value)
	borderStyle = property(_get_borderStyle, _set_borderStyle)

	#margin
	def _get_margin(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().margin)
	def _set_margin(self, value):
		self.__get_instance_IHTMLCurrentStyle().margin = unwrap(value)
	margin = property(_get_margin, _set_margin)

	#display
	def _get_display(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().display)
	def _set_display(self, value):
		self.__get_instance_IHTMLCurrentStyle().display = unwrap(value)
	display = property(_get_display, _set_display)

	#listStyleType
	def _get_listStyleType(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().listStyleType)
	def _set_listStyleType(self, value):
		self.__get_instance_IHTMLCurrentStyle().listStyleType = unwrap(value)
	listStyleType = property(_get_listStyleType, _set_listStyleType)

	#borderLeftStyle
	def _get_borderLeftStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderLeftStyle)
	def _set_borderLeftStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderLeftStyle = unwrap(value)
	borderLeftStyle = property(_get_borderLeftStyle, _set_borderLeftStyle)

	#fontFamily
	def _get_fontFamily(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().fontFamily)
	def _set_fontFamily(self, value):
		self.__get_instance_IHTMLCurrentStyle().fontFamily = unwrap(value)
	fontFamily = property(_get_fontFamily, _set_fontFamily)

	#borderBottomWidth
	def _get_borderBottomWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderBottomWidth)
	def _set_borderBottomWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderBottomWidth = unwrap(value)
	borderBottomWidth = property(_get_borderBottomWidth, _set_borderBottomWidth)

	#marginRight
	def _get_marginRight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().marginRight)
	def _set_marginRight(self, value):
		self.__get_instance_IHTMLCurrentStyle().marginRight = unwrap(value)
	marginRight = property(_get_marginRight, _set_marginRight)

	#borderTopColor
	def _get_borderTopColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderTopColor)
	def _set_borderTopColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderTopColor = unwrap(value)
	borderTopColor = property(_get_borderTopColor, _set_borderTopColor)

	#rubyOverhang
	def _get_rubyOverhang(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().rubyOverhang)
	def _set_rubyOverhang(self, value):
		self.__get_instance_IHTMLCurrentStyle().rubyOverhang = unwrap(value)
	rubyOverhang = property(_get_rubyOverhang, _set_rubyOverhang)

	#marginLeft
	def _get_marginLeft(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().marginLeft)
	def _set_marginLeft(self, value):
		self.__get_instance_IHTMLCurrentStyle().marginLeft = unwrap(value)
	marginLeft = property(_get_marginLeft, _set_marginLeft)

	#backgroundImage
	def _get_backgroundImage(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundImage)
	def _set_backgroundImage(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundImage = unwrap(value)
	backgroundImage = property(_get_backgroundImage, _set_backgroundImage)

	#rubyPosition
	def _get_rubyPosition(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().rubyPosition)
	def _set_rubyPosition(self, value):
		self.__get_instance_IHTMLCurrentStyle().rubyPosition = unwrap(value)
	rubyPosition = property(_get_rubyPosition, _set_rubyPosition)

	#blockDirection
	def _get_blockDirection(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().blockDirection)
	def _set_blockDirection(self, value):
		self.__get_instance_IHTMLCurrentStyle().blockDirection = unwrap(value)
	blockDirection = property(_get_blockDirection, _set_blockDirection)

	#zIndex
	def _get_zIndex(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().zIndex)
	def _set_zIndex(self, value):
		self.__get_instance_IHTMLCurrentStyle().zIndex = unwrap(value)
	zIndex = property(_get_zIndex, _set_zIndex)

	#fontWeight
	def _get_fontWeight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().fontWeight)
	def _set_fontWeight(self, value):
		self.__get_instance_IHTMLCurrentStyle().fontWeight = unwrap(value)
	fontWeight = property(_get_fontWeight, _set_fontWeight)

	#lineBreak
	def _get_lineBreak(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().lineBreak)
	def _set_lineBreak(self, value):
		self.__get_instance_IHTMLCurrentStyle().lineBreak = unwrap(value)
	lineBreak = property(_get_lineBreak, _set_lineBreak)

	#borderBottomColor
	def _get_borderBottomColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderBottomColor)
	def _set_borderBottomColor(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderBottomColor = unwrap(value)
	borderBottomColor = property(_get_borderBottomColor, _set_borderBottomColor)

	#clear
	def _get_clear(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().clear)
	def _set_clear(self, value):
		self.__get_instance_IHTMLCurrentStyle().clear = unwrap(value)
	clear = property(_get_clear, _set_clear)

	#borderRightStyle
	def _get_borderRightStyle(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().borderRightStyle)
	def _set_borderRightStyle(self, value):
		self.__get_instance_IHTMLCurrentStyle().borderRightStyle = unwrap(value)
	borderRightStyle = property(_get_borderRightStyle, _set_borderRightStyle)

	#position
	def _get_position(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().position)
	def _set_position(self, value):
		self.__get_instance_IHTMLCurrentStyle().position = unwrap(value)
	position = property(_get_position, _set_position)

	#paddingRight
	def _get_paddingRight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().paddingRight)
	def _set_paddingRight(self, value):
		self.__get_instance_IHTMLCurrentStyle().paddingRight = unwrap(value)
	paddingRight = property(_get_paddingRight, _set_paddingRight)

	#textTransform
	def _get_textTransform(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().textTransform)
	def _set_textTransform(self, value):
		self.__get_instance_IHTMLCurrentStyle().textTransform = unwrap(value)
	textTransform = property(_get_textTransform, _set_textTransform)

	#backgroundAttachment
	def _get_backgroundAttachment(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle().backgroundAttachment)
	def _set_backgroundAttachment(self, value):
		self.__get_instance_IHTMLCurrentStyle().backgroundAttachment = unwrap(value)
	backgroundAttachment = property(_get_backgroundAttachment, _set_backgroundAttachment)

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCurrentStyle().getAttribute(*args))

wrapperClasses['{3050F3DB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle
backWrapperClasses[IHTMLCurrentStyle] = '{3050F3DB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle2
#
class IHTMLCurrentStyle2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCurrentStyle2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#scrollbarHighlightColor
	def _get_scrollbarHighlightColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarHighlightColor)
	def _set_scrollbarHighlightColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarHighlightColor = unwrap(value)
	scrollbarHighlightColor = property(_get_scrollbarHighlightColor, _set_scrollbarHighlightColor)

	#isBlock
	def _get_isBlock(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().isBlock)
	def _set_isBlock(self, value):
		self.__get_instance_IHTMLCurrentStyle2().isBlock = unwrap(value)
	isBlock = property(_get_isBlock, _set_isBlock)

	#hasLayout
	def _get_hasLayout(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().hasLayout)
	def _set_hasLayout(self, value):
		self.__get_instance_IHTMLCurrentStyle2().hasLayout = unwrap(value)
	hasLayout = property(_get_hasLayout, _set_hasLayout)

	#zoom
	def _get_zoom(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().zoom)
	def _set_zoom(self, value):
		self.__get_instance_IHTMLCurrentStyle2().zoom = unwrap(value)
	zoom = property(_get_zoom, _set_zoom)

	#scrollbarDarkShadowColor
	def _get_scrollbarDarkShadowColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarDarkShadowColor)
	def _set_scrollbarDarkShadowColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarDarkShadowColor = unwrap(value)
	scrollbarDarkShadowColor = property(_get_scrollbarDarkShadowColor, _set_scrollbarDarkShadowColor)

	#writingMode
	def _get_writingMode(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().writingMode)
	def _set_writingMode(self, value):
		self.__get_instance_IHTMLCurrentStyle2().writingMode = unwrap(value)
	writingMode = property(_get_writingMode, _set_writingMode)

	#scrollbarShadowColor
	def _get_scrollbarShadowColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarShadowColor)
	def _set_scrollbarShadowColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarShadowColor = unwrap(value)
	scrollbarShadowColor = property(_get_scrollbarShadowColor, _set_scrollbarShadowColor)

	#scrollbarFaceColor
	def _get_scrollbarFaceColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarFaceColor)
	def _set_scrollbarFaceColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarFaceColor = unwrap(value)
	scrollbarFaceColor = property(_get_scrollbarFaceColor, _set_scrollbarFaceColor)

	#scrollbarTrackColor
	def _get_scrollbarTrackColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarTrackColor)
	def _set_scrollbarTrackColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarTrackColor = unwrap(value)
	scrollbarTrackColor = property(_get_scrollbarTrackColor, _set_scrollbarTrackColor)

	#scrollbar3dLightColor
	def _get_scrollbar3dLightColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbar3dLightColor)
	def _set_scrollbar3dLightColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbar3dLightColor = unwrap(value)
	scrollbar3dLightColor = property(_get_scrollbar3dLightColor, _set_scrollbar3dLightColor)

	#scrollbarBaseColor
	def _get_scrollbarBaseColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarBaseColor)
	def _set_scrollbarBaseColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarBaseColor = unwrap(value)
	scrollbarBaseColor = property(_get_scrollbarBaseColor, _set_scrollbarBaseColor)

	#scrollbarArrowColor
	def _get_scrollbarArrowColor(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().scrollbarArrowColor)
	def _set_scrollbarArrowColor(self, value):
		self.__get_instance_IHTMLCurrentStyle2().scrollbarArrowColor = unwrap(value)
	scrollbarArrowColor = property(_get_scrollbarArrowColor, _set_scrollbarArrowColor)

	#textAlignLast
	def _get_textAlignLast(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().textAlignLast)
	def _set_textAlignLast(self, value):
		self.__get_instance_IHTMLCurrentStyle2().textAlignLast = unwrap(value)
	textAlignLast = property(_get_textAlignLast, _set_textAlignLast)

	#wordWrap
	def _get_wordWrap(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().wordWrap)
	def _set_wordWrap(self, value):
		self.__get_instance_IHTMLCurrentStyle2().wordWrap = unwrap(value)
	wordWrap = property(_get_wordWrap, _set_wordWrap)

	#textKashidaSpace
	def _get_textKashidaSpace(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().textKashidaSpace)
	def _set_textKashidaSpace(self, value):
		self.__get_instance_IHTMLCurrentStyle2().textKashidaSpace = unwrap(value)
	textKashidaSpace = property(_get_textKashidaSpace, _set_textKashidaSpace)

	#layoutFlow
	def _get_layoutFlow(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().layoutFlow)
	def _set_layoutFlow(self, value):
		self.__get_instance_IHTMLCurrentStyle2().layoutFlow = unwrap(value)
	layoutFlow = property(_get_layoutFlow, _set_layoutFlow)

	#filter
	def _get_filter(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().filter)
	def _set_filter(self, value):
		self.__get_instance_IHTMLCurrentStyle2().filter = unwrap(value)
	filter = property(_get_filter, _set_filter)

	#textUnderlinePosition
	def _get_textUnderlinePosition(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle2().textUnderlinePosition)
	def _set_textUnderlinePosition(self, value):
		self.__get_instance_IHTMLCurrentStyle2().textUnderlinePosition = unwrap(value)
	textUnderlinePosition = property(_get_textUnderlinePosition, _set_textUnderlinePosition)

wrapperClasses['{3050F658-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle2
backWrapperClasses[IHTMLCurrentStyle2] = '{3050F658-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle3
#
class IHTMLCurrentStyle3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCurrentStyle3(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle3
		return Dispatch(self.__instance__.QueryInterface(kls))
	#wordSpacing
	def _get_wordSpacing(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle3().wordSpacing)
	def _set_wordSpacing(self, value):
		self.__get_instance_IHTMLCurrentStyle3().wordSpacing = unwrap(value)
	wordSpacing = property(_get_wordSpacing, _set_wordSpacing)

	#textOverflow
	def _get_textOverflow(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle3().textOverflow)
	def _set_textOverflow(self, value):
		self.__get_instance_IHTMLCurrentStyle3().textOverflow = unwrap(value)
	textOverflow = property(_get_textOverflow, _set_textOverflow)

	#minHeight
	def _get_minHeight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle3().minHeight)
	def _set_minHeight(self, value):
		self.__get_instance_IHTMLCurrentStyle3().minHeight = unwrap(value)
	minHeight = property(_get_minHeight, _set_minHeight)

	#whiteSpace
	def _get_whiteSpace(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle3().whiteSpace)
	def _set_whiteSpace(self, value):
		self.__get_instance_IHTMLCurrentStyle3().whiteSpace = unwrap(value)
	whiteSpace = property(_get_whiteSpace, _set_whiteSpace)

wrapperClasses['{3050F818-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle3
backWrapperClasses[IHTMLCurrentStyle3] = '{3050F818-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCurrentStyle4
#
class IHTMLCurrentStyle4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCurrentStyle4(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCurrentStyle4
		return Dispatch(self.__instance__.QueryInterface(kls))
	#msInterpolationMode
	def _get_msInterpolationMode(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle4().msInterpolationMode)
	def _set_msInterpolationMode(self, value):
		self.__get_instance_IHTMLCurrentStyle4().msInterpolationMode = unwrap(value)
	msInterpolationMode = property(_get_msInterpolationMode, _set_msInterpolationMode)

	#minWidth
	def _get_minWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle4().minWidth)
	def _set_minWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle4().minWidth = unwrap(value)
	minWidth = property(_get_minWidth, _set_minWidth)

	#maxWidth
	def _get_maxWidth(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle4().maxWidth)
	def _set_maxWidth(self, value):
		self.__get_instance_IHTMLCurrentStyle4().maxWidth = unwrap(value)
	maxWidth = property(_get_maxWidth, _set_maxWidth)

	#maxHeight
	def _get_maxHeight(self):
		return wrap(self.__get_instance_IHTMLCurrentStyle4().maxHeight)
	def _set_maxHeight(self, value):
		self.__get_instance_IHTMLCurrentStyle4().maxHeight = unwrap(value)
	maxHeight = property(_get_maxHeight, _set_maxHeight)

wrapperClasses['{3050F33B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCurrentStyle4
backWrapperClasses[IHTMLCurrentStyle4] = '{3050F33B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLCurrentStyle
#
class DispHTMLCurrentStyle(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLCurrentStyle(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLCurrentStyle
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F557-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLCurrentStyle
backWrapperClasses[DispHTMLCurrentStyle] = '{3050F557-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRect
#
class IHTMLRect(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLRect(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRect
		return Dispatch(self.__instance__.QueryInterface(kls))
	#top
	def _get_top(self):
		return wrap(self.__get_instance_IHTMLRect().top)
	def _set_top(self, value):
		self.__get_instance_IHTMLRect().top = unwrap(value)
	top = property(_get_top, _set_top)

	#right
	def _get_right(self):
		return wrap(self.__get_instance_IHTMLRect().right)
	def _set_right(self, value):
		self.__get_instance_IHTMLRect().right = unwrap(value)
	right = property(_get_right, _set_right)

	#bottom
	def _get_bottom(self):
		return wrap(self.__get_instance_IHTMLRect().bottom)
	def _set_bottom(self, value):
		self.__get_instance_IHTMLRect().bottom = unwrap(value)
	bottom = property(_get_bottom, _set_bottom)

	#left
	def _get_left(self):
		return wrap(self.__get_instance_IHTMLRect().left)
	def _set_left(self, value):
		self.__get_instance_IHTMLRect().left = unwrap(value)
	left = property(_get_left, _set_left)

wrapperClasses['{3050F4A3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRect
backWrapperClasses[IHTMLRect] = '{3050F4A3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLRectCollection
#
class IHTMLRectCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLRectCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLRectCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLRectCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLRectCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLRectCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLRectCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLRectCollection().item(*args))

wrapperClasses['{3050F4A4-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLRectCollection
backWrapperClasses[IHTMLRectCollection] = '{3050F4A4-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMNode
#
class IHTMLDOMNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMNode(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMNode
		return Dispatch(self.__instance__.QueryInterface(kls))
	#lastChild
	def _get_lastChild(self):
		return wrap(self.__get_instance_IHTMLDOMNode().lastChild)
	def _set_lastChild(self, value):
		self.__get_instance_IHTMLDOMNode().lastChild = unwrap(value)
	lastChild = property(_get_lastChild, _set_lastChild)

	#nodeType
	def _get_nodeType(self):
		return wrap(self.__get_instance_IHTMLDOMNode().nodeType)
	def _set_nodeType(self, value):
		self.__get_instance_IHTMLDOMNode().nodeType = unwrap(value)
	nodeType = property(_get_nodeType, _set_nodeType)

	#nodeName
	def _get_nodeName(self):
		return wrap(self.__get_instance_IHTMLDOMNode().nodeName)
	def _set_nodeName(self, value):
		self.__get_instance_IHTMLDOMNode().nodeName = unwrap(value)
	nodeName = property(_get_nodeName, _set_nodeName)

	#nextSibling
	def _get_nextSibling(self):
		return wrap(self.__get_instance_IHTMLDOMNode().nextSibling)
	def _set_nextSibling(self, value):
		self.__get_instance_IHTMLDOMNode().nextSibling = unwrap(value)
	nextSibling = property(_get_nextSibling, _set_nextSibling)

	#nodeValue
	def _get_nodeValue(self):
		return wrap(self.__get_instance_IHTMLDOMNode().nodeValue)
	def _set_nodeValue(self, value):
		self.__get_instance_IHTMLDOMNode().nodeValue = unwrap(value)
	nodeValue = property(_get_nodeValue, _set_nodeValue)

	#firstChild
	def _get_firstChild(self):
		return wrap(self.__get_instance_IHTMLDOMNode().firstChild)
	def _set_firstChild(self, value):
		self.__get_instance_IHTMLDOMNode().firstChild = unwrap(value)
	firstChild = property(_get_firstChild, _set_firstChild)

	#parentNode
	def _get_parentNode(self):
		return wrap(self.__get_instance_IHTMLDOMNode().parentNode)
	def _set_parentNode(self, value):
		self.__get_instance_IHTMLDOMNode().parentNode = unwrap(value)
	parentNode = property(_get_parentNode, _set_parentNode)

	#attributes
	def _get_attributes(self):
		return wrap(self.__get_instance_IHTMLDOMNode().attributes)
	def _set_attributes(self, value):
		self.__get_instance_IHTMLDOMNode().attributes = unwrap(value)
	attributes = property(_get_attributes, _set_attributes)

	#childNodes
	def _get_childNodes(self):
		return wrap(self.__get_instance_IHTMLDOMNode().childNodes)
	def _set_childNodes(self, value):
		self.__get_instance_IHTMLDOMNode().childNodes = unwrap(value)
	childNodes = property(_get_childNodes, _set_childNodes)

	#previousSibling
	def _get_previousSibling(self):
		return wrap(self.__get_instance_IHTMLDOMNode().previousSibling)
	def _set_previousSibling(self, value):
		self.__get_instance_IHTMLDOMNode().previousSibling = unwrap(value)
	previousSibling = property(_get_previousSibling, _set_previousSibling)

	#appendChild
	def appendChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().appendChild(*args))

	#insertBefore
	def insertBefore(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().insertBefore(*args))

	#removeNode
	def removeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().removeNode(*args))

	#replaceNode
	def replaceNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().replaceNode(*args))

	#swapNode
	def swapNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().swapNode(*args))

	#cloneNode
	def cloneNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().cloneNode(*args))

	#removeChild
	def removeChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().removeChild(*args))

	#hasChildNodes
	def hasChildNodes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().hasChildNodes(*args))

	#replaceChild
	def replaceChild(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMNode().replaceChild(*args))

wrapperClasses['{3050F5DA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMNode
backWrapperClasses[IHTMLDOMNode] = '{3050F5DA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMNode2
#
class IHTMLDOMNode2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMNode2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMNode2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#ownerDocument
	def _get_ownerDocument(self):
		return wrap(self.__get_instance_IHTMLDOMNode2().ownerDocument)
	def _set_ownerDocument(self, value):
		self.__get_instance_IHTMLDOMNode2().ownerDocument = unwrap(value)
	ownerDocument = property(_get_ownerDocument, _set_ownerDocument)

wrapperClasses['{3050F80B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMNode2
backWrapperClasses[IHTMLDOMNode2] = '{3050F80B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMAttribute
#
class IHTMLDOMAttribute(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMAttribute(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMAttribute
		return Dispatch(self.__instance__.QueryInterface(kls))
	#nodeName
	def _get_nodeName(self):
		return wrap(self.__get_instance_IHTMLDOMAttribute().nodeName)
	def _set_nodeName(self, value):
		self.__get_instance_IHTMLDOMAttribute().nodeName = unwrap(value)
	nodeName = property(_get_nodeName, _set_nodeName)

	#nodeValue
	def _get_nodeValue(self):
		return wrap(self.__get_instance_IHTMLDOMAttribute().nodeValue)
	def _set_nodeValue(self, value):
		self.__get_instance_IHTMLDOMAttribute().nodeValue = unwrap(value)
	nodeValue = property(_get_nodeValue, _set_nodeValue)

	#specified
	def _get_specified(self):
		return wrap(self.__get_instance_IHTMLDOMAttribute().specified)
	def _set_specified(self, value):
		self.__get_instance_IHTMLDOMAttribute().specified = unwrap(value)
	specified = property(_get_specified, _set_specified)

wrapperClasses['{3050F4B0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMAttribute
backWrapperClasses[IHTMLDOMAttribute] = '{3050F4B0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMTextNode
#
class IHTMLDOMTextNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMTextNode(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMTextNode
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLDOMTextNode().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLDOMTextNode().length = unwrap(value)
	length = property(_get_length, _set_length)

	#data
	def _get_data(self):
		return wrap(self.__get_instance_IHTMLDOMTextNode().data)
	def _set_data(self, value):
		self.__get_instance_IHTMLDOMTextNode().data = unwrap(value)
	data = property(_get_data, _set_data)

	#splitText
	def splitText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode().splitText(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode().toString(*args))

wrapperClasses['{3050F4B1-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMTextNode
backWrapperClasses[IHTMLDOMTextNode] = '{3050F4B1-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMTextNode2
#
class IHTMLDOMTextNode2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMTextNode2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMTextNode2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#appendData
	def appendData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode2().appendData(*args))

	#deleteData
	def deleteData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode2().deleteData(*args))

	#substringData
	def substringData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode2().substringData(*args))

	#insertData
	def insertData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode2().insertData(*args))

	#replaceData
	def replaceData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMTextNode2().replaceData(*args))

wrapperClasses['{3050F809-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMTextNode2
backWrapperClasses[IHTMLDOMTextNode2] = '{3050F809-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMImplementation
#
class IHTMLDOMImplementation(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMImplementation(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMImplementation
		return Dispatch(self.__instance__.QueryInterface(kls))
	#hasFeature
	def hasFeature(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMImplementation().hasFeature(*args))

wrapperClasses['{3050F80D-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMImplementation
backWrapperClasses[IHTMLDOMImplementation] = '{3050F80D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLDOMTextNode
#
class DispHTMLDOMTextNode(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLDOMTextNode(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLDOMTextNode
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F565-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLDOMTextNode
backWrapperClasses[DispHTMLDOMTextNode] = '{3050F565-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDOMChildrenCollection
#
class IHTMLDOMChildrenCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDOMChildrenCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDOMChildrenCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLDOMChildrenCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLDOMChildrenCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLDOMChildrenCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLDOMChildrenCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDOMChildrenCollection().item(*args))

wrapperClasses['{3050F5AB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDOMChildrenCollection
backWrapperClasses[IHTMLDOMChildrenCollection] = '{3050F5AB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispDOMChildrenCollection
#
class DispDOMChildrenCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispDOMChildrenCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.DispDOMChildrenCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F577-98B5-11CF-BB82-00AA00BDCE0B}'] = DispDOMChildrenCollection
backWrapperClasses[DispDOMChildrenCollection] = '{3050F577-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement
#
class IHTMLElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#all
	def _get_all(self):
		return wrap(self.__get_instance_IHTMLElement().all)
	def _set_all(self, value):
		self.__get_instance_IHTMLElement().all = unwrap(value)
	all = property(_get_all, _set_all)

	#onrowexit
	def _get_onrowexit(self):
		return wrap(self.__get_instance_IHTMLElement().onrowexit)
	def _set_onrowexit(self, value):
		self.__get_instance_IHTMLElement().onrowexit = unwrap(value)
	onrowexit = property(_get_onrowexit, _set_onrowexit)

	#parentElement
	def _get_parentElement(self):
		return wrap(self.__get_instance_IHTMLElement().parentElement)
	def _set_parentElement(self, value):
		self.__get_instance_IHTMLElement().parentElement = unwrap(value)
	parentElement = property(_get_parentElement, _set_parentElement)

	#onafterupdate
	def _get_onafterupdate(self):
		return wrap(self.__get_instance_IHTMLElement().onafterupdate)
	def _set_onafterupdate(self, value):
		self.__get_instance_IHTMLElement().onafterupdate = unwrap(value)
	onafterupdate = property(_get_onafterupdate, _set_onafterupdate)

	#innerHTML
	def _get_innerHTML(self):
		return wrap(self.__get_instance_IHTMLElement().innerHTML)
	def _set_innerHTML(self, value):
		self.__get_instance_IHTMLElement().innerHTML = unwrap(value)
	innerHTML = property(_get_innerHTML, _set_innerHTML)

	#onmousedown
	def _get_onmousedown(self):
		return wrap(self.__get_instance_IHTMLElement().onmousedown)
	def _set_onmousedown(self, value):
		self.__get_instance_IHTMLElement().onmousedown = unwrap(value)
	onmousedown = property(_get_onmousedown, _set_onmousedown)

	#outerHTML
	def _get_outerHTML(self):
		return wrap(self.__get_instance_IHTMLElement().outerHTML)
	def _set_outerHTML(self, value):
		self.__get_instance_IHTMLElement().outerHTML = unwrap(value)
	outerHTML = property(_get_outerHTML, _set_outerHTML)

	#tagName
	def _get_tagName(self):
		return wrap(self.__get_instance_IHTMLElement().tagName)
	def _set_tagName(self, value):
		self.__get_instance_IHTMLElement().tagName = unwrap(value)
	tagName = property(_get_tagName, _set_tagName)

	#offsetHeight
	def _get_offsetHeight(self):
		return wrap(self.__get_instance_IHTMLElement().offsetHeight)
	def _set_offsetHeight(self, value):
		self.__get_instance_IHTMLElement().offsetHeight = unwrap(value)
	offsetHeight = property(_get_offsetHeight, _set_offsetHeight)

	#onerrorupdate
	def _get_onerrorupdate(self):
		return wrap(self.__get_instance_IHTMLElement().onerrorupdate)
	def _set_onerrorupdate(self, value):
		self.__get_instance_IHTMLElement().onerrorupdate = unwrap(value)
	onerrorupdate = property(_get_onerrorupdate, _set_onerrorupdate)

	#onfilterchange
	def _get_onfilterchange(self):
		return wrap(self.__get_instance_IHTMLElement().onfilterchange)
	def _set_onfilterchange(self, value):
		self.__get_instance_IHTMLElement().onfilterchange = unwrap(value)
	onfilterchange = property(_get_onfilterchange, _set_onfilterchange)

	#id
	def _get_id(self):
		return wrap(self.__get_instance_IHTMLElement().id)
	def _set_id(self, value):
		self.__get_instance_IHTMLElement().id = unwrap(value)
	id = property(_get_id, _set_id)

	#offsetParent
	def _get_offsetParent(self):
		return wrap(self.__get_instance_IHTMLElement().offsetParent)
	def _set_offsetParent(self, value):
		self.__get_instance_IHTMLElement().offsetParent = unwrap(value)
	offsetParent = property(_get_offsetParent, _set_offsetParent)

	#style
	def _get_style(self):
		return wrap(self.__get_instance_IHTMLElement().style)
	def _set_style(self, value):
		self.__get_instance_IHTMLElement().style = unwrap(value)
	style = property(_get_style, _set_style)

	#ondataavailable
	def _get_ondataavailable(self):
		return wrap(self.__get_instance_IHTMLElement().ondataavailable)
	def _set_ondataavailable(self, value):
		self.__get_instance_IHTMLElement().ondataavailable = unwrap(value)
	ondataavailable = property(_get_ondataavailable, _set_ondataavailable)

	#title
	def _get_title(self):
		return wrap(self.__get_instance_IHTMLElement().title)
	def _set_title(self, value):
		self.__get_instance_IHTMLElement().title = unwrap(value)
	title = property(_get_title, _set_title)

	#filters
	def _get_filters(self):
		return wrap(self.__get_instance_IHTMLElement().filters)
	def _set_filters(self, value):
		self.__get_instance_IHTMLElement().filters = unwrap(value)
	filters = property(_get_filters, _set_filters)

	#isTextEdit
	def _get_isTextEdit(self):
		return wrap(self.__get_instance_IHTMLElement().isTextEdit)
	def _set_isTextEdit(self, value):
		self.__get_instance_IHTMLElement().isTextEdit = unwrap(value)
	isTextEdit = property(_get_isTextEdit, _set_isTextEdit)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance_IHTMLElement().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance_IHTMLElement().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#children
	def _get_children(self):
		return wrap(self.__get_instance_IHTMLElement().children)
	def _set_children(self, value):
		self.__get_instance_IHTMLElement().children = unwrap(value)
	children = property(_get_children, _set_children)

	#onmousemove
	def _get_onmousemove(self):
		return wrap(self.__get_instance_IHTMLElement().onmousemove)
	def _set_onmousemove(self, value):
		self.__get_instance_IHTMLElement().onmousemove = unwrap(value)
	onmousemove = property(_get_onmousemove, _set_onmousemove)

	#ondatasetcomplete
	def _get_ondatasetcomplete(self):
		return wrap(self.__get_instance_IHTMLElement().ondatasetcomplete)
	def _set_ondatasetcomplete(self, value):
		self.__get_instance_IHTMLElement().ondatasetcomplete = unwrap(value)
	ondatasetcomplete = property(_get_ondatasetcomplete, _set_ondatasetcomplete)

	#onclick
	def _get_onclick(self):
		return wrap(self.__get_instance_IHTMLElement().onclick)
	def _set_onclick(self, value):
		self.__get_instance_IHTMLElement().onclick = unwrap(value)
	onclick = property(_get_onclick, _set_onclick)

	#offsetTop
	def _get_offsetTop(self):
		return wrap(self.__get_instance_IHTMLElement().offsetTop)
	def _set_offsetTop(self, value):
		self.__get_instance_IHTMLElement().offsetTop = unwrap(value)
	offsetTop = property(_get_offsetTop, _set_offsetTop)

	#offsetLeft
	def _get_offsetLeft(self):
		return wrap(self.__get_instance_IHTMLElement().offsetLeft)
	def _set_offsetLeft(self, value):
		self.__get_instance_IHTMLElement().offsetLeft = unwrap(value)
	offsetLeft = property(_get_offsetLeft, _set_offsetLeft)

	#document
	def _get_document(self):
		return wrap(self.__get_instance_IHTMLElement().document)
	def _set_document(self, value):
		self.__get_instance_IHTMLElement().document = unwrap(value)
	document = property(_get_document, _set_document)

	#ondragstart
	def _get_ondragstart(self):
		return wrap(self.__get_instance_IHTMLElement().ondragstart)
	def _set_ondragstart(self, value):
		self.__get_instance_IHTMLElement().ondragstart = unwrap(value)
	ondragstart = property(_get_ondragstart, _set_ondragstart)

	#onmouseup
	def _get_onmouseup(self):
		return wrap(self.__get_instance_IHTMLElement().onmouseup)
	def _set_onmouseup(self, value):
		self.__get_instance_IHTMLElement().onmouseup = unwrap(value)
	onmouseup = property(_get_onmouseup, _set_onmouseup)

	#onmouseout
	def _get_onmouseout(self):
		return wrap(self.__get_instance_IHTMLElement().onmouseout)
	def _set_onmouseout(self, value):
		self.__get_instance_IHTMLElement().onmouseout = unwrap(value)
	onmouseout = property(_get_onmouseout, _set_onmouseout)

	#onkeypress
	def _get_onkeypress(self):
		return wrap(self.__get_instance_IHTMLElement().onkeypress)
	def _set_onkeypress(self, value):
		self.__get_instance_IHTMLElement().onkeypress = unwrap(value)
	onkeypress = property(_get_onkeypress, _set_onkeypress)

	#onbeforeupdate
	def _get_onbeforeupdate(self):
		return wrap(self.__get_instance_IHTMLElement().onbeforeupdate)
	def _set_onbeforeupdate(self, value):
		self.__get_instance_IHTMLElement().onbeforeupdate = unwrap(value)
	onbeforeupdate = property(_get_onbeforeupdate, _set_onbeforeupdate)

	#onkeydown
	def _get_onkeydown(self):
		return wrap(self.__get_instance_IHTMLElement().onkeydown)
	def _set_onkeydown(self, value):
		self.__get_instance_IHTMLElement().onkeydown = unwrap(value)
	onkeydown = property(_get_onkeydown, _set_onkeydown)

	#onmouseover
	def _get_onmouseover(self):
		return wrap(self.__get_instance_IHTMLElement().onmouseover)
	def _set_onmouseover(self, value):
		self.__get_instance_IHTMLElement().onmouseover = unwrap(value)
	onmouseover = property(_get_onmouseover, _set_onmouseover)

	#parentTextEdit
	def _get_parentTextEdit(self):
		return wrap(self.__get_instance_IHTMLElement().parentTextEdit)
	def _set_parentTextEdit(self, value):
		self.__get_instance_IHTMLElement().parentTextEdit = unwrap(value)
	parentTextEdit = property(_get_parentTextEdit, _set_parentTextEdit)

	#recordNumber
	def _get_recordNumber(self):
		return wrap(self.__get_instance_IHTMLElement().recordNumber)
	def _set_recordNumber(self, value):
		self.__get_instance_IHTMLElement().recordNumber = unwrap(value)
	recordNumber = property(_get_recordNumber, _set_recordNumber)

	#lang
	def _get_lang(self):
		return wrap(self.__get_instance_IHTMLElement().lang)
	def _set_lang(self, value):
		self.__get_instance_IHTMLElement().lang = unwrap(value)
	lang = property(_get_lang, _set_lang)

	#onrowenter
	def _get_onrowenter(self):
		return wrap(self.__get_instance_IHTMLElement().onrowenter)
	def _set_onrowenter(self, value):
		self.__get_instance_IHTMLElement().onrowenter = unwrap(value)
	onrowenter = property(_get_onrowenter, _set_onrowenter)

	#language
	def _get_language(self):
		return wrap(self.__get_instance_IHTMLElement().language)
	def _set_language(self, value):
		self.__get_instance_IHTMLElement().language = unwrap(value)
	language = property(_get_language, _set_language)

	#offsetWidth
	def _get_offsetWidth(self):
		return wrap(self.__get_instance_IHTMLElement().offsetWidth)
	def _set_offsetWidth(self, value):
		self.__get_instance_IHTMLElement().offsetWidth = unwrap(value)
	offsetWidth = property(_get_offsetWidth, _set_offsetWidth)

	#ondatasetchanged
	def _get_ondatasetchanged(self):
		return wrap(self.__get_instance_IHTMLElement().ondatasetchanged)
	def _set_ondatasetchanged(self, value):
		self.__get_instance_IHTMLElement().ondatasetchanged = unwrap(value)
	ondatasetchanged = property(_get_ondatasetchanged, _set_ondatasetchanged)

	#className
	def _get_className(self):
		return wrap(self.__get_instance_IHTMLElement().className)
	def _set_className(self, value):
		self.__get_instance_IHTMLElement().className = unwrap(value)
	className = property(_get_className, _set_className)

	#sourceIndex
	def _get_sourceIndex(self):
		return wrap(self.__get_instance_IHTMLElement().sourceIndex)
	def _set_sourceIndex(self, value):
		self.__get_instance_IHTMLElement().sourceIndex = unwrap(value)
	sourceIndex = property(_get_sourceIndex, _set_sourceIndex)

	#innerText
	def _get_innerText(self):
		return wrap(self.__get_instance_IHTMLElement().innerText)
	def _set_innerText(self, value):
		self.__get_instance_IHTMLElement().innerText = unwrap(value)
	innerText = property(_get_innerText, _set_innerText)

	#onkeyup
	def _get_onkeyup(self):
		return wrap(self.__get_instance_IHTMLElement().onkeyup)
	def _set_onkeyup(self, value):
		self.__get_instance_IHTMLElement().onkeyup = unwrap(value)
	onkeyup = property(_get_onkeyup, _set_onkeyup)

	#ondblclick
	def _get_ondblclick(self):
		return wrap(self.__get_instance_IHTMLElement().ondblclick)
	def _set_ondblclick(self, value):
		self.__get_instance_IHTMLElement().ondblclick = unwrap(value)
	ondblclick = property(_get_ondblclick, _set_ondblclick)

	#onselectstart
	def _get_onselectstart(self):
		return wrap(self.__get_instance_IHTMLElement().onselectstart)
	def _set_onselectstart(self, value):
		self.__get_instance_IHTMLElement().onselectstart = unwrap(value)
	onselectstart = property(_get_onselectstart, _set_onselectstart)

	#outerText
	def _get_outerText(self):
		return wrap(self.__get_instance_IHTMLElement().outerText)
	def _set_outerText(self, value):
		self.__get_instance_IHTMLElement().outerText = unwrap(value)
	outerText = property(_get_outerText, _set_outerText)

	#removeAttribute
	def removeAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().removeAttribute(*args))

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().getAttribute(*args))

	#insertAdjacentText
	def insertAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().insertAdjacentText(*args))

	#contains
	def contains(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().contains(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().setAttribute(*args))

	#scrollIntoView
	def scrollIntoView(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().scrollIntoView(*args))

	#insertAdjacentHTML
	def insertAdjacentHTML(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().insertAdjacentHTML(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().toString(*args))

	#click
	def click(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement().click(*args))

wrapperClasses['{3050F1FF-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement
backWrapperClasses[IHTMLElement] = '{3050F1FF-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement2
#
class IHTMLElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLElement2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#behaviorUrns
	def _get_behaviorUrns(self):
		return wrap(self.__get_instance_IHTMLElement2().behaviorUrns)
	def _set_behaviorUrns(self, value):
		self.__get_instance_IHTMLElement2().behaviorUrns = unwrap(value)
	behaviorUrns = property(_get_behaviorUrns, _set_behaviorUrns)

	#clientHeight
	def _get_clientHeight(self):
		return wrap(self.__get_instance_IHTMLElement2().clientHeight)
	def _set_clientHeight(self, value):
		self.__get_instance_IHTMLElement2().clientHeight = unwrap(value)
	clientHeight = property(_get_clientHeight, _set_clientHeight)

	#ondragenter
	def _get_ondragenter(self):
		return wrap(self.__get_instance_IHTMLElement2().ondragenter)
	def _set_ondragenter(self, value):
		self.__get_instance_IHTMLElement2().ondragenter = unwrap(value)
	ondragenter = property(_get_ondragenter, _set_ondragenter)

	#onrowsinserted
	def _get_onrowsinserted(self):
		return wrap(self.__get_instance_IHTMLElement2().onrowsinserted)
	def _set_onrowsinserted(self, value):
		self.__get_instance_IHTMLElement2().onrowsinserted = unwrap(value)
	onrowsinserted = property(_get_onrowsinserted, _set_onrowsinserted)

	#onbeforecut
	def _get_onbeforecut(self):
		return wrap(self.__get_instance_IHTMLElement2().onbeforecut)
	def _set_onbeforecut(self, value):
		self.__get_instance_IHTMLElement2().onbeforecut = unwrap(value)
	onbeforecut = property(_get_onbeforecut, _set_onbeforecut)

	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance_IHTMLElement2().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance_IHTMLElement2().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#clientTop
	def _get_clientTop(self):
		return wrap(self.__get_instance_IHTMLElement2().clientTop)
	def _set_clientTop(self, value):
		self.__get_instance_IHTMLElement2().clientTop = unwrap(value)
	clientTop = property(_get_clientTop, _set_clientTop)

	#oncopy
	def _get_oncopy(self):
		return wrap(self.__get_instance_IHTMLElement2().oncopy)
	def _set_oncopy(self, value):
		self.__get_instance_IHTMLElement2().oncopy = unwrap(value)
	oncopy = property(_get_oncopy, _set_oncopy)

	#onbeforepaste
	def _get_onbeforepaste(self):
		return wrap(self.__get_instance_IHTMLElement2().onbeforepaste)
	def _set_onbeforepaste(self, value):
		self.__get_instance_IHTMLElement2().onbeforepaste = unwrap(value)
	onbeforepaste = property(_get_onbeforepaste, _set_onbeforepaste)

	#runtimeStyle
	def _get_runtimeStyle(self):
		return wrap(self.__get_instance_IHTMLElement2().runtimeStyle)
	def _set_runtimeStyle(self, value):
		self.__get_instance_IHTMLElement2().runtimeStyle = unwrap(value)
	runtimeStyle = property(_get_runtimeStyle, _set_runtimeStyle)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance_IHTMLElement2().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance_IHTMLElement2().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#scrollWidth
	def _get_scrollWidth(self):
		return wrap(self.__get_instance_IHTMLElement2().scrollWidth)
	def _set_scrollWidth(self, value):
		self.__get_instance_IHTMLElement2().scrollWidth = unwrap(value)
	scrollWidth = property(_get_scrollWidth, _set_scrollWidth)

	#ondragover
	def _get_ondragover(self):
		return wrap(self.__get_instance_IHTMLElement2().ondragover)
	def _set_ondragover(self, value):
		self.__get_instance_IHTMLElement2().ondragover = unwrap(value)
	ondragover = property(_get_ondragover, _set_ondragover)

	#clientLeft
	def _get_clientLeft(self):
		return wrap(self.__get_instance_IHTMLElement2().clientLeft)
	def _set_clientLeft(self, value):
		self.__get_instance_IHTMLElement2().clientLeft = unwrap(value)
	clientLeft = property(_get_clientLeft, _set_clientLeft)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance_IHTMLElement2().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance_IHTMLElement2().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#oncellchange
	def _get_oncellchange(self):
		return wrap(self.__get_instance_IHTMLElement2().oncellchange)
	def _set_oncellchange(self, value):
		self.__get_instance_IHTMLElement2().oncellchange = unwrap(value)
	oncellchange = property(_get_oncellchange, _set_oncellchange)

	#ondragleave
	def _get_ondragleave(self):
		return wrap(self.__get_instance_IHTMLElement2().ondragleave)
	def _set_ondragleave(self, value):
		self.__get_instance_IHTMLElement2().ondragleave = unwrap(value)
	ondragleave = property(_get_ondragleave, _set_ondragleave)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance_IHTMLElement2().onresize)
	def _set_onresize(self, value):
		self.__get_instance_IHTMLElement2().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance_IHTMLElement2().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance_IHTMLElement2().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#ondrag
	def _get_ondrag(self):
		return wrap(self.__get_instance_IHTMLElement2().ondrag)
	def _set_ondrag(self, value):
		self.__get_instance_IHTMLElement2().ondrag = unwrap(value)
	ondrag = property(_get_ondrag, _set_ondrag)

	#currentStyle
	def _get_currentStyle(self):
		return wrap(self.__get_instance_IHTMLElement2().currentStyle)
	def _set_currentStyle(self, value):
		self.__get_instance_IHTMLElement2().currentStyle = unwrap(value)
	currentStyle = property(_get_currentStyle, _set_currentStyle)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance_IHTMLElement2().onblur)
	def _set_onblur(self, value):
		self.__get_instance_IHTMLElement2().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#ondrop
	def _get_ondrop(self):
		return wrap(self.__get_instance_IHTMLElement2().ondrop)
	def _set_ondrop(self, value):
		self.__get_instance_IHTMLElement2().ondrop = unwrap(value)
	ondrop = property(_get_ondrop, _set_ondrop)

	#onrowsdelete
	def _get_onrowsdelete(self):
		return wrap(self.__get_instance_IHTMLElement2().onrowsdelete)
	def _set_onrowsdelete(self, value):
		self.__get_instance_IHTMLElement2().onrowsdelete = unwrap(value)
	onrowsdelete = property(_get_onrowsdelete, _set_onrowsdelete)

	#onpropertychange
	def _get_onpropertychange(self):
		return wrap(self.__get_instance_IHTMLElement2().onpropertychange)
	def _set_onpropertychange(self, value):
		self.__get_instance_IHTMLElement2().onpropertychange = unwrap(value)
	onpropertychange = property(_get_onpropertychange, _set_onpropertychange)

	#scrollLeft
	def _get_scrollLeft(self):
		return wrap(self.__get_instance_IHTMLElement2().scrollLeft)
	def _set_scrollLeft(self, value):
		self.__get_instance_IHTMLElement2().scrollLeft = unwrap(value)
	scrollLeft = property(_get_scrollLeft, _set_scrollLeft)

	#onbeforeeditfocus
	def _get_onbeforeeditfocus(self):
		return wrap(self.__get_instance_IHTMLElement2().onbeforeeditfocus)
	def _set_onbeforeeditfocus(self, value):
		self.__get_instance_IHTMLElement2().onbeforeeditfocus = unwrap(value)
	onbeforeeditfocus = property(_get_onbeforeeditfocus, _set_onbeforeeditfocus)

	#onbeforecopy
	def _get_onbeforecopy(self):
		return wrap(self.__get_instance_IHTMLElement2().onbeforecopy)
	def _set_onbeforecopy(self, value):
		self.__get_instance_IHTMLElement2().onbeforecopy = unwrap(value)
	onbeforecopy = property(_get_onbeforecopy, _set_onbeforecopy)

	#onpaste
	def _get_onpaste(self):
		return wrap(self.__get_instance_IHTMLElement2().onpaste)
	def _set_onpaste(self, value):
		self.__get_instance_IHTMLElement2().onpaste = unwrap(value)
	onpaste = property(_get_onpaste, _set_onpaste)

	#scrollHeight
	def _get_scrollHeight(self):
		return wrap(self.__get_instance_IHTMLElement2().scrollHeight)
	def _set_scrollHeight(self, value):
		self.__get_instance_IHTMLElement2().scrollHeight = unwrap(value)
	scrollHeight = property(_get_scrollHeight, _set_scrollHeight)

	#oncontextmenu
	def _get_oncontextmenu(self):
		return wrap(self.__get_instance_IHTMLElement2().oncontextmenu)
	def _set_oncontextmenu(self, value):
		self.__get_instance_IHTMLElement2().oncontextmenu = unwrap(value)
	oncontextmenu = property(_get_oncontextmenu, _set_oncontextmenu)

	#clientWidth
	def _get_clientWidth(self):
		return wrap(self.__get_instance_IHTMLElement2().clientWidth)
	def _set_clientWidth(self, value):
		self.__get_instance_IHTMLElement2().clientWidth = unwrap(value)
	clientWidth = property(_get_clientWidth, _set_clientWidth)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLElement2().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLElement2().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#ondragend
	def _get_ondragend(self):
		return wrap(self.__get_instance_IHTMLElement2().ondragend)
	def _set_ondragend(self, value):
		self.__get_instance_IHTMLElement2().ondragend = unwrap(value)
	ondragend = property(_get_ondragend, _set_ondragend)

	#scopeName
	def _get_scopeName(self):
		return wrap(self.__get_instance_IHTMLElement2().scopeName)
	def _set_scopeName(self, value):
		self.__get_instance_IHTMLElement2().scopeName = unwrap(value)
	scopeName = property(_get_scopeName, _set_scopeName)

	#onlosecapture
	def _get_onlosecapture(self):
		return wrap(self.__get_instance_IHTMLElement2().onlosecapture)
	def _set_onlosecapture(self, value):
		self.__get_instance_IHTMLElement2().onlosecapture = unwrap(value)
	onlosecapture = property(_get_onlosecapture, _set_onlosecapture)

	#oncut
	def _get_oncut(self):
		return wrap(self.__get_instance_IHTMLElement2().oncut)
	def _set_oncut(self, value):
		self.__get_instance_IHTMLElement2().oncut = unwrap(value)
	oncut = property(_get_oncut, _set_oncut)

	#canHaveChildren
	def _get_canHaveChildren(self):
		return wrap(self.__get_instance_IHTMLElement2().canHaveChildren)
	def _set_canHaveChildren(self, value):
		self.__get_instance_IHTMLElement2().canHaveChildren = unwrap(value)
	canHaveChildren = property(_get_canHaveChildren, _set_canHaveChildren)

	#scrollTop
	def _get_scrollTop(self):
		return wrap(self.__get_instance_IHTMLElement2().scrollTop)
	def _set_scrollTop(self, value):
		self.__get_instance_IHTMLElement2().scrollTop = unwrap(value)
	scrollTop = property(_get_scrollTop, _set_scrollTop)

	#readyStateValue
	def _get_readyStateValue(self):
		return wrap(self.__get_instance_IHTMLElement2().readyStateValue)
	def _set_readyStateValue(self, value):
		self.__get_instance_IHTMLElement2().readyStateValue = unwrap(value)
	readyStateValue = property(_get_readyStateValue, _set_readyStateValue)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance_IHTMLElement2().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance_IHTMLElement2().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance_IHTMLElement2().dir)
	def _set_dir(self, value):
		self.__get_instance_IHTMLElement2().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#tagUrn
	def _get_tagUrn(self):
		return wrap(self.__get_instance_IHTMLElement2().tagUrn)
	def _set_tagUrn(self, value):
		self.__get_instance_IHTMLElement2().tagUrn = unwrap(value)
	tagUrn = property(_get_tagUrn, _set_tagUrn)

	#setCapture
	def setCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().setCapture(*args))

	#releaseCapture
	def releaseCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().releaseCapture(*args))

	#replaceAdjacentText
	def replaceAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().replaceAdjacentText(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().attachEvent(*args))

	#createControlRange
	def createControlRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().createControlRange(*args))

	#getExpression
	def getExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().getExpression(*args))

	#getBoundingClientRect
	def getBoundingClientRect(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().getBoundingClientRect(*args))

	#removeExpression
	def removeExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().removeExpression(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().blur(*args))

	#getAdjacentText
	def getAdjacentText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().getAdjacentText(*args))

	#clearAttributes
	def clearAttributes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().clearAttributes(*args))

	#addBehavior
	def addBehavior(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().addBehavior(*args))

	#getClientRects
	def getClientRects(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().getClientRects(*args))

	#applyElement
	def applyElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().applyElement(*args))

	#getElementsByTagName
	def getElementsByTagName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().getElementsByTagName(*args))

	#insertAdjacentElement
	def insertAdjacentElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().insertAdjacentElement(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().focus(*args))

	#doScroll
	def doScroll(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().doScroll(*args))

	#removeBehavior
	def removeBehavior(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().removeBehavior(*args))

	#setExpression
	def setExpression(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().setExpression(*args))

	#mergeAttributes
	def mergeAttributes(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().mergeAttributes(*args))

	#componentFromPoint
	def componentFromPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().componentFromPoint(*args))

	#addFilter
	def addFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().addFilter(*args))

	#removeFilter
	def removeFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().removeFilter(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement2().detachEvent(*args))

wrapperClasses['{3050F434-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement2
backWrapperClasses[IHTMLElement2] = '{3050F434-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement3
#
class IHTMLElement3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLElement3(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement3
		return Dispatch(self.__instance__.QueryInterface(kls))
	#contentEditable
	def _get_contentEditable(self):
		return wrap(self.__get_instance_IHTMLElement3().contentEditable)
	def _set_contentEditable(self, value):
		self.__get_instance_IHTMLElement3().contentEditable = unwrap(value)
	contentEditable = property(_get_contentEditable, _set_contentEditable)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLElement3().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLElement3().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#onresizestart
	def _get_onresizestart(self):
		return wrap(self.__get_instance_IHTMLElement3().onresizestart)
	def _set_onresizestart(self, value):
		self.__get_instance_IHTMLElement3().onresizestart = unwrap(value)
	onresizestart = property(_get_onresizestart, _set_onresizestart)

	#ondeactivate
	def _get_ondeactivate(self):
		return wrap(self.__get_instance_IHTMLElement3().ondeactivate)
	def _set_ondeactivate(self, value):
		self.__get_instance_IHTMLElement3().ondeactivate = unwrap(value)
	ondeactivate = property(_get_ondeactivate, _set_ondeactivate)

	#onpage
	def _get_onpage(self):
		return wrap(self.__get_instance_IHTMLElement3().onpage)
	def _set_onpage(self, value):
		self.__get_instance_IHTMLElement3().onpage = unwrap(value)
	onpage = property(_get_onpage, _set_onpage)

	#isDisabled
	def _get_isDisabled(self):
		return wrap(self.__get_instance_IHTMLElement3().isDisabled)
	def _set_isDisabled(self, value):
		self.__get_instance_IHTMLElement3().isDisabled = unwrap(value)
	isDisabled = property(_get_isDisabled, _set_isDisabled)

	#glyphMode
	def _get_glyphMode(self):
		return wrap(self.__get_instance_IHTMLElement3().glyphMode)
	def _set_glyphMode(self, value):
		self.__get_instance_IHTMLElement3().glyphMode = unwrap(value)
	glyphMode = property(_get_glyphMode, _set_glyphMode)

	#oncontrolselect
	def _get_oncontrolselect(self):
		return wrap(self.__get_instance_IHTMLElement3().oncontrolselect)
	def _set_oncontrolselect(self, value):
		self.__get_instance_IHTMLElement3().oncontrolselect = unwrap(value)
	oncontrolselect = property(_get_oncontrolselect, _set_oncontrolselect)

	#onresizeend
	def _get_onresizeend(self):
		return wrap(self.__get_instance_IHTMLElement3().onresizeend)
	def _set_onresizeend(self, value):
		self.__get_instance_IHTMLElement3().onresizeend = unwrap(value)
	onresizeend = property(_get_onresizeend, _set_onresizeend)

	#onmoveend
	def _get_onmoveend(self):
		return wrap(self.__get_instance_IHTMLElement3().onmoveend)
	def _set_onmoveend(self, value):
		self.__get_instance_IHTMLElement3().onmoveend = unwrap(value)
	onmoveend = property(_get_onmoveend, _set_onmoveend)

	#isMultiLine
	def _get_isMultiLine(self):
		return wrap(self.__get_instance_IHTMLElement3().isMultiLine)
	def _set_isMultiLine(self, value):
		self.__get_instance_IHTMLElement3().isMultiLine = unwrap(value)
	isMultiLine = property(_get_isMultiLine, _set_isMultiLine)

	#hideFocus
	def _get_hideFocus(self):
		return wrap(self.__get_instance_IHTMLElement3().hideFocus)
	def _set_hideFocus(self, value):
		self.__get_instance_IHTMLElement3().hideFocus = unwrap(value)
	hideFocus = property(_get_hideFocus, _set_hideFocus)

	#isContentEditable
	def _get_isContentEditable(self):
		return wrap(self.__get_instance_IHTMLElement3().isContentEditable)
	def _set_isContentEditable(self, value):
		self.__get_instance_IHTMLElement3().isContentEditable = unwrap(value)
	isContentEditable = property(_get_isContentEditable, _set_isContentEditable)

	#onactivate
	def _get_onactivate(self):
		return wrap(self.__get_instance_IHTMLElement3().onactivate)
	def _set_onactivate(self, value):
		self.__get_instance_IHTMLElement3().onactivate = unwrap(value)
	onactivate = property(_get_onactivate, _set_onactivate)

	#onmouseleave
	def _get_onmouseleave(self):
		return wrap(self.__get_instance_IHTMLElement3().onmouseleave)
	def _set_onmouseleave(self, value):
		self.__get_instance_IHTMLElement3().onmouseleave = unwrap(value)
	onmouseleave = property(_get_onmouseleave, _set_onmouseleave)

	#inflateBlock
	def _get_inflateBlock(self):
		return wrap(self.__get_instance_IHTMLElement3().inflateBlock)
	def _set_inflateBlock(self, value):
		self.__get_instance_IHTMLElement3().inflateBlock = unwrap(value)
	inflateBlock = property(_get_inflateBlock, _set_inflateBlock)

	#canHaveHTML
	def _get_canHaveHTML(self):
		return wrap(self.__get_instance_IHTMLElement3().canHaveHTML)
	def _set_canHaveHTML(self, value):
		self.__get_instance_IHTMLElement3().canHaveHTML = unwrap(value)
	canHaveHTML = property(_get_canHaveHTML, _set_canHaveHTML)

	#onmouseenter
	def _get_onmouseenter(self):
		return wrap(self.__get_instance_IHTMLElement3().onmouseenter)
	def _set_onmouseenter(self, value):
		self.__get_instance_IHTMLElement3().onmouseenter = unwrap(value)
	onmouseenter = property(_get_onmouseenter, _set_onmouseenter)

	#onlayoutcomplete
	def _get_onlayoutcomplete(self):
		return wrap(self.__get_instance_IHTMLElement3().onlayoutcomplete)
	def _set_onlayoutcomplete(self, value):
		self.__get_instance_IHTMLElement3().onlayoutcomplete = unwrap(value)
	onlayoutcomplete = property(_get_onlayoutcomplete, _set_onlayoutcomplete)

	#onbeforedeactivate
	def _get_onbeforedeactivate(self):
		return wrap(self.__get_instance_IHTMLElement3().onbeforedeactivate)
	def _set_onbeforedeactivate(self, value):
		self.__get_instance_IHTMLElement3().onbeforedeactivate = unwrap(value)
	onbeforedeactivate = property(_get_onbeforedeactivate, _set_onbeforedeactivate)

	#onmovestart
	def _get_onmovestart(self):
		return wrap(self.__get_instance_IHTMLElement3().onmovestart)
	def _set_onmovestart(self, value):
		self.__get_instance_IHTMLElement3().onmovestart = unwrap(value)
	onmovestart = property(_get_onmovestart, _set_onmovestart)

	#onmove
	def _get_onmove(self):
		return wrap(self.__get_instance_IHTMLElement3().onmove)
	def _set_onmove(self, value):
		self.__get_instance_IHTMLElement3().onmove = unwrap(value)
	onmove = property(_get_onmove, _set_onmove)

	#fireEvent
	def fireEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement3().fireEvent(*args))

wrapperClasses['{3050F673-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement3
backWrapperClasses[IHTMLElement3] = '{3050F673-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElement4
#
class IHTMLElement4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLElement4(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElement4
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onfocusout
	def _get_onfocusout(self):
		return wrap(self.__get_instance_IHTMLElement4().onfocusout)
	def _set_onfocusout(self, value):
		self.__get_instance_IHTMLElement4().onfocusout = unwrap(value)
	onfocusout = property(_get_onfocusout, _set_onfocusout)

	#onmousewheel
	def _get_onmousewheel(self):
		return wrap(self.__get_instance_IHTMLElement4().onmousewheel)
	def _set_onmousewheel(self, value):
		self.__get_instance_IHTMLElement4().onmousewheel = unwrap(value)
	onmousewheel = property(_get_onmousewheel, _set_onmousewheel)

	#onfocusin
	def _get_onfocusin(self):
		return wrap(self.__get_instance_IHTMLElement4().onfocusin)
	def _set_onfocusin(self, value):
		self.__get_instance_IHTMLElement4().onfocusin = unwrap(value)
	onfocusin = property(_get_onfocusin, _set_onfocusin)

	#onbeforeactivate
	def _get_onbeforeactivate(self):
		return wrap(self.__get_instance_IHTMLElement4().onbeforeactivate)
	def _set_onbeforeactivate(self, value):
		self.__get_instance_IHTMLElement4().onbeforeactivate = unwrap(value)
	onbeforeactivate = property(_get_onbeforeactivate, _set_onbeforeactivate)

	#normalize
	def normalize(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement4().normalize(*args))

	#getAttributeNode
	def getAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement4().getAttributeNode(*args))

	#setAttributeNode
	def setAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement4().setAttributeNode(*args))

	#removeAttributeNode
	def removeAttributeNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElement4().removeAttributeNode(*args))

wrapperClasses['{3050F80F-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElement4
backWrapperClasses[IHTMLElement4] = '{3050F80F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLGenericElement
#
class IHTMLGenericElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLGenericElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLGenericElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#recordset
	def _get_recordset(self):
		return wrap(self.__get_instance_IHTMLGenericElement().recordset)
	def _set_recordset(self, value):
		self.__get_instance_IHTMLGenericElement().recordset = unwrap(value)
	recordset = property(_get_recordset, _set_recordset)

	#namedRecordset
	def namedRecordset(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLGenericElement().namedRecordset(*args))

wrapperClasses['{3050F4B7-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLGenericElement
backWrapperClasses[IHTMLGenericElement] = '{3050F4B7-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLGenericElement
#
class DispHTMLGenericElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLGenericElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLGenericElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F563-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLGenericElement
backWrapperClasses[DispHTMLGenericElement] = '{3050F563-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetRule
#
class IHTMLStyleSheetRule(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheetRule(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetRule
		return Dispatch(self.__instance__.QueryInterface(kls))
	#style
	def _get_style(self):
		return wrap(self.__get_instance_IHTMLStyleSheetRule().style)
	def _set_style(self, value):
		self.__get_instance_IHTMLStyleSheetRule().style = unwrap(value)
	style = property(_get_style, _set_style)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance_IHTMLStyleSheetRule().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance_IHTMLStyleSheetRule().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#selectorText
	def _get_selectorText(self):
		return wrap(self.__get_instance_IHTMLStyleSheetRule().selectorText)
	def _set_selectorText(self, value):
		self.__get_instance_IHTMLStyleSheetRule().selectorText = unwrap(value)
	selectorText = property(_get_selectorText, _set_selectorText)

wrapperClasses['{3050F357-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetRule
backWrapperClasses[IHTMLStyleSheetRule] = '{3050F357-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetRulesCollection
#
class IHTMLStyleSheetRulesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheetRulesCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetRulesCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLStyleSheetRulesCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLStyleSheetRulesCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheetRulesCollection().item(*args))

wrapperClasses['{3050F2E5-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetRulesCollection
backWrapperClasses[IHTMLStyleSheetRulesCollection] = '{3050F2E5-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetPage
#
class IHTMLStyleSheetPage(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheetPage(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetPage
		return Dispatch(self.__instance__.QueryInterface(kls))
	#pseudoClass
	def _get_pseudoClass(self):
		return wrap(self.__get_instance_IHTMLStyleSheetPage().pseudoClass)
	def _set_pseudoClass(self, value):
		self.__get_instance_IHTMLStyleSheetPage().pseudoClass = unwrap(value)
	pseudoClass = property(_get_pseudoClass, _set_pseudoClass)

	#selector
	def _get_selector(self):
		return wrap(self.__get_instance_IHTMLStyleSheetPage().selector)
	def _set_selector(self, value):
		self.__get_instance_IHTMLStyleSheetPage().selector = unwrap(value)
	selector = property(_get_selector, _set_selector)

wrapperClasses['{3050F7EE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetPage
backWrapperClasses[IHTMLStyleSheetPage] = '{3050F7EE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetPagesCollection
#
class IHTMLStyleSheetPagesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheetPagesCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetPagesCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLStyleSheetPagesCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLStyleSheetPagesCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheetPagesCollection().item(*args))

wrapperClasses['{3050F7F0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetPagesCollection
backWrapperClasses[IHTMLStyleSheetPagesCollection] = '{3050F7F0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheet
#
class IHTMLStyleSheet(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheet(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheet
		return Dispatch(self.__instance__.QueryInterface(kls))
	#title
	def _get_title(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().title)
	def _set_title(self, value):
		self.__get_instance_IHTMLStyleSheet().title = unwrap(value)
	title = property(_get_title, _set_title)

	#parentStyleSheet
	def _get_parentStyleSheet(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().parentStyleSheet)
	def _set_parentStyleSheet(self, value):
		self.__get_instance_IHTMLStyleSheet().parentStyleSheet = unwrap(value)
	parentStyleSheet = property(_get_parentStyleSheet, _set_parentStyleSheet)

	#imports
	def _get_imports(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().imports)
	def _set_imports(self, value):
		self.__get_instance_IHTMLStyleSheet().imports = unwrap(value)
	imports = property(_get_imports, _set_imports)

	#cssText
	def _get_cssText(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().cssText)
	def _set_cssText(self, value):
		self.__get_instance_IHTMLStyleSheet().cssText = unwrap(value)
	cssText = property(_get_cssText, _set_cssText)

	#owningElement
	def _get_owningElement(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().owningElement)
	def _set_owningElement(self, value):
		self.__get_instance_IHTMLStyleSheet().owningElement = unwrap(value)
	owningElement = property(_get_owningElement, _set_owningElement)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLStyleSheet().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#rules
	def _get_rules(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().rules)
	def _set_rules(self, value):
		self.__get_instance_IHTMLStyleSheet().rules = unwrap(value)
	rules = property(_get_rules, _set_rules)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance_IHTMLStyleSheet().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#href
	def _get_href(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().href)
	def _set_href(self, value):
		self.__get_instance_IHTMLStyleSheet().href = unwrap(value)
	href = property(_get_href, _set_href)

	#media
	def _get_media(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().media)
	def _set_media(self, value):
		self.__get_instance_IHTMLStyleSheet().media = unwrap(value)
	media = property(_get_media, _set_media)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLStyleSheet().type = unwrap(value)
	type = property(_get_type, _set_type)

	#id
	def _get_id(self):
		return wrap(self.__get_instance_IHTMLStyleSheet().id)
	def _set_id(self, value):
		self.__get_instance_IHTMLStyleSheet().id = unwrap(value)
	id = property(_get_id, _set_id)

	#addRule
	def addRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheet().addRule(*args))

	#removeRule
	def removeRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheet().removeRule(*args))

	#removeImport
	def removeImport(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheet().removeImport(*args))

	#addImport
	def addImport(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheet().addImport(*args))

wrapperClasses['{3050F2E3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheet
backWrapperClasses[IHTMLStyleSheet] = '{3050F2E3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheet2
#
class IHTMLStyleSheet2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheet2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheet2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#pages
	def _get_pages(self):
		return wrap(self.__get_instance_IHTMLStyleSheet2().pages)
	def _set_pages(self, value):
		self.__get_instance_IHTMLStyleSheet2().pages = unwrap(value)
	pages = property(_get_pages, _set_pages)

	#addPageRule
	def addPageRule(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheet2().addPageRule(*args))

wrapperClasses['{3050F3D1-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheet2
backWrapperClasses[IHTMLStyleSheet2] = '{3050F3D1-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLStyleSheet
#
class DispHTMLStyleSheet(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLStyleSheet(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLStyleSheet
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F58D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLStyleSheet
backWrapperClasses[DispHTMLStyleSheet] = '{3050F58D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLStyleSheetsCollection
#
class IHTMLStyleSheetsCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLStyleSheetsCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLStyleSheetsCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLStyleSheetsCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLStyleSheetsCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLStyleSheetsCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLStyleSheetsCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLStyleSheetsCollection().item(*args))

wrapperClasses['{3050F37E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLStyleSheetsCollection
backWrapperClasses[IHTMLStyleSheetsCollection] = '{3050F37E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTxtRange
#
class IHTMLTxtRange(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTxtRange(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTxtRange
		return Dispatch(self.__instance__.QueryInterface(kls))
	#text
	def _get_text(self):
		return wrap(self.__get_instance_IHTMLTxtRange().text)
	def _set_text(self, value):
		self.__get_instance_IHTMLTxtRange().text = unwrap(value)
	text = property(_get_text, _set_text)

	#htmlText
	def _get_htmlText(self):
		return wrap(self.__get_instance_IHTMLTxtRange().htmlText)
	def _set_htmlText(self, value):
		self.__get_instance_IHTMLTxtRange().htmlText = unwrap(value)
	htmlText = property(_get_htmlText, _set_htmlText)

	#moveStart
	def moveStart(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().moveStart(*args))

	#parentElement
	def parentElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().parentElement(*args))

	#move
	def move(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().move(*args))

	#findText
	def findText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().findText(*args))

	#getBookmark
	def getBookmark(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().getBookmark(*args))

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().select(*args))

	#setEndPoint
	def setEndPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().setEndPoint(*args))

	#moveEnd
	def moveEnd(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().moveEnd(*args))

	#execCommandShowHelp
	def execCommandShowHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().execCommandShowHelp(*args))

	#duplicate
	def duplicate(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().duplicate(*args))

	#expand
	def expand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().expand(*args))

	#inRange
	def inRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().inRange(*args))

	#queryCommandIndeterm
	def queryCommandIndeterm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandIndeterm(*args))

	#pasteHTML
	def pasteHTML(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().pasteHTML(*args))

	#collapse
	def collapse(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().collapse(*args))

	#compareEndPoints
	def compareEndPoints(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().compareEndPoints(*args))

	#queryCommandState
	def queryCommandState(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandState(*args))

	#moveToPoint
	def moveToPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().moveToPoint(*args))

	#moveToBookmark
	def moveToBookmark(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().moveToBookmark(*args))

	#queryCommandValue
	def queryCommandValue(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandValue(*args))

	#queryCommandSupported
	def queryCommandSupported(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandSupported(*args))

	#scrollIntoView
	def scrollIntoView(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().scrollIntoView(*args))

	#execCommand
	def execCommand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().execCommand(*args))

	#queryCommandText
	def queryCommandText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandText(*args))

	#moveToElementText
	def moveToElementText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().moveToElementText(*args))

	#queryCommandEnabled
	def queryCommandEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().queryCommandEnabled(*args))

	#isEqual
	def isEqual(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTxtRange().isEqual(*args))

wrapperClasses['{3050F220-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTxtRange
backWrapperClasses[IHTMLTxtRange] = '{3050F220-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFormElement
#
class IHTMLFormElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLFormElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFormElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#elements
	def _get_elements(self):
		return wrap(self.__get_instance_IHTMLFormElement().elements)
	def _set_elements(self, value):
		self.__get_instance_IHTMLFormElement().elements = unwrap(value)
	elements = property(_get_elements, _set_elements)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLFormElement()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLFormElement()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#target
	def _get_target(self):
		return wrap(self.__get_instance_IHTMLFormElement().target)
	def _set_target(self, value):
		self.__get_instance_IHTMLFormElement().target = unwrap(value)
	target = property(_get_target, _set_target)

	#encoding
	def _get_encoding(self):
		return wrap(self.__get_instance_IHTMLFormElement().encoding)
	def _set_encoding(self, value):
		self.__get_instance_IHTMLFormElement().encoding = unwrap(value)
	encoding = property(_get_encoding, _set_encoding)

	#onreset
	def _get_onreset(self):
		return wrap(self.__get_instance_IHTMLFormElement().onreset)
	def _set_onreset(self, value):
		self.__get_instance_IHTMLFormElement().onreset = unwrap(value)
	onreset = property(_get_onreset, _set_onreset)

	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLFormElement().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLFormElement().length = unwrap(value)
	length = property(_get_length, _set_length)

	#onsubmit
	def _get_onsubmit(self):
		return wrap(self.__get_instance_IHTMLFormElement().onsubmit)
	def _set_onsubmit(self, value):
		self.__get_instance_IHTMLFormElement().onsubmit = unwrap(value)
	onsubmit = property(_get_onsubmit, _set_onsubmit)

	#action
	def _get_action(self):
		return wrap(self.__get_instance_IHTMLFormElement().action)
	def _set_action(self, value):
		self.__get_instance_IHTMLFormElement().action = unwrap(value)
	action = property(_get_action, _set_action)

	#method
	def _get_method(self):
		return wrap(self.__get_instance_IHTMLFormElement().method)
	def _set_method(self, value):
		self.__get_instance_IHTMLFormElement().method = unwrap(value)
	method = property(_get_method, _set_method)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance_IHTMLFormElement().dir)
	def _set_dir(self, value):
		self.__get_instance_IHTMLFormElement().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLFormElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLFormElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#reset
	def reset(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFormElement().reset(*args))

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFormElement().item(*args))

	#submit
	def submit(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFormElement().submit(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFormElement().tags(*args))

wrapperClasses['{3050F1F7-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFormElement
backWrapperClasses[IHTMLFormElement] = '{3050F1F7-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTextContainer
#
class IHTMLTextContainer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTextContainer(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTextContainer
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance_IHTMLTextContainer().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance_IHTMLTextContainer().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#scrollTop
	def _get_scrollTop(self):
		return wrap(self.__get_instance_IHTMLTextContainer().scrollTop)
	def _set_scrollTop(self, value):
		self.__get_instance_IHTMLTextContainer().scrollTop = unwrap(value)
	scrollTop = property(_get_scrollTop, _set_scrollTop)

	#scrollWidth
	def _get_scrollWidth(self):
		return wrap(self.__get_instance_IHTMLTextContainer().scrollWidth)
	def _set_scrollWidth(self, value):
		self.__get_instance_IHTMLTextContainer().scrollWidth = unwrap(value)
	scrollWidth = property(_get_scrollWidth, _set_scrollWidth)

	#scrollLeft
	def _get_scrollLeft(self):
		return wrap(self.__get_instance_IHTMLTextContainer().scrollLeft)
	def _set_scrollLeft(self, value):
		self.__get_instance_IHTMLTextContainer().scrollLeft = unwrap(value)
	scrollLeft = property(_get_scrollLeft, _set_scrollLeft)

	#scrollHeight
	def _get_scrollHeight(self):
		return wrap(self.__get_instance_IHTMLTextContainer().scrollHeight)
	def _set_scrollHeight(self, value):
		self.__get_instance_IHTMLTextContainer().scrollHeight = unwrap(value)
	scrollHeight = property(_get_scrollHeight, _set_scrollHeight)

	#createControlRange
	def createControlRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTextContainer().createControlRange(*args))

wrapperClasses['{3050F230-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTextContainer
backWrapperClasses[IHTMLTextContainer] = '{3050F230-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLImgElement
#
class IHTMLImgElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLImgElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLImgElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance_IHTMLImgElement().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance_IHTMLImgElement().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance_IHTMLImgElement().protocol)
	def _set_protocol(self, value):
		self.__get_instance_IHTMLImgElement().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance_IHTMLImgElement().onerror)
	def _set_onerror(self, value):
		self.__get_instance_IHTMLImgElement().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#fileCreatedDate
	def _get_fileCreatedDate(self):
		return wrap(self.__get_instance_IHTMLImgElement().fileCreatedDate)
	def _set_fileCreatedDate(self, value):
		self.__get_instance_IHTMLImgElement().fileCreatedDate = unwrap(value)
	fileCreatedDate = property(_get_fileCreatedDate, _set_fileCreatedDate)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLImgElement().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLImgElement().height = unwrap(value)
	height = property(_get_height, _set_height)

	#href
	def _get_href(self):
		return wrap(self.__get_instance_IHTMLImgElement().href)
	def _set_href(self, value):
		self.__get_instance_IHTMLImgElement().href = unwrap(value)
	href = property(_get_href, _set_href)

	#alt
	def _get_alt(self):
		return wrap(self.__get_instance_IHTMLImgElement().alt)
	def _set_alt(self, value):
		self.__get_instance_IHTMLImgElement().alt = unwrap(value)
	alt = property(_get_alt, _set_alt)

	#fileModifiedDate
	def _get_fileModifiedDate(self):
		return wrap(self.__get_instance_IHTMLImgElement().fileModifiedDate)
	def _set_fileModifiedDate(self, value):
		self.__get_instance_IHTMLImgElement().fileModifiedDate = unwrap(value)
	fileModifiedDate = property(_get_fileModifiedDate, _set_fileModifiedDate)

	#hspace
	def _get_hspace(self):
		return wrap(self.__get_instance_IHTMLImgElement().hspace)
	def _set_hspace(self, value):
		self.__get_instance_IHTMLImgElement().hspace = unwrap(value)
	hspace = property(_get_hspace, _set_hspace)

	#onabort
	def _get_onabort(self):
		return wrap(self.__get_instance_IHTMLImgElement().onabort)
	def _set_onabort(self, value):
		self.__get_instance_IHTMLImgElement().onabort = unwrap(value)
	onabort = property(_get_onabort, _set_onabort)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance_IHTMLImgElement().onload)
	def _set_onload(self, value):
		self.__get_instance_IHTMLImgElement().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#start
	def _get_start(self):
		return wrap(self.__get_instance_IHTMLImgElement().start)
	def _set_start(self, value):
		self.__get_instance_IHTMLImgElement().start = unwrap(value)
	start = property(_get_start, _set_start)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLImgElement().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLImgElement().border = unwrap(value)
	border = property(_get_border, _set_border)

	#vspace
	def _get_vspace(self):
		return wrap(self.__get_instance_IHTMLImgElement().vspace)
	def _set_vspace(self, value):
		self.__get_instance_IHTMLImgElement().vspace = unwrap(value)
	vspace = property(_get_vspace, _set_vspace)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLImgElement().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLImgElement().width = unwrap(value)
	width = property(_get_width, _set_width)

	#useMap
	def _get_useMap(self):
		return wrap(self.__get_instance_IHTMLImgElement().useMap)
	def _set_useMap(self, value):
		self.__get_instance_IHTMLImgElement().useMap = unwrap(value)
	useMap = property(_get_useMap, _set_useMap)

	#vrml
	def _get_vrml(self):
		return wrap(self.__get_instance_IHTMLImgElement().vrml)
	def _set_vrml(self, value):
		self.__get_instance_IHTMLImgElement().vrml = unwrap(value)
	vrml = property(_get_vrml, _set_vrml)

	#fileUpdatedDate
	def _get_fileUpdatedDate(self):
		return wrap(self.__get_instance_IHTMLImgElement().fileUpdatedDate)
	def _set_fileUpdatedDate(self, value):
		self.__get_instance_IHTMLImgElement().fileUpdatedDate = unwrap(value)
	fileUpdatedDate = property(_get_fileUpdatedDate, _set_fileUpdatedDate)

	#complete
	def _get_complete(self):
		return wrap(self.__get_instance_IHTMLImgElement().complete)
	def _set_complete(self, value):
		self.__get_instance_IHTMLImgElement().complete = unwrap(value)
	complete = property(_get_complete, _set_complete)

	#fileSize
	def _get_fileSize(self):
		return wrap(self.__get_instance_IHTMLImgElement().fileSize)
	def _set_fileSize(self, value):
		self.__get_instance_IHTMLImgElement().fileSize = unwrap(value)
	fileSize = property(_get_fileSize, _set_fileSize)

	#src
	def _get_src(self):
		return wrap(self.__get_instance_IHTMLImgElement().src)
	def _set_src(self, value):
		self.__get_instance_IHTMLImgElement().src = unwrap(value)
	src = property(_get_src, _set_src)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLImgElement().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLImgElement().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLImgElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLImgElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#lowsrc
	def _get_lowsrc(self):
		return wrap(self.__get_instance_IHTMLImgElement().lowsrc)
	def _set_lowsrc(self, value):
		self.__get_instance_IHTMLImgElement().lowsrc = unwrap(value)
	lowsrc = property(_get_lowsrc, _set_lowsrc)

	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLImgElement().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLImgElement().align = unwrap(value)
	align = property(_get_align, _set_align)

	#isMap
	def _get_isMap(self):
		return wrap(self.__get_instance_IHTMLImgElement().isMap)
	def _set_isMap(self, value):
		self.__get_instance_IHTMLImgElement().isMap = unwrap(value)
	isMap = property(_get_isMap, _set_isMap)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance_IHTMLImgElement().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance_IHTMLImgElement().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#dynsrc
	def _get_dynsrc(self):
		return wrap(self.__get_instance_IHTMLImgElement().dynsrc)
	def _set_dynsrc(self, value):
		self.__get_instance_IHTMLImgElement().dynsrc = unwrap(value)
	dynsrc = property(_get_dynsrc, _set_dynsrc)

	#loop
	def _get_loop(self):
		return wrap(self.__get_instance_IHTMLImgElement().loop)
	def _set_loop(self, value):
		self.__get_instance_IHTMLImgElement().loop = unwrap(value)
	loop = property(_get_loop, _set_loop)

wrapperClasses['{3050F240-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLImgElement
backWrapperClasses[IHTMLImgElement] = '{3050F240-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLImageElementFactory
#
class IHTMLImageElementFactory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLImageElementFactory(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLImageElementFactory
		return Dispatch(self.__instance__.QueryInterface(kls))
	#create
	def create(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLImageElementFactory().create(*args))

wrapperClasses['{3050F38E-98B5-11CF-BB82-00AAA0BDCE0B}'] = IHTMLImageElementFactory
backWrapperClasses[IHTMLImageElementFactory] = '{3050F38E-98B5-11CF-BB82-00AAA0BDCE0B}'

##############################
# DispHTMLImg
#
class DispHTMLImg(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLImg(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLImg
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F51C-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLImg
backWrapperClasses[DispHTMLImg] = '{3050F51C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLUniqueName
#
class IHTMLUniqueName(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLUniqueName(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLUniqueName
		return Dispatch(self.__instance__.QueryInterface(kls))
	#uniqueID
	def _get_uniqueID(self):
		return wrap(self.__get_instance_IHTMLUniqueName().uniqueID)
	def _set_uniqueID(self, value):
		self.__get_instance_IHTMLUniqueName().uniqueID = unwrap(value)
	uniqueID = property(_get_uniqueID, _set_uniqueID)

	#uniqueNumber
	def _get_uniqueNumber(self):
		return wrap(self.__get_instance_IHTMLUniqueName().uniqueNumber)
	def _set_uniqueNumber(self, value):
		self.__get_instance_IHTMLUniqueName().uniqueNumber = unwrap(value)
	uniqueNumber = property(_get_uniqueNumber, _set_uniqueNumber)

wrapperClasses['{3050F4D0-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLUniqueName
backWrapperClasses[IHTMLUniqueName] = '{3050F4D0-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLControlElement
#
class IHTMLControlElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLControlElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLControlElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance_IHTMLControlElement().onblur)
	def _set_onblur(self, value):
		self.__get_instance_IHTMLControlElement().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#clientLeft
	def _get_clientLeft(self):
		return wrap(self.__get_instance_IHTMLControlElement().clientLeft)
	def _set_clientLeft(self, value):
		self.__get_instance_IHTMLControlElement().clientLeft = unwrap(value)
	clientLeft = property(_get_clientLeft, _set_clientLeft)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance_IHTMLControlElement().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance_IHTMLControlElement().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#clientHeight
	def _get_clientHeight(self):
		return wrap(self.__get_instance_IHTMLControlElement().clientHeight)
	def _set_clientHeight(self, value):
		self.__get_instance_IHTMLControlElement().clientHeight = unwrap(value)
	clientHeight = property(_get_clientHeight, _set_clientHeight)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance_IHTMLControlElement().onresize)
	def _set_onresize(self, value):
		self.__get_instance_IHTMLControlElement().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#clientWidth
	def _get_clientWidth(self):
		return wrap(self.__get_instance_IHTMLControlElement().clientWidth)
	def _set_clientWidth(self, value):
		self.__get_instance_IHTMLControlElement().clientWidth = unwrap(value)
	clientWidth = property(_get_clientWidth, _set_clientWidth)

	#clientTop
	def _get_clientTop(self):
		return wrap(self.__get_instance_IHTMLControlElement().clientTop)
	def _set_clientTop(self, value):
		self.__get_instance_IHTMLControlElement().clientTop = unwrap(value)
	clientTop = property(_get_clientTop, _set_clientTop)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance_IHTMLControlElement().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance_IHTMLControlElement().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance_IHTMLControlElement().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance_IHTMLControlElement().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#removeFilter
	def removeFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLControlElement().removeFilter(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLControlElement().focus(*args))

	#addFilter
	def addFilter(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLControlElement().addFilter(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLControlElement().blur(*args))

wrapperClasses['{3050F4E9-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLControlElement
backWrapperClasses[IHTMLControlElement] = '{3050F4E9-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLBodyElement
#
class IHTMLBodyElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLBodyElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBodyElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onload
	def _get_onload(self):
		return wrap(self.__get_instance_IHTMLBodyElement().onload)
	def _set_onload(self, value):
		self.__get_instance_IHTMLBodyElement().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#onunload
	def _get_onunload(self):
		return wrap(self.__get_instance_IHTMLBodyElement().onunload)
	def _set_onunload(self, value):
		self.__get_instance_IHTMLBodyElement().onunload = unwrap(value)
	onunload = property(_get_onunload, _set_onunload)

	#noWrap
	def _get_noWrap(self):
		return wrap(self.__get_instance_IHTMLBodyElement().noWrap)
	def _set_noWrap(self, value):
		self.__get_instance_IHTMLBodyElement().noWrap = unwrap(value)
	noWrap = property(_get_noWrap, _set_noWrap)

	#vLink
	def _get_vLink(self):
		return wrap(self.__get_instance_IHTMLBodyElement().vLink)
	def _set_vLink(self, value):
		self.__get_instance_IHTMLBodyElement().vLink = unwrap(value)
	vLink = property(_get_vLink, _set_vLink)

	#topMargin
	def _get_topMargin(self):
		return wrap(self.__get_instance_IHTMLBodyElement().topMargin)
	def _set_topMargin(self, value):
		self.__get_instance_IHTMLBodyElement().topMargin = unwrap(value)
	topMargin = property(_get_topMargin, _set_topMargin)

	#rightMargin
	def _get_rightMargin(self):
		return wrap(self.__get_instance_IHTMLBodyElement().rightMargin)
	def _set_rightMargin(self, value):
		self.__get_instance_IHTMLBodyElement().rightMargin = unwrap(value)
	rightMargin = property(_get_rightMargin, _set_rightMargin)

	#aLink
	def _get_aLink(self):
		return wrap(self.__get_instance_IHTMLBodyElement().aLink)
	def _set_aLink(self, value):
		self.__get_instance_IHTMLBodyElement().aLink = unwrap(value)
	aLink = property(_get_aLink, _set_aLink)

	#text
	def _get_text(self):
		return wrap(self.__get_instance_IHTMLBodyElement().text)
	def _set_text(self, value):
		self.__get_instance_IHTMLBodyElement().text = unwrap(value)
	text = property(_get_text, _set_text)

	#onbeforeunload
	def _get_onbeforeunload(self):
		return wrap(self.__get_instance_IHTMLBodyElement().onbeforeunload)
	def _set_onbeforeunload(self, value):
		self.__get_instance_IHTMLBodyElement().onbeforeunload = unwrap(value)
	onbeforeunload = property(_get_onbeforeunload, _set_onbeforeunload)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance_IHTMLBodyElement().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance_IHTMLBodyElement().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#bgProperties
	def _get_bgProperties(self):
		return wrap(self.__get_instance_IHTMLBodyElement().bgProperties)
	def _set_bgProperties(self, value):
		self.__get_instance_IHTMLBodyElement().bgProperties = unwrap(value)
	bgProperties = property(_get_bgProperties, _set_bgProperties)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance_IHTMLBodyElement().onselect)
	def _set_onselect(self, value):
		self.__get_instance_IHTMLBodyElement().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#link
	def _get_link(self):
		return wrap(self.__get_instance_IHTMLBodyElement().link)
	def _set_link(self, value):
		self.__get_instance_IHTMLBodyElement().link = unwrap(value)
	link = property(_get_link, _set_link)

	#background
	def _get_background(self):
		return wrap(self.__get_instance_IHTMLBodyElement().background)
	def _set_background(self, value):
		self.__get_instance_IHTMLBodyElement().background = unwrap(value)
	background = property(_get_background, _set_background)

	#bottomMargin
	def _get_bottomMargin(self):
		return wrap(self.__get_instance_IHTMLBodyElement().bottomMargin)
	def _set_bottomMargin(self, value):
		self.__get_instance_IHTMLBodyElement().bottomMargin = unwrap(value)
	bottomMargin = property(_get_bottomMargin, _set_bottomMargin)

	#scroll
	def _get_scroll(self):
		return wrap(self.__get_instance_IHTMLBodyElement().scroll)
	def _set_scroll(self, value):
		self.__get_instance_IHTMLBodyElement().scroll = unwrap(value)
	scroll = property(_get_scroll, _set_scroll)

	#leftMargin
	def _get_leftMargin(self):
		return wrap(self.__get_instance_IHTMLBodyElement().leftMargin)
	def _set_leftMargin(self, value):
		self.__get_instance_IHTMLBodyElement().leftMargin = unwrap(value)
	leftMargin = property(_get_leftMargin, _set_leftMargin)

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLBodyElement().createTextRange(*args))

wrapperClasses['{3050F1D8-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBodyElement
backWrapperClasses[IHTMLBodyElement] = '{3050F1D8-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLBodyElement2
#
class IHTMLBodyElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLBodyElement2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBodyElement2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onbeforeprint
	def _get_onbeforeprint(self):
		return wrap(self.__get_instance_IHTMLBodyElement2().onbeforeprint)
	def _set_onbeforeprint(self, value):
		self.__get_instance_IHTMLBodyElement2().onbeforeprint = unwrap(value)
	onbeforeprint = property(_get_onbeforeprint, _set_onbeforeprint)

	#onafterprint
	def _get_onafterprint(self):
		return wrap(self.__get_instance_IHTMLBodyElement2().onafterprint)
	def _set_onafterprint(self, value):
		self.__get_instance_IHTMLBodyElement2().onafterprint = unwrap(value)
	onafterprint = property(_get_onafterprint, _set_onafterprint)

wrapperClasses['{3050F5C5-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBodyElement2
backWrapperClasses[IHTMLBodyElement2] = '{3050F5C5-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLBody
#
class DispHTMLBody(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLBody(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLBody
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F507-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLBody
backWrapperClasses[DispHTMLBody] = '{3050F507-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLAnchorElement
#
class IHTMLAnchorElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLAnchorElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLAnchorElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance_IHTMLAnchorElement().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance_IHTMLAnchorElement().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#search
	def _get_search(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().search)
	def _set_search(self, value):
		self.__get_instance_IHTMLAnchorElement().search = unwrap(value)
	search = property(_get_search, _set_search)

	#accessKey
	def _get_accessKey(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().accessKey)
	def _set_accessKey(self, value):
		self.__get_instance_IHTMLAnchorElement().accessKey = unwrap(value)
	accessKey = property(_get_accessKey, _set_accessKey)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().protocol)
	def _set_protocol(self, value):
		self.__get_instance_IHTMLAnchorElement().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#target
	def _get_target(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().target)
	def _set_target(self, value):
		self.__get_instance_IHTMLAnchorElement().target = unwrap(value)
	target = property(_get_target, _set_target)

	#urn
	def _get_urn(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().urn)
	def _set_urn(self, value):
		self.__get_instance_IHTMLAnchorElement().urn = unwrap(value)
	urn = property(_get_urn, _set_urn)

	#hostname
	def _get_hostname(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().hostname)
	def _set_hostname(self, value):
		self.__get_instance_IHTMLAnchorElement().hostname = unwrap(value)
	hostname = property(_get_hostname, _set_hostname)

	#rev
	def _get_rev(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().rev)
	def _set_rev(self, value):
		self.__get_instance_IHTMLAnchorElement().rev = unwrap(value)
	rev = property(_get_rev, _set_rev)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().onblur)
	def _set_onblur(self, value):
		self.__get_instance_IHTMLAnchorElement().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLAnchorElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#host
	def _get_host(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().host)
	def _set_host(self, value):
		self.__get_instance_IHTMLAnchorElement().host = unwrap(value)
	host = property(_get_host, _set_host)

	#href
	def _get_href(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().href)
	def _set_href(self, value):
		self.__get_instance_IHTMLAnchorElement().href = unwrap(value)
	href = property(_get_href, _set_href)

	#pathname
	def _get_pathname(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().pathname)
	def _set_pathname(self, value):
		self.__get_instance_IHTMLAnchorElement().pathname = unwrap(value)
	pathname = property(_get_pathname, _set_pathname)

	#rel
	def _get_rel(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().rel)
	def _set_rel(self, value):
		self.__get_instance_IHTMLAnchorElement().rel = unwrap(value)
	rel = property(_get_rel, _set_rel)

	#protocolLong
	def _get_protocolLong(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().protocolLong)
	def _set_protocolLong(self, value):
		self.__get_instance_IHTMLAnchorElement().protocolLong = unwrap(value)
	protocolLong = property(_get_protocolLong, _set_protocolLong)

	#hash
	def _get_hash(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().hash)
	def _set_hash(self, value):
		self.__get_instance_IHTMLAnchorElement().hash = unwrap(value)
	hash = property(_get_hash, _set_hash)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance_IHTMLAnchorElement().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#tabIndex
	def _get_tabIndex(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().tabIndex)
	def _set_tabIndex(self, value):
		self.__get_instance_IHTMLAnchorElement().tabIndex = unwrap(value)
	tabIndex = property(_get_tabIndex, _set_tabIndex)

	#port
	def _get_port(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().port)
	def _set_port(self, value):
		self.__get_instance_IHTMLAnchorElement().port = unwrap(value)
	port = property(_get_port, _set_port)

	#Methods
	def _get_Methods(self):
		return wrap(self.__get_instance_IHTMLAnchorElement().Methods)
	def _set_Methods(self, value):
		self.__get_instance_IHTMLAnchorElement().Methods = unwrap(value)
	Methods = property(_get_Methods, _set_Methods)

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLAnchorElement().focus(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLAnchorElement().blur(*args))

wrapperClasses['{3050F1DA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLAnchorElement
backWrapperClasses[IHTMLAnchorElement] = '{3050F1DA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLElementCollection
#
class IHTMLElementCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLElementCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLElementCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLElementCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLElementCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLElementCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLElementCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElementCollection().item(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElementCollection().toString(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLElementCollection().tags(*args))

wrapperClasses['{3050F21F-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLElementCollection
backWrapperClasses[IHTMLElementCollection] = '{3050F21F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLElementCollection
#
class DispHTMLElementCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLElementCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLElementCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F56B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLElementCollection
backWrapperClasses[DispHTMLElementCollection] = '{3050F56B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLSelectElement
#
class IHTMLSelectElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLSelectElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLSelectElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#multiple
	def _get_multiple(self):
		return wrap(self.__get_instance_IHTMLSelectElement().multiple)
	def _set_multiple(self, value):
		self.__get_instance_IHTMLSelectElement().multiple = unwrap(value)
	multiple = property(_get_multiple, _set_multiple)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLSelectElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLSelectElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance_IHTMLSelectElement().form)
	def _set_form(self, value):
		self.__get_instance_IHTMLSelectElement().form = unwrap(value)
	form = property(_get_form, _set_form)

	#value
	def _get_value(self):
		return wrap(self.__get_instance_IHTMLSelectElement().value)
	def _set_value(self, value):
		self.__get_instance_IHTMLSelectElement().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLSelectElement().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLSelectElement().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLSelectElement().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLSelectElement().length = unwrap(value)
	length = property(_get_length, _set_length)

	#selectedIndex
	def _get_selectedIndex(self):
		return wrap(self.__get_instance_IHTMLSelectElement().selectedIndex)
	def _set_selectedIndex(self, value):
		self.__get_instance_IHTMLSelectElement().selectedIndex = unwrap(value)
	selectedIndex = property(_get_selectedIndex, _set_selectedIndex)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLSelectElement()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLSelectElement()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance_IHTMLSelectElement().onchange)
	def _set_onchange(self, value):
		self.__get_instance_IHTMLSelectElement().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLSelectElement().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLSelectElement().type = unwrap(value)
	type = property(_get_type, _set_type)

	#options
	def _get_options(self):
		return wrap(self.__get_instance_IHTMLSelectElement().options)
	def _set_options(self, value):
		self.__get_instance_IHTMLSelectElement().options = unwrap(value)
	options = property(_get_options, _set_options)

	#size
	def _get_size(self):
		return wrap(self.__get_instance_IHTMLSelectElement().size)
	def _set_size(self, value):
		self.__get_instance_IHTMLSelectElement().size = unwrap(value)
	size = property(_get_size, _set_size)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectElement().item(*args))

	#add
	def add(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectElement().add(*args))

	#remove
	def remove(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectElement().remove(*args))

	#tags
	def tags(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectElement().tags(*args))

wrapperClasses['{3050F244-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLSelectElement
backWrapperClasses[IHTMLSelectElement] = '{3050F244-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLSelectElement
#
class DispHTMLSelectElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLSelectElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLSelectElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F531-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLSelectElement
backWrapperClasses[DispHTMLSelectElement] = '{3050F531-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLSelectionObject
#
class IHTMLSelectionObject(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLSelectionObject(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLSelectionObject
		return Dispatch(self.__instance__.QueryInterface(kls))
	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLSelectionObject().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLSelectionObject().type = unwrap(value)
	type = property(_get_type, _set_type)

	#createRange
	def createRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectionObject().createRange(*args))

	#clear
	def clear(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectionObject().clear(*args))

	#empty
	def empty(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLSelectionObject().empty(*args))

wrapperClasses['{3050F25A-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLSelectionObject
backWrapperClasses[IHTMLSelectionObject] = '{3050F25A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOptionElement
#
class IHTMLOptionElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLOptionElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOptionElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#index
	def _get_index(self):
		return wrap(self.__get_instance_IHTMLOptionElement().index)
	def _set_index(self, value):
		self.__get_instance_IHTMLOptionElement().index = unwrap(value)
	index = property(_get_index, _set_index)

	#selected
	def _get_selected(self):
		return wrap(self.__get_instance_IHTMLOptionElement().selected)
	def _set_selected(self, value):
		self.__get_instance_IHTMLOptionElement().selected = unwrap(value)
	selected = property(_get_selected, _set_selected)

	#form
	def _get_form(self):
		return wrap(self.__get_instance_IHTMLOptionElement().form)
	def _set_form(self, value):
		self.__get_instance_IHTMLOptionElement().form = unwrap(value)
	form = property(_get_form, _set_form)

	#text
	def _get_text(self):
		return wrap(self.__get_instance_IHTMLOptionElement().text)
	def _set_text(self, value):
		self.__get_instance_IHTMLOptionElement().text = unwrap(value)
	text = property(_get_text, _set_text)

	#defaultSelected
	def _get_defaultSelected(self):
		return wrap(self.__get_instance_IHTMLOptionElement().defaultSelected)
	def _set_defaultSelected(self, value):
		self.__get_instance_IHTMLOptionElement().defaultSelected = unwrap(value)
	defaultSelected = property(_get_defaultSelected, _set_defaultSelected)

	#value
	def _get_value(self):
		return wrap(self.__get_instance_IHTMLOptionElement().value)
	def _set_value(self, value):
		self.__get_instance_IHTMLOptionElement().value = unwrap(value)
	value = property(_get_value, _set_value)

wrapperClasses['{3050F211-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOptionElement
backWrapperClasses[IHTMLOptionElement] = '{3050F211-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOptionElementFactory
#
class IHTMLOptionElementFactory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLOptionElementFactory(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOptionElementFactory
		return Dispatch(self.__instance__.QueryInterface(kls))
	#create
	def create(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOptionElementFactory().create(*args))

wrapperClasses['{3050F38C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOptionElementFactory
backWrapperClasses[IHTMLOptionElementFactory] = '{3050F38C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLOptionElement
#
class DispHTMLOptionElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLOptionElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLOptionElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F52B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLOptionElement
backWrapperClasses[DispHTMLOptionElement] = '{3050F52B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLInputElement
#
class IHTMLInputElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLInputElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLInputElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#defaultChecked
	def _get_defaultChecked(self):
		return wrap(self.__get_instance_IHTMLInputElement().defaultChecked)
	def _set_defaultChecked(self, value):
		self.__get_instance_IHTMLInputElement().defaultChecked = unwrap(value)
	defaultChecked = property(_get_defaultChecked, _set_defaultChecked)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance_IHTMLInputElement().onerror)
	def _set_onerror(self, value):
		self.__get_instance_IHTMLInputElement().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLInputElement().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLInputElement().height = unwrap(value)
	height = property(_get_height, _set_height)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLInputElement().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLInputElement().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#alt
	def _get_alt(self):
		return wrap(self.__get_instance_IHTMLInputElement().alt)
	def _set_alt(self, value):
		self.__get_instance_IHTMLInputElement().alt = unwrap(value)
	alt = property(_get_alt, _set_alt)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance_IHTMLInputElement().onchange)
	def _set_onchange(self, value):
		self.__get_instance_IHTMLInputElement().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLInputElement().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLInputElement().border = unwrap(value)
	border = property(_get_border, _set_border)

	#size
	def _get_size(self):
		return wrap(self.__get_instance_IHTMLInputElement().size)
	def _set_size(self, value):
		self.__get_instance_IHTMLInputElement().size = unwrap(value)
	size = property(_get_size, _set_size)

	#onabort
	def _get_onabort(self):
		return wrap(self.__get_instance_IHTMLInputElement().onabort)
	def _set_onabort(self, value):
		self.__get_instance_IHTMLInputElement().onabort = unwrap(value)
	onabort = property(_get_onabort, _set_onabort)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance_IHTMLInputElement().onload)
	def _set_onload(self, value):
		self.__get_instance_IHTMLInputElement().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#checked
	def _get_checked(self):
		return wrap(self.__get_instance_IHTMLInputElement().checked)
	def _set_checked(self, value):
		self.__get_instance_IHTMLInputElement().checked = unwrap(value)
	checked = property(_get_checked, _set_checked)

	#start
	def _get_start(self):
		return wrap(self.__get_instance_IHTMLInputElement().start)
	def _set_start(self, value):
		self.__get_instance_IHTMLInputElement().start = unwrap(value)
	start = property(_get_start, _set_start)

	#hspace
	def _get_hspace(self):
		return wrap(self.__get_instance_IHTMLInputElement().hspace)
	def _set_hspace(self, value):
		self.__get_instance_IHTMLInputElement().hspace = unwrap(value)
	hspace = property(_get_hspace, _set_hspace)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance_IHTMLInputElement().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance_IHTMLInputElement().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#indeterminate
	def _get_indeterminate(self):
		return wrap(self.__get_instance_IHTMLInputElement().indeterminate)
	def _set_indeterminate(self, value):
		self.__get_instance_IHTMLInputElement().indeterminate = unwrap(value)
	indeterminate = property(_get_indeterminate, _set_indeterminate)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLInputElement().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLInputElement().width = unwrap(value)
	width = property(_get_width, _set_width)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance_IHTMLInputElement().onselect)
	def _set_onselect(self, value):
		self.__get_instance_IHTMLInputElement().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLInputElement().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLInputElement().type = unwrap(value)
	type = property(_get_type, _set_type)

	#vrml
	def _get_vrml(self):
		return wrap(self.__get_instance_IHTMLInputElement().vrml)
	def _set_vrml(self, value):
		self.__get_instance_IHTMLInputElement().vrml = unwrap(value)
	vrml = property(_get_vrml, _set_vrml)

	#status
	def _get_status(self):
		return wrap(self.__get_instance_IHTMLInputElement().status)
	def _set_status(self, value):
		self.__get_instance_IHTMLInputElement().status = unwrap(value)
	status = property(_get_status, _set_status)

	#complete
	def _get_complete(self):
		return wrap(self.__get_instance_IHTMLInputElement().complete)
	def _set_complete(self, value):
		self.__get_instance_IHTMLInputElement().complete = unwrap(value)
	complete = property(_get_complete, _set_complete)

	#form
	def _get_form(self):
		return wrap(self.__get_instance_IHTMLInputElement().form)
	def _set_form(self, value):
		self.__get_instance_IHTMLInputElement().form = unwrap(value)
	form = property(_get_form, _set_form)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance_IHTMLInputElement().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance_IHTMLInputElement().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#maxLength
	def _get_maxLength(self):
		return wrap(self.__get_instance_IHTMLInputElement().maxLength)
	def _set_maxLength(self, value):
		self.__get_instance_IHTMLInputElement().maxLength = unwrap(value)
	maxLength = property(_get_maxLength, _set_maxLength)

	#src
	def _get_src(self):
		return wrap(self.__get_instance_IHTMLInputElement().src)
	def _set_src(self, value):
		self.__get_instance_IHTMLInputElement().src = unwrap(value)
	src = property(_get_src, _set_src)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLInputElement().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLInputElement().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLInputElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLInputElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#lowsrc
	def _get_lowsrc(self):
		return wrap(self.__get_instance_IHTMLInputElement().lowsrc)
	def _set_lowsrc(self, value):
		self.__get_instance_IHTMLInputElement().lowsrc = unwrap(value)
	lowsrc = property(_get_lowsrc, _set_lowsrc)

	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLInputElement().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLInputElement().align = unwrap(value)
	align = property(_get_align, _set_align)

	#value
	def _get_value(self):
		return wrap(self.__get_instance_IHTMLInputElement().value)
	def _set_value(self, value):
		self.__get_instance_IHTMLInputElement().value = unwrap(value)
	value = property(_get_value, _set_value)

	#vspace
	def _get_vspace(self):
		return wrap(self.__get_instance_IHTMLInputElement().vspace)
	def _set_vspace(self, value):
		self.__get_instance_IHTMLInputElement().vspace = unwrap(value)
	vspace = property(_get_vspace, _set_vspace)

	#dynsrc
	def _get_dynsrc(self):
		return wrap(self.__get_instance_IHTMLInputElement().dynsrc)
	def _set_dynsrc(self, value):
		self.__get_instance_IHTMLInputElement().dynsrc = unwrap(value)
	dynsrc = property(_get_dynsrc, _set_dynsrc)

	#loop
	def _get_loop(self):
		return wrap(self.__get_instance_IHTMLInputElement().loop)
	def _set_loop(self, value):
		self.__get_instance_IHTMLInputElement().loop = unwrap(value)
	loop = property(_get_loop, _set_loop)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLInputElement().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLInputElement().createTextRange(*args))

wrapperClasses['{3050F5D2-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLInputElement
backWrapperClasses[IHTMLInputElement] = '{3050F5D2-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLInputTextElement
#
class IHTMLInputTextElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLInputTextElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLInputTextElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#status
	def _get_status(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().status)
	def _set_status(self, value):
		self.__get_instance_IHTMLInputTextElement().status = unwrap(value)
	status = property(_get_status, _set_status)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLInputTextElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().form)
	def _set_form(self, value):
		self.__get_instance_IHTMLInputTextElement().form = unwrap(value)
	form = property(_get_form, _set_form)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance_IHTMLInputTextElement().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#value
	def _get_value(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().value)
	def _set_value(self, value):
		self.__get_instance_IHTMLInputTextElement().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLInputTextElement().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance_IHTMLInputTextElement().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().onselect)
	def _set_onselect(self, value):
		self.__get_instance_IHTMLInputTextElement().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#maxLength
	def _get_maxLength(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().maxLength)
	def _set_maxLength(self, value):
		self.__get_instance_IHTMLInputTextElement().maxLength = unwrap(value)
	maxLength = property(_get_maxLength, _set_maxLength)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().onchange)
	def _set_onchange(self, value):
		self.__get_instance_IHTMLInputTextElement().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLInputTextElement().type = unwrap(value)
	type = property(_get_type, _set_type)

	#size
	def _get_size(self):
		return wrap(self.__get_instance_IHTMLInputTextElement().size)
	def _set_size(self, value):
		self.__get_instance_IHTMLInputTextElement().size = unwrap(value)
	size = property(_get_size, _set_size)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLInputTextElement().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLInputTextElement().createTextRange(*args))

wrapperClasses['{3050F2A6-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLInputTextElement
backWrapperClasses[IHTMLInputTextElement] = '{3050F2A6-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLInputElement
#
class DispHTMLInputElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLInputElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLInputElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F57D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLInputElement
backWrapperClasses[DispHTMLInputElement] = '{3050F57D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTextAreaElement
#
class IHTMLTextAreaElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTextAreaElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTextAreaElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#status
	def _get_status(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().status)
	def _set_status(self, value):
		self.__get_instance_IHTMLTextAreaElement().status = unwrap(value)
	status = property(_get_status, _set_status)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().rows)
	def _set_rows(self, value):
		self.__get_instance_IHTMLTextAreaElement().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLTextAreaElement().name = unwrap(value)
	name = property(_get_name, _set_name)

	#form
	def _get_form(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().form)
	def _set_form(self, value):
		self.__get_instance_IHTMLTextAreaElement().form = unwrap(value)
	form = property(_get_form, _set_form)

	#defaultValue
	def _get_defaultValue(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().defaultValue)
	def _set_defaultValue(self, value):
		self.__get_instance_IHTMLTextAreaElement().defaultValue = unwrap(value)
	defaultValue = property(_get_defaultValue, _set_defaultValue)

	#cols
	def _get_cols(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().cols)
	def _set_cols(self, value):
		self.__get_instance_IHTMLTextAreaElement().cols = unwrap(value)
	cols = property(_get_cols, _set_cols)

	#value
	def _get_value(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().value)
	def _set_value(self, value):
		self.__get_instance_IHTMLTextAreaElement().value = unwrap(value)
	value = property(_get_value, _set_value)

	#disabled
	def _get_disabled(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().disabled)
	def _set_disabled(self, value):
		self.__get_instance_IHTMLTextAreaElement().disabled = unwrap(value)
	disabled = property(_get_disabled, _set_disabled)

	#readOnly
	def _get_readOnly(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().readOnly)
	def _set_readOnly(self, value):
		self.__get_instance_IHTMLTextAreaElement().readOnly = unwrap(value)
	readOnly = property(_get_readOnly, _set_readOnly)

	#onselect
	def _get_onselect(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().onselect)
	def _set_onselect(self, value):
		self.__get_instance_IHTMLTextAreaElement().onselect = unwrap(value)
	onselect = property(_get_onselect, _set_onselect)

	#wrap
	def _get_wrap(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().wrap)
	def _set_wrap(self, value):
		self.__get_instance_IHTMLTextAreaElement().wrap = unwrap(value)
	wrap = property(_get_wrap, _set_wrap)

	#onchange
	def _get_onchange(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().onchange)
	def _set_onchange(self, value):
		self.__get_instance_IHTMLTextAreaElement().onchange = unwrap(value)
	onchange = property(_get_onchange, _set_onchange)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLTextAreaElement().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLTextAreaElement().type = unwrap(value)
	type = property(_get_type, _set_type)

	#select
	def select(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTextAreaElement().select(*args))

	#createTextRange
	def createTextRange(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTextAreaElement().createTextRange(*args))

wrapperClasses['{3050F2AA-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTextAreaElement
backWrapperClasses[IHTMLTextAreaElement] = '{3050F2AA-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLUnknownElement
#
class DispHTMLUnknownElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLUnknownElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLUnknownElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F539-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLUnknownElement
backWrapperClasses[DispHTMLUnknownElement] = '{3050F539-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IOmHistory
#
class IOmHistory(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IOmHistory(self, kls=None):
		if kls is None:
			kls = MSHTML.IOmHistory
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IOmHistory().length)
	def _set_length(self, value):
		self.__get_instance_IOmHistory().length = unwrap(value)
	length = property(_get_length, _set_length)

	#forward
	def forward(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmHistory().forward(*args))

	#go
	def go(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmHistory().go(*args))

	#back
	def back(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmHistory().back(*args))

wrapperClasses['{FECEAAA2-8405-11CF-8BA1-00AA00476DA6}'] = IOmHistory
backWrapperClasses[IOmHistory] = '{FECEAAA2-8405-11CF-8BA1-00AA00476DA6}'

##############################
# IHTMLMimeTypesCollection
#
class IHTMLMimeTypesCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLMimeTypesCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLMimeTypesCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLMimeTypesCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLMimeTypesCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

wrapperClasses['{3050F3FC-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLMimeTypesCollection
backWrapperClasses[IHTMLMimeTypesCollection] = '{3050F3FC-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLPluginsCollection
#
class IHTMLPluginsCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLPluginsCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLPluginsCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLPluginsCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLPluginsCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#refresh
	def refresh(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLPluginsCollection().refresh(*args))

wrapperClasses['{3050F3FD-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLPluginsCollection
backWrapperClasses[IHTMLPluginsCollection] = '{3050F3FD-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLOpsProfile
#
class IHTMLOpsProfile(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLOpsProfile(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLOpsProfile
		return Dispatch(self.__instance__.QueryInterface(kls))
	#doRequest
	def doRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().doRequest(*args))

	#addReadRequest
	def addReadRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().addReadRequest(*args))

	#getAttribute
	def getAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().getAttribute(*args))

	#setAttribute
	def setAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().setAttribute(*args))

	#clearRequest
	def clearRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().clearRequest(*args))

	#doWriteRequest
	def doWriteRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().doWriteRequest(*args))

	#doReadRequest
	def doReadRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().doReadRequest(*args))

	#commitChanges
	def commitChanges(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().commitChanges(*args))

	#addRequest
	def addRequest(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLOpsProfile().addRequest(*args))

wrapperClasses['{3050F401-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLOpsProfile
backWrapperClasses[IHTMLOpsProfile] = '{3050F401-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IOmNavigator
#
class IOmNavigator(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IOmNavigator(self, kls=None):
		if kls is None:
			kls = MSHTML.IOmNavigator
		return Dispatch(self.__instance__.QueryInterface(kls))
	#mimeTypes
	def _get_mimeTypes(self):
		return wrap(self.__get_instance_IOmNavigator().mimeTypes)
	def _set_mimeTypes(self, value):
		self.__get_instance_IOmNavigator().mimeTypes = unwrap(value)
	mimeTypes = property(_get_mimeTypes, _set_mimeTypes)

	#userProfile
	def _get_userProfile(self):
		return wrap(self.__get_instance_IOmNavigator().userProfile)
	def _set_userProfile(self, value):
		self.__get_instance_IOmNavigator().userProfile = unwrap(value)
	userProfile = property(_get_userProfile, _set_userProfile)

	#appName
	def _get_appName(self):
		return wrap(self.__get_instance_IOmNavigator().appName)
	def _set_appName(self, value):
		self.__get_instance_IOmNavigator().appName = unwrap(value)
	appName = property(_get_appName, _set_appName)

	#appCodeName
	def _get_appCodeName(self):
		return wrap(self.__get_instance_IOmNavigator().appCodeName)
	def _set_appCodeName(self, value):
		self.__get_instance_IOmNavigator().appCodeName = unwrap(value)
	appCodeName = property(_get_appCodeName, _set_appCodeName)

	#opsProfile
	def _get_opsProfile(self):
		return wrap(self.__get_instance_IOmNavigator().opsProfile)
	def _set_opsProfile(self, value):
		self.__get_instance_IOmNavigator().opsProfile = unwrap(value)
	opsProfile = property(_get_opsProfile, _set_opsProfile)

	#onLine
	def _get_onLine(self):
		return wrap(self.__get_instance_IOmNavigator().onLine)
	def _set_onLine(self, value):
		self.__get_instance_IOmNavigator().onLine = unwrap(value)
	onLine = property(_get_onLine, _set_onLine)

	#cookieEnabled
	def _get_cookieEnabled(self):
		return wrap(self.__get_instance_IOmNavigator().cookieEnabled)
	def _set_cookieEnabled(self, value):
		self.__get_instance_IOmNavigator().cookieEnabled = unwrap(value)
	cookieEnabled = property(_get_cookieEnabled, _set_cookieEnabled)

	#appVersion
	def _get_appVersion(self):
		return wrap(self.__get_instance_IOmNavigator().appVersion)
	def _set_appVersion(self, value):
		self.__get_instance_IOmNavigator().appVersion = unwrap(value)
	appVersion = property(_get_appVersion, _set_appVersion)

	#connectionSpeed
	def _get_connectionSpeed(self):
		return wrap(self.__get_instance_IOmNavigator().connectionSpeed)
	def _set_connectionSpeed(self, value):
		self.__get_instance_IOmNavigator().connectionSpeed = unwrap(value)
	connectionSpeed = property(_get_connectionSpeed, _set_connectionSpeed)

	#appMinorVersion
	def _get_appMinorVersion(self):
		return wrap(self.__get_instance_IOmNavigator().appMinorVersion)
	def _set_appMinorVersion(self, value):
		self.__get_instance_IOmNavigator().appMinorVersion = unwrap(value)
	appMinorVersion = property(_get_appMinorVersion, _set_appMinorVersion)

	#platform
	def _get_platform(self):
		return wrap(self.__get_instance_IOmNavigator().platform)
	def _set_platform(self, value):
		self.__get_instance_IOmNavigator().platform = unwrap(value)
	platform = property(_get_platform, _set_platform)

	#systemLanguage
	def _get_systemLanguage(self):
		return wrap(self.__get_instance_IOmNavigator().systemLanguage)
	def _set_systemLanguage(self, value):
		self.__get_instance_IOmNavigator().systemLanguage = unwrap(value)
	systemLanguage = property(_get_systemLanguage, _set_systemLanguage)

	#cpuClass
	def _get_cpuClass(self):
		return wrap(self.__get_instance_IOmNavigator().cpuClass)
	def _set_cpuClass(self, value):
		self.__get_instance_IOmNavigator().cpuClass = unwrap(value)
	cpuClass = property(_get_cpuClass, _set_cpuClass)

	#plugins
	def _get_plugins(self):
		return wrap(self.__get_instance_IOmNavigator().plugins)
	def _set_plugins(self, value):
		self.__get_instance_IOmNavigator().plugins = unwrap(value)
	plugins = property(_get_plugins, _set_plugins)

	#userAgent
	def _get_userAgent(self):
		return wrap(self.__get_instance_IOmNavigator().userAgent)
	def _set_userAgent(self, value):
		self.__get_instance_IOmNavigator().userAgent = unwrap(value)
	userAgent = property(_get_userAgent, _set_userAgent)

	#userLanguage
	def _get_userLanguage(self):
		return wrap(self.__get_instance_IOmNavigator().userLanguage)
	def _set_userLanguage(self, value):
		self.__get_instance_IOmNavigator().userLanguage = unwrap(value)
	userLanguage = property(_get_userLanguage, _set_userLanguage)

	#browserLanguage
	def _get_browserLanguage(self):
		return wrap(self.__get_instance_IOmNavigator().browserLanguage)
	def _set_browserLanguage(self, value):
		self.__get_instance_IOmNavigator().browserLanguage = unwrap(value)
	browserLanguage = property(_get_browserLanguage, _set_browserLanguage)

	#javaEnabled
	def javaEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmNavigator().javaEnabled(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmNavigator().toString(*args))

	#taintEnabled
	def taintEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IOmNavigator().taintEnabled(*args))

wrapperClasses['{FECEAAA5-8405-11CF-8BA1-00AA00476DA6}'] = IOmNavigator
backWrapperClasses[IOmNavigator] = '{FECEAAA5-8405-11CF-8BA1-00AA00476DA6}'

##############################
# IHTMLLocation
#
class IHTMLLocation(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLLocation(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLLocation
		return Dispatch(self.__instance__.QueryInterface(kls))
	#search
	def _get_search(self):
		return wrap(self.__get_instance_IHTMLLocation().search)
	def _set_search(self, value):
		self.__get_instance_IHTMLLocation().search = unwrap(value)
	search = property(_get_search, _set_search)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance_IHTMLLocation().protocol)
	def _set_protocol(self, value):
		self.__get_instance_IHTMLLocation().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#hostname
	def _get_hostname(self):
		return wrap(self.__get_instance_IHTMLLocation().hostname)
	def _set_hostname(self, value):
		self.__get_instance_IHTMLLocation().hostname = unwrap(value)
	hostname = property(_get_hostname, _set_hostname)

	#host
	def _get_host(self):
		return wrap(self.__get_instance_IHTMLLocation().host)
	def _set_host(self, value):
		self.__get_instance_IHTMLLocation().host = unwrap(value)
	host = property(_get_host, _set_host)

	#href
	def _get_href(self):
		return wrap(self.__get_instance_IHTMLLocation().href)
	def _set_href(self, value):
		self.__get_instance_IHTMLLocation().href = unwrap(value)
	href = property(_get_href, _set_href)

	#pathname
	def _get_pathname(self):
		return wrap(self.__get_instance_IHTMLLocation().pathname)
	def _set_pathname(self, value):
		self.__get_instance_IHTMLLocation().pathname = unwrap(value)
	pathname = property(_get_pathname, _set_pathname)

	#hash
	def _get_hash(self):
		return wrap(self.__get_instance_IHTMLLocation().hash)
	def _set_hash(self, value):
		self.__get_instance_IHTMLLocation().hash = unwrap(value)
	hash = property(_get_hash, _set_hash)

	#port
	def _get_port(self):
		return wrap(self.__get_instance_IHTMLLocation().port)
	def _set_port(self, value):
		self.__get_instance_IHTMLLocation().port = unwrap(value)
	port = property(_get_port, _set_port)

	#reload
	def reload(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLLocation().reload(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLLocation().toString(*args))

	#assign
	def assign(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLLocation().assign(*args))

	#replace
	def replace(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLLocation().replace(*args))

wrapperClasses['{163BB1E0-6E00-11CF-837A-48DC04C10000}'] = IHTMLLocation
backWrapperClasses[IHTMLLocation] = '{163BB1E0-6E00-11CF-837A-48DC04C10000}'

##############################
# IHTMLBookmarkCollection
#
class IHTMLBookmarkCollection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLBookmarkCollection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLBookmarkCollection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLBookmarkCollection().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLBookmarkCollection().length = unwrap(value)
	length = property(_get_length, _set_length)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLBookmarkCollection()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLBookmarkCollection()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLBookmarkCollection().item(*args))

wrapperClasses['{3050F4CE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLBookmarkCollection
backWrapperClasses[IHTMLBookmarkCollection] = '{3050F4CE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDataTransfer
#
class IHTMLDataTransfer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDataTransfer(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDataTransfer
		return Dispatch(self.__instance__.QueryInterface(kls))
	#effectAllowed
	def _get_effectAllowed(self):
		return wrap(self.__get_instance_IHTMLDataTransfer().effectAllowed)
	def _set_effectAllowed(self, value):
		self.__get_instance_IHTMLDataTransfer().effectAllowed = unwrap(value)
	effectAllowed = property(_get_effectAllowed, _set_effectAllowed)

	#dropEffect
	def _get_dropEffect(self):
		return wrap(self.__get_instance_IHTMLDataTransfer().dropEffect)
	def _set_dropEffect(self, value):
		self.__get_instance_IHTMLDataTransfer().dropEffect = unwrap(value)
	dropEffect = property(_get_dropEffect, _set_dropEffect)

	#getData
	def getData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDataTransfer().getData(*args))

	#clearData
	def clearData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDataTransfer().clearData(*args))

	#setData
	def setData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDataTransfer().setData(*args))

wrapperClasses['{3050F4B3-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDataTransfer
backWrapperClasses[IHTMLDataTransfer] = '{3050F4B3-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEventObj
#
class IHTMLEventObj(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLEventObj(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEventObj
		return Dispatch(self.__instance__.QueryInterface(kls))
	#returnValue
	def _get_returnValue(self):
		return wrap(self.__get_instance_IHTMLEventObj().returnValue)
	def _set_returnValue(self, value):
		self.__get_instance_IHTMLEventObj().returnValue = unwrap(value)
	returnValue = property(_get_returnValue, _set_returnValue)

	#ctrlKey
	def _get_ctrlKey(self):
		return wrap(self.__get_instance_IHTMLEventObj().ctrlKey)
	def _set_ctrlKey(self, value):
		self.__get_instance_IHTMLEventObj().ctrlKey = unwrap(value)
	ctrlKey = property(_get_ctrlKey, _set_ctrlKey)

	#fromElement
	def _get_fromElement(self):
		return wrap(self.__get_instance_IHTMLEventObj().fromElement)
	def _set_fromElement(self, value):
		self.__get_instance_IHTMLEventObj().fromElement = unwrap(value)
	fromElement = property(_get_fromElement, _set_fromElement)

	#screenY
	def _get_screenY(self):
		return wrap(self.__get_instance_IHTMLEventObj().screenY)
	def _set_screenY(self, value):
		self.__get_instance_IHTMLEventObj().screenY = unwrap(value)
	screenY = property(_get_screenY, _set_screenY)

	#screenX
	def _get_screenX(self):
		return wrap(self.__get_instance_IHTMLEventObj().screenX)
	def _set_screenX(self, value):
		self.__get_instance_IHTMLEventObj().screenX = unwrap(value)
	screenX = property(_get_screenX, _set_screenX)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLEventObj().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLEventObj().type = unwrap(value)
	type = property(_get_type, _set_type)

	#clientX
	def _get_clientX(self):
		return wrap(self.__get_instance_IHTMLEventObj().clientX)
	def _set_clientX(self, value):
		self.__get_instance_IHTMLEventObj().clientX = unwrap(value)
	clientX = property(_get_clientX, _set_clientX)

	#clientY
	def _get_clientY(self):
		return wrap(self.__get_instance_IHTMLEventObj().clientY)
	def _set_clientY(self, value):
		self.__get_instance_IHTMLEventObj().clientY = unwrap(value)
	clientY = property(_get_clientY, _set_clientY)

	#qualifier
	def _get_qualifier(self):
		return wrap(self.__get_instance_IHTMLEventObj().qualifier)
	def _set_qualifier(self, value):
		self.__get_instance_IHTMLEventObj().qualifier = unwrap(value)
	qualifier = property(_get_qualifier, _set_qualifier)

	#altKey
	def _get_altKey(self):
		return wrap(self.__get_instance_IHTMLEventObj().altKey)
	def _set_altKey(self, value):
		self.__get_instance_IHTMLEventObj().altKey = unwrap(value)
	altKey = property(_get_altKey, _set_altKey)

	#reason
	def _get_reason(self):
		return wrap(self.__get_instance_IHTMLEventObj().reason)
	def _set_reason(self, value):
		self.__get_instance_IHTMLEventObj().reason = unwrap(value)
	reason = property(_get_reason, _set_reason)

	#x
	def _get_x(self):
		return wrap(self.__get_instance_IHTMLEventObj().x)
	def _set_x(self, value):
		self.__get_instance_IHTMLEventObj().x = unwrap(value)
	x = property(_get_x, _set_x)

	#cancelBubble
	def _get_cancelBubble(self):
		return wrap(self.__get_instance_IHTMLEventObj().cancelBubble)
	def _set_cancelBubble(self, value):
		self.__get_instance_IHTMLEventObj().cancelBubble = unwrap(value)
	cancelBubble = property(_get_cancelBubble, _set_cancelBubble)

	#toElement
	def _get_toElement(self):
		return wrap(self.__get_instance_IHTMLEventObj().toElement)
	def _set_toElement(self, value):
		self.__get_instance_IHTMLEventObj().toElement = unwrap(value)
	toElement = property(_get_toElement, _set_toElement)

	#srcElement
	def _get_srcElement(self):
		return wrap(self.__get_instance_IHTMLEventObj().srcElement)
	def _set_srcElement(self, value):
		self.__get_instance_IHTMLEventObj().srcElement = unwrap(value)
	srcElement = property(_get_srcElement, _set_srcElement)

	#shiftKey
	def _get_shiftKey(self):
		return wrap(self.__get_instance_IHTMLEventObj().shiftKey)
	def _set_shiftKey(self, value):
		self.__get_instance_IHTMLEventObj().shiftKey = unwrap(value)
	shiftKey = property(_get_shiftKey, _set_shiftKey)

	#button
	def _get_button(self):
		return wrap(self.__get_instance_IHTMLEventObj().button)
	def _set_button(self, value):
		self.__get_instance_IHTMLEventObj().button = unwrap(value)
	button = property(_get_button, _set_button)

	#offsetX
	def _get_offsetX(self):
		return wrap(self.__get_instance_IHTMLEventObj().offsetX)
	def _set_offsetX(self, value):
		self.__get_instance_IHTMLEventObj().offsetX = unwrap(value)
	offsetX = property(_get_offsetX, _set_offsetX)

	#offsetY
	def _get_offsetY(self):
		return wrap(self.__get_instance_IHTMLEventObj().offsetY)
	def _set_offsetY(self, value):
		self.__get_instance_IHTMLEventObj().offsetY = unwrap(value)
	offsetY = property(_get_offsetY, _set_offsetY)

	#y
	def _get_y(self):
		return wrap(self.__get_instance_IHTMLEventObj().y)
	def _set_y(self, value):
		self.__get_instance_IHTMLEventObj().y = unwrap(value)
	y = property(_get_y, _set_y)

	#srcFilter
	def _get_srcFilter(self):
		return wrap(self.__get_instance_IHTMLEventObj().srcFilter)
	def _set_srcFilter(self, value):
		self.__get_instance_IHTMLEventObj().srcFilter = unwrap(value)
	srcFilter = property(_get_srcFilter, _set_srcFilter)

	#keyCode
	def _get_keyCode(self):
		return wrap(self.__get_instance_IHTMLEventObj().keyCode)
	def _set_keyCode(self, value):
		self.__get_instance_IHTMLEventObj().keyCode = unwrap(value)
	keyCode = property(_get_keyCode, _set_keyCode)

wrapperClasses['{3050F32D-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLEventObj
backWrapperClasses[IHTMLEventObj] = '{3050F32D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispCEventObj
#
class DispCEventObj(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispCEventObj(self, kls=None):
		if kls is None:
			kls = MSHTML.DispCEventObj
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F558-98B5-11CF-BB82-00AA00BDCE0B}'] = DispCEventObj
backWrapperClasses[DispCEventObj] = '{3050F558-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFramesCollection2
#
class IHTMLFramesCollection2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLFramesCollection2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFramesCollection2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLFramesCollection2().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLFramesCollection2().length = unwrap(value)
	length = property(_get_length, _set_length)

	#item
	def item(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLFramesCollection2().item(*args))

wrapperClasses['{332C4426-26CB-11D0-B483-00C04FD90119}'] = IHTMLFramesCollection2
backWrapperClasses[IHTMLFramesCollection2] = '{332C4426-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLScreen
#
class IHTMLScreen(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLScreen(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScreen
		return Dispatch(self.__instance__.QueryInterface(kls))
	#availWidth
	def _get_availWidth(self):
		return wrap(self.__get_instance_IHTMLScreen().availWidth)
	def _set_availWidth(self, value):
		self.__get_instance_IHTMLScreen().availWidth = unwrap(value)
	availWidth = property(_get_availWidth, _set_availWidth)

	#bufferDepth
	def _get_bufferDepth(self):
		return wrap(self.__get_instance_IHTMLScreen().bufferDepth)
	def _set_bufferDepth(self, value):
		self.__get_instance_IHTMLScreen().bufferDepth = unwrap(value)
	bufferDepth = property(_get_bufferDepth, _set_bufferDepth)

	#availHeight
	def _get_availHeight(self):
		return wrap(self.__get_instance_IHTMLScreen().availHeight)
	def _set_availHeight(self, value):
		self.__get_instance_IHTMLScreen().availHeight = unwrap(value)
	availHeight = property(_get_availHeight, _set_availHeight)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLScreen().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLScreen().height = unwrap(value)
	height = property(_get_height, _set_height)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLScreen().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLScreen().width = unwrap(value)
	width = property(_get_width, _set_width)

	#fontSmoothingEnabled
	def _get_fontSmoothingEnabled(self):
		return wrap(self.__get_instance_IHTMLScreen().fontSmoothingEnabled)
	def _set_fontSmoothingEnabled(self, value):
		self.__get_instance_IHTMLScreen().fontSmoothingEnabled = unwrap(value)
	fontSmoothingEnabled = property(_get_fontSmoothingEnabled, _set_fontSmoothingEnabled)

	#colorDepth
	def _get_colorDepth(self):
		return wrap(self.__get_instance_IHTMLScreen().colorDepth)
	def _set_colorDepth(self, value):
		self.__get_instance_IHTMLScreen().colorDepth = unwrap(value)
	colorDepth = property(_get_colorDepth, _set_colorDepth)

	#updateInterval
	def _get_updateInterval(self):
		return wrap(self.__get_instance_IHTMLScreen().updateInterval)
	def _set_updateInterval(self, value):
		self.__get_instance_IHTMLScreen().updateInterval = unwrap(value)
	updateInterval = property(_get_updateInterval, _set_updateInterval)

wrapperClasses['{3050F35C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScreen
backWrapperClasses[IHTMLScreen] = '{3050F35C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLWindow2
#
class IHTMLWindow2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLWindow2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLWindow2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#defaultStatus
	def _get_defaultStatus(self):
		return wrap(self.__get_instance_IHTMLWindow2().defaultStatus)
	def _set_defaultStatus(self, value):
		self.__get_instance_IHTMLWindow2().defaultStatus = unwrap(value)
	defaultStatus = property(_get_defaultStatus, _set_defaultStatus)

	#clientInformation
	def _get_clientInformation(self):
		return wrap(self.__get_instance_IHTMLWindow2().clientInformation)
	def _set_clientInformation(self, value):
		self.__get_instance_IHTMLWindow2().clientInformation = unwrap(value)
	clientInformation = property(_get_clientInformation, _set_clientInformation)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance_IHTMLWindow2().onerror)
	def _set_onerror(self, value):
		self.__get_instance_IHTMLWindow2().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#onscroll
	def _get_onscroll(self):
		return wrap(self.__get_instance_IHTMLWindow2().onscroll)
	def _set_onscroll(self, value):
		self.__get_instance_IHTMLWindow2().onscroll = unwrap(value)
	onscroll = property(_get_onscroll, _set_onscroll)

	#frames
	def _get_frames(self):
		return wrap(self.__get_instance_IHTMLWindow2().frames)
	def _set_frames(self, value):
		self.__get_instance_IHTMLWindow2().frames = unwrap(value)
	frames = property(_get_frames, _set_frames)

	#navigator
	def _get_navigator(self):
		return wrap(self.__get_instance_IHTMLWindow2().navigator)
	def _set_navigator(self, value):
		self.__get_instance_IHTMLWindow2().navigator = unwrap(value)
	navigator = property(_get_navigator, _set_navigator)

	#event
	def _get_event(self):
		return wrap(self.__get_instance_IHTMLWindow2().event)
	def _set_event(self, value):
		self.__get_instance_IHTMLWindow2().event = unwrap(value)
	event = property(_get_event, _set_event)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance_IHTMLWindow2().onload)
	def _set_onload(self, value):
		self.__get_instance_IHTMLWindow2().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#Option
	def _get_Option(self):
		return wrap(self.__get_instance_IHTMLWindow2().Option)
	def _set_Option(self, value):
		self.__get_instance_IHTMLWindow2().Option = unwrap(value)
	Option = property(_get_Option, _set_Option)

	#top
	def _get_top(self):
		return wrap(self.__get_instance_IHTMLWindow2().top)
	def _set_top(self, value):
		self.__get_instance_IHTMLWindow2().top = unwrap(value)
	top = property(_get_top, _set_top)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance_IHTMLWindow2().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance_IHTMLWindow2().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#onresize
	def _get_onresize(self):
		return wrap(self.__get_instance_IHTMLWindow2().onresize)
	def _set_onresize(self, value):
		self.__get_instance_IHTMLWindow2().onresize = unwrap(value)
	onresize = property(_get_onresize, _set_onresize)

	#window
	def _get_window(self):
		return wrap(self.__get_instance_IHTMLWindow2().window)
	def _set_window(self, value):
		self.__get_instance_IHTMLWindow2().window = unwrap(value)
	window = property(_get_window, _set_window)

	#opener
	def _get_opener(self):
		return wrap(self.__get_instance_IHTMLWindow2().opener)
	def _set_opener(self, value):
		self.__get_instance_IHTMLWindow2().opener = unwrap(value)
	opener = property(_get_opener, _set_opener)

	#location
	def _get_location(self):
		return wrap(self.__get_instance_IHTMLWindow2().location)
	def _set_location(self, value):
		self.__get_instance_IHTMLWindow2().location = unwrap(value)
	location = property(_get_location, _set_location)

	#closed
	def _get_closed(self):
		return wrap(self.__get_instance_IHTMLWindow2().closed)
	def _set_closed(self, value):
		self.__get_instance_IHTMLWindow2().closed = unwrap(value)
	closed = property(_get_closed, _set_closed)

	#onfocus
	def _get_onfocus(self):
		return wrap(self.__get_instance_IHTMLWindow2().onfocus)
	def _set_onfocus(self, value):
		self.__get_instance_IHTMLWindow2().onfocus = unwrap(value)
	onfocus = property(_get_onfocus, _set_onfocus)

	#document
	def _get_document(self):
		return wrap(self.__get_instance_IHTMLWindow2().document)
	def _set_document(self, value):
		self.__get_instance_IHTMLWindow2().document = unwrap(value)
	document = property(_get_document, _set_document)

	#status
	def _get_status(self):
		return wrap(self.__get_instance_IHTMLWindow2().status)
	def _set_status(self, value):
		self.__get_instance_IHTMLWindow2().status = unwrap(value)
	status = property(_get_status, _set_status)

	#onblur
	def _get_onblur(self):
		return wrap(self.__get_instance_IHTMLWindow2().onblur)
	def _set_onblur(self, value):
		self.__get_instance_IHTMLWindow2().onblur = unwrap(value)
	onblur = property(_get_onblur, _set_onblur)

	#parent
	def _get_parent(self):
		return wrap(self.__get_instance_IHTMLWindow2().parent)
	def _set_parent(self, value):
		self.__get_instance_IHTMLWindow2().parent = unwrap(value)
	parent = property(_get_parent, _set_parent)

	#screen
	def _get_screen(self):
		return wrap(self.__get_instance_IHTMLWindow2().screen)
	def _set_screen(self, value):
		self.__get_instance_IHTMLWindow2().screen = unwrap(value)
	screen = property(_get_screen, _set_screen)

	#external
	def _get_external(self):
		return wrap(self.__get_instance_IHTMLWindow2().external)
	def _set_external(self, value):
		self.__get_instance_IHTMLWindow2().external = unwrap(value)
	external = property(_get_external, _set_external)

	#offscreenBuffering
	def _get_offscreenBuffering(self):
		return wrap(self.__get_instance_IHTMLWindow2().offscreenBuffering)
	def _set_offscreenBuffering(self, value):
		self.__get_instance_IHTMLWindow2().offscreenBuffering = unwrap(value)
	offscreenBuffering = property(_get_offscreenBuffering, _set_offscreenBuffering)

	#onunload
	def _get_onunload(self):
		return wrap(self.__get_instance_IHTMLWindow2().onunload)
	def _set_onunload(self, value):
		self.__get_instance_IHTMLWindow2().onunload = unwrap(value)
	onunload = property(_get_onunload, _set_onunload)

	#_newEnum
	def _get__newEnum(self):
		return wrap(self.__get_instance_IHTMLWindow2()._newEnum)
	def _set__newEnum(self, value):
		self.__get_instance_IHTMLWindow2()._newEnum = unwrap(value)
	_newEnum = property(_get__newEnum, _set__newEnum)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLWindow2().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLWindow2().name = unwrap(value)
	name = property(_get_name, _set_name)

	#Image
	def _get_Image(self):
		return wrap(self.__get_instance_IHTMLWindow2().Image)
	def _set_Image(self, value):
		self.__get_instance_IHTMLWindow2().Image = unwrap(value)
	Image = property(_get_Image, _set_Image)

	#onbeforeunload
	def _get_onbeforeunload(self):
		return wrap(self.__get_instance_IHTMLWindow2().onbeforeunload)
	def _set_onbeforeunload(self, value):
		self.__get_instance_IHTMLWindow2().onbeforeunload = unwrap(value)
	onbeforeunload = property(_get_onbeforeunload, _set_onbeforeunload)

	#self
	def _get_self(self):
		return wrap(self.__get_instance_IHTMLWindow2().self)
	def _set_self(self, value):
		self.__get_instance_IHTMLWindow2().self = unwrap(value)
	self = property(_get_self, _set_self)

	#history
	def _get_history(self):
		return wrap(self.__get_instance_IHTMLWindow2().history)
	def _set_history(self, value):
		self.__get_instance_IHTMLWindow2().history = unwrap(value)
	history = property(_get_history, _set_history)

	#moveTo
	def moveTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().moveTo(*args))

	#prompt
	def prompt(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().prompt(*args))

	#scrollTo
	def scrollTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().scrollTo(*args))

	#navigate
	def navigate(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().navigate(*args))

	#clearInterval
	def clearInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().clearInterval(*args))

	#close
	def close(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().close(*args))

	#open
	def open(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().open(*args))

	#showHelp
	def showHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().showHelp(*args))

	#setTimeout
	def setTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().setTimeout(*args))

	#confirm
	def confirm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().confirm(*args))

	#clearTimeout
	def clearTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().clearTimeout(*args))

	#resizeBy
	def resizeBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().resizeBy(*args))

	#execScript
	def execScript(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().execScript(*args))

	#moveBy
	def moveBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().moveBy(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().toString(*args))

	#blur
	def blur(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().blur(*args))

	#setInterval
	def setInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().setInterval(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().focus(*args))

	#alert
	def alert(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().alert(*args))

	#showModalDialog
	def showModalDialog(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().showModalDialog(*args))

	#scrollBy
	def scrollBy(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().scrollBy(*args))

	#resizeTo
	def resizeTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().resizeTo(*args))

	#scroll
	def scroll(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow2().scroll(*args))

wrapperClasses['{332C4427-26CB-11D0-B483-00C04FD90119}'] = IHTMLWindow2
backWrapperClasses[IHTMLWindow2] = '{332C4427-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLWindow3
#
class IHTMLWindow3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLWindow3(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLWindow3
		return Dispatch(self.__instance__.QueryInterface(kls))
	#onafterprint
	def _get_onafterprint(self):
		return wrap(self.__get_instance_IHTMLWindow3().onafterprint)
	def _set_onafterprint(self, value):
		self.__get_instance_IHTMLWindow3().onafterprint = unwrap(value)
	onafterprint = property(_get_onafterprint, _set_onafterprint)

	#onbeforeprint
	def _get_onbeforeprint(self):
		return wrap(self.__get_instance_IHTMLWindow3().onbeforeprint)
	def _set_onbeforeprint(self, value):
		self.__get_instance_IHTMLWindow3().onbeforeprint = unwrap(value)
	onbeforeprint = property(_get_onbeforeprint, _set_onbeforeprint)

	#screenTop
	def _get_screenTop(self):
		return wrap(self.__get_instance_IHTMLWindow3().screenTop)
	def _set_screenTop(self, value):
		self.__get_instance_IHTMLWindow3().screenTop = unwrap(value)
	screenTop = property(_get_screenTop, _set_screenTop)

	#screenLeft
	def _get_screenLeft(self):
		return wrap(self.__get_instance_IHTMLWindow3().screenLeft)
	def _set_screenLeft(self, value):
		self.__get_instance_IHTMLWindow3().screenLeft = unwrap(value)
	screenLeft = property(_get_screenLeft, _set_screenLeft)

	#clipboardData
	def _get_clipboardData(self):
		return wrap(self.__get_instance_IHTMLWindow3().clipboardData)
	def _set_clipboardData(self, value):
		self.__get_instance_IHTMLWindow3().clipboardData = unwrap(value)
	clipboardData = property(_get_clipboardData, _set_clipboardData)

	#setInterval
	def setInterval(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow3().setInterval(*args))

	#showModelessDialog
	def showModelessDialog(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow3().showModelessDialog(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow3().attachEvent(*args))

	#print_
	def print_(self, *args):
		args = map(unwrap, args)
		fn = getattr('IHTMLWindow3', self.__get_instance_print())
		return wrap(fn(*args))

	#setTimeout
	def setTimeout(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow3().setTimeout(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLWindow3().detachEvent(*args))

wrapperClasses['{3050F4AE-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLWindow3
backWrapperClasses[IHTMLWindow3] = '{3050F4AE-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLWindow2
#
class DispHTMLWindow2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLWindow2(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLWindow2
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F55D-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLWindow2
backWrapperClasses[DispHTMLWindow2] = '{3050F55D-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLDocumentEvents2
#
class HTMLDocumentEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLDocumentEvents2(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLDocumentEvents2
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F613-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDocumentEvents2
backWrapperClasses[HTMLDocumentEvents2] = '{3050F613-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLDocumentEvents
#
class HTMLDocumentEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLDocumentEvents(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLDocumentEvents
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F260-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLDocumentEvents
backWrapperClasses[HTMLDocumentEvents] = '{3050F260-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLTextContainerEvents
#
class HTMLTextContainerEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLTextContainerEvents(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTextContainerEvents
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{1FF6AA72-5842-11CF-A707-00AA00C0098D}'] = HTMLTextContainerEvents
backWrapperClasses[HTMLTextContainerEvents] = '{1FF6AA72-5842-11CF-A707-00AA00C0098D}'

##############################
# HTMLTextContainerEvents2
#
class HTMLTextContainerEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLTextContainerEvents2(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTextContainerEvents2
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F624-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLTextContainerEvents2
backWrapperClasses[HTMLTextContainerEvents2] = '{3050F624-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument
#
class IHTMLDocument(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDocument(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument
		return Dispatch(self.__instance__.QueryInterface(kls))
	#Script
	def _get_Script(self):
		return wrap(self.__get_instance_IHTMLDocument().Script)
	def _set_Script(self, value):
		self.__get_instance_IHTMLDocument().Script = unwrap(value)
	Script = property(_get_Script, _set_Script)

wrapperClasses['{626FC520-A41E-11CF-A731-00A0C9082637}'] = IHTMLDocument
backWrapperClasses[IHTMLDocument] = '{626FC520-A41E-11CF-A731-00A0C9082637}'

##############################
# IHTMLDocument2
#
class IHTMLDocument2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDocument2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#mimeType
	def _get_mimeType(self):
		return wrap(self.__get_instance_IHTMLDocument2().mimeType)
	def _set_mimeType(self, value):
		self.__get_instance_IHTMLDocument2().mimeType = unwrap(value)
	mimeType = property(_get_mimeType, _set_mimeType)

	#fileUpdatedDate
	def _get_fileUpdatedDate(self):
		return wrap(self.__get_instance_IHTMLDocument2().fileUpdatedDate)
	def _set_fileUpdatedDate(self, value):
		self.__get_instance_IHTMLDocument2().fileUpdatedDate = unwrap(value)
	fileUpdatedDate = property(_get_fileUpdatedDate, _set_fileUpdatedDate)

	#all
	def _get_all(self):
		return wrap(self.__get_instance_IHTMLDocument2().all)
	def _set_all(self, value):
		self.__get_instance_IHTMLDocument2().all = unwrap(value)
	all = property(_get_all, _set_all)

	#selection
	def _get_selection(self):
		return wrap(self.__get_instance_IHTMLDocument2().selection)
	def _set_selection(self, value):
		self.__get_instance_IHTMLDocument2().selection = unwrap(value)
	selection = property(_get_selection, _set_selection)

	#protocol
	def _get_protocol(self):
		return wrap(self.__get_instance_IHTMLDocument2().protocol)
	def _set_protocol(self, value):
		self.__get_instance_IHTMLDocument2().protocol = unwrap(value)
	protocol = property(_get_protocol, _set_protocol)

	#links
	def _get_links(self):
		return wrap(self.__get_instance_IHTMLDocument2().links)
	def _set_links(self, value):
		self.__get_instance_IHTMLDocument2().links = unwrap(value)
	links = property(_get_links, _set_links)

	#onafterupdate
	def _get_onafterupdate(self):
		return wrap(self.__get_instance_IHTMLDocument2().onafterupdate)
	def _set_onafterupdate(self, value):
		self.__get_instance_IHTMLDocument2().onafterupdate = unwrap(value)
	onafterupdate = property(_get_onafterupdate, _set_onafterupdate)

	#domain
	def _get_domain(self):
		return wrap(self.__get_instance_IHTMLDocument2().domain)
	def _set_domain(self, value):
		self.__get_instance_IHTMLDocument2().domain = unwrap(value)
	domain = property(_get_domain, _set_domain)

	#onmousedown
	def _get_onmousedown(self):
		return wrap(self.__get_instance_IHTMLDocument2().onmousedown)
	def _set_onmousedown(self, value):
		self.__get_instance_IHTMLDocument2().onmousedown = unwrap(value)
	onmousedown = property(_get_onmousedown, _set_onmousedown)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance_IHTMLDocument2().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance_IHTMLDocument2().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#designMode
	def _get_designMode(self):
		return wrap(self.__get_instance_IHTMLDocument2().designMode)
	def _set_designMode(self, value):
		self.__get_instance_IHTMLDocument2().designMode = unwrap(value)
	designMode = property(_get_designMode, _set_designMode)

	#plugins
	def _get_plugins(self):
		return wrap(self.__get_instance_IHTMLDocument2().plugins)
	def _set_plugins(self, value):
		self.__get_instance_IHTMLDocument2().plugins = unwrap(value)
	plugins = property(_get_plugins, _set_plugins)

	#frames
	def _get_frames(self):
		return wrap(self.__get_instance_IHTMLDocument2().frames)
	def _set_frames(self, value):
		self.__get_instance_IHTMLDocument2().frames = unwrap(value)
	frames = property(_get_frames, _set_frames)

	#onrowexit
	def _get_onrowexit(self):
		return wrap(self.__get_instance_IHTMLDocument2().onrowexit)
	def _set_onrowexit(self, value):
		self.__get_instance_IHTMLDocument2().onrowexit = unwrap(value)
	onrowexit = property(_get_onrowexit, _set_onrowexit)

	#fileModifiedDate
	def _get_fileModifiedDate(self):
		return wrap(self.__get_instance_IHTMLDocument2().fileModifiedDate)
	def _set_fileModifiedDate(self, value):
		self.__get_instance_IHTMLDocument2().fileModifiedDate = unwrap(value)
	fileModifiedDate = property(_get_fileModifiedDate, _set_fileModifiedDate)

	#title
	def _get_title(self):
		return wrap(self.__get_instance_IHTMLDocument2().title)
	def _set_title(self, value):
		self.__get_instance_IHTMLDocument2().title = unwrap(value)
	title = property(_get_title, _set_title)

	#applets
	def _get_applets(self):
		return wrap(self.__get_instance_IHTMLDocument2().applets)
	def _set_applets(self, value):
		self.__get_instance_IHTMLDocument2().applets = unwrap(value)
	applets = property(_get_applets, _set_applets)

	#charset
	def _get_charset(self):
		return wrap(self.__get_instance_IHTMLDocument2().charset)
	def _set_charset(self, value):
		self.__get_instance_IHTMLDocument2().charset = unwrap(value)
	charset = property(_get_charset, _set_charset)

	#onhelp
	def _get_onhelp(self):
		return wrap(self.__get_instance_IHTMLDocument2().onhelp)
	def _set_onhelp(self, value):
		self.__get_instance_IHTMLDocument2().onhelp = unwrap(value)
	onhelp = property(_get_onhelp, _set_onhelp)

	#forms
	def _get_forms(self):
		return wrap(self.__get_instance_IHTMLDocument2().forms)
	def _set_forms(self, value):
		self.__get_instance_IHTMLDocument2().forms = unwrap(value)
	forms = property(_get_forms, _set_forms)

	#URL
	def _get_URL(self):
		return wrap(self.__get_instance_IHTMLDocument2().URL)
	def _set_URL(self, value):
		self.__get_instance_IHTMLDocument2().URL = unwrap(value)
	URL = property(_get_URL, _set_URL)

	#onmouseup
	def _get_onmouseup(self):
		return wrap(self.__get_instance_IHTMLDocument2().onmouseup)
	def _set_onmouseup(self, value):
		self.__get_instance_IHTMLDocument2().onmouseup = unwrap(value)
	onmouseup = property(_get_onmouseup, _set_onmouseup)

	#linkColor
	def _get_linkColor(self):
		return wrap(self.__get_instance_IHTMLDocument2().linkColor)
	def _set_linkColor(self, value):
		self.__get_instance_IHTMLDocument2().linkColor = unwrap(value)
	linkColor = property(_get_linkColor, _set_linkColor)

	#vlinkColor
	def _get_vlinkColor(self):
		return wrap(self.__get_instance_IHTMLDocument2().vlinkColor)
	def _set_vlinkColor(self, value):
		self.__get_instance_IHTMLDocument2().vlinkColor = unwrap(value)
	vlinkColor = property(_get_vlinkColor, _set_vlinkColor)

	#onclick
	def _get_onclick(self):
		return wrap(self.__get_instance_IHTMLDocument2().onclick)
	def _set_onclick(self, value):
		self.__get_instance_IHTMLDocument2().onclick = unwrap(value)
	onclick = property(_get_onclick, _set_onclick)

	#onbeforeupdate
	def _get_onbeforeupdate(self):
		return wrap(self.__get_instance_IHTMLDocument2().onbeforeupdate)
	def _set_onbeforeupdate(self, value):
		self.__get_instance_IHTMLDocument2().onbeforeupdate = unwrap(value)
	onbeforeupdate = property(_get_onbeforeupdate, _set_onbeforeupdate)

	#onmousemove
	def _get_onmousemove(self):
		return wrap(self.__get_instance_IHTMLDocument2().onmousemove)
	def _set_onmousemove(self, value):
		self.__get_instance_IHTMLDocument2().onmousemove = unwrap(value)
	onmousemove = property(_get_onmousemove, _set_onmousemove)

	#onrowenter
	def _get_onrowenter(self):
		return wrap(self.__get_instance_IHTMLDocument2().onrowenter)
	def _set_onrowenter(self, value):
		self.__get_instance_IHTMLDocument2().onrowenter = unwrap(value)
	onrowenter = property(_get_onrowenter, _set_onrowenter)

	#location
	def _get_location(self):
		return wrap(self.__get_instance_IHTMLDocument2().location)
	def _set_location(self, value):
		self.__get_instance_IHTMLDocument2().location = unwrap(value)
	location = property(_get_location, _set_location)

	#body
	def _get_body(self):
		return wrap(self.__get_instance_IHTMLDocument2().body, DispHTMLBody)
	def _set_body(self, value):
		self.__get_instance_IHTMLDocument2().body = unwrap(value)
	body = property(_get_body, _set_body)

	#ondragstart
	def _get_ondragstart(self):
		return wrap(self.__get_instance_IHTMLDocument2().ondragstart)
	def _set_ondragstart(self, value):
		self.__get_instance_IHTMLDocument2().ondragstart = unwrap(value)
	ondragstart = property(_get_ondragstart, _set_ondragstart)

	#anchors
	def _get_anchors(self):
		return wrap(self.__get_instance_IHTMLDocument2().anchors)
	def _set_anchors(self, value):
		self.__get_instance_IHTMLDocument2().anchors = unwrap(value)
	anchors = property(_get_anchors, _set_anchors)

	#onmouseout
	def _get_onmouseout(self):
		return wrap(self.__get_instance_IHTMLDocument2().onmouseout)
	def _set_onmouseout(self, value):
		self.__get_instance_IHTMLDocument2().onmouseout = unwrap(value)
	onmouseout = property(_get_onmouseout, _set_onmouseout)

	#onkeypress
	def _get_onkeypress(self):
		return wrap(self.__get_instance_IHTMLDocument2().onkeypress)
	def _set_onkeypress(self, value):
		self.__get_instance_IHTMLDocument2().onkeypress = unwrap(value)
	onkeypress = property(_get_onkeypress, _set_onkeypress)

	#embeds
	def _get_embeds(self):
		return wrap(self.__get_instance_IHTMLDocument2().embeds)
	def _set_embeds(self, value):
		self.__get_instance_IHTMLDocument2().embeds = unwrap(value)
	embeds = property(_get_embeds, _set_embeds)

	#images
	def _get_images(self):
		return wrap(self.__get_instance_IHTMLDocument2().images)
	def _set_images(self, value):
		self.__get_instance_IHTMLDocument2().images = unwrap(value)
	images = property(_get_images, _set_images)

	#onerrorupdate
	def _get_onerrorupdate(self):
		return wrap(self.__get_instance_IHTMLDocument2().onerrorupdate)
	def _set_onerrorupdate(self, value):
		self.__get_instance_IHTMLDocument2().onerrorupdate = unwrap(value)
	onerrorupdate = property(_get_onerrorupdate, _set_onerrorupdate)

	#onkeydown
	def _get_onkeydown(self):
		return wrap(self.__get_instance_IHTMLDocument2().onkeydown)
	def _set_onkeydown(self, value):
		self.__get_instance_IHTMLDocument2().onkeydown = unwrap(value)
	onkeydown = property(_get_onkeydown, _set_onkeydown)

	#fileCreatedDate
	def _get_fileCreatedDate(self):
		return wrap(self.__get_instance_IHTMLDocument2().fileCreatedDate)
	def _set_fileCreatedDate(self, value):
		self.__get_instance_IHTMLDocument2().fileCreatedDate = unwrap(value)
	fileCreatedDate = property(_get_fileCreatedDate, _set_fileCreatedDate)

	#onkeyup
	def _get_onkeyup(self):
		return wrap(self.__get_instance_IHTMLDocument2().onkeyup)
	def _set_onkeyup(self, value):
		self.__get_instance_IHTMLDocument2().onkeyup = unwrap(value)
	onkeyup = property(_get_onkeyup, _set_onkeyup)

	#cookie
	def _get_cookie(self):
		return wrap(self.__get_instance_IHTMLDocument2().cookie)
	def _set_cookie(self, value):
		self.__get_instance_IHTMLDocument2().cookie = unwrap(value)
	cookie = property(_get_cookie, _set_cookie)

	#fileSize
	def _get_fileSize(self):
		return wrap(self.__get_instance_IHTMLDocument2().fileSize)
	def _set_fileSize(self, value):
		self.__get_instance_IHTMLDocument2().fileSize = unwrap(value)
	fileSize = property(_get_fileSize, _set_fileSize)

	#scripts
	def _get_scripts(self):
		return wrap(self.__get_instance_IHTMLDocument2().scripts)
	def _set_scripts(self, value):
		self.__get_instance_IHTMLDocument2().scripts = unwrap(value)
	scripts = property(_get_scripts, _set_scripts)

	#parentWindow
	def _get_parentWindow(self):
		return wrap(self.__get_instance_IHTMLDocument2().parentWindow)
	def _set_parentWindow(self, value):
		self.__get_instance_IHTMLDocument2().parentWindow = unwrap(value)
	parentWindow = property(_get_parentWindow, _set_parentWindow)

	#activeElement
	def _get_activeElement(self):
		return wrap(self.__get_instance_IHTMLDocument2().activeElement)
	def _set_activeElement(self, value):
		self.__get_instance_IHTMLDocument2().activeElement = unwrap(value)
	activeElement = property(_get_activeElement, _set_activeElement)

	#expando
	def _get_expando(self):
		return wrap(self.__get_instance_IHTMLDocument2().expando)
	def _set_expando(self, value):
		self.__get_instance_IHTMLDocument2().expando = unwrap(value)
	expando = property(_get_expando, _set_expando)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLDocument2().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLDocument2().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#referrer
	def _get_referrer(self):
		return wrap(self.__get_instance_IHTMLDocument2().referrer)
	def _set_referrer(self, value):
		self.__get_instance_IHTMLDocument2().referrer = unwrap(value)
	referrer = property(_get_referrer, _set_referrer)

	#onmouseover
	def _get_onmouseover(self):
		return wrap(self.__get_instance_IHTMLDocument2().onmouseover)
	def _set_onmouseover(self, value):
		self.__get_instance_IHTMLDocument2().onmouseover = unwrap(value)
	onmouseover = property(_get_onmouseover, _set_onmouseover)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance_IHTMLDocument2().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance_IHTMLDocument2().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#styleSheets
	def _get_styleSheets(self):
		return wrap(self.__get_instance_IHTMLDocument2().styleSheets)
	def _set_styleSheets(self, value):
		self.__get_instance_IHTMLDocument2().styleSheets = unwrap(value)
	styleSheets = property(_get_styleSheets, _set_styleSheets)

	#nameProp
	def _get_nameProp(self):
		return wrap(self.__get_instance_IHTMLDocument2().nameProp)
	def _set_nameProp(self, value):
		self.__get_instance_IHTMLDocument2().nameProp = unwrap(value)
	nameProp = property(_get_nameProp, _set_nameProp)

	#lastModified
	def _get_lastModified(self):
		return wrap(self.__get_instance_IHTMLDocument2().lastModified)
	def _set_lastModified(self, value):
		self.__get_instance_IHTMLDocument2().lastModified = unwrap(value)
	lastModified = property(_get_lastModified, _set_lastModified)

	#alinkColor
	def _get_alinkColor(self):
		return wrap(self.__get_instance_IHTMLDocument2().alinkColor)
	def _set_alinkColor(self, value):
		self.__get_instance_IHTMLDocument2().alinkColor = unwrap(value)
	alinkColor = property(_get_alinkColor, _set_alinkColor)

	#security
	def _get_security(self):
		return wrap(self.__get_instance_IHTMLDocument2().security)
	def _set_security(self, value):
		self.__get_instance_IHTMLDocument2().security = unwrap(value)
	security = property(_get_security, _set_security)

	#ondblclick
	def _get_ondblclick(self):
		return wrap(self.__get_instance_IHTMLDocument2().ondblclick)
	def _set_ondblclick(self, value):
		self.__get_instance_IHTMLDocument2().ondblclick = unwrap(value)
	ondblclick = property(_get_ondblclick, _set_ondblclick)

	#onselectstart
	def _get_onselectstart(self):
		return wrap(self.__get_instance_IHTMLDocument2().onselectstart)
	def _set_onselectstart(self, value):
		self.__get_instance_IHTMLDocument2().onselectstart = unwrap(value)
	onselectstart = property(_get_onselectstart, _set_onselectstart)

	#fgColor
	def _get_fgColor(self):
		return wrap(self.__get_instance_IHTMLDocument2().fgColor)
	def _set_fgColor(self, value):
		self.__get_instance_IHTMLDocument2().fgColor = unwrap(value)
	fgColor = property(_get_fgColor, _set_fgColor)

	#defaultCharset
	def _get_defaultCharset(self):
		return wrap(self.__get_instance_IHTMLDocument2().defaultCharset)
	def _set_defaultCharset(self, value):
		self.__get_instance_IHTMLDocument2().defaultCharset = unwrap(value)
	defaultCharset = property(_get_defaultCharset, _set_defaultCharset)

	#writeln
	def writeln(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().writeln(*args))

	#execCommandShowHelp
	def execCommandShowHelp(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().execCommandShowHelp(*args))

	#execCommand
	def execCommand(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().execCommand(*args))

	#clear
	def clear(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().clear(*args))

	#queryCommandState
	def queryCommandState(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandState(*args))

	#createStyleSheet
	def createStyleSheet(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().createStyleSheet(*args))

	#createElement
	def createElement(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().createElement(*args))

	#write
	def write(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().write(*args))

	#queryCommandEnabled
	def queryCommandEnabled(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandEnabled(*args))

	#queryCommandText
	def queryCommandText(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandText(*args))

	#toString
	def toString(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().toString(*args))

	#queryCommandIndeterm
	def queryCommandIndeterm(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandIndeterm(*args))

	#queryCommandValue
	def queryCommandValue(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandValue(*args))

	#close
	def close(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().close(*args))

	#elementFromPoint
	def elementFromPoint(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().elementFromPoint(*args))

	#open
	def open(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().open(*args))

	#queryCommandSupported
	def queryCommandSupported(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument2().queryCommandSupported(*args))

wrapperClasses['{332C4425-26CB-11D0-B483-00C04FD90119}'] = IHTMLDocument2
backWrapperClasses[IHTMLDocument2] = '{332C4425-26CB-11D0-B483-00C04FD90119}'

##############################
# IHTMLDocument3
#
class IHTMLDocument3(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDocument3(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument3
		return Dispatch(self.__instance__.QueryInterface(kls))
	#oncontextmenu
	def _get_oncontextmenu(self):
		return wrap(self.__get_instance_IHTMLDocument3().oncontextmenu)
	def _set_oncontextmenu(self, value):
		self.__get_instance_IHTMLDocument3().oncontextmenu = unwrap(value)
	oncontextmenu = property(_get_oncontextmenu, _set_oncontextmenu)

	#onrowsdelete
	def _get_onrowsdelete(self):
		return wrap(self.__get_instance_IHTMLDocument3().onrowsdelete)
	def _set_onrowsdelete(self, value):
		self.__get_instance_IHTMLDocument3().onrowsdelete = unwrap(value)
	onrowsdelete = property(_get_onrowsdelete, _set_onrowsdelete)

	#ondataavailable
	def _get_ondataavailable(self):
		return wrap(self.__get_instance_IHTMLDocument3().ondataavailable)
	def _set_ondataavailable(self, value):
		self.__get_instance_IHTMLDocument3().ondataavailable = unwrap(value)
	ondataavailable = property(_get_ondataavailable, _set_ondataavailable)

	#documentElement
	def _get_documentElement(self):
		return wrap(self.__get_instance_IHTMLDocument3().documentElement)
	def _set_documentElement(self, value):
		self.__get_instance_IHTMLDocument3().documentElement = unwrap(value)
	documentElement = property(_get_documentElement, _set_documentElement)

	#oncellchange
	def _get_oncellchange(self):
		return wrap(self.__get_instance_IHTMLDocument3().oncellchange)
	def _set_oncellchange(self, value):
		self.__get_instance_IHTMLDocument3().oncellchange = unwrap(value)
	oncellchange = property(_get_oncellchange, _set_oncellchange)

	#enableDownload
	def _get_enableDownload(self):
		return wrap(self.__get_instance_IHTMLDocument3().enableDownload)
	def _set_enableDownload(self, value):
		self.__get_instance_IHTMLDocument3().enableDownload = unwrap(value)
	enableDownload = property(_get_enableDownload, _set_enableDownload)

	#onpropertychange
	def _get_onpropertychange(self):
		return wrap(self.__get_instance_IHTMLDocument3().onpropertychange)
	def _set_onpropertychange(self, value):
		self.__get_instance_IHTMLDocument3().onpropertychange = unwrap(value)
	onpropertychange = property(_get_onpropertychange, _set_onpropertychange)

	#baseUrl
	def _get_baseUrl(self):
		return wrap(self.__get_instance_IHTMLDocument3().baseUrl)
	def _set_baseUrl(self, value):
		self.__get_instance_IHTMLDocument3().baseUrl = unwrap(value)
	baseUrl = property(_get_baseUrl, _set_baseUrl)

	#onrowsinserted
	def _get_onrowsinserted(self):
		return wrap(self.__get_instance_IHTMLDocument3().onrowsinserted)
	def _set_onrowsinserted(self, value):
		self.__get_instance_IHTMLDocument3().onrowsinserted = unwrap(value)
	onrowsinserted = property(_get_onrowsinserted, _set_onrowsinserted)

	#ondatasetchanged
	def _get_ondatasetchanged(self):
		return wrap(self.__get_instance_IHTMLDocument3().ondatasetchanged)
	def _set_ondatasetchanged(self, value):
		self.__get_instance_IHTMLDocument3().ondatasetchanged = unwrap(value)
	ondatasetchanged = property(_get_ondatasetchanged, _set_ondatasetchanged)

	#onbeforeeditfocus
	def _get_onbeforeeditfocus(self):
		return wrap(self.__get_instance_IHTMLDocument3().onbeforeeditfocus)
	def _set_onbeforeeditfocus(self, value):
		self.__get_instance_IHTMLDocument3().onbeforeeditfocus = unwrap(value)
	onbeforeeditfocus = property(_get_onbeforeeditfocus, _set_onbeforeeditfocus)

	#ondatasetcomplete
	def _get_ondatasetcomplete(self):
		return wrap(self.__get_instance_IHTMLDocument3().ondatasetcomplete)
	def _set_ondatasetcomplete(self, value):
		self.__get_instance_IHTMLDocument3().ondatasetcomplete = unwrap(value)
	ondatasetcomplete = property(_get_ondatasetcomplete, _set_ondatasetcomplete)

	#uniqueID
	def _get_uniqueID(self):
		return wrap(self.__get_instance_IHTMLDocument3().uniqueID)
	def _set_uniqueID(self, value):
		self.__get_instance_IHTMLDocument3().uniqueID = unwrap(value)
	uniqueID = property(_get_uniqueID, _set_uniqueID)

	#inheritStyleSheets
	def _get_inheritStyleSheets(self):
		return wrap(self.__get_instance_IHTMLDocument3().inheritStyleSheets)
	def _set_inheritStyleSheets(self, value):
		self.__get_instance_IHTMLDocument3().inheritStyleSheets = unwrap(value)
	inheritStyleSheets = property(_get_inheritStyleSheets, _set_inheritStyleSheets)

	#childNodes
	def _get_childNodes(self):
		return wrap(self.__get_instance_IHTMLDocument3().childNodes)
	def _set_childNodes(self, value):
		self.__get_instance_IHTMLDocument3().childNodes = unwrap(value)
	childNodes = property(_get_childNodes, _set_childNodes)

	#parentDocument
	def _get_parentDocument(self):
		return wrap(self.__get_instance_IHTMLDocument3().parentDocument)
	def _set_parentDocument(self, value):
		self.__get_instance_IHTMLDocument3().parentDocument = unwrap(value)
	parentDocument = property(_get_parentDocument, _set_parentDocument)

	#dir
	def _get_dir(self):
		return wrap(self.__get_instance_IHTMLDocument3().dir)
	def _set_dir(self, value):
		self.__get_instance_IHTMLDocument3().dir = unwrap(value)
	dir = property(_get_dir, _set_dir)

	#onstop
	def _get_onstop(self):
		return wrap(self.__get_instance_IHTMLDocument3().onstop)
	def _set_onstop(self, value):
		self.__get_instance_IHTMLDocument3().onstop = unwrap(value)
	onstop = property(_get_onstop, _set_onstop)

	#getElementsByName
	def getElementsByName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().getElementsByName(*args))

	#recalc
	def recalc(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().recalc(*args))

	#getElementsByTagName
	def getElementsByTagName(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().getElementsByTagName(*args))

	#releaseCapture
	def releaseCapture(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().releaseCapture(*args))

	#attachEvent
	def attachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().attachEvent(*args))

	#getElementById
	def getElementById(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().getElementById(*args))

	#createDocumentFragment
	def createDocumentFragment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().createDocumentFragment(*args))

	#detachEvent
	def detachEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().detachEvent(*args))

	#createTextNode
	def createTextNode(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument3().createTextNode(*args))

wrapperClasses['{3050F485-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument3
backWrapperClasses[IHTMLDocument3] = '{3050F485-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument4
#
class IHTMLDocument4(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDocument4(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument4
		return Dispatch(self.__instance__.QueryInterface(kls))
	#media
	def _get_media(self):
		return wrap(self.__get_instance_IHTMLDocument4().media)
	def _set_media(self, value):
		self.__get_instance_IHTMLDocument4().media = unwrap(value)
	media = property(_get_media, _set_media)

	#onselectionchange
	def _get_onselectionchange(self):
		return wrap(self.__get_instance_IHTMLDocument4().onselectionchange)
	def _set_onselectionchange(self, value):
		self.__get_instance_IHTMLDocument4().onselectionchange = unwrap(value)
	onselectionchange = property(_get_onselectionchange, _set_onselectionchange)

	#URLUnencoded
	def _get_URLUnencoded(self):
		return wrap(self.__get_instance_IHTMLDocument4().URLUnencoded)
	def _set_URLUnencoded(self, value):
		self.__get_instance_IHTMLDocument4().URLUnencoded = unwrap(value)
	URLUnencoded = property(_get_URLUnencoded, _set_URLUnencoded)

	#namespaces
	def _get_namespaces(self):
		return wrap(self.__get_instance_IHTMLDocument4().namespaces)
	def _set_namespaces(self, value):
		self.__get_instance_IHTMLDocument4().namespaces = unwrap(value)
	namespaces = property(_get_namespaces, _set_namespaces)

	#oncontrolselect
	def _get_oncontrolselect(self):
		return wrap(self.__get_instance_IHTMLDocument4().oncontrolselect)
	def _set_oncontrolselect(self, value):
		self.__get_instance_IHTMLDocument4().oncontrolselect = unwrap(value)
	oncontrolselect = property(_get_oncontrolselect, _set_oncontrolselect)

	#hasFocus
	def hasFocus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().hasFocus(*args))

	#focus
	def focus(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().focus(*args))

	#createDocumentFromUrl
	def createDocumentFromUrl(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().createDocumentFromUrl(*args))

	#createRenderStyle
	def createRenderStyle(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().createRenderStyle(*args))

	#createEventObject
	def createEventObject(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().createEventObject(*args))

	#fireEvent
	def fireEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument4().fireEvent(*args))

wrapperClasses['{3050F69A-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument4
backWrapperClasses[IHTMLDocument4] = '{3050F69A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLDocument5
#
class IHTMLDocument5(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLDocument5(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLDocument5
		return Dispatch(self.__instance__.QueryInterface(kls))
	#ondeactivate
	def _get_ondeactivate(self):
		return wrap(self.__get_instance_IHTMLDocument5().ondeactivate)
	def _set_ondeactivate(self, value):
		self.__get_instance_IHTMLDocument5().ondeactivate = unwrap(value)
	ondeactivate = property(_get_ondeactivate, _set_ondeactivate)

	#implementation
	def _get_implementation(self):
		return wrap(self.__get_instance_IHTMLDocument5().implementation)
	def _set_implementation(self, value):
		self.__get_instance_IHTMLDocument5().implementation = unwrap(value)
	implementation = property(_get_implementation, _set_implementation)

	#onfocusout
	def _get_onfocusout(self):
		return wrap(self.__get_instance_IHTMLDocument5().onfocusout)
	def _set_onfocusout(self, value):
		self.__get_instance_IHTMLDocument5().onfocusout = unwrap(value)
	onfocusout = property(_get_onfocusout, _set_onfocusout)

	#doctype
	def _get_doctype(self):
		return wrap(self.__get_instance_IHTMLDocument5().doctype)
	def _set_doctype(self, value):
		self.__get_instance_IHTMLDocument5().doctype = unwrap(value)
	doctype = property(_get_doctype, _set_doctype)

	#onbeforeactivate
	def _get_onbeforeactivate(self):
		return wrap(self.__get_instance_IHTMLDocument5().onbeforeactivate)
	def _set_onbeforeactivate(self, value):
		self.__get_instance_IHTMLDocument5().onbeforeactivate = unwrap(value)
	onbeforeactivate = property(_get_onbeforeactivate, _set_onbeforeactivate)

	#onbeforedeactivate
	def _get_onbeforedeactivate(self):
		return wrap(self.__get_instance_IHTMLDocument5().onbeforedeactivate)
	def _set_onbeforedeactivate(self, value):
		self.__get_instance_IHTMLDocument5().onbeforedeactivate = unwrap(value)
	onbeforedeactivate = property(_get_onbeforedeactivate, _set_onbeforedeactivate)

	#onactivate
	def _get_onactivate(self):
		return wrap(self.__get_instance_IHTMLDocument5().onactivate)
	def _set_onactivate(self, value):
		self.__get_instance_IHTMLDocument5().onactivate = unwrap(value)
	onactivate = property(_get_onactivate, _set_onactivate)

	#compatMode
	def _get_compatMode(self):
		return wrap(self.__get_instance_IHTMLDocument5().compatMode)
	def _set_compatMode(self, value):
		self.__get_instance_IHTMLDocument5().compatMode = unwrap(value)
	compatMode = property(_get_compatMode, _set_compatMode)

	#onmousewheel
	def _get_onmousewheel(self):
		return wrap(self.__get_instance_IHTMLDocument5().onmousewheel)
	def _set_onmousewheel(self, value):
		self.__get_instance_IHTMLDocument5().onmousewheel = unwrap(value)
	onmousewheel = property(_get_onmousewheel, _set_onmousewheel)

	#onfocusin
	def _get_onfocusin(self):
		return wrap(self.__get_instance_IHTMLDocument5().onfocusin)
	def _set_onfocusin(self, value):
		self.__get_instance_IHTMLDocument5().onfocusin = unwrap(value)
	onfocusin = property(_get_onfocusin, _set_onfocusin)

	#createAttribute
	def createAttribute(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument5().createAttribute(*args))

	#createComment
	def createComment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLDocument5().createComment(*args))

wrapperClasses['{3050F80C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLDocument5
backWrapperClasses[IHTMLDocument5] = '{3050F80C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLDocument
#
class DispHTMLDocument(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLDocument(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLDocument
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F55F-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLDocument
backWrapperClasses[DispHTMLDocument] = '{3050F55F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCommentElement
#
class IHTMLCommentElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCommentElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCommentElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#text
	def _get_text(self):
		return wrap(self.__get_instance_IHTMLCommentElement().text)
	def _set_text(self, value):
		self.__get_instance_IHTMLCommentElement().text = unwrap(value)
	text = property(_get_text, _set_text)

	#atomic
	def _get_atomic(self):
		return wrap(self.__get_instance_IHTMLCommentElement().atomic)
	def _set_atomic(self, value):
		self.__get_instance_IHTMLCommentElement().atomic = unwrap(value)
	atomic = property(_get_atomic, _set_atomic)

wrapperClasses['{3050F20C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCommentElement
backWrapperClasses[IHTMLCommentElement] = '{3050F20C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLCommentElement2
#
class IHTMLCommentElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLCommentElement2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLCommentElement2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#length
	def _get_length(self):
		return wrap(self.__get_instance_IHTMLCommentElement2().length)
	def _set_length(self, value):
		self.__get_instance_IHTMLCommentElement2().length = unwrap(value)
	length = property(_get_length, _set_length)

	#data
	def _get_data(self):
		return wrap(self.__get_instance_IHTMLCommentElement2().data)
	def _set_data(self, value):
		self.__get_instance_IHTMLCommentElement2().data = unwrap(value)
	data = property(_get_data, _set_data)

	#appendData
	def appendData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCommentElement2().appendData(*args))

	#deleteData
	def deleteData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCommentElement2().deleteData(*args))

	#substringData
	def substringData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCommentElement2().substringData(*args))

	#insertData
	def insertData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCommentElement2().insertData(*args))

	#replaceData
	def replaceData(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLCommentElement2().replaceData(*args))

wrapperClasses['{3050F813-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLCommentElement2
backWrapperClasses[IHTMLCommentElement2] = '{3050F813-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLCommentElement
#
class DispHTMLCommentElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLCommentElement(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLCommentElement
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F50A-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLCommentElement
backWrapperClasses[DispHTMLCommentElement] = '{3050F50A-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLElementEvents2
#
class HTMLElementEvents2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLElementEvents2(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLElementEvents2
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F60F-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLElementEvents2
backWrapperClasses[HTMLElementEvents2] = '{3050F60F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLElementEvents
#
class HTMLElementEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLElementEvents(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLElementEvents
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F33C-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLElementEvents
backWrapperClasses[HTMLElementEvents] = '{3050F33C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# HTMLTableEvents
#
class HTMLTableEvents(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_HTMLTableEvents(self, kls=None):
		if kls is None:
			kls = MSHTML.HTMLTableEvents
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F407-98B5-11CF-BB82-00AA00BDCE0B}'] = HTMLTableEvents
backWrapperClasses[HTMLTableEvents] = '{3050F407-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableCaption
#
class IHTMLTableCaption(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTableCaption(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableCaption
		return Dispatch(self.__instance__.QueryInterface(kls))
	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLTableCaption().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLTableCaption().align = unwrap(value)
	align = property(_get_align, _set_align)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance_IHTMLTableCaption().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance_IHTMLTableCaption().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

wrapperClasses['{3050F2EB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableCaption
backWrapperClasses[IHTMLTableCaption] = '{3050F2EB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTable
#
class IHTMLTable(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTable(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTable
		return Dispatch(self.__instance__.QueryInterface(kls))
	#frame
	def _get_frame(self):
		return wrap(self.__get_instance_IHTMLTable().frame)
	def _set_frame(self, value):
		self.__get_instance_IHTMLTable().frame = unwrap(value)
	frame = property(_get_frame, _set_frame)

	#borderColorDark
	def _get_borderColorDark(self):
		return wrap(self.__get_instance_IHTMLTable().borderColorDark)
	def _set_borderColorDark(self, value):
		self.__get_instance_IHTMLTable().borderColorDark = unwrap(value)
	borderColorDark = property(_get_borderColorDark, _set_borderColorDark)

	#cols
	def _get_cols(self):
		return wrap(self.__get_instance_IHTMLTable().cols)
	def _set_cols(self, value):
		self.__get_instance_IHTMLTable().cols = unwrap(value)
	cols = property(_get_cols, _set_cols)

	#height
	def _get_height(self):
		return wrap(self.__get_instance_IHTMLTable().height)
	def _set_height(self, value):
		self.__get_instance_IHTMLTable().height = unwrap(value)
	height = property(_get_height, _set_height)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance_IHTMLTable().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance_IHTMLTable().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#tFoot
	def _get_tFoot(self):
		return wrap(self.__get_instance_IHTMLTable().tFoot)
	def _set_tFoot(self, value):
		self.__get_instance_IHTMLTable().tFoot = unwrap(value)
	tFoot = property(_get_tFoot, _set_tFoot)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLTable().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLTable().border = unwrap(value)
	border = property(_get_border, _set_border)

	#tHead
	def _get_tHead(self):
		return wrap(self.__get_instance_IHTMLTable().tHead)
	def _set_tHead(self, value):
		self.__get_instance_IHTMLTable().tHead = unwrap(value)
	tHead = property(_get_tHead, _set_tHead)

	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance_IHTMLTable().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance_IHTMLTable().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance_IHTMLTable().rows)
	def _set_rows(self, value):
		self.__get_instance_IHTMLTable().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#cellSpacing
	def _get_cellSpacing(self):
		return wrap(self.__get_instance_IHTMLTable().cellSpacing)
	def _set_cellSpacing(self, value):
		self.__get_instance_IHTMLTable().cellSpacing = unwrap(value)
	cellSpacing = property(_get_cellSpacing, _set_cellSpacing)

	#dataPageSize
	def _get_dataPageSize(self):
		return wrap(self.__get_instance_IHTMLTable().dataPageSize)
	def _set_dataPageSize(self, value):
		self.__get_instance_IHTMLTable().dataPageSize = unwrap(value)
	dataPageSize = property(_get_dataPageSize, _set_dataPageSize)

	#width
	def _get_width(self):
		return wrap(self.__get_instance_IHTMLTable().width)
	def _set_width(self, value):
		self.__get_instance_IHTMLTable().width = unwrap(value)
	width = property(_get_width, _set_width)

	#tBodies
	def _get_tBodies(self):
		return wrap(self.__get_instance_IHTMLTable().tBodies)
	def _set_tBodies(self, value):
		self.__get_instance_IHTMLTable().tBodies = unwrap(value)
	tBodies = property(_get_tBodies, _set_tBodies)

	#rules
	def _get_rules(self):
		return wrap(self.__get_instance_IHTMLTable().rules)
	def _set_rules(self, value):
		self.__get_instance_IHTMLTable().rules = unwrap(value)
	rules = property(_get_rules, _set_rules)

	#borderColorLight
	def _get_borderColorLight(self):
		return wrap(self.__get_instance_IHTMLTable().borderColorLight)
	def _set_borderColorLight(self, value):
		self.__get_instance_IHTMLTable().borderColorLight = unwrap(value)
	borderColorLight = property(_get_borderColorLight, _set_borderColorLight)

	#background
	def _get_background(self):
		return wrap(self.__get_instance_IHTMLTable().background)
	def _set_background(self, value):
		self.__get_instance_IHTMLTable().background = unwrap(value)
	background = property(_get_background, _set_background)

	#cellPadding
	def _get_cellPadding(self):
		return wrap(self.__get_instance_IHTMLTable().cellPadding)
	def _set_cellPadding(self, value):
		self.__get_instance_IHTMLTable().cellPadding = unwrap(value)
	cellPadding = property(_get_cellPadding, _set_cellPadding)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLTable().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLTable().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLTable().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLTable().align = unwrap(value)
	align = property(_get_align, _set_align)

	#caption
	def _get_caption(self):
		return wrap(self.__get_instance_IHTMLTable().caption)
	def _set_caption(self, value):
		self.__get_instance_IHTMLTable().caption = unwrap(value)
	caption = property(_get_caption, _set_caption)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance_IHTMLTable().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance_IHTMLTable().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#deleteTFoot
	def deleteTFoot(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().deleteTFoot(*args))

	#deleteTHead
	def deleteTHead(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().deleteTHead(*args))

	#createTFoot
	def createTFoot(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().createTFoot(*args))

	#refresh
	def refresh(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().refresh(*args))

	#createCaption
	def createCaption(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().createCaption(*args))

	#insertRow
	def insertRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().insertRow(*args))

	#deleteRow
	def deleteRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().deleteRow(*args))

	#deleteCaption
	def deleteCaption(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().deleteCaption(*args))

	#nextPage
	def nextPage(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().nextPage(*args))

	#createTHead
	def createTHead(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().createTHead(*args))

	#previousPage
	def previousPage(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTable().previousPage(*args))

wrapperClasses['{3050F21E-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTable
backWrapperClasses[IHTMLTable] = '{3050F21E-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableSection
#
class IHTMLTableSection(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTableSection(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableSection
		return Dispatch(self.__instance__.QueryInterface(kls))
	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance_IHTMLTableSection().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance_IHTMLTableSection().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLTableSection().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLTableSection().align = unwrap(value)
	align = property(_get_align, _set_align)

	#rows
	def _get_rows(self):
		return wrap(self.__get_instance_IHTMLTableSection().rows)
	def _set_rows(self, value):
		self.__get_instance_IHTMLTableSection().rows = unwrap(value)
	rows = property(_get_rows, _set_rows)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance_IHTMLTableSection().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance_IHTMLTableSection().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

	#insertRow
	def insertRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTableSection().insertRow(*args))

	#deleteRow
	def deleteRow(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTableSection().deleteRow(*args))

wrapperClasses['{3050F23B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableSection
backWrapperClasses[IHTMLTableSection] = '{3050F23B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLTableRow
#
class IHTMLTableRow(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLTableRow(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLTableRow
		return Dispatch(self.__instance__.QueryInterface(kls))
	#borderColor
	def _get_borderColor(self):
		return wrap(self.__get_instance_IHTMLTableRow().borderColor)
	def _set_borderColor(self, value):
		self.__get_instance_IHTMLTableRow().borderColor = unwrap(value)
	borderColor = property(_get_borderColor, _set_borderColor)

	#sectionRowIndex
	def _get_sectionRowIndex(self):
		return wrap(self.__get_instance_IHTMLTableRow().sectionRowIndex)
	def _set_sectionRowIndex(self, value):
		self.__get_instance_IHTMLTableRow().sectionRowIndex = unwrap(value)
	sectionRowIndex = property(_get_sectionRowIndex, _set_sectionRowIndex)

	#rowIndex
	def _get_rowIndex(self):
		return wrap(self.__get_instance_IHTMLTableRow().rowIndex)
	def _set_rowIndex(self, value):
		self.__get_instance_IHTMLTableRow().rowIndex = unwrap(value)
	rowIndex = property(_get_rowIndex, _set_rowIndex)

	#borderColorLight
	def _get_borderColorLight(self):
		return wrap(self.__get_instance_IHTMLTableRow().borderColorLight)
	def _set_borderColorLight(self, value):
		self.__get_instance_IHTMLTableRow().borderColorLight = unwrap(value)
	borderColorLight = property(_get_borderColorLight, _set_borderColorLight)

	#align
	def _get_align(self):
		return wrap(self.__get_instance_IHTMLTableRow().align)
	def _set_align(self, value):
		self.__get_instance_IHTMLTableRow().align = unwrap(value)
	align = property(_get_align, _set_align)

	#borderColorDark
	def _get_borderColorDark(self):
		return wrap(self.__get_instance_IHTMLTableRow().borderColorDark)
	def _set_borderColorDark(self, value):
		self.__get_instance_IHTMLTableRow().borderColorDark = unwrap(value)
	borderColorDark = property(_get_borderColorDark, _set_borderColorDark)

	#bgColor
	def _get_bgColor(self):
		return wrap(self.__get_instance_IHTMLTableRow().bgColor)
	def _set_bgColor(self, value):
		self.__get_instance_IHTMLTableRow().bgColor = unwrap(value)
	bgColor = property(_get_bgColor, _set_bgColor)

	#vAlign
	def _get_vAlign(self):
		return wrap(self.__get_instance_IHTMLTableRow().vAlign)
	def _set_vAlign(self, value):
		self.__get_instance_IHTMLTableRow().vAlign = unwrap(value)
	vAlign = property(_get_vAlign, _set_vAlign)

	#cells
	def _get_cells(self):
		return wrap(self.__get_instance_IHTMLTableRow().cells)
	def _set_cells(self, value):
		self.__get_instance_IHTMLTableRow().cells = unwrap(value)
	cells = property(_get_cells, _set_cells)

	#insertCell
	def insertCell(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTableRow().insertCell(*args))

	#deleteCell
	def deleteCell(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLTableRow().deleteCell(*args))

wrapperClasses['{3050F23C-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLTableRow
backWrapperClasses[IHTMLTableRow] = '{3050F23C-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLTable
#
class DispHTMLTable(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLTable(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLTable
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F532-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLTable
backWrapperClasses[DispHTMLTable] = '{3050F532-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLTableRow
#
class DispHTMLTableRow(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLTableRow(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLTableRow
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F535-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLTableRow
backWrapperClasses[DispHTMLTableRow] = '{3050F535-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLScriptElement
#
class IHTMLScriptElement(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLScriptElement(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScriptElement
		return Dispatch(self.__instance__.QueryInterface(kls))
	#defer
	def _get_defer(self):
		return wrap(self.__get_instance_IHTMLScriptElement().defer)
	def _set_defer(self, value):
		self.__get_instance_IHTMLScriptElement().defer = unwrap(value)
	defer = property(_get_defer, _set_defer)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLScriptElement().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLScriptElement().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

	#src
	def _get_src(self):
		return wrap(self.__get_instance_IHTMLScriptElement().src)
	def _set_src(self, value):
		self.__get_instance_IHTMLScriptElement().src = unwrap(value)
	src = property(_get_src, _set_src)

	#onerror
	def _get_onerror(self):
		return wrap(self.__get_instance_IHTMLScriptElement().onerror)
	def _set_onerror(self, value):
		self.__get_instance_IHTMLScriptElement().onerror = unwrap(value)
	onerror = property(_get_onerror, _set_onerror)

	#text
	def _get_text(self):
		return wrap(self.__get_instance_IHTMLScriptElement().text)
	def _set_text(self, value):
		self.__get_instance_IHTMLScriptElement().text = unwrap(value)
	text = property(_get_text, _set_text)

	#htmlFor
	def _get_htmlFor(self):
		return wrap(self.__get_instance_IHTMLScriptElement().htmlFor)
	def _set_htmlFor(self, value):
		self.__get_instance_IHTMLScriptElement().htmlFor = unwrap(value)
	htmlFor = property(_get_htmlFor, _set_htmlFor)

	#type
	def _get_type(self):
		return wrap(self.__get_instance_IHTMLScriptElement().type)
	def _set_type(self, value):
		self.__get_instance_IHTMLScriptElement().type = unwrap(value)
	type = property(_get_type, _set_type)

	#event
	def _get_event(self):
		return wrap(self.__get_instance_IHTMLScriptElement().event)
	def _set_event(self, value):
		self.__get_instance_IHTMLScriptElement().event = unwrap(value)
	event = property(_get_event, _set_event)

wrapperClasses['{3050F28B-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScriptElement
backWrapperClasses[IHTMLScriptElement] = '{3050F28B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLScriptElement2
#
class IHTMLScriptElement2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLScriptElement2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLScriptElement2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#charset
	def _get_charset(self):
		return wrap(self.__get_instance_IHTMLScriptElement2().charset)
	def _set_charset(self, value):
		self.__get_instance_IHTMLScriptElement2().charset = unwrap(value)
	charset = property(_get_charset, _set_charset)

wrapperClasses['{3050F828-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLScriptElement2
backWrapperClasses[IHTMLScriptElement2] = '{3050F828-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFrameBase
#
class IHTMLFrameBase(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLFrameBase(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFrameBase
		return Dispatch(self.__instance__.QueryInterface(kls))
	#src
	def _get_src(self):
		return wrap(self.__get_instance_IHTMLFrameBase().src)
	def _set_src(self, value):
		self.__get_instance_IHTMLFrameBase().src = unwrap(value)
	src = property(_get_src, _set_src)

	#name
	def _get_name(self):
		return wrap(self.__get_instance_IHTMLFrameBase().name)
	def _set_name(self, value):
		self.__get_instance_IHTMLFrameBase().name = unwrap(value)
	name = property(_get_name, _set_name)

	#scrolling
	def _get_scrolling(self):
		return wrap(self.__get_instance_IHTMLFrameBase().scrolling)
	def _set_scrolling(self, value):
		self.__get_instance_IHTMLFrameBase().scrolling = unwrap(value)
	scrolling = property(_get_scrolling, _set_scrolling)

	#frameSpacing
	def _get_frameSpacing(self):
		return wrap(self.__get_instance_IHTMLFrameBase().frameSpacing)
	def _set_frameSpacing(self, value):
		self.__get_instance_IHTMLFrameBase().frameSpacing = unwrap(value)
	frameSpacing = property(_get_frameSpacing, _set_frameSpacing)

	#marginWidth
	def _get_marginWidth(self):
		return wrap(self.__get_instance_IHTMLFrameBase().marginWidth)
	def _set_marginWidth(self, value):
		self.__get_instance_IHTMLFrameBase().marginWidth = unwrap(value)
	marginWidth = property(_get_marginWidth, _set_marginWidth)

	#marginHeight
	def _get_marginHeight(self):
		return wrap(self.__get_instance_IHTMLFrameBase().marginHeight)
	def _set_marginHeight(self, value):
		self.__get_instance_IHTMLFrameBase().marginHeight = unwrap(value)
	marginHeight = property(_get_marginHeight, _set_marginHeight)

	#border
	def _get_border(self):
		return wrap(self.__get_instance_IHTMLFrameBase().border)
	def _set_border(self, value):
		self.__get_instance_IHTMLFrameBase().border = unwrap(value)
	border = property(_get_border, _set_border)

	#frameBorder
	def _get_frameBorder(self):
		return wrap(self.__get_instance_IHTMLFrameBase().frameBorder)
	def _set_frameBorder(self, value):
		self.__get_instance_IHTMLFrameBase().frameBorder = unwrap(value)
	frameBorder = property(_get_frameBorder, _set_frameBorder)

	#noResize
	def _get_noResize(self):
		return wrap(self.__get_instance_IHTMLFrameBase().noResize)
	def _set_noResize(self, value):
		self.__get_instance_IHTMLFrameBase().noResize = unwrap(value)
	noResize = property(_get_noResize, _set_noResize)

wrapperClasses['{3050F311-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFrameBase
backWrapperClasses[IHTMLFrameBase] = '{3050F311-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLFrameBase2
#
class IHTMLFrameBase2(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLFrameBase2(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLFrameBase2
		return Dispatch(self.__instance__.QueryInterface(kls))
	#allowTransparency
	def _get_allowTransparency(self):
		return wrap(self.__get_instance_IHTMLFrameBase2().allowTransparency)
	def _set_allowTransparency(self, value):
		self.__get_instance_IHTMLFrameBase2().allowTransparency = unwrap(value)
	allowTransparency = property(_get_allowTransparency, _set_allowTransparency)

	#onload
	def _get_onload(self):
		return wrap(self.__get_instance_IHTMLFrameBase2().onload)
	def _set_onload(self, value):
		self.__get_instance_IHTMLFrameBase2().onload = unwrap(value)
	onload = property(_get_onload, _set_onload)

	#contentWindow
	def _get_contentWindow(self):
		return wrap(self.__get_instance_IHTMLFrameBase2().contentWindow)
	def _set_contentWindow(self, value):
		self.__get_instance_IHTMLFrameBase2().contentWindow = unwrap(value)
	contentWindow = property(_get_contentWindow, _set_contentWindow)

	#onreadystatechange
	def _get_onreadystatechange(self):
		return wrap(self.__get_instance_IHTMLFrameBase2().onreadystatechange)
	def _set_onreadystatechange(self, value):
		self.__get_instance_IHTMLFrameBase2().onreadystatechange = unwrap(value)
	onreadystatechange = property(_get_onreadystatechange, _set_onreadystatechange)

	#readyState
	def _get_readyState(self):
		return wrap(self.__get_instance_IHTMLFrameBase2().readyState)
	def _set_readyState(self, value):
		self.__get_instance_IHTMLFrameBase2().readyState = unwrap(value)
	readyState = property(_get_readyState, _set_readyState)

wrapperClasses['{3050F6DB-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLFrameBase2
backWrapperClasses[IHTMLFrameBase2] = '{3050F6DB-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# DispHTMLIFrame
#
class DispHTMLIFrame(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_DispHTMLIFrame(self, kls=None):
		if kls is None:
			kls = MSHTML.DispHTMLIFrame
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F51B-98B5-11CF-BB82-00AA00BDCE0B}'] = DispHTMLIFrame
backWrapperClasses[DispHTMLIFrame] = '{3050F51B-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IMarkupContainer
#
class IMarkupContainer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IMarkupContainer(self, kls=None):
		if kls is None:
			kls = MSHTML.IMarkupContainer
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F5F9-98B5-11CF-BB82-00AA00BDCE0B}'] = IMarkupContainer
backWrapperClasses[IMarkupContainer] = '{3050F5F9-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IMarkupPointer
#
class IMarkupPointer(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IMarkupPointer(self, kls=None):
		if kls is None:
			kls = MSHTML.IMarkupPointer
		return Dispatch(self.__instance__.QueryInterface(kls))
	#Right
	def Right(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().Right(*args))

	#IsRightOfOrEqualTo
	def IsRightOfOrEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().IsRightOfOrEqualTo(*args))

	#IsEqualTo
	def IsEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().IsEqualTo(*args))

	#MoveUnit
	def MoveUnit(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().MoveUnit(*args))

	#IsRightOf
	def IsRightOf(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().IsRightOf(*args))

	#IsLeftOfOrEqualTo
	def IsLeftOfOrEqualTo(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().IsLeftOfOrEqualTo(*args))

	#CurrentScope
	def CurrentScope(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().CurrentScope(*args))

	#MoveToPointer
	def MoveToPointer(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().MoveToPointer(*args))

	#Left
	def Left(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IMarkupPointer().Left(*args))

wrapperClasses['{3050F49F-98B5-11CF-BB82-00AA00BDCE0B}'] = IMarkupPointer
backWrapperClasses[IMarkupPointer] = '{3050F49F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISegment
#
class ISegment(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_ISegment(self, kls=None):
		if kls is None:
			kls = MSHTML.ISegment
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F683-98B5-11CF-BB82-00AA00BDCE0B}'] = ISegment
backWrapperClasses[ISegment] = '{3050F683-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IElementSegment
#
class IElementSegment(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IElementSegment(self, kls=None):
		if kls is None:
			kls = MSHTML.IElementSegment
		return Dispatch(self.__instance__.QueryInterface(kls))
wrapperClasses['{3050F68F-98B5-11CF-BB82-00AA00BDCE0B}'] = IElementSegment
backWrapperClasses[IElementSegment] = '{3050F68F-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISelectionServicesListener
#
class ISelectionServicesListener(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_ISelectionServicesListener(self, kls=None):
		if kls is None:
			kls = MSHTML.ISelectionServicesListener
		return Dispatch(self.__instance__.QueryInterface(kls))
	#GetTypeDetail
	def GetTypeDetail(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_ISelectionServicesListener().GetTypeDetail(*args))

	#OnChangeType
	def OnChangeType(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_ISelectionServicesListener().OnChangeType(*args))

wrapperClasses['{3050F699-98B5-11CF-BB82-00AA00BDCE0B}'] = ISelectionServicesListener
backWrapperClasses[ISelectionServicesListener] = '{3050F699-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# ISelectionServices
#
class ISelectionServices(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_ISelectionServices(self, kls=None):
		if kls is None:
			kls = MSHTML.ISelectionServices
		return Dispatch(self.__instance__.QueryInterface(kls))
	#AddElementSegment
	def AddElementSegment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_ISelectionServices().AddElementSegment(*args))

	#RemoveSegment
	def RemoveSegment(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_ISelectionServices().RemoveSegment(*args))

	#GetMarkupContainer
	def GetMarkupContainer(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_ISelectionServices().GetMarkupContainer(*args))

wrapperClasses['{3050F684-98B5-11CF-BB82-00AA00BDCE0B}'] = ISelectionServices
backWrapperClasses[ISelectionServices] = '{3050F684-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEditDesigner
#
class IHTMLEditDesigner(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLEditDesigner(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEditDesigner
		return Dispatch(self.__instance__.QueryInterface(kls))
	#PostHandleEvent
	def PostHandleEvent(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLEditDesigner().PostHandleEvent(*args))

	#PostEditorEventNotify
	def PostEditorEventNotify(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLEditDesigner().PostEditorEventNotify(*args))

	#TranslateAccelerator
	def TranslateAccelerator(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLEditDesigner().TranslateAccelerator(*args))

wrapperClasses['{3050F662-98B5-11CF-BB82-00AA00BDCE0B}'] = IHTMLEditDesigner
backWrapperClasses[IHTMLEditDesigner] = '{3050F662-98B5-11CF-BB82-00AA00BDCE0B}'

##############################
# IHTMLEditServices
#
class IHTMLEditServices(object):
	def __init__(self, item):
		self.__dict__['__instance__'] = item

	def __get_instance_IHTMLEditServices(self, kls=None):
		if kls is None:
			kls = MSHTML.IHTMLEditServices
		return Dispatch(self.__instance__.QueryInterface(kls))
	#MoveToSelectionAnchor
	def MoveToSelectionAnchor(self, *args):
		args = map(unwrap, args)
		return wrap(self.__get_instance_IHTMLEditServices().MoveToSelectionAnchor(*args))

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

