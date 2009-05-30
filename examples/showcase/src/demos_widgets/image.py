"""
The ``ui.Image`` class is used to display an image.

The ``Image`` class can display any image that is specified by a URL.  This can
be an image stored somewhere on the internet, or alternatively you can store an
image in the "public" directory within your application's source folder, and
then access it using a relative URL, as shown below.

In this example, the image file named "myImage.jpg" is stored inside the
"images" sub-directory, which is in the "public" directory within the
application's main source directory.

As well as passing the image URL to the initialiser, you can call ``setURL()``
to change the image being displayed at any time.  You can also call
``addClickListener()`` to add a listener function to be called when the user
clicks on the image.
"""
from pyjamas.ui.SimplePanel import SimplePanel
from pyjamas.ui.Image import Image
from pyjamas import Window

class ImageDemo(SimplePanel):
    def __init__(self):
        SimplePanel.__init__(self)

        # We display the "myImage.jpg" file, stored in the "public/images"
        # directory, where "public" is in the application's source directory.

        img = Image("images/myImage.jpg")
        img.addClickListener(getattr(self, "onImageClicked"))
        self.add(img)


    def onImageClicked(self, sender=None):
        Window.alert("Stop that!")

