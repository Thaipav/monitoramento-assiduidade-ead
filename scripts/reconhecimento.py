import cv2 
import os
import face_recognition

def executar_reconhecimento():
    pasta_cadastro = "Cadastro"
    foto_cadastro_nome = "aluno_cadastrado.jpg" 
    caminho_cadastro = os.path.join(pasta_cadastro, foto_cadastro_nome)
    
    pasta_temp = "capturas_temporarias"
    foto_temp_nome = "temp_frame.jpg"
    caminho_temp = os.path.join(pasta_temp, foto_temp_nome)
    
    if not os.path.exists(caminho_cadastro):
        print(f"[ERRO - CÉREBRO]: Foto inicial de cadastro não encontrada em '{caminho_cadastro}'")
        return False

    if not os.path.exists(caminho_temp):
        print(f"[ERRO - CÉREBRO]: Captura temporária não encontrada em '{caminho_temp}'")
        return False

    try:

        imagem_cadastro = face_recognition.load_image_file(caminho_cadastro)
        imagem_temp = face_recognition.load_image_file(caminho_temp)

        encodings_cadastro = face_recognition.face_encodings(imagem_cadastro)
        encodings_temp = face_recognition.face_encodings(imagem_temp)

        if len(encodings_cadastro) == 0:
            print("[ERRO - CÉREBRO]: Nenhum rosto detectado na foto de CADASTRO.")
            return False
            

        if len(encodings_temp) == 0:
            print("[AVISO - CÉREBRO]: Nenhum rosto detectado na webcam nesta verificação.")
            return False

        match = face_recognition.compare_faces([encodings_cadastro[0]], encodings_temp[0], tolerance=0.6)
        
        if match[0]:
            print("[SUCESSO - CÉREBRO]: BATEU! O aluno está presente na tela.")
            return True
        else:
            print("[ALERTA - CÉREBRO]: NÃO BATEU! O rosto na webcam não é o do aluno cadastrado.")
            return False

    except Exception as e:
        print(f"[ERRO - CÉREBRO]: Falha ao processar reconhecimento: {e}")
        return False

if __name__ == "__main__":
    print("Testando a lógica de comparação isoladamente...")
    executar_reconhecimento()