from pyjamas.ui.RootPanel import RootPanel
from pyjamas.ui.VerticalPanel import VerticalPanel
from pyjamas.ui.Label import Label
from pyjamas.ui.Button import Button
from SWFUpload import SWFUpload, Settings, SWFUploadInterface
from pyjamas import log


class SWFUploadExample(SWFUploadInterface):
    
    def onModuleLoad(self):
        self.panel = VerticalPanel()
        self.panel.setSpacing(10)
        RootPanel().add(self.panel)
        
        self.swfUpload = self.getSWFUpload()
        self.panel.add(self.swfUpload)
        
        self.fileids = []
        self.queue = VerticalPanel()
        self.panel.add(self.queue)
        
        startButton = Button('Start Upload')
        startButton.addClickListener(getattr(self, 'onStartUpload'))
        self.panel.add(startButton)
        
        self.progress = Label()
        self.panel.add(self.progress)
    
    def getSWFUpload(self):
        swfUpload = SWFUpload()
        swfUpload.setSettings(self.getSettings())
        swfUpload.setID('SWFUploadPanel')
        return swfUpload
        
    def showQueue(self):
        self.queue.clear()
        for fileid in self.fileids:
            file = self.swfUpload.getFile(fileid)
            label = Label('%s (%s Bytes)' % (file.name, file.size))
            self.queue.add(label)
        
    def getSettings(self):
        settings = Settings()
        settings.setURL('upload.html')
        
        settings.setButtonHTML('<span class="uploadButton">add Files</span>')
        settings.setButtonCSS('.uploadButton { font-size: 12; font-weight: bold; }')
        settings.setButtonWidth(60)
        settings.setButtonHeight(25)
        settings.setButtonTopPadding(10)
        settings.setButtonLeftPadding(5)
        
        settings.setEventListener(self)
        settings.setFlashURL('swf/swfupload.swf')
        
        return settings
    
    def onStartUpload(self):
        #log.writebr('Starting Upload')
        self.swfUpload.startUpload()
        
    """
    SWFUpload Events
    """
    
    def swfUploadLoaded(self):
        #log.writebr('swfUploadLoaded')
        pass
        
    def uploadProgress(self, file, bytesLoaded, totalBytes):
        self.progress.setText('%s - %s of %s uploaded' % (file.name, bytesLoaded, totalBytes))
        
    def uploadError(self, file, errorCode, message):
        log.writebr('uploadError: %s, %s' % (errorCode, message))
    
    def uploadSuccess(self, file, receivedResponse, serverData):
        self.fileids.remove(file.id)
        self.showQueue()
        
    def uploadComplete(self, file):
        #log.writebr('uploadComplete: %s' % file.name)
        if len(self.fileids) > 0:
            self.swfUpload.startUpload()
        else:
            self.progress.setText('All files uploaded')
        
    def fileDialogStart(self):
        #log.writebr('fileDialogStart')
        pass
        
    def fileQueued(self, file):
        #log.writebr('fileQueued: %s' % file.name)
        self.fileids.append(file.id)
        
    def fileQueueError(self, file, errorCode, message):
        log.writebr('fileQueueError: %s, %s' % (errorCode, message))
        
    def fileDialogComplete(self, sel, qu, tqu):
        #log.writebr('fileDialogComplete: %s, %s, %s' % (sel, qu, tqu))
        self.showQueue()
        
    def uploadStart(self, file):
        #log.writebr('uploadStart')
        # Do something before the upload starts, and return True to start the upload
        return True
        
if __name__ == '__main__':
    app = SWFUploadExample()
    app.onModuleLoad()
    