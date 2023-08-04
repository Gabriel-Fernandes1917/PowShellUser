from userInfos import inputs 
from userInfos import cleanInfors
from acessLetter import acessLetter

def UserAd():
    userData = inputs()
    path = open("./configs/distinguishedName.txt","r").read()
    longName = open("./configs/@userloginName.txt","r").read()
    

    script = f"PowerShell New-ADUser -Name '{userData[0]}' -UserPrincipalName '{userData[0]+longName}' -GivenName  '{userData[1]}' -Surname  '{userData[2]}' -DisplayName '{userData[3]}' -AccountPassword (ConvertTo-SecureString -AsPlainText '{userData[4]}' -force) -ChangePasswordAtLogon $true -Company '{userData[5]}' -Description '{userData[6]}' -Title '{userData[7]}' -Department '{userData[8]}' -Path '{path}' -Enabled $true"
    
    acessLetter(userData[3],userData[0], userData[4], userData[6])
    cleanInfors()
    return script


