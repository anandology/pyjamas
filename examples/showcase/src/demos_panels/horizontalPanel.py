"""
The ``ui.HorizontalPanel`` class is a panel that lays out its contents from
left to right.

It is often useful to call ``setSpacing(spacing)`` to add space between each of
the panel's widgets.  You can also call ``setHorizontalAlignment(alignment)``
and ``setVerticalAlignment(alignment)`` before adding widgets to control how
those widgets are aligned within the available space.  Alternatively, you can
call ``setCellHorizontalAlignment(widget, alignment)`` and
``setCellVerticalAlignment(widget, alignment)`` to change the alignment of a
single widget after it has been added.

Note that if you want to have different widgets within the panel take up
different amounts of space, don't call ``widget.setWidth(width)`` or
``widget.setHeight(height)`` as these are ignored by the panel.  Instead, call
``panel.setCellWidth(widget, width)`` and ``panel.setCellHeight(widget,
height)``.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.HorizontalPanel import HorizontalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui import HasAlignment

class HorizontalPanelDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        panel = HorizontalPanel()
        panel.setBorderWidth(1)

        panel.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        panel.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)

        part1 = Label("Part 1")
        part2 = Label("Part 2")
        part3 = Label("Part 3")
        part4 = Label("Part 4")

        panel.add(part1)
        panel.add(part2)
        panel.add(part3)
        panel.add(part4)

        panel.setCellWidth(part1, "10%")
        panel.setCellWidth(part2, "70%")
        panel.setCellWidth(part3, "10%")
        panel.setCellWidth(part4, "10%")

        panel.setCellVerticalAlignment(part3, HasAlignment.ALIGN_BOTTOM)

        panel.setWidth("100%")
        panel.setHeight("200px")

        self.add(panel)

