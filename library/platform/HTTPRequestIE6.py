class HTTPRequest:
    def doCreateXmlHTTPRequest(self):
        JS("""
        return new ActiveXObject("Msxml2.XMLHTTP");
        """)

