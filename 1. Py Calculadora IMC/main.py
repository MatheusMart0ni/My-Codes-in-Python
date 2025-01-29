import customtkinter as ctk

######## Cores ########
cor0 = "#2C3E50"  # Azul Escuro para texto e rótulos (profissional e moderno)
cor1 = "#ECF0F1"  # Cinza Claro para fundo e texto (limpo e legível)
cor2 = "#3498DB"  # Azul para botões (calmo e moderno)
cor3 = "#E5E8E8"  # Cinza Claro para fundo da janela
cor4 = "#16A085"  # Verde Água para detalhes (fresco e estiloso)
cor5 = "#95A5A6"  # Cinza para texto secundário

janela = ctk.CTk()
janela.title("Calculadora de IMC")
janela.geometry('440x540')
janela.configure(bg=cor3)

# Dividindo a Janela
quadro_superior = ctk.CTkFrame(janela, width=400, height=90, corner_radius=15)
quadro_superior.grid(row=0, column=0, sticky='nsew', padx=20, pady=20)

quadro_inferior = ctk.CTkFrame(janela, width=400, height=380, corner_radius=15)
quadro_inferior.grid(row=1, column=0, sticky='nsew', padx=20, pady=20)

#Configurando o quadro superior
nome_app = ctk.CTkLabel(quadro_superior, text='Calculadora de IMC', 
                                        text_color=cor4, 
                                        anchor='center', 
                                        font=('Helvetica', 30, 'bold'),
                                        )
nome_app.place(x=0, y=25, relwidth=1)


#Função para calcular IMC
def calcular():
    peso = float(e_peso.get())
    altura = float(e_altura.get()) ** 2
    resultado = peso / altura

    if resultado < 18.6:
        l_texto_resultado.configure(text='Seu IMC é: Abaixo do peso')
    elif resultado >= 18.5 and resultado < 24.9:
        l_texto_resultado.configure(text='Seu IMC é: Normal')
    elif resultado >= 25 and resultado < 29.9:
        l_texto_resultado.configure(text='Seu IMC é: Sobrepeso')
    else:
        l_texto_resultado.configure(text='Seu IMC é: Obesidade')

    l_resultado.configure(text="{:.{}f}".format(resultado,2))

#Configurando o quadro inferior
l_peso = ctk.CTkLabel(quadro_inferior, text='Digite o seu peso (Kg):', 
                                        text_color=cor1, 
                                        font=('Helvetica', 14),
                                        )
l_peso.grid(row=0, column=0, sticky='nw', padx=15, pady=15)

e_peso = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16),justify='center', corner_radius=12)
e_peso.grid(row=0, column=1, sticky='nsew', padx=15, pady=15)

l_altura = ctk.CTkLabel(quadro_inferior, text='Digite a sua altura (m):', 
                                        text_color=cor1, 
                                        font=('Helvetica', 14),
                                        )
l_altura.grid(row=1, column=0, sticky='nw', padx=15, pady=15)

e_altura = ctk.CTkEntry(quadro_inferior, width=180, font=('Helvetica', 16),justify='center', corner_radius=12)
e_altura.grid(row=1, column=1, sticky='nsew', padx=15, pady=15)

l_resultado = ctk.CTkLabel(quadro_inferior, text='---', width=5, height=1,
                                        text_color=cor1, 
                                        font=('Helvetica', 32, 'bold'),
                                        anchor='center',
                                        corner_radius=12
                                        )
l_resultado.grid(row=2, column=0, columnspan=2, padx=15, pady=30)

l_texto_resultado = ctk.CTkLabel(quadro_inferior, text='',
                                        text_color=cor1, 
                                        font=('Helvetica', 16),
                                        anchor='center',
                                        )
l_texto_resultado.grid(row=3, column=0, columnspan=2, padx=15, pady=15)


b_calcular = ctk.CTkButton(quadro_inferior, text='Calcular', width=180, 
                                            height=50, 
                                            font=('Helvetica', 16,'bold'),
                                            hover_color="#2980B9",
                                            corner_radius=12,
                                            command=calcular)

b_calcular.grid(row=34, column=0, columnspan=2, padx=15, pady=25)



janela.mainloop()