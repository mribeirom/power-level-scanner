import customtkinter
from PIL import Image

class View():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("600x600")
        self.root.title('Força Saiyajin')
        self.root.minsize(400, 400)

        self.estrutura_imagem(self.root)

        # Frame borda preta da interface
        self.frame_borda = customtkinter.CTkFrame(self.root,
                                                      width=500,
                                                      height=500,
                                                      corner_radius=12,
                                                      fg_color="#000000")
        self.frame_borda.pack(padx=45, pady=45)

        # Frame fundo azul da interface
        self.frame_fundo_azul = customtkinter.CTkFrame(self.frame_borda,
                                                width=500,
                                                height=500,
                                                corner_radius=12,
                                                fg_color="#66ccff")
        self.frame_fundo_azul.pack(padx=3, pady=3)
        self.frame_fundo_azul.pack_propagate(False) # Permite que todo o container seja exibido

        self.tela_login(self.frame_fundo_azul)
        #self.tela_registro(self.frame_fundo_azul)
        #self.tela_exercicio(self.frame_fundo_azul)

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

    def mostrar_tela_exercicio(self):
        self.container_exercicio.tkraise()

    def tela_login(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_login = customtkinter.CTkFrame(frame_fundo_azul,
                                                 width=500,
                                                 height=500,
                                                 fg_color="transparent")
        self.container_login.pack(padx=20,
                             pady=(30, 0))
        self.container_login.grid_propagate(False)
        

        # Label Email
        self.label_email = customtkinter.CTkLabel(self.container_login,
                                                  text=f"EMAIL",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_email.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry Email
        self.entry_email = customtkinter.CTkEntry(self.container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_email.grid(row=0, column=1, sticky="ew" , pady=(0, 20))

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
        self.button = customtkinter.CTkButton(self.container_login,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='LOGIN',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF")
        
        self.button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        self.container_login.grid_columnconfigure(1, weight=1) # Função para fazer a column 1 do grid ocupar o espaço sobrando
    
    def tela_registro(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_registro = customtkinter.CTkFrame(frame_fundo_azul,
                                                 width=500,
                                                 height=500,
                                                 fg_color="transparent")
        self.container_registro.pack(padx=20,
                             pady=(30, 0))
        self.container_registro.grid_propagate(False)

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
        self.label_email = customtkinter.CTkLabel(self.container_registro,
                                                  text=f"EMAIL",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_email.grid(row=1, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Entry Email
        self.entry_email = customtkinter.CTkEntry(self.container_registro,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_email.grid(row=1, column=1, sticky="ew" , pady=(0, 20))

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
        self.button = customtkinter.CTkButton(self.container_registro,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='REGISTRAR',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF")
        
        self.button.grid(row=3, column=0, columnspan=2, pady=(20, 0))

        self.container_registro.grid_columnconfigure(1, weight=1) # Função para fazer a column 1 do grid ocupar o espaço sobrando

    def tela_exercicio(self, frame_fundo_azul):
        # Frame para armazenar os componentes do login
        self.container_exercicio = customtkinter.CTkFrame(frame_fundo_azul,
                                                 width=500,
                                                 height=500,
                                                 fg_color="transparent")
        self.container_exercicio.pack(padx=20,
                             pady=(30, 0))
        self.container_exercicio.grid_propagate(False)

        # Label nome
        self.label_nome = customtkinter.CTkLabel(self.container_exercicio,
                                                  text=f"PARABENS VOCÊ LOGOU",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_nome.pack()

    


        


if __name__ == '__main__':
    View()
