import customtkinter
from modcalc import *
import logging
from config_banco import database


logging.basicConfig(level=logging.INFO, filename="programa.txt", format="%(asctime)s | %(levelname)s | %(message)s")

Imc = CalculaImc()



def aux_imc():
    Imc.imc_calc(peso=Imc.ckeck_number(peso.get()), altura=Imc.ckeck_number(altura.get()))
    classificacao = Imc.classificacao(n=Imc.imc)
    categoria.configure(text=classificacao)
    numero.configure(text=f"{Imc.imc:.2f}")
    database.insert({"Peso":f"{peso.get()}", "Altura":f"{altura.get()}", "IMC":f"{Imc.imc}", "Categoria":f"{classificacao}"})

app = customtkinter.CTk()
app.geometry("630x370")
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)
app.iconbitmap("imc.ico")
app.title("IMC")
app.resizable(False,False)
#app.configure(fg_color="red")

fonteSize = customtkinter.CTkFont(size=18)
fonteSize2 = customtkinter.CTkFont(size=20)
fonteSize3 = customtkinter.CTkFont(size=36)
fonteSize4 = customtkinter.CTkFont(size=14)



msgDesc = customtkinter.StringVar(name="O índice de massa corporal (IMC)\né uma medida internacional usada para\ncalcular se uma pessoa está no peso ideal.")


frameDesc = customtkinter.CTkFrame(app, fg_color="transparent")
frameDesc.grid(row=0, column=0, sticky='w', padx=20, pady=10)

titulo = customtkinter.CTkLabel(frameDesc, text="Cálculo de IMC:", font=fonteSize)
titulo.grid(row=0, column=0, sticky="w", padx=10, pady=3)

desc = customtkinter.CTkLabel(frameDesc, text=msgDesc, justify="left", font=fonteSize4)
desc.grid(row=1, column=0, sticky="w", padx=10, pady=3)



frame = customtkinter.CTkFrame(app)
frame.grid(row=1, column=0, sticky='w', padx=20)

altura = customtkinter.CTkEntry(frame, placeholder_text="Ex: 1.75 - Altura", width=180, height=50)
altura.grid(row=0, column=0, padx=20, pady=10, sticky='w')

peso = customtkinter.CTkEntry(frame, placeholder_text="Ex: 70 - Peso", width=180, height=50)
peso.grid(row=1, column=0, padx=20, pady=10, sticky='w')
 

button = customtkinter.CTkButton(app, text="Calcular", fg_color="#Fb1717", width=100, height=40, command=aux_imc, font=fonteSize4)
button.grid(row=2, column=0, padx=20, pady=20, sticky="w")

frameRes = customtkinter.CTkFrame(app, width=300, height=310, fg_color="transparent")
frameRes.grid(row=0, column=1, padx=7, pady=5, rowspan=3)


frameLinha = customtkinter.CTkFrame(frameRes, width=300, height=310, border_width=1, border_color="red")
frameLinha.columnconfigure(0, weight=1)
frameLinha.rowconfigure(0, weight=1)
frameLinha.rowconfigure(1, weight=1)
frameLinha.grid(row=0, column=1)

categoria = customtkinter.CTkLabel(frameLinha, text="---", width=200, height=100, font=fonteSize2, bg_color="#Fb1717")
categoria.grid(row=0, column=0, pady=5, padx=5)

numero = customtkinter.CTkLabel(frameLinha, text="-0.0-", width=200, height=210,  font=fonteSize3, bg_color="#Fb1717")
numero.grid(row=1, column=0, pady=5, padx=5)



app.mainloop()
