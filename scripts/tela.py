import customtkinter as ctk

class AppAssiduidade(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Frequência")
        self.geometry("600x550")
        ctk.set_appearance_mode("dark")

        self.video_label = ctk.CTkLabel(self, text="Inicializando câmera...", width=400, height=300, fg_color="black")
        self.video_label.pack(pady=20)

        self.titulo = ctk.CTkLabel(self, text="Bem-vindo!", font=("Segoe UI", 24, "bold"))
        self.titulo.pack()
        
        self.mensagem = ctk.CTkLabel(self, text="Aguarde o início...", font=("Segoe UI", 16))
        self.mensagem.pack(pady=15)

    def atualizar_interface(self, titulo, msg, sub_msg="", erro=False):
        cor_titulo = "#FF6B6B" if erro else "#4CAF50"
        self.titulo.configure(text=titulo, text_color=cor_titulo)
        texto_final = f"{msg}\n{sub_msg}" if sub_msg else msg
        self.mensagem.configure(text=texto_final)
        self.update()