import cv2  
import os   
import time 

def executar_captura():
   
    pasta_destino = "capturas_temporarias"
    nome_arquivo = "temp_frame.jpg"
    caminho_completo = os.path.join(pasta_destino, nome_arquivo)
    
    if not os.path.exists(pasta_destino):
        os.makedirs(pasta_destino)
        
    camera = cv2.VideoCapture(0)

    if not camera.isOpened():
        print("Não foi possível acessar a webcam.")
        return False
    
    try:

        time.sleep(1)
      
        sucesso, frame = camera.read()
        
        if sucesso:
        
            cv2.imwrite(caminho_completo, frame)
            print(f"[SUCESSO - OLHOS]: Nova imagem salva em '{caminho_completo}'")
            return True
        else:
            print("[ERRO - OLHOS]: Falha ao capturar o frame da câmera.")
            return False
            
    finally:
        camera.release()

if __name__ == "__main__":
    print("Testando o script de captura isoladamente...")
    executar_captura()