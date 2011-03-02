""" Pyjamas UI BuilderWidget: takes a PyJsGlade builder spec
    and creates a widget.

Copyright (C) 2010 Luke Kenneth Casson Leighton <lkcl@lkcl.net>

Create a BuilderWidget as follows:

from pyjamas.builder.Builder import Builder
from pyjamas.ui.BuilderWidget import BuilderWidget

either:

class ApplicationEventReceivingClassWhatever:

    def onSomeRandomClickThing(self, sender):
        print "some random widget was clicked, it was this one:", sender

    app = ApplicationEventReceivingClassWhatever()
    b = Builder()
    xml = "<?xml .... ?><pyjsglade> .... </pyjsglade>"
    bw = BuilderWidget(Builder=b,
                       EventReceiver=app,
                       BuilderText=xml_file,
                       InstanceName="WidgetListedInXmlFile")

or:

    app = ApplicationEventReceivingClassWhatever()
    xml = "<?xml .... ?><pyjsglade> .... </pyjsglade>"
    b = Builder(xml)
    bw = BuilderWidget(Builder=b,
                       EventReceiver=app,
                       InstanceName="WidgetListedInXmlFile")

or:

class BuilderWidgetWithIntegratedEventHandling(BuilderWidget):
    def onSomeRandomClickThing(self, sender):
        print "some random widget was clicked, it was this one:", sender

    b = Builder(xml)
    bw = BuilderWidgetWithIntegratedEventHandling(Builder=b,
                       InstanceName="WidgetListedInXmlFile")

or:

    b = Builder()
    bw = BuilderWidgetWithIntegratedEventHandling(Builder=b,
                       BuilderText=xml_file,
                       InstanceName="WidgetListedInXmlFile")

"""

from pyjamas.ui.Composite import Composite


class BuilderWidget(Composite):

    def __init__(self, **kwargs):
        
        self.b = None
        self.text = None
        self.instance_name = None
        self.event_receiver = None
        Composite.__init__(self, **kwargs)

    def setBuilderText(self, text):
        self.text = text
        self.autoCreateInstance()

    def setBuilder(self, builder):
        self.b = builder
        self.autoCreateInstance()

    def setEventReceiver(self, event_receiver):
        """ sets the instance where the events named in the builder
            will be received (callbacks called).
            passing in None will set the event receiver to be this
            widget.
        """
        self.event_receiver = event_receiver or self
        self.autoCreateInstance()

    def setInstanceName(self, instance_name):
        self.instance_name = instance_name
        self.autoCreateInstance()

    def autoCreateInstance(self):
        """ when all the required arguments have been set, the
            widget instance will be created.  it's done this way
            because **kwargs goes through to pyjamas.ui.Applier,
            and the order in which the setXXX functions will be called
            cannot be determined or guaranteed (kwargs is a dictionary).
        """
        if self.b and self.text:
            self.b.setText(self.text)
        if not self.b or not self.instance_name or not self.event_receiver:
            return
        if not self.b.builder_text:
            return
        widget = self.b.createInstance(self.instance_name, self.event_receiver)
        self.initWidget(widget)

