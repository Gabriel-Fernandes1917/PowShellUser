from datetime import date
from checkAD import checkUserExists

def password():
    data = date.today().strftime('%d-%m-%Y').split("-")
    year = data[-1].split('20')
    passData = data[0]+data[1]+year[-1]
    
    return passData
    


def inputs():
    fullnameUser = input("Digite o nome completo do usuário: ")

    nameSplited = fullnameUser.split(" ")
    
    userName = checkUserExists(nameSplited)
    givenName = f'{nameSplited[0]}'
    surname= ''
    for i in range(1, len(nameSplited)): surname = f'{surname} {nameSplited[i]}'
    surname = surname.replace(' ', '', 1)
    displayName = fullnameUser
    accountPassword = f'Sef@{password()}' 
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