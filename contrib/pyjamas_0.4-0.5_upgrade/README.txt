The ui classes have been restructured so that ui.py is not one whopping
great file.  javascript cache output is therefore dramatically reduced.

This tool takes classes, looks for "from pyjamas.ui import X,Y,Z"
and outputs:
from pyjamas.ui.X import X
from pyjamas.ui.Y import X
from pyjamas.ui.Z import Z

*except* for HasAlignment, HasVerticalAlignment and HasHorizontalAlignment


