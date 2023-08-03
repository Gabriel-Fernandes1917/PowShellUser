from docx import Document
import os

def acessLetter(iname, iuserName, isenha, imatricula):
    documento = Document('CartaDeAcesso.docx')


    #print(documento.paragraphs)
    nome = f"{iname}"
    userName = f"{iuserName}"
    senha = f"{isenha}"
    matricula = f"{imatricula}"
    email = f"{iuserName.lower()}@sefa.pa.gov.br"

    for paragrafo in documento.paragraphs:
        # print(paragrafo.text)
        paragrafo.text = paragrafo.text.replace("NOME COMPLETO", nome)
        paragrafo.text = paragrafo.text.replace("USUARIO DE REDE", userName)
        paragrafo.text = paragrafo.text.replace("SENHA DE REDE", senha)
        paragrafo.text = paragrafo.text.replace("USUARIO DE EMAIL@sefa.pa.gov.br", email)
        paragrafo.text = paragrafo.text.replace("MATRICULA", matricula)


    documento.save(f"""Carta de Acesso - {nome}.docx""")

