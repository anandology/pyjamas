from pyjamas.ui.Button import Button
from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.HTML import HTML
from pyjamas import Window
from pyjamas import DOM
#import pyjamas.dynamicajax.js
#import dtest.js

def greet(sender):
    body = DOM.getElementById("idbody")
    html = DOM.getInnerHTML(body)
    Window.alert(html)

    JS("""
       /*other.test.Fred();*/
       test_fn();

        """)

JS("""
// ImportListener that triggers the Examples page's initialization once all
// required modules are ready for use.
function isPageReady(moduleName)
{  
  if(  "undefined" == typeof other.test)
     return;

  Ajile.RemoveImportListener(isPageReady);
  isPageReady = true;
  testImportListener();
}  

// Add listener to observe any import/include events.

// Tests whether all imports were successful.
function testImportListener()
{  
  var status = isPageReady == true ? ' ' : " NOT ";

  alert( "Import Listener test was" + status +"successful! "
       + "All required modules have"+ status +"been imported.");
}  
""")

class AjaxTest:

    ClickMe = "Click me"

    def onModuleLoad(self):
        b = Button(ClickMe, greet)
        RootPanel().add(b)
        #pyjs_ajax_dlink(None, "test.js", "test_fn()")
        pyjs_ajax_eval("test.js", "test_fn()")
        JS("""
        /*
            other = function() {};
            other.test = function() {};

            Namespace("other.test");

           Include("other.test.Fred.js");
           Import("other.test");
           Ajile.AddImportListener(isPageReady);
        */
            """)
