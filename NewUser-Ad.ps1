$splat = @{
    Name = 'DAVID.NERES'
    GivenName = "David"
    Surname = 'Souza Neres'
    DisplayName = "David Souza Neres"
    AccountPassword = (Read-Host -AsSecureString 'Senha123')
    ChangePasswordAtLogon = $true
    Company = "SEFA"
    Description = "559754545"
    Title = "Secretario de Gabinete"
    Department = "Gabinete Secretario"
    Path = "OU=Usuarios,DC=ramati,DC=local"
    Enabled = $true
}
New-ADUser @splat



 