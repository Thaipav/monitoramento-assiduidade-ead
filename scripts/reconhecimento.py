import os
import face_recognition

def executar_reconhecimento():
    
    pasta_fotos = "Cadastro" 
    caminho_atual = os.path.join(pasta_fotos, "captura_atual.jpg")
    caminho_passada = os.path.join(pasta_fotos, "captura_passada.jpg")
    
    if not os.path.exists(caminho_passada):
        print("[AVISO - CÉREBRO]: Primeira verificação. Ainda não há foto anterior (captura_passada.jpg).")
        return True 

    if not os.path.exists(caminho_atual):
        print(f"[ERRO - CÉREBRO]: Foto atual não encontrada!")
        return False

    try:
        imagem_passada = face_recognition.load_image_file(caminho_passada)
        imagem_atual = face_recognition.load_image_file(caminho_atual)

        encodings_passada = face_recognition.face_encodings(imagem_passada)
        encodings_atual = face_recognition.face_encodings(imagem_atual)

        if len(encodings_passada) == 0 or len(encodings_atual) == 0:
            print("[AVISO - CÉREBRO]: Rosto não detectado em uma das fotos.")
            return False

        match = face_recognition.compare_faces([encodings_passada[0]], encodings_atual[0], tolerance=0.6)
        
        if match[0]:
            print("[SUCESSO - CÉREBRO]: O aluno continua o mesmo!")
            return True
        else:
            print("[ALERTA - CÉREBRO]: O rosto mudou!")
            return False
    except Exception as e:
        print(f"[ERRO - CÉREBRO]: Falha na comparação: {e}")
        return False