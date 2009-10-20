from pyjamas.ui.Grid import Grid

_logger = None

class LoggerCls(Grid):

    def __init__(self):

        Grid.__init__(self)

        self.targets=[]
        self.targets.append("app")
        #self.targets.append("ui")
        self.resize(len(self.targets)+1, 2)
        self.setBorderWidth("1px")
        self.counter=0
        
        self.setHTML(0, 0, "<b>Log</b>")
        self.setText(1, 0, "app")
        for i in range(len(self.targets)):
            target=self.targets[i]
            self.setText(i+1, 0, target)

    def addTarget(self, target):
        self.targets.append(target)
        self.resize(len(self.targets)+1, 2)
        self.setText(len(self.targets), 0, target)
        return self.targets.index(target)
        
    def write(self, target, message):
        self.counter+=1
        
        if target=='':
            target='app'
        try:
            target_idx=self.targets.index(target)
        except ValueError:
            target_idx = -1
        
        # add new target
        if target_idx<0:
            target_idx=self.addTarget(target)
        
        target_row=target_idx+1     
        old_text=self.getHTML(target_row, 1)
        log_line="%d: " % self.counter + message

        if old_text=='&nbsp;':
            new_text=log_line            
        else:
            new_text=old_text + "<br>" + log_line
        self.setHTML(target_row, 1, new_text) 

def Logger(target="", message=""):
    global _logger
    # make sure there is only one instance of this class
    if not _logger:
        _logger = LoggerCls()

    _logger.write(target, message)
    
    return _logger
