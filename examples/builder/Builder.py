import pyjd # this is dummy in pyjs.
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.builder.Builder import Builder

xmlfile = """\
<properties>
	<property name="puremvc" value="False"/>
	<property name="xmlfile" value="ws.xml"/>
	<property name="version" value="0.1"/>
	<property name="name" value="ws"/>
	<property name="codefile" value="ws.py"/>
</properties>
<components>
	<component id="AppFrame" name="VerticalPanel" type="Panel" index="None" left="241" top="377" visible="True">
		<properties name="elements">
		</properties>
		<properties name="layout">
			<property name="spacing" value="0"/>
			<property name="padding" value="0"/>
		</properties>
		<properties name="common">
			<property name="name" value="AppFrame"/>
		</properties>
		<components>
			<component id="txbTextBoxSurname" name="TextBox" type="Widget" index="0">
				<properties name="common">
					<property name="name" value="txbTextBoxSurname"/>
				</properties>
			</component>
		</components>
	</component>
</components>
"""

if __name__ == '__main__':
    pyjd.setup("public/Builder.html?fred=foo#me")
    b = Builder(xmlfile)
    i = b.createInstance("AppFrame")
    RootPanel().add(i)
    pyjd.run()
