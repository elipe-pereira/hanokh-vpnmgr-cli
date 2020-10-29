class Login(object):
    def __init__(self):
        self._username = "Anonymous"
        self._password = " "

    def setUsername(self, username):
        self._username = username
    
    def getUsername(self):
        return self._username

    def setPassword(self, password):
        self._password = password
    
    def getPassword(self):
        return self._password
    
    def isValidUser(self, username, password):
        if self._username == username and self._password == password:
            return True
        
        else:
            return False
    