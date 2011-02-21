'''
@since on 17 Dec 2010

@author: me@carlroach.com

    @summary: Manager for handling a web browser's History, <title> & bread crumbs within a Pyjamas application.

    Catches the onHistoryChanged() notification of Pyjamas and converts it into a series of objects 

    An app needs to be structured such that any state a user can bookmark
    can be reached programmatically. Optionally, if <title> and/or  breadcrumb are employed
    then every point these changes also need to be reached in the same manner.

    @attention: Managing history in an app isn't straightforward.
    Most likely BuoyServive will be difficult to retrofit as any history code would be.

    See example Navigate.py application for sample usage code.
'''

from pyjamas import History
from pyjamas.Timer import Timer

class Flare(object):
    '''
    A navigable state within an app
    A series of flares marks a specific route through an app

    Used by BuoyService to record/follow a route through an application
    '''
    def __init__(self):
        self.params = {}
        self.flare = None

    def get_parameters(self):
        return self.params

    def set_parameters(self, params):
        self.params = params

class Buoy(object):
    '''
    a navigable point within an application
    '''
    def __init__(self, parent, title, *args, **kwargs):
        '''
            @param parent: parent of this new buoy
            @type parent: Buoy
            @param title: title of page
            @type title: string
            @param crumb: breadcrumb text of page
            @type crumb: string
            @param kwargs: attribute/value pair {attribute:value}
            @type kwargs: dict
        '''
        self.parent = parent
        self.flare = None
        self.params = {}
        for arg in args:
            self.add_parameters(arg)
        crumb = kwargs['crumb'] if 'crumb' in kwargs else None
        self.title = title
        self.crumb = crumb if crumb else title

    def new(self, title, *args, **kwargs):
        '''
            when an app has navigated to a new state create a buoy to mark the occasion

            @param title: title of page
            @type title: string
            @param crumb: breadcrumb text of page
            @type crumb: string
            @param kwargs: attribute/value pair {attribute:value}
            @type kwargs: dict
            @return: a new Buoy tied to this buoy
            @rtype: Buoy
        '''
        return Buoy(self, title, *args, **kwargs)

    def checkpoint(self):
        '''
        Checks Buoy for a flare
        If not found drops Buoy to mark end state 

        @return: any parameters of flare or {}
        @rtype: dict
        '''
        params = self.navigate()
        if not params:
            self.drop_buoy()
        return params

    def navigate(self):
        '''
        Checks buoy for a flare.
        Buoy is not an end app state

        @return: any parameters of flare or {}
        @rtype: dict
        '''
        if not self.parent._is_service() and self.parent.flare:
            self.flare = self.parent.flare.flare
        else:
            self.flare = self.parent.flare

        self.parent.flare = None # allow no followers

        return self.flare.get_parameters() if self.flare else {}

    def end(self):
        '''
        Checks buoy for a flare.
        Regardless, Buoy is app end state

        @return: any parameters of flare or {}
        @rtype: dict
        '''
        params = self.navigate()
        if params:
            self.update_buoy()
        else:
            self.drop_buoy()
        return params

    def plan(self):
        '''
        Looks ahead at next flare and returns its parameters without navigating the next Buoy.
        Useful for a parent Buoy to determine which route through an App to follow.

        @return: any parameters of flare or {}
        @rtype: dict
        '''
        if not self._is_service() and self.flare:
            flare = self.flare.flare
        else:
            flare = self.flare
        return flare.get_parameters() if flare else {}

    def drop_buoy(self):
        '''
        update browser History and UI
        '''
        self._get_service().new_item(self.construct_token())
        self.notify()

    def update_buoy(self):
        '''
        defines this page's name and crumb label and updates UI
        update's UI for browser window title & bread crumbs

        @param title: title of page
        @type title: string
        @param crumb: breadcrumb text of page
        @type crumb: string
        '''
        self.notify()

    def notify(self):
        '''
        sends event so that app can update <title> and bread crumbs
        if listeners are set
        '''
        titles = self._get_titles()
        service = self._get_service()
        service.onTitlesChanged(titles)
        crumbs = self._get_breadcrumbs()
        service.onBreadcrumbsChanged(crumbs)

    def set_parameters(self, params):
        '''
        scratch any existing parameters and replace with params

        params are used to create tokens (/about/history=all) & to drive apps

        @type params: dict
        @param params: {'name' : value} set value to None for valueless parameters 
        '''
        self.params = params

    def add_parameters(self, params):
        '''
        add/update existing parameters

        @type params: dict
        @param: params: {'name' : value}
        '''
        self.params.update(params)

    def _get_titles(self):
        '''
        a list of buoy title strings.
        used to generate list for setting of <title> content 

        @return: list of titles
        @rtype: list
        '''
        titles = []
        obj = self
        while obj:
            titles.insert(0, obj.title)
            obj = obj.parent
        return titles

    def _get_breadcrumbs(self):
        '''
        a list of dicts.
        used to generate list for setting bread crumbs

        a dict has a 'label' & an anchor 'token'

        use the dict to display a bread crumb trail such as: here > there

        prefix  a 'home' link as required

        @return: breadcumbs from this buoy up
        @rtype: dict
        '''
        breadcrumbs = []
        obj = self
        while obj:
            if obj.crumb and len(obj.crumb):
                breadcrumbs.insert(0, {'label' : obj.crumb,
                                       'token' : obj.construct_token()})
            obj = obj.parent
        return breadcrumbs

    @staticmethod
    def construct_event(params):
        '''
        every buoy has one or more parameters which define an event.
        an event serialises buoy.params which is a dict of attribute/value pairs.

        serialising produces: a1=v1&a2/a3/a4=v4

        @param params: dict of attribute/value pairs. Note: value can be None
        @type params: dict
        '''
        event = ''
        for param in params:
            if params[param]:
                event += '%s=%s&' % (param, params[param])
            else:
                event += '%s&' % param
        if event[-1] == '&':
            event = event[:-1]
        return event

    def construct_token(self):
        '''
        every Buoy but the first has a parent (which is BuoyService)

        token takes form p1=v1&p2=v2/p3&p4=v4
        at the top of the parents is a BuoyService
        skip up through buoys & put together token

        override for an alternative format

        @return: history token
        @rtype: string
        '''
        token = ''
        obj = self
        while not obj._is_service():
            p = ''
            if len(obj.params):
                p += '/' + Buoy.construct_event(obj.params)
            token = p + token
            obj = obj.parent

        if token and token[0] == '/':
            token = token[1:]

        return token

    @staticmethod
    def deconstruct_command(command):
        '''
        @type command: string
        @param command: attribute=value
        @rtype: dict
        @return: dict of one command
        '''
        attributes = command.split('=')
        if len(attributes) == 1:
            return {attributes[0] : None}
        else:
            return {attributes[0] : attributes[1]}

    @staticmethod
    def deconstruct_token(token):
        '''
        parse token string into events

        token takes form p1=v1&p2=v2/p3&p4=v4

        token element terminology:
            token: event/event/event
            event: command&command&command
            command: attribute=value

        method placed in Buoy rather than BuoyService as it is the mirror of construct_token()

        override for an alternative format 

        @type token: string
        @param token: a History token
        @return: list of dict parameters 
        @rtype: list
        '''
        events = []
        for event in token.split('/'):
            parsed_command = {}
            for command in event.split('&'):
                parsed_command.update(Buoy.deconstruct_command(command))
            events.append(parsed_command)
        return events

    def _is_service(self):
        return hasattr(self, 'cast_off')

    def _get_service(self):
        '''
        skip up through buoys' parents to return instance of BuoyService

        @return: instance of the BuoyService
        @rtype: BuoyService
        '''
        obj = self
        while not obj._is_service():
            obj = obj.parent
        return obj

class BuoyService(Buoy):
    '''
        The BuoyService approach
        ------------------------
        Buoys mark each state a user can pass or stop at in an app
        As a user interacts with an app new buoys are created, attached to the buoy above them in the site navigation

        When a user arrives at the end state in a navigation BuoyService fires events off to app
        enabling it to update <title> text and a bread crumb trial

        When a user hits back/forward buttons in a browser or picks a bookmark to the app
        BuoyService creates a series of Flare objects marking the route of Buoys required to be followed
        BuoyService fires an onFlare() event to app for it to update its state

        Usage:Setup
        -----------
            In an App startup: create a BuoyService:

            def onModuleLoad(self)
                ...
                service = BuoyService('App Name')
                service.set_titles_listener(self) # optional
                service.set_breadcrumbs_listener(self) # optional
                service.add_flare_listener(self)

            and add handlers for buoy events:

                def onFlare(self, service, prefixes):
                    pass service through the code to update UI

                def onBreadCrumbsChanged(self, crumbs)
                    update app's bread crumbs UI

                def onTitlesChanged(self, titles):
                    create a string using list of titles and separators
                    and call Window.setTitle()

        Usage:General
        -------------
            Create a new Buoy at every state a user can navigate to.
            Pass 'service' to the first level of states to call service.new()

            Pass returned Buoy of call to service.new() to next level of states

            there are three types of navigable points in an app:

            1. has a state that can be displayed to user or can lead to another state

              buoy = parent_buoy.new('settings', {'open' : None})

              params = buoy.checkpoint()

              if params: ... refine state based upon params. pass buoy to code of lower-level state

              if params is {} then this is an end state of the app

            2. is an end state in an app's hierarchy state

              article_ref = ...

              buoy = parent_buoy.new('Article', {'a' : article_ref})

              buoy.end()

            3. is a state that is never a landing state but is a decision point

              buoy = parent_buoy.new('Account', {'account' : None})

              params = buoy.navigate()

              ... route user based upon params. if params is {} then route to a default state

        @note: History tokens
        ---------------------
        Creating a hierarchy of Buoy instances will enable BuoyService to generate tokens in the form below.
        e.g.,
            #agent&user=1&tab=team/sort=alpha/all/english

        e.g.,
            #view/credit=all&height=1024
    '''
    def __init__(self, title, crumb=None):
        '''
        create one BuoyService per application

        @param title: Application title 
        @type title: string
        @param crumb: First bread crumb string. Defaults to title
        @type crumb: string
        '''
        Buoy.__init__(self, None, title, crumb=crumb)
        self.timer_count = -1
        self.listeners = []
        self.title_listener = None
        self.breadcrumbs_listener = None

    def add_flare_listener(self, listener):
        '''
        register an instance to receive onFlare() calls
        yes add_flare_watcher makes a better name but for consistency with Pyjamas we're listening :)

        Apps can set-up multiple flare listeners but one is suffice for most

        @param listener: class instance supporting onBuoysChange() method
        @type listener: class instance
        '''
        self.listeners.append(listener)

    def remove_flare_listener(self, listener):
        '''
        @param listener: buoys listener
        @type listener: class instance
        '''
        self.listeners.remove(listener)

    def set_titles_listener(self, listener):
        '''
        installs a sole listener to enable App to update browser title string

        @param listener: class instance supporting onTitlesChanged() method
        @type listener: class instance
        '''
        self.title_listener = listener

    def unset_titles_listener(self):
        '''
        remove sole listener
        '''
        self.title_listener= None

    def set_breadcrumbs_listener(self, listener):
        '''
        installs a sole listener to enable App to update a bread crumb trail

        @param listener: class instance supporting onBreadcrumbsChanged() method
        @type listener: class instance 
        '''
        self.breadcrumbs_listener = listener

    def unset_breadcrumb_listener(self):
        '''
        remove sole listener
        '''
        self.breadcrumbs_listener = None

    def cast_off(self):
        '''
        sets up notifications to call App when page history changes.

        @note: set-up Application's listeners and then call cast_off()
        which will fire off the appropriate events to your app.
        '''
        self.timer_count = 0
        self._set_history_listener(True, on_period=1)
        token = History.getToken()
        if len(token):
            self.onHistoryChanged(token)

    def onTitlesChanged(self, titles):
        '''
        call App listener to update the Browser Window title

        @param titles: list of page titles from App title down to lowest page title
        @type titles: list of string
        '''
        if self.title_listener:
            self.title_listener.onTitlesChanged(titles)

    def onBreadcrumbsChanged(self, crumbs):
        '''
        call App listener to update the site's bread crumb trail

        [{'label' : crumb-title, 'token' : crumb-hash-token},]

        @param crumbs: list of crumb titles & hash tokens from top-most page down to lowest site page
        @type crumbs: list of dicts
        '''
        if self.breadcrumbs_listener:
            self.breadcrumbs_listener.onBreadcrumbsChanged(crumbs)

    def onHistoryChanged(self, token):
        '''
        Called when user has picked a bookmark or an item from browser's history list
        or clicked on a hyperlink to the application

        @param token: hash token
        @type token: string

        Only the basics of the app may have been initiated so we need to find the handler for this token
        so objects, if needs be, can be created.

        @note: if an URL end in a hash token with no further content the token passed in will '#' rather than empty
        we catch this special case for consistent handling
        '''
        flares, events = self._build_flares(self, token)

        if len(events):
            first_event_keys = [] if token=='#' else events[0].keys()
            for listener in self.listeners:
                listener.onFlare(flares, first_event_keys)

    def new_item(self, token):
        '''
        updates the current URL's hash token. 
        disables the calling of BuoyService's onHistoryChanged() when a Buoy adds a new item

        @param token: hash token
        @type token: string

        when an app is placed in a state by user interaction it calls Buoy.drop_anchor()
        which calls BuoyService.new_item(). The subsequent call to History.newItem() will call
        BuoyService.onHistoryChanged() but as the app is already in the correct state
        there is such requirement. So we smoother it by disabling BuoyService's history listener
        until after the new item is added. 
        '''
        self._set_history_listener(False)
        History.newItem(token)
        self._set_history_listener(True)

    def _build_flares(self, service, token):
        '''
        using ServiceBuoy build a route & events based on a token
        
        @param service: app's ServiceBuoy instance
        @type service: serviceBuoy
        @param token: hash token
        @type token: string

        @return: the BuoyService instance
        @rtype: BuoyService
        @return: event list of flare route
        @rtype: list of events
        '''
        obj = service
        events = Buoy.deconstruct_token(token)
        for event in events:
            obj.flare = Flare()
            obj.flare.set_parameters(event)
            obj = obj.flare
        return service, events

    def _set_history_listener(self, on, on_period=251):
        '''
        pyjamas/library/pyjamas/History.py is checking every 250ms if URL has changed
        
        By default, BuoyService checks every 250+1ms before turning its listener back on.
        An initial call in BuoyService() set-up needs to set on_period to 1 for immediate listening

        Rapid UI-interaction can lead to multiple nested calls.
        A count is kept to control when to add/remove the sole history listener.
        If a count wasn't kept then History will wobble
        '''
        if on:
            self.timer = Timer(on_period, self)
        else:
            if self.timer_count == 1:
                History.removeHistoryListener(self)
            self.timer_count -= 1

    def onTimer(self, id):
        '''
        turn history listener on once all 'off' periods have completed 
        '''
        self.timer_count += 1
        if self.timer_count == 1:
            History.addHistoryListener(self)
