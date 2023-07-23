
def inputs():
    fullnameUser = input("Digite o nome completo do usuário: ")

    nameSplited = fullnameUser.split(" ")
    
    userName = f'{nameSplited[0].upper()}.{nameSplited[-1].upper()}'
    givenName = f'{nameSplited[0]}'
    surname= ''
    for i in range(1, len(nameSplited)): surname = f'{surname} {nameSplited[i]}'
    surname = surname.replace(' ', '', 1)
    displayName = fullnameUser
    accountPassword = 'Senha123' 
    company = input("Qual empresa o usuário pertence ?: ")
    description = input("Digite a matrícula do usuário: ")
    title = input("Digite o cargo do usuário: ")
    department = input("Digite o Departamento do usuário: ")
    path = 'OU=Usuarios,DC=ramati,DC=local'

    return userName, givenName , surname ,displayName , accountPassword, company, description, title, department, path


def cleanInfors():
    fullnameUser = ''
    nameSplited = ''
    userName = ''
    givenName = ''
    surname = ''
    displayName = ''
    company = ''
    description = ''
    title = ''
    department = ''