class Html(object):
    def __init__(self):
        self._cgi_content_type = "Content-type: text/html \n\n"
        self._charset = "utf-8"
        self._pageTitle = "VPNMGR | Página Inicial"

    
    def getContentType(self):
        return self._cgi_content_type

    
    def setPageTitle(self, title):
        self._pageTitle = title
    

    def getPageTitle(self):
        return self._pageTitle
    
    

