from gwt.ui.DialogBox import (
    DOM,
    DialogBox,
    Factory,
    FlexTable,
    GlassWidget,
    HTML,
    HasHorizontalAlignment,
    HasVerticalAlignment,
    PopupPanel,
)


class DialogBox(DialogBox):

    def __init__(self, autoHide=None, modal=True, centered=False,
                 **kwargs):
        super(DialogBox, self).__init__(
            autoHide=autoHide,
            modal=modal,
            **kwargs)
        self.centered = centered

    def onWindowResized(self, width, height):
        super(DialogBox, self).onWindowResized(width, height)
        if self.centered:
            self.centerBox()

    def show(self):
        super(DialogBox, self).show()
        if self.centered:
            self.centerBox()

Factory.registerClass('pyjamas.ui.DialogBox', 'DialogBox', DialogBox)
