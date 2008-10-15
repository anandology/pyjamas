from ui import TabPanel, HasAlignment, Image, VerticalPanel, RootPanel

class Tabs:

    def onModuleLoad(self):

        red = Image("images/user_red.png")
        red.setStyleName('gwt-TabBarItem')
        self.fTabs = TabPanel()
        self.fTabs.add(self.createImage("rembrandt/JohannesElison.jpg"), red)
        self.fTabs.add(self.createImage("rembrandt/SelfPortrait1640.jpg"), "1640")
        self.fTabs.add(self.createImage("rembrandt/LaMarcheNocturne.jpg"), "1642")
        self.fTabs.add(self.createImage("rembrandt/TheReturnOfTheProdigalSon.jpg"), "1662")
        self.fTabs.selectTab(0)

        self.fTabs.setWidth("100%")
        self.fTabs.setHeight("100%")

        RootPanel().add(self.fTabs)

    def createImage(self, imageUrl):
        image = Image(imageUrl)
        image.setStyleName("ks-images-Image")
        
        p = VerticalPanel()
        p.setHorizontalAlignment(HasAlignment.ALIGN_CENTER)
        p.setVerticalAlignment(HasAlignment.ALIGN_MIDDLE)
        p.add(image)

        return p
