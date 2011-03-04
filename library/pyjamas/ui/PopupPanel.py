from gwt.ui.PopupPanel import (
    DOM,
    Factory,
    KeyboardListener,
    MouseListener,
    PopupPanel,
    RootPanel,
    SimplePanel,
    Window,
)


class PopupPanel(PopupPanel):

    def __init__(self, autoHide=False, modal=True, rootpanel=None, glass=False,
                 **kwargs):
        super(PopupPanel, self).__init__(
            autoHide=autoHide,
            modal=modal,
            **kwargs)

        if rootpanel is None:
            rootpanel = RootPanel()
        self.rootpanel = rootpanel

        if glass:
            self.setGlassEnabled(True)
            if 'GlassStyleName' in kwargs:
                self.setGlassStyleName(kwargs.pop('GlassStyleName'))

Factory.registerClass('pyjamas.ui.PopupPanel', 'PopupPanel', PopupPanel)
