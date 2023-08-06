from docx import Document


def acessLetter(iname, iuserName, isenha, imatricula):
    documento = Document('CartaDeAcesso.docx')
    emailDomin = open("./configs/emialDomin.txt","r").read()

   
    nome = f"{iname}"
    userName = f"{iuserName}"
    senha = f"{isenha}"
    matricula = f"{imatricula}"
    email = f"{iuserName.lower()}{emailDomin}"

    for paragrafo in documento.paragraphs:
       
        paragrafo.text = paragrafo.text.replace("NOME COMPLETO", nome)
        paragrafo.text = paragrafo.text.replace("USUARIO DE REDE", userName)
        paragrafo.text = paragrafo.text.replace("SENHA DE REDE", senha)
        paragrafo.text = paragrafo.text.replace("USUARIO DE EMAIL", email)
        paragrafo.text = paragrafo.text.replace("MATRICULA", matricula)
    

    documento.save(f"""Carta de Acesso - {nome}.docx""")

