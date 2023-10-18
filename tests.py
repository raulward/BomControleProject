from UserMainLogin.UserLoginGetData import UserLoginGetData
from UserMainLogin.UserLoginVerifyData import UserLoginVerify


from UserMainLogin.UserLoginGetData import UserLoginGetData
from UserMainLogin.UserLoginVerifyData import UserLoginVerify

while True:
    # Instanciando a classe para obter os dados de login
    login_data = UserLoginGetData()
    email = login_data.getLoginEmail()
    password = login_data.getLoginPassword()

    # Instanciando a classe para verificar os dados de login
    verify_user = UserLoginVerify(email, password)
    
    email_result = verify_user.emailLoginVerify()
    if email_result:
        print(f'O endereço de e-mail "{email_result}" é válido.')
    else:
        print(f'O endereço de e-mail "{email}" é inválido.')
        continue
   
    password_result = verify_user.passwordLoginVerify()

    if password_result:
        print(f'A senha "{password_result}" é válida.')
        break
    else:
        print(f'A senha é inválida.')

    # Pergunta se o usuário deseja tentar novamente
    tentar_novamente = input("Deseja tentar novamente? (s/n): ")
    if tentar_novamente.lower() != 's':
        break

