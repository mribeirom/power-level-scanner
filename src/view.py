import customtkinter
from PIL import Image
from controller import Controller

class View():
    def __init__(self):

        self.controller = Controller(self)


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

        self.tela_registro(self.frame_fundo_azul)
        self.tela_menu(self.frame_fundo_azul)
        self.tela_calculo(self.frame_fundo_azul)
        self.tela_login(self.frame_fundo_azul)


        self.root.mainloop()

    def estrutura_imagem(self, container):
        container_imagem = customtkinter.CTkFrame(container, width=500, fg_color="transparent")
        container_imagem.pack(pady=(30, 0))

        imagem = Image.open('vegeta_weight_training.png')
        imagem_ctk = customtkinter.CTkImage(light_image=imagem, size=(150, 150))

        self.label_imagem = customtkinter.CTkLabel(container_imagem, image=imagem_ctk, text="")
        self.label_imagem.pack()

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
                                                        font=("Arial", 30, "bold"))
        
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
                                                  font=("Arial", 30, "bold"))
        self.label_senha.grid(row=1, column=0, sticky="w", padx=(0, 20))

        # Entry Senha
        self.entry_senha_login = customtkinter.CTkEntry(self.container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3,
                                                  show="*")
        
        self.entry_senha_login.grid(row=1, column=1, sticky="ew")

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
                                                    command=self.view_login)
        
        self.button_logar.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        # botão para interface de registro
        self.button_login_registro = customtkinter.CTkButton(self.container_login,
                                                     text=f"FAÇA SEU CADASTRO AQUI",
                                                     text_color='#000000',
                                                     fg_color="transparent",
                                                     hover_color="#66ccff",
                                                     font=("Arial", 15, "bold"),
                                                     command=self.mostrar_tela_registro)
        
        self.button_login_registro.grid(row=3, column=0, columnspan=2, pady=(10, 0))


        # aviso de erro
        self.label_aviso_login = customtkinter.CTkLabel(self.container_login,
                                                        text="",
                                                        text_color='#000000',
                                                        font=("Arial", 20, "bold"))
        self.label_aviso_login.grid(row=4, column=0, columnspan=2, pady=(15, 0))
        

        
    
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
                                                 font=("Arial", 30, "bold"))
        
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
                                                  font=("Arial", 30, "bold"))
        
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
                                                  font=("Arial", 30, "bold"))
        self.label_senha.grid(row=2, column=0, sticky="w", padx=(0, 20))

        # Entry Senha
        self.entry_senha_registro = customtkinter.CTkEntry(self.container_registro,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3,
                                                  show="*")
        
        self.entry_senha_registro.grid(row=2, column=1, sticky="ew")

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
                                              command=self.view_registro)
        
        self.button_registro.grid(row=3, column=0, columnspan=2, pady=(20, 0))


        # botão para interface de login
        self.button_registro_login = customtkinter.CTkButton(self.container_registro,
                                                     text=f"FAÇA SEU LOGIN AQUI",
                                                     text_color='#000000',
                                                     fg_color="transparent",
                                                     hover_color="#66ccff",
                                                     font=("Arial", 15, "bold"),
                                                     command=self.mostrar_tela_login)
        
        self.button_registro_login.grid(row=4, column=0, columnspan=2, pady=(10, 0))

        # aviso de erro

        self.label_aviso_registro = customtkinter.CTkLabel(self.container_registro,
                                                        text="",
                                                        text_color='#000000',
                                                        font=("Arial", 20, "bold"))
        self.label_aviso_registro.grid(row=5, column=0, columnspan=2, pady=(15, 0))

        

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
                                                     font=("Arial", 30, "bold"),
                                                     command=self.mostrar_tela_perfil)
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
                                                     command=self.view_logout)
        self.button_sair.grid(row=2, column=0, pady=(0, 0))



        self.trocar_cor_button(self.button_calcular)
        self.trocar_cor_button(self.button_perfil)
        self.trocar_cor_button(self.button_sair)


    def tela_perfil(self, frame_fundo_azul):
        usuario_logado = self.controller.solicitar_usuario_logado()
        self.container_perfil = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_perfil.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.container_perfil.grid_columnconfigure(1, weight=1)

        self.label_perfil = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'SEU PERFIL',
                                            text_color='black',
                                            font=("Arial", 30, "bold"))
        self.label_perfil.grid(row=0, column=0, columnspan=2, pady=(20, 0))
        
        self.label_nome = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'NOME',
                                            text_color='black',
                                            font=("Arial", 25, "bold"))
        self.label_nome.grid(row=1, column=0, sticky='w', pady=(10, 0))

        self.label_nome_usuario = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'{usuario_logado.get('nome').upper()}',
                                            text_color='black',
                                            font=("Arial", 20),
                                            wraplength=450,
                                            justify='left')
        self.label_nome_usuario.grid(row=2, column=0, sticky='w', padx=(20, 0))

        self.label_email_perfil = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'EMAIL',
                                            text_color='black',
                                            font=("Arial", 25, "bold"))
        self.label_email_perfil.grid(row=3, column=0, sticky='w', pady=(10, 0))

        self.label_email_perfil_usuario = customtkinter.CTkLabel(self.container_perfil,
                                            text=f'{usuario_logado.get('email').upper()}',
                                            text_color='black',
                                            font=("Arial", 20),
                                            wraplength=450,
                                            justify='left')
        self.label_email_perfil_usuario.grid(row=4, column=0, sticky='w', padx=(20, 0))

        # Botão para voltar para o menu
        self.button_menu = customtkinter.CTkButton(self.container_perfil,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='MENU',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF",
                                              command=self.mostrar_tela_menu)
        
        self.button_menu.grid(row=5, column=0, columnspan=2, pady=(20, 0))



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
                                                 font=("Arial", 20, "bold"))
        
        self.label_exercicio.grid(row=0, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Combobox exercicio
        self.combobox_exercicio = customtkinter.CTkComboBox(self.container_calculo,
                                                         values=['SUPINO',
                                                                 'DEADLIFT',
                                                                 'AGACHAMENTO'],
                                                         font=("Arial", 20),
                                                         fg_color="#66ccff",
                                                         border_color="#000000",
                                                         border_width=3,
                                                         dropdown_hover_color='#66ccff')
        
        self.combobox_exercicio.configure(state="readonly")
        
        self.combobox_exercicio.grid(row=0, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Label carga
        self.label_carga = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"CARGA",
                                                  text_color="black",
                                                  font=("Arial", 20, "bold"))
        
        self.label_carga.grid(row=1, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Entry carga
        self.entry_carga = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 20),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_carga.grid(row=1, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Label repetição
        self.label_repeticao = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"REPETIÇÃO",
                                                  text_color="black",
                                                  font=("Arial", 20, "bold"))
        self.label_repeticao.grid(row=2, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Entry repetição
        self.entry_repeticao = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 20),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_repeticao.grid(row=2, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Label genero
        self.label_genero = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"GENERO",
                                                  text_color="black",
                                                  font=("Arial", 20, "bold"))
        self.label_genero.grid(row=3, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Combobox genero
        self.combobox_genero = customtkinter.CTkComboBox(self.container_calculo,
                                                         values=['MASCULINO',
                                                                 'FEMININO'],
                                                         font=("Arial", 20),
                                                         fg_color="#66ccff",
                                                         border_color="#000000",
                                                         border_width=3,
                                                         dropdown_hover_color='#66ccff')
        
        self.combobox_genero.configure(state="readonly")
        
        self.combobox_genero.grid(row=3, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Label idade
        self.label_idade = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"IDADE",
                                                  text_color="black",
                                                  font=("Arial", 20, "bold"))
        self.label_idade.grid(row=4, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Entry idade
        self.entry_idade = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 20),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_idade.grid(row=4, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Label peso
        self.label_peso = customtkinter.CTkLabel(self.container_calculo,
                                                  text=f"PESO",
                                                  text_color="black",
                                                  font=("Arial", 20, "bold"))
        self.label_peso.grid(row=5, column=0, sticky="w", padx=(60, 10), pady=(0, 10))

        # Entry peso
        self.entry_peso = customtkinter.CTkEntry(self.container_calculo,
                                                  font=("Arial", 20),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_peso.grid(row=5, column=1, sticky="ew", padx=(0, 60), pady=(0, 10))

        # Botão para calcular
        self.button_calcular = customtkinter.CTkButton(self.container_calculo,
                                            corner_radius=20,
                                            height=30,
                                            width=70,
                                            font=("Arial", 15),
                                            text='CALCULAR',
                                            fg_color="#000000",
                                            hover_color="#595959",
                                            text_color="#FFFFFF",
                                            command=self.view_calculo)
        
        self.button_calcular.grid(row=6, column=0, columnspan=2)

        # Label de aviso de erro
        self.label_aviso_calculo = customtkinter.CTkLabel(self.container_calculo,
                                                        text="",
                                                        text_color='#000000',
                                                        font=("Arial", 15, "bold"))
        self.label_aviso_calculo.grid(row=7, column=0, columnspan=2)


    def tela_resultado(self, frame_fundo_azul):
        resultado = self.controller.solicitar_resultado()
        self.container_resultado = customtkinter.CTkFrame(frame_fundo_azul,
                                                          width=500,
                                                          height=500,
                                                          fg_color="transparent")
        self.container_resultado.grid(row=0,
                                 column=0,
                                 sticky='nsew',
                                 padx=20,
                                 pady=(30, 0))
        
        self.container_resultado.grid_columnconfigure(0, weight=1)

        self.container_frame_nivel(resultado)
        

        self.label_maximo = customtkinter.CTkLabel(self.container_resultado,
                                                   text=f'ESTIMA-SE QUE O SEU MÁXIMO PARA UMA REPETIÇÃO SEJA {int(resultado.get('repeticao_maxima'))} KG',
                                                   text_color='black',
                                                   font=('Arial', 15, "bold"),
                                                   wraplength=300)
        self.label_maximo.grid(row=1, column=0, pady=(10, 0))

        # Botão para voltar para o menu
        self.button_menu = customtkinter.CTkButton(self.container_resultado,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='MENU',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF",
                                              command=self.mostrar_tela_menu)
        
        self.button_menu.grid(row=2, column=0, columnspan=2, pady=(20, 0))



    def container_frame_nivel(self, resultado):
        # Frame auxiliar para centralizar as 3 labels finais
        self.container_nivel = customtkinter.CTkFrame(self.container_resultado,
                                                       fg_color="black",)
        self.container_nivel.grid(row=0, column=0, sticky='nsew', padx=20, pady=10)

        self.container_nivel.columnconfigure(0, weight=1)

        self.label_nivel_forca = customtkinter.CTkLabel(self.container_nivel,
                                            text=f'SEU NIVEL DE FORÇA PARA O {resultado.get('exercicio')} É {resultado.get('nivel')}',
                                            text_color='white',
                                            font=("Arial", 25, "bold"),
                                            wraplength=470)
        self.label_nivel_forca.grid(row=0, column=0, pady=20)



    def trocar_cor_button(self, button):
        button.bind("<Enter>", lambda e: button.configure(text_color="#FFFFFF", fg_color="#000000"))
        button.bind("<Leave>", lambda e: button.configure(text_color="#000000", fg_color="transparent"))
    
    # Troca de tela da interface
    def mostrar_tela_login(self):
        self.limpar_tela_login()
        self.container_login.tkraise()

    def mostrar_tela_registro(self):
        self.limpar_tela_registro()
        self.container_registro.tkraise()

    def mostrar_tela_menu(self):
        self.container_menu.tkraise()

    def mostrar_tela_perfil(self):
        self.tela_perfil(self.frame_fundo_azul)

    def mostrar_tela_calculo(self):
        self.limpar_tela_calculo()
        self.container_calculo.tkraise()
    
    def mostrar_tela_resultado(self):
        self.tela_resultado(self.frame_fundo_azul)

    # Limpar os campos de entry da tela
    def limpar_tela_login(self):
        self.entry_email_login.delete(0, customtkinter.END)
        self.entry_senha_login.delete(0, customtkinter.END)

    def limpar_tela_registro(self):
        self.entry_nome.delete(0, customtkinter.END)
        self.entry_email_registro.delete(0, customtkinter.END)
        self.entry_senha_registro.delete(0, customtkinter.END)

    def limpar_tela_calculo(self):
        self.entry_carga.delete(0, customtkinter.END)
        self.entry_repeticao.delete(0, customtkinter.END)
        self.entry_idade.delete(0, customtkinter.END)
        self.entry_peso.delete(0, customtkinter.END)


    # conexão com o controller

    #registro
    def view_registro(self):
        nome = self.entry_nome.get()
        email = self.entry_email_registro.get()
        senha = self.entry_senha_registro.get()


        self.controller.controller_registro(nome, email, senha)
        
    def registro_sucesso(self):
        self.mostrar_tela_login()
        self.label_aviso_registro.configure(text="")

    def registro_mensagem_erro(self, mensagem):
        self.label_aviso_registro.configure(text=mensagem)
        self.mostrar_tela_registro()
    
    #login
    def view_login(self):
        email = self.entry_email_login.get()
        senha = self.entry_senha_login.get()

        self.controller.controller_login(email, senha)

    def login_sucesso(self):
        self.label_aviso_login.configure(text="")
        self.mostrar_tela_menu()    
        
    def login_mensagem_erro(self, mensagem):
        self.label_aviso_login.configure(text=mensagem)
        self.mostrar_tela_login()

    #calculo
    def view_calculo(self):
        exercicio = self.combobox_exercicio.get()
        carga = self.entry_carga.get()
        repeticao = self.entry_repeticao.get()
        genero = self.combobox_genero.get()
        idade = self.entry_idade.get()
        peso = self.entry_peso.get()



        self.controller.controller_calculo(exercicio, carga, repeticao, genero, idade, peso)
    
    def calculo_sucesso(self):
        self.label_aviso_calculo.configure(text="")
        self.mostrar_tela_resultado()
    
    def calculo_mensagem_erro(self, mensagem):
        self.label_aviso_calculo.configure(text=mensagem)
        self.mostrar_tela_calculo()

    # logout

    def view_logout(self):
        self.controller.controller_logout()

if __name__ == '__main__':
    View()
