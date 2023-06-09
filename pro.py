import requests
from tkinter import *


def pegar_temperatura():
    API_KEY = "83dd637ae41af132c9428d25b5427133"
    cidade = 'Salvador'
    LINK = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&lang=pt_br"

    requisicao = requests.get(LINK)

    requisicao_dic = requisicao.json()
    descricao = requisicao_dic["weather"][0]["description"]
    temperatura = requisicao_dic["main"]["temp"] - 273.15
    texto_previsao["text"] = descricao, temperatura


# interface grafica

janela = Tk()
janela.title("Previsão do Tempo")
janela.geometry("200x200")
texto_orientacao = Label(janela, text="Previsão do Tempo em Salvador")
texto_orientacao.grid(column=0, row=0, padx=10, pady=10)
botao = Button(janela, text="Clique aqui!", command=pegar_temperatura)
botao.grid(column=0, row=1, padx=10, pady=10)
texto_previsao = Label(janela, text="")
texto_previsao.grid(column=0, row=2)
janela.mainloop()
