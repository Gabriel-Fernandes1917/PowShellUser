from userInfos import inputs 
from userInfos import cleanInfors
from acessLetter import acessLetter

def UserAd():
    userData = inputs()
    
    script = f"PowerShell New-ADUser -Name '{userData[0]}' -UserPrincipalName '{userData[0]}@ramati.local' -GivenName  '{userData[1]}' -Surname  '{userData[2]}' -DisplayName '{userData[3]}' -AccountPassword (ConvertTo-SecureString -AsPlainText '{userData[4]}' -force) -ChangePasswordAtLogon $true -Company '{userData[5]}' -Description '{userData[6]}' -Title '{userData[7]}' -Department '{userData[8]}' -Path '{userData[9]}' -Enabled $true"
    
    acessLetter(userData[3],userData[0], userData[4], userData[6])
    cleanInfors()
    return script

