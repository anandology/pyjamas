
class Location:
    def getHash(self):
        return unescape(self.location.hash)
    
    def getSearch(self):
        return unescape(self.location.search)
