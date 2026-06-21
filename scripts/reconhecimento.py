import os
from deepface import DeepFace

def executar_reconhecimento():
    caminho_atual = "Cadastro/captura_atual.jpg"
    caminho_passada = "Cadastro/captura_passada.jpg"
    
    if not os.path.exists(caminho_passada):
        return None 

    if not os.path.exists(caminho_atual):
        return False

    try:
        resultado = DeepFace.verify(
            img1_path=caminho_passada, img2_path=caminho_atual,
            model_name="VGG-Face", detector_backend="opencv", enforce_detection=False 
        )
        return resultado.get("verified", False) and resultado.get("distance", 1.0) < 0.4
    except Exception as e:
        print(f"[ERRO - IA]: {e}")
        return False