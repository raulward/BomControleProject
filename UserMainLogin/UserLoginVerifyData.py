import re
from vars import RE_EMAIL_PATTERN

class UserLoginVerify:
    
    def __init__(self, email, password):
        self._email = email
        self._password = password

    def emailLoginVerify(self):
        if re.match(RE_EMAIL_PATTERN, self._email):
            return self._email
        else:
            return False
        
    def passwordLoginVerify(self):
        if self._password != '':
            return self._password
        else: 
            return False
    
            
            

    