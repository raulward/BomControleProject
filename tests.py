from UserMainLogin.UserLoginGetData import UserLoginGetData
from UserMainLogin.UserLoginVerifyData import UserLoginVerify


from UserMainLogin.UserLoginGetData import UserLoginGetData
from UserMainLogin.UserLoginVerifyData import UserLoginVerify

from webdriver.ChromeWebDriver import initializeDriver

while True:
    # Instanciando a classe para obter os dados de login
    login_data = UserLoginGetData()
    email = login_data.getLoginEmail()
    password = login_data.getLoginPassword()

    # Instanciando a classe para verificar os dados de login
    verifyUser = UserLoginVerify(email, password)
    
    emailResult = verifyUser.emailLoginVerify()
    if emailResult:
        print(f'O endereço de e-mail "{emailResult}" é válido.')
    else:
        print(f'O endereço de e-mail "{email}" é inválido.')
        continue
   
    passwordResult = verifyUser.passwordLoginVerify()

    if passwordResult:
        print(f'A senha "{passwordResult}" é válida.')
        break
    else:
        print(f'A senha é inválida.')

    # Pergunta se o usuário deseja tentar novamente
    userOption = input("Deseja tentar novamente? (s/n): ")
    if userOption.lower() != 's':
        break

initializeDriver()



