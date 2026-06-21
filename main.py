import cv2
import threading
import os
import shutil
from PIL import Image, ImageTk
from scripts.tela import AppAssiduidade
from scripts.reconhecimento import executar_reconhecimento
from scripts.logs import registrar_presenca

app = AppAssiduidade()
cap = cv2.VideoCapture(0)

def rodar_ia():
    try:
        if not os.path.exists("Cadastro"): os.makedirs("Cadastro")
        ret, frame = cap.read()
        if ret:
            if os.path.exists("Cadastro/captura_atual.jpg"):
                shutil.copy("Cadastro/captura_atual.jpg", "Cadastro/captura_passada.jpg")
            cv2.imwrite("Cadastro/captura_atual.jpg", frame)
            
            resultado = executar_reconhecimento()
            
            if resultado is None:
                app.atualizar_interface("Configurando", "Foto inicial salva.", "Aguarde 30s.")
            elif resultado:
                registrar_presenca(True)
                app.atualizar_interface("Aluno Presente, bons estudos!", "Frequência registrada.", "Bons estudos!")
            else:
                registrar_presenca(False)
                app.atualizar_interface("Aluno Ausente, atenção, esteja atento!", "Rosto não identificado.", "Posicione-se melhor!", erro=True)
    except Exception as e:
        print(f"[ERRO CRÍTICO]: {e}")
    
    iniciar_contagem(30)

def iniciar_contagem(segundos):
    if segundos > 0:
        app.mensagem.configure(text=f"Próxima checagem em {segundos}s...")
        app.update()
        app.after(1000, lambda: iniciar_contagem(segundos - 1))
    else:
        threading.Thread(target=rodar_ia, daemon=True).start()

def atualizar_preview():
    ret, frame = cap.read()
    if ret:
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = ImageTk.PhotoImage(image=Image.fromarray(frame).resize((400, 300)))
        app.video_label.configure(image=img, text="")
        app.video_label.image = img
    app.after(33, atualizar_preview)

def iniciar_sistema():
    app.atualizar_interface("Sistema de Monitoramento de Assiduidade EAD", "Iniciando em 5 segundos...")
    app.after(5000, lambda: threading.Thread(target=rodar_ia, daemon=True).start())

atualizar_preview()
iniciar_sistema()
app.mainloop()
cap.release()