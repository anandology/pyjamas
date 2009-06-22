import pyjslib

def makeUrlDict(s):
    dict = {}
    pairs = s.split("&")
    for pair in pairs:
        if len(pair) < 3: continue
        kv = pair.split("=",1)
        dict[kv[0]] = kv[1]
    return dict

def makeUrlStringFromDict(d):
    pairs = []
    for k,v in d.iteritems():
        pairs.append(k+"="+v)
    return "&".join(pairs)

class Location:
    """
        Retrieve this class by calling Window.getLocation().
        
        This provides a pyjs wrapper for the current location,
        with some utility methods for convenience.
        
    """
    def __init__(self, location):
        self.location = location
        self.searchDict = None
    
    def getHash(self):
        return self.location.props.hash
    
    def getHashDict(self):
        if not self.hashDict or self.hashDictHash != self.getHash():
            self.hashDictHash = self.getHash()
            self.hashDict = makeUrlDict(self.getHash()[1:])
        return self.hashDict
    
    def getHost(self):
        return self.location.props.host
    
    def getHostname(self):
        return self.location.props.hostname
    
    def getHref(self):
        return self.location.props.href
    
    def getPageHref(self):
        """
        Return href with any search or hash stripped
        """
        href = self.location.props.href
        if href.find("?"): href = href.split("?")[0]
        if href.find("#"): href = href.split("#")[0]
        return href
    
    def getPathname(self):
        return self.location.props.pathname
    
    def getPort(self):
        return self.location.props.port
    
    def getProtocol(self):
        return self.location.props.protocol
        
    def getSearch(self):
        return ""+self.location.props.search
    
    def getSearchDict(self):
        if pyjslib.isString(self.location):
            return {}
        if not self.searchDict:
            self.searchDict = makeUrlDict(self.getSearch()[1:])
        return self.searchDict

    def getSearchVar(self, key):
        searchDict = self.getSearchDict()
        return searchDict[key]
    
    def reload(self):
        self.location.props.reload()
        
    def setHref(self, href):
        self.location.props.href = href

    def setSearch(self, search):
        self.location.props.search = search
        
    def setSearchDict(self, searchDict):
        self.setSearch(makeUrlStringFromDict(searchDict))
        
    def setHash(self, hash):
        self.location.props.hash = hash
        
    def setHashDict(self, hashDict):
        self.setHash(makeUrlStringFromDict(hashDict))
        

