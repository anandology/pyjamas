class CustomButton (ButtonBase):

    def onClick(self, sender=None):
        """
        Called when the user finishes clicking on this button.
        The default behavior is to fire the click event to
        listeners. Subclasses that override onClickStart() should
        override this method to restore the normal widget display.
        """
        # Allow the click we're about to synthesize to pass through to the
        # superclass and containing elements. Element.dispatchEvent() is
        # synchronous, so we simply set and clear the flag within this method.
        self.allowClick = True
        
        # Mouse coordinates are not always available (e.g., when the click is
        # caused by a keyboard event).
        evt = None # we NEED to initialize evt, to be in the same namespace 
                   # as the evt *inside* of JS block
        JS("""
        // We disallow setting the button here, because IE doesn't provide the
        // button property for click events.
        
        // there is a good explanation about all the arguments of initMouseEvent
        // at: https://developer.mozilla.org/En/DOM:event.initMouseEvent
        
        evt = $doc.createEvent('MouseEvents');
        evt.initMouseEvent("click", true, true, $wnd, 1, 0, 0, 0, 0, false, 
                           false, false, false, 0, null);
        """)
        
        self.getElement().dispatchEvent(evt)
        self.allowClick = False
