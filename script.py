
def UserAd():
    #name = input("Digite o nome do arquivo txt")

    script = "PowerShell New-ADUser -Name 'DAVID.NERES' -GivenName  'David' -Surname  'Souza Neres' -DisplayName 'David Souza Neres' -AccountPassword (ConvertTo-SecureString -AsPlainText 'Senha123' -force) -ChangePasswordAtLogon $true -Company 'SEFA' -Description '559754545' -Title 'Secretario de Gabinete' -Department 'Gabinete Secretario' -Path 'OU=Usuarios,DC=ramati,DC=local' -Enabled $true"

    return script

