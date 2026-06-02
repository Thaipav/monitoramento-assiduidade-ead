import customtkinter as ctk
import os

class AppAssiduidade(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Sistema de Presença")
        self.geometry("550x350") 
        
        self.attributes("-topmost", True)
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'{width}x{height}+{x}+{y}')
        
        self.attributes("-alpha", 0.95)

        self.frame = ctk.CTkFrame(self, corner_radius=20)
        self.frame.pack(pady=20, padx=20, fill="both", expand=True)

        self.titulo = ctk.CTkLabel(
            self.frame, 
            text="Olá! Hora da Verificação ✨", 
            font=("Segoe UI", 22, "bold"),
            text_color="#A5D6A7" 
        )
        self.titulo.pack(pady=(35, 10))

        self.mensagem = ctk.CTkLabel(
            self.frame, 
            text="Por favor, olhe para a câmera.\nEstamos confirmando sua presença...", 
            font=("Segoe UI", 14),
            text_color="#E0E0E0"
        )
        self.mensagem.pack(pady=10)

        self.progresso = ctk.CTkProgressBar(self.frame, width=280, height=8, progress_color="#A5D6A7")
        self.progresso.pack(pady=25)
        self.progresso.set(0)
        self.progresso.start()

        self.after(15000, self.finalizar)

    def mostrar_aviso_ausencia(self):
        
        aviso = ctk.CTk()
        aviso.title("Aviso de Posicionamento")
        aviso.geometry("400x200")
        aviso.attributes("-topmost", True)
        
        x = (aviso.winfo_screenwidth() // 2) - 200
        y = (aviso.winfo_screenheight() // 2) - 100
        aviso.geometry(f"+{x}+{y}")

        frame = ctk.CTkFrame(aviso, corner_radius=15, fg_color="#333333")
        frame.pack(pady=15, padx=15, fill="both", expand=True)

        label = ctk.CTkLabel(
            frame, 
            text="Ops! Não te vimos agora. 🧐", 
            font=("Segoe UI", 16, "bold"),
            text_color="#FFCC80"
        )
        label.pack(pady=(20, 5))

        sub_label = ctk.CTkLabel(
            frame, 
            text="Verifique se o local está iluminado\ne se você está de frente para a câmera.", 
            font=("Segoe UI", 12),
            text_color="#E0E0E0"
        )
        sub_label.pack(pady=10)

        btn = ctk.CTkButton(frame, text="Entendido", command=aviso.destroy, width=100)
        btn.pack(pady=10)

        aviso.mainloop()

    def finalizar(self):

        self.titulo.configure(text="Tudo certo! ✨", text_color="#A5D6A7")
        self.mensagem.configure(text="Sua presença foi registrada.\nBons estudos!")
        self.progresso.set(1) 
        
        self.after(2000, self.destroy)

if __name__ == "__main__":

    app = AppAssiduidade()
    app.mainloop()