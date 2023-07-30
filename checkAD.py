# Get-ADUser -Filter 'Name -eq "LUIZA.MATOS"' ---> Check if user exists or not 
import subprocess

def check(checkName):
    check = subprocess.run(f"""PowerShell Get-ADUser -identity {checkName}""", capture_output=True, text=True)
    return check.stderr

def checkUserExists(nameSplited):
    # nameSplited = "Gabriel Guilherme Santos Fernandes".split(" ")
    i = -1
    #print(check(nameSplited))
    # print(check.returncode)
    
    if "Cannot find an object with identity" in check(f"{nameSplited[0].upper()}.{nameSplited[i].upper()}"):
        #user not exists
        userName = f"{nameSplited[0].upper()}.{nameSplited[i].upper()}"
        return userName
    elif "Cannot find an object with identity" not in check(f"{nameSplited[0].upper()}.{nameSplited[i].upper()}"):
        while "Cannot find an object with identity" not in check(f"{nameSplited[0].upper()}.{nameSplited[i].upper()}"):
            i = i-1
        
        userName = f"{nameSplited[0].upper()}.{nameSplited[i].upper()}"
        return userName

    
# print(checkUserExists("x"))