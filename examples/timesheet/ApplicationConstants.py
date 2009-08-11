
# vim: set ts=4 sw=4 expandtab:

class Notification(object):

    STARTUP           = "startup"
    SHOW_DIALOG       = "showDialog"
    HELLO             = "hello"

    # Menu
    MENU_FILE_OPEN      = "menuFileOpen"
    MENU_FILE_SAVEAS    = "menuFileSaveAs"
    MENU_FILE_PREFS     = "menuFilePreferences"
    MENU_VIEW_EDIT      = "menuViewEdit"
    MENU_VIEW_SUM       = "menuViewSummary"
    MENU_HELP_CONTENTS  = "menuHelpContents"
    MENU_HELP_ABOUT     = "menuHelpAbout"

    FILE_LOADED         = "fileLoaded"
    EDIT_SELECTED       = "editMode"
    SUM_SELECTED        = "summaryMode"

    # Date picker
    DISPLAY_DAY         = "displayDay"
    PREV_DAY            = "previousDay"
    NEXT_DAY            = "nextDay"
    PREV_WEEK           = "previousWeek"
    NEXT_WEEK           = "nextWeek"
    DATE_SELECTED       = "dateSelected"

    # Time Grid
    CELL_SELECTED       = "cellSelected"
    CELL_UPDATED        = "cellUpdated"

