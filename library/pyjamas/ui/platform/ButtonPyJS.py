class Button(ButtonBase):

    def adjustType(self, button):
        JS("""
        if (button.type == 'submit') {
            try { button.setAttribute("type", "button"); } catch (e) { }
        }
        """)

