# Copyright 2009 Daniel Carvalho <idnael@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from __pyjamas__ import JS

#???
def toJSON(jsarray):
    JS("return Object.toJSON(jsarray);")


# Used to convert the json structures returned from the javascript functions to python...

def gmapsJsObjectToPy(obj, fieldName, fields):
    JS("""
    //console.log("gmapsJsObjectToPy2 "+fieldName)

    if (! (fieldName in fields)) 
    {
      //console.log("eh nada")
      return obj;
    }
    else{
        action=fields[fieldName]
        //console.log("action="+action)

        if (action=='d')
        {
          //console.log("eh dict")
          var newobj=pyjslib({})
          for (var i in obj)
             // vai ficar disponivel como uma propriedade, no python!
             newobj[i]=Utils.gmapsJsObjectToPy(obj[i], i,fields );
          return newobj

        }
        else if (action=='l')
        {
          //console.log("eh list")
          var newobj=pyjslib.List([])
          for (var i in obj)
             newobj.append(Utils.gmapsJsObjectToPy(obj[i],fieldName+"[]",fields ));
          return newobj
        }
        else
        {
          //console.log("eh function")
          return action(obj)
        }
    }
    """)


#def gmapsJsObjectToPy(obj, fieldName, listFields, dictFields):
#    JS("""
#    //console.log("gmapsJsObjectToPy "+fieldName)
#    if (dictFields.indexOf(fieldName)!=-1) 
#    {
#      //console.log("eh dict")
#      var newobj=pyjslib({})
#      for (var i in obj)
#         // vai ficar disponivel como uma propriedade, no python!
#         newobj[i]=Utils.gmapsJsObjectToPy(obj[i], i,listFields, dictFields );
#      return newobj
#
#    }
#    else if (listFields.indexOf(fieldName)!=-1) 
#    {
#      //console.log("eh list")
#      var newobj=pyjslib.List([])
#      for (var i in obj)
#         newobj.append(Utils.gmapsJsObjectToPy(obj[i],fieldName+"[]",listFields, dictFields ));
#      return newobj
#    }
#    else
#    {
#      //console.log("eh nada")
#      return obj;
#    }
#    """)


# this function converts a python dictionary into a javascript equivalent.
# It is to be used in the functions that creates objects like MapOptions or MapTypeControlOptions

# For instance:
# def MapOptions(**params):
#    return dictToJs(params)

# It treats a special case, that is, when MapOptions is called without arguments,
# dict is undefined and the for loop will give an exception.
def dictToJs(dict):
    #if dict:
    #   gives always True... so I don't know how to detect if dict is defined or not...
    #   but print dict gives undefined...

    obj=JS("{}")
    try:
        for key in dict: 
            value=dict[key]
            JS("obj[key]=value")
    except:
        pass

    return obj



# LISTENERS

def createListenerMethods(obj):
   obj.addListener = __addListener
   obj.removeListener = __removeListener
   obj.clearListeners = __clearListeners
   obj.clearInstanceListeners = __clearInstanceListeners

   #obj.dumpListeners = __dumpListeners # para debug

   obj.__listeners={} #__ !
    
def __dumpListeners():
    self=JS("this")
    print "DUMP"
    for eventName in self.__listeners:
        print "  "+eventName
        for list in self.__listeners[eventName]:
            print "    "+str(list)

def __addListener(eventName,callback):
    self=JS("this")

    list=JS("""
       $wnd.google.maps.event.addListener(this, eventName, function(event) {
         callback(event);
       });
    """)

    if eventName in self.__listeners:
        self.__listeners[eventName].append(list)
    else:
        self.__listeners[eventName]=[list]

    return list

def __removeListener(list):
    self=JS("this")

    for eventName in self.__listeners:
        if list in self.__listeners[eventName]:
            JS("""$wnd.google.maps.event.removeListener(list);""")
            self.__listeners[eventName].remove(list)
            return
    # nothing to remove, the listener specified doesn't exist or does not belong to this object

def __clearListeners(eventName):
    self=JS("this")

    JS("""$wnd.google.maps.event.clearListeners(this,eventName);""")
    if eventName in self.__listeners:
        del self.__listeners[eventName]

def __clearInstanceListeners():
    self=JS("this")

    JS("""$wnd.google.maps.event.clearInstanceListeners(this);""")
    self.__listeners={}
