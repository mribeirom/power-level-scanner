import customtkinter
from PIL import Image

class View():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("600x600")
        self.root.title('Força Saiyajin')
        self.root.minsize(500, 500)


        self.estrutura_imagem(self.root)

        # Frame borda preta da interface
        self.frame_borda = customtkinter.CTkFrame(self.root,
                                                  width=500,
                                                  height=500,
                                                  corner_radius=12,
                                                  fg_color="#000000")
        self.frame_borda.pack(padx=45, pady=45)

        self.frame_borda.grid_rowconfigure(0, weight=1)
        self.frame_borda.grid_columnconfigure(0, weight=1)

        # Frame fundo azul da interface
        self.frame_fundo_azul = customtkinter.CTkFrame(self.frame_borda,
                                                       width=500,
                                                       height=500,
                                                       corner_radius=12,
                                                       fg_color="#66ccff")
        self.frame_fundo_azul.pack(padx=3, pady=3)
        self.frame_fundo_azul.grid_propagate(False)

        self.frame_fundo_azul.grid_rowconfigure(0, weight=1)
        self.frame_fundo_azul.grid_columnconfigure(0, weight=1)

        self.tela_login(self.frame_fundo_azul)
        self.tela_registro(self.frame_fundo_azul)
        self.tela_menu(self.frame_fundo_azul)
        self.tela_perfil(self.frame_fundo_azul)
        self.tela_calculo(self.frame_fundo_azul)
        self.tela_resultado(self.frame_fundo_azul)

        self.mostrar_tela_login()

        self.root.mainloop()

    def estrutura_imagem(self, container):
        container_imagem = customtkinter.CTkFrame(container, width=500, fg_color="transparent")
        container_imagem.pack(pady=(30, 0))

        imagem = Image.open('vegeta_weight_training.png')
        imagem_ctk = customtkinter.CTkImage(light_image=imagem, size=(150, 150))

        self.label_imagem = customtkinter.CTkLabel(container_imagem, image=imagem_ctk, text="")
        self.label_imagem.pack()

    def mostrar_tela_login(self):
        self.container_login.tkraise()

    def mostrar_tela_registro(self):
        self.container_registro.tkraise()

    def mostrar_tela_menu(self):
        self.container_menu.tkraise()

    def mostrar_tela_perfil(self):
        self.container_perfil.tkraise()

    def mostrar_tela_calculo(self):
        self.container_calculo.tkraise()
    
    def mostrar_tela_resultado(self):
        self.container_resultado.tkraise()

    def tela_login(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_login = customtkinter.CTkFrame(frame_fundo_azul,
                                                      width=500,
                                                      height=500,
                                                      fg_color="transparent")
        self.container_login.grid(row=0,
                                  column=0,
                                  sticky='nsew',
                                  padx=20,
                                  pady=(30, 0))
        
        self.container_login.grid_columnconfigure(1, weight=1)
        

        # Label Email
        self.label_email_login = customtkinter.CTkLabel(self.container_login,
                                                  text=f"EMAIL",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_email_login.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry Email
        self.entry_email_login = customtkinter.CTkEntry(self.container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_email_login.grid(row=0, column=1, sticky="ew" , pady=(0, 20))

        # Label Senha
        self.label_senha = customtkinter.CTkLabel(self.container_login,
                                                  text=f"SENHA",
                                                  text_color="black",
                                                  anchor="w",
                                                  font=("Arial", 30, "bold"))
        self.label_senha.grid(row=1, column=0, sticky="w", padx=(0, 20))

        # Entry Senha
        self.entry_senha = customtkinter.CTkEntry(self.container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_senha.grid(row=1, column=1, sticky="ew")

        # Botão para logar
        self.button_logar = customtkinter.CTkButton(self.container_login,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='LOGIN',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF",
                                              command=self.mostrar_tela_menu)
        
        self.button_logar.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        self.label_registro = customtkinter.CTkButton(self.container_login,
                                                     text=f"FAÇA SEU CADASTRO AQUI",
                                                     text_color='#000000',
                                                     fg_color="transparent",
                                                     hover_color="#66ccff",
                                                     font=("Arial", 15, "bold"),
                                                     command=self.mostrar_tela_registro)
        
        self.label_registro.grid(row=3, column=0, columnspan=2, pady=(10, 0))

        
    
    def tela_registro(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_registro = customtkinter.CTkFrame(frame_fundo_azul,
                                                         width=500,
                                                         height=500,
                                                         fg_color="transparent")
        self.container_registro.grid(row=0,
                                     column=0,
                                     sticky='nsew',
                                     padx=20,
                                     pady=(30, 0))
        
        self.container_registro.grid_columnconfigure(1, weight=1)

        # Label nome
        self.label_nome = customtkinter.CTkLabel(self.container_registro,
                                                 text=f"NOME",
                                                 text_color="black",
                                                 anchor="w", font=("Arial", 30, "bold"))
        
        self.label_nome.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry nome
        self.entry_nome = customtkinter.CTkEntry(self.container_registro,
                                                 font=("Arial", 25),
                                                 fg_color="#66ccff",
                                                 border_color="#000000",
                                                 border_width=3)
        
        self.entry_nome.grid(row=0, column=1, sticky="ew" , pady=(0, 20))

        # Label Email
        self.label_email_registro = customtkinter.CTkLabel(self.container_registro,
                                                  text=f"EMAIL",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_email_registro.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry Email
        self.entry_email_registro = customtkinter.CTkEntry(self.container_registro,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_email_registro.grid(row=1, column=1, sticky="ew" , pady=(0, 20))

        # Label Senha
        self.label_senha = customtkinter.CTkLabel(self.container_registro,
                                                  text=f"SENHA",
                                                  text_color="black",
                                                  anchor="w",
                                                  font=("Arial", 30, "bold"))
        self.label_senha.grid(row=2, column=0, sticky="w", padx=(0, 20))

        # Entry Senha
        self.entry_senha = customtkinter.CTkEntry(self.container_registro,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_senha.grid(row=2, column=1, sticky="ew")

        # Botão para registrar
        self.button_registro = customtkinter.CTkButton(self.container_registro,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='REGISTRAR',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF",
                                              command=self.mostrar_tela_login)
        
        self.button_registro.grid(row=3, column=0, columnspan=2, pady=(20, 0))

        self.label_login = customtkinter.CTkButton(self.container_registro,
                                                     text=f"FAÇA SEU LOGIN AQUI",
                                                     text_color='#000000',
                                                     fg_color="transparent",
                                                     hover_color="#66ccff",
                                                     font=("Arial", 15, "bold"),
                                                     command=self.mostrar_tela_login)
        
        self.label_login.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        

    def tela_menu(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_menu = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_menu.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.container_menu.grid_columnconfigure(0, weight=1)
        

        #Botão Calcular
        self.button_calcular = customtkinter.CTkButton(self.container_menu,
                                                     corner_radius=5,
                                                     height=60,
                                                     width=230,
                                                     text=f'CALCULAR',
                                                     text_color="#000000",
                                                     fg_color='transparent',
                                                     font=("Arial", 30, "bold"),
                                                     command=self.mostrar_tela_calculo)
        self.button_calcular.grid(row=0, column=0, pady=(30, 0))

        # Botão Perfil
        self.button_perfil = customtkinter.CTkButton(self.container_menu,
                                                     corner_radius=5,
                                                     height=60,
                                                     width=230,
                                                     text=f'PERFIL',
                                                     text_color="#000000",
                                                     fg_color='transparent',
                                                     font=("Arial", 30, "bold"))
        self.button_perfil.grid(row=1, column=0, pady=(0, 0))


        # Botão Sair
        self.button_sair = customtkinter.CTkButton(self.container_menu,
                                                     corner_radius=5,
                                                     height=60,
                                                     width=230,
                                                     text=f'SAIR',
                                                     text_color="#000000",
                                                     fg_color='transparent',
                                                     font=("Arial", 30, "bold"),
                                                     command=self.mostrar_tela_login)
        self.button_sair.grid(row=2, column=0, pady=(0, 0))



        self.trocar_cor_button(self.button_calcular)
        self.trocar_cor_button(self.button_perfil)
        self.trocar_cor_button(self.button_sair)


    def tela_perfil(self, frame_fundo_azul):
        self.container_perfil = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_perfil.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.label_nome = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'NOME')
        self.label_nome.grid()

    def tela_calculo(self, frame_fundo_azul):
        self.container_calculo = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_calculo.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.container_calculo.grid_columnconfigure(1, weight=1)
        
        # Label exercicio
        self.label_exercicio = customtkinter.CTkLabel(self.container_calculo,
                                                 text=f"EXERCICIO",
                                                 text_color="black",
                                                 anchor="w", font=("Arial", 30, "bold"))
        
        self.label_exercicio.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Combobox exercicio
        self.entry_exercicio = customtkinter.CTkComboBox(self.container_calculo,
                                                         values=['SUPINO',
                                                                 'LEVANTAMENTO TERRA',
                                                                 'AGACHAMENTO'],
                                                         font=("Arial", 25),
                                                         fg_color="#66ccff",
                                                         border_color="#000000",
                                                         border_width=3,
                                                         dropdown_hover_color='#66ccff')
        
        self.entry_exercicio.grid(row=0, column=1, sticky="ew" , pady=(0, 20))

        # Label peso
        self.label_peso = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"PESO",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_peso.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry peso
        self.entry_peso = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_peso.grid(row=1, column=1, sticky="ew" , pady=(0, 20))

        # Label repetição
        self.label_repeticao = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"REPETIÇÃO",
                                                  text_color="black",
                                                  anchor="w",
                                                  font=("Arial", 30, "bold"))
        self.label_repeticao.grid(row=2, column=0, sticky="w", padx=(0, 20))

        # Entry repetição
        self.entry_repeticao = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_repeticao.grid(row=2, column=1, sticky="ew")

        # Botão para calcular
        self.button_calcular = customtkinter.CTkButton(self.container_calculo,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='CALCULAR',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF",
                                              command=self.mostrar_tela_resultado)
        
        self.button_calcular.grid(row=3, column=0, columnspan=2, pady=(20, 0))

    def tela_resultado(self, frame_fundo_azul):
        self.container_resultado = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_resultado.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.label_resultado = customtkinter.CTkLabel(self.container_resultado,
                                            text=f'RESULTADO')
        self.label_resultado.grid()



    def trocar_cor_button(self, button):
        button.bind("<Enter>", lambda e: button.configure(text_color="#FFFFFF", fg_color="#000000"))
        button.bind("<Leave>", lambda e: button.configure(text_color="#000000", fg_color="transparent"))







if __name__ == '__main__':
    View()
