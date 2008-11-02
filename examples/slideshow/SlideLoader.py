
class SlideListLoader:
    def __init__(self, panel, url):
        self.panel = panel

    def onCompletion(self, text):
        res = []
        for l in text.split('\n'):
            if not l:
                continue
            l = l.split(':')
            if len(l) != 2:
                continue
            res.append([l[0].strip(), l[1].strip()])
        self.panel.setSlides(res)

    def onError(self, text, code):
        self.panel.onError(text, code)

    def onTimeout(self, text):
        self.panel.onTimeout(text)


class SlideLoader:
    def __init__(self, panel, url):
        self.panel = panel

    def onCompletion(self, text):
        self.panel.setSlide(text)

    def onError(self, text, code):
        self.panel.onError(text, code)

    def onTimeout(self, text):
        self.panel.onTimeout(text)


