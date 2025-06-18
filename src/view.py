import customtkinter
from PIL import Image

class View():
    def __init__(self):
        self.root = customtkinter.CTk()
        self.root.geometry("600x600")
        self.root.title('Força Saiyajin')
        self.root.minsize(400, 400)

        self.estrutura_imagem(self.root)

        # Frame para ser a borda do container principal
        self.container_borda = customtkinter.CTkFrame(self.root,
                                                      width=500,
                                                      height=500,
                                                      corner_radius=12,
                                                      fg_color="#000000")
        self.container_borda.pack(padx=45, pady=45)

        # Frame principal
        self.container = customtkinter.CTkFrame(self.container_borda,
                                                width=500,
                                                height=500,
                                                corner_radius=12,
                                                fg_color="#66ccff")
        self.container.pack(padx=3, pady=3)
        self.container.pack_propagate(False) # Permite que todo o container seja exibido

        self.estrutura_container(self.container)

        self.root.mainloop()

    def estrutura_imagem(self, container):
        container_imagem = customtkinter.CTkFrame(container, width=500, fg_color="transparent")
        container_imagem.pack(pady=(30, 0))

        imagem = Image.open('vegeta_weight_training.png')
        imagem_ctk = customtkinter.CTkImage(light_image=imagem, size=(150, 150))

        self.label_imagem = customtkinter.CTkLabel(container_imagem, image=imagem_ctk, text="")
        self.label_imagem.pack()



    def estrutura_container(self, container):
        # Cria um frame para armazenar todos os componentes
        container_login = customtkinter.CTkFrame(container,
                                                 width=500,
                                                 fg_color="transparent")
        container_login.pack(padx=20,
                             pady=(30, 0))
        container_login.grid_propagate(False)

        self.estrutura_container_login(container_login)

    def estrutura_container_login(self, container_login):
        # EMAIL
        # Label EMAIL
        self.label_email = customtkinter.CTkLabel(container_login,
                                                  text=f"EMAIL",
                                                  text_color="black",
                                                  anchor="w", font=("Arial", 30, "bold"))
        
        self.label_email.grid(row=0, column=0, sticky="w", padx=(0, 20), pady=(0, 20))

        # Label ENTRY
        self.entry_email = customtkinter.CTkEntry(container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_email.grid(row=0, column=1, sticky="ew" , pady=(0, 20))

        #SENHA 
        # Label SENHA
        self.label_senha = customtkinter.CTkLabel(container_login,
                                                  text=f"SENHA",
                                                  text_color="black",
                                                  anchor="w",
                                                  font=("Arial", 30, "bold"))
        self.label_senha.grid(row=1, column=0, sticky="w", padx=(0, 20))

        # Entry SENHA
        self.entry_senha = customtkinter.CTkEntry(container_login,
                                                  font=("Arial", 25),
                                                  fg_color="#66ccff",
                                                  border_color="#000000",
                                                  border_width=3)
        
        self.entry_senha.grid(row=1, column=1, sticky="ew")

        # Botão para logar
        self.button = customtkinter.CTkButton(container_login,
                                              corner_radius=20,
                                              height=40,
                                              width=70,
                                              font=("Arial", 20),
                                              text='LOGIN',
                                              fg_color="#000000",
                                              hover_color="#595959",
                                              text_color="#FFFFFF")
        
        self.button.grid(row=2, column=0, columnspan=2, pady=(20, 0))

        container_login.grid_columnconfigure(1, weight=1) # Função para fazer a column 1 do grid ocupar o espaço sobrando 
    


        


if __name__ == '__main__':
    View()
