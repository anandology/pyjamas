def log(text):
  JS("""
     console.log(text)
  """)

class MainTest:
  def onModuleLoad(self):
    s = StoringObject()
    s.save(getattr(self,'printable'))
    s.call()
  def printable(self,text):
    log(text)
    
class StoringObject:
  def save(self,func):
    self.func = func
  def call(self):
    self.func('Called from storing object')
  
