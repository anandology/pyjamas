import gtk
from pyjamas.HTTPRequest import HTTPRequest

def create_xml_doc(text):
    JS("""
try //Internet Explorer
  {
  xmlDoc=new ActiveXObject("Microsoft.XMLDOM");
  xmlDoc.async="false";
  xmlDoc.loadXML(text);
  }
catch(e)
  {
  try //Firefox, Mozilla, Opera, etc.
    {
    parser=new DOMParser();
    xmlDoc=parser.parseFromString(text,"text/xml");
    }
  catch(e)
  {
    return null;
  }
  }
  return xmlDoc;
  """)

class XMLloader:
    def __init__(self, panel):
        self.panel = panel

    def onCompletion(self, xmldoc):
        self.panel.doStuff(create_xml_doc(xmldoc))

    def onError(self, text, code):
        self.panel.onError(text, code)

    def onTimeout(self, text):
        self.panel.onTimeout(text)

class XMLload:

    def onModuleLoad(self):

        HTTPRequest().asyncGet(None, None,
                    "address_form.ui", 
                    XMLloader(self))

    def onError(self, text, code):
        # FIXME
        pass
          
    def onTimeout(self, text):
        # FIXME 
        pass
             
    def doStuff(self, xmldoc):

        b = gtk.Builder()
        
        b.add_from_string(xmldoc)

        for o in b.get_objects():
            o.show()
        gtk.main()

if __name__ == '__main__':

    #pyjd.setup("./public/XMLload.html")
    app = XMLload()
    app.onModuleLoad()
    #pyjd.run()

