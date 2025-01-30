#importando Tkinter
import tkinter
from tkinter import *
from tkinter import ttk

#cores 
co0 = "#444466"  # Preta
co1 = "#feffff"  # branca / white
co2 = "#6f9fbd"  # azul
co3 = "#38576b"  # valor
co4 = "#403d3d"  # letra
co5='#e89613'    # laranja

janela = Tk()
janela.title('')
janela.geometry ('400x310')
janela.configure(bg=co1)

style = ttk.Style()
style.theme_use('clam')
ttk.Separator(janela, orient=HORIZONTAL).grid(row=0, columnspan=1, ipadx=190)

#Dividindo a janela em 2 frames

Frame_cima = Frame(janela, width=400, height=60, bg=co1, pady=0, padx=0)
Frame_cima.grid(row=1, column=0)

Frame_baixo = Frame(janela, width=400, height=300, bg=co1, pady=12, padx=20)
Frame_baixo.grid(row=2, column=0, sticky=NW)


#Configurando frame cima
app_nome = Label(Frame_cima, text="Conversor de base numérica", relief=FLAT, anchor='center', font=('Arial 20'), bg=co2, fg=co1)
app_nome.place(x=10, y=15)


#Função Converter
def converter():
    #função para converter qualquer número em uma base para o seu correspondente em Decimal
    número = e_valor.get()
    base = combo.get()

    def número_para_decimal(número, base):
        # o número decimal correspondente
        decimal = int(número, base)

        binário = bin(decimal)
        octal = oct(decimal)
        hexadecimal = hex(decimal)

        l_binario['text'] = str(binário[2:])
        l_octal['text'] = str(octal[2:]) 
        l_decimal['text'] = str(decimal)
        l_hexadecimal['text'] = str(hexadecimal[2:].upper())

    número = e_valor.get()
    base = combo.get()

    #definindo o valor da base
    if base == 'Binário':
        base =2
    elif base == 'Octal':
        base =8
    elif  base == 'Decimal':
        base =10
    else:
        base =16

    # chamando a função
    número_para_decimal(número, base)


#Configurando frame baixo

bases =['Binário','Octal','Decimal','Hexadecimal']   
combo = ttk.Combobox(Frame_baixo, width=12, justify=CENTER, font=('Arial 12 bold'))
combo['values'] = (bases)
combo.place(x=15, y=10)

e_valor = Entry(Frame_baixo, width=9, justify='center', font=("", 13), highlightthickness=1, relief='solid')
e_valor.place(x=160, y=10)

b_converter = Button(Frame_baixo, command=converter, text="Converter", relief=RAISED, overrelief=RIDGE, font=('Ivy 8 bold'), bg=co1, fg=co4)
b_converter.place(x=247, y=10)

l_binario = Label(Frame_baixo, text="Binário", width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co1)
l_binario.place(x=35, y=60) 
l_binario = Label(Frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_binario.place(x=170, y=60) 

l_octal = Label(Frame_baixo, text="Octal", width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co1)
l_octal.place(x=35, y=100) 
l_octal = Label(Frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_octal.place(x=170, y=100) 

l_decimal = Label(Frame_baixo, text="Decimal", width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co1)
l_decimal.place(x=35, y=140) 
l_decimal = Label(Frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_decimal.place(x=170, y=140) 

l_hexadecimal = Label(Frame_baixo, text="Hexadecimal", width=12, relief=FLAT, anchor='nw', font=('Verdana 13 bold'), bg=co5, fg=co1)
l_hexadecimal.place(x=35, y=180) 
l_hexadecimal = Label(Frame_baixo, text="", width=13, relief=FLAT, anchor='center', font=('Verdana 13'), fg=co4)
l_hexadecimal.place(x=170, y=180) 

janela.mainloop()