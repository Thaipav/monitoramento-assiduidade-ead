import cv2  
import os   
import time 

def executar_captura():
    pasta_destino = "Cadastro"
    nome_arquivo = "captura_atual.jpg" 
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("[ERRO - OLHOS]: Não foi possível acessar a webcam.")
        return False
    
    try:
        time.sleep(1) 
        sucesso, frame = camera.read()
        
        if sucesso:
            cv2.imwrite(caminho_completo, frame)
            print(f"[SUCESSO - OLHOS]: Foto salva para comparação em '{caminho_completo}'")
            return True
        else:
            print("[ERRO - OLHOS]: Falha ao capturar o frame.")
            return False
    finally:
        camera.release()