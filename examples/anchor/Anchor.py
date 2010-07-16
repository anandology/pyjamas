import pyjd
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.Image import Image
from pyjamas.ui.Anchor import Anchor

if __name__ == '__main__':
    pyjd.setup("Anchor.html")

    root = RootPanel()
    image_url = "http://www.dcuktec.com/static/images/logo.png"
    image = Image(image_url)
    anchor = Anchor(Widget=image)
    anchor.href.set('http://www.dcuktec.com')
    root.add(anchor)

    pyjd.run()

