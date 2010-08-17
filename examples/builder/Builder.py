import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.builder.Builder import Builder

xmlfile = """\
<?xml version="1.0" encoding="UTF-8"?>
<pyjsglade>
<properties>
	<property name="puremvc" value="False" />
	<property name="xmlfile" value="ws.xml" />
	<property name="version" value="0.1" />
	<property name="name" value="ws" />
	<property name="codefile" value="ws.py" />
</properties>
<components>
	<component id="AppFrame" name="VerticalPanel" type="Panel" index="None" left="241" top="377" visible="True">
		<properties name="elements">
		</properties>
		<properties name="layout">
			<property name="spacing" value="0" />
			<property name="padding" value="0" />
		</properties>
		<properties name="common">
			<property name="name" value="AppFrame" />
		</properties>
		<components>
			<component id="txbHTML" name="Label" module="pyjamas.ui.Label" type="Widget" index="0">
				<properties name="widget">
					<property name="label" value="txbHTML" />
				</properties>
				<properties name="common">
					<property name="name" value="txbHTML" />
				</properties>
				<properties name="events">
					<property name="onClick" value="onHTMLClicked" />
					<property name="onMouseMove" value="onHTMLMouseMoved" />
				</properties>
			</component>
			<component id="txbTextBoxSurname" name="TextBox" type="Widget" index="1">
				<properties name="common">
					<property name="name" value="txbTextBoxSurname" />
				</properties>
				<properties name="events">
					<property name="onFocus" value="onInputBoxFocus" />
				</properties>
			</component>
		</components>
	</component>
</components>
</pyjsglade>
"""

class EventTest(object):

    def onHTMLMouseMoved(self, sender, x, y):
        print "moved", sender, x, y

    def onInputBoxFocus(self, sender):
        print "input box focus", sender

    def onHTMLClicked(self, sender):
        print "clicked", sender

if __name__ == '__main__':
    pyjd.setup("public/Builder.html?fred=foo#me")
    b = Builder(xmlfile)
    et = EventTest()
    i = b.createInstance("AppFrame", et)
    #print dir(et)
    #print dir(i.txbHTML)
    RootPanel().add(i)
    pyjd.run()
