# Get-ADUser -Filter 'Name -eq "LUIZA.MATOS"' ---> Check if user exists or not 

import subprocess

def checkUserExists(nameSplited):
    i = -1
    check = subprocess(f"""Get-ADUser -Filter 'Name -eq "{nameSplited[0].upper()}.{nameSplited[i].upper()}"'""", capture_output=True, text=True)
    if f"Name              : {nameSplited[0].upper()}.{nameSplited[i].upper()}" in check:
        f'{nameSplited[0].upper()}.{nameSplited[-1].upper()}'


    while f"Name              : {nameSplited[0].upper()}.{nameSplited[i].upper()}" in check:
        