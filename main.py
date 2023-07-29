import subprocess
import os
from script import UserAd 



systemRespon = subprocess.run(UserAd(), capture_output=True, text=True)



if "The term 'New-ADUser' is not recognized as the name of a cmdlet, function, script file, or operable" in systemRespon.stderr:

    print("Não Foi possivel acessar o AD no servidor")

    print("Error \n",systemRespon.stderr)
if "The specified account already exists" in systemRespon.stderr:
    print("Usuário já existe")
    print("Error \n", systemRespon.stderr)
    input("Deseja Usar o nome e penultimo nome ?")
    

# "The term 'New-ADUser' is not recognized as the name of a cmdlet," in systemRespon.stderr
