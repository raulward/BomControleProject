# Classe responsável por obter os dados de login 
class UserLoginGetData():
    def __init__(self) -> None:
        pass

    # Definindo a função que irá inputar o e-mail
    def getLoginEmail(self):
       self._email = input("Digite seu e-mail de acesso Bom Controle: ")
       return self._email.lower()
     
    # Definindo a função que irá inputar a senha 
    def getLoginPassword(self):
        self._password = input("Digite sua senha de acesso ao Bom Controle: ")
        return self._password.lower()