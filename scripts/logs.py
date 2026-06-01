import os
import csv
from datetime import datetime

def registrar_presenca(status_match):
    pasta_logs = "Logs"
    arquivo_csv = "registro_assiduidade.csv"
    caminho_completo = os.path.join(pasta_logs, arquivo_csv)

    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)

    nome_aluno = "Aluno Cadastrado"
    agora = datetime.now()
    data_atual = agora.strftime("%d/%m/%Y")
    hora_atual = agora.strftime("%H:%M:%S")
    status = "PRESENTE" if status_match else "AUSENTE / INCORRETO"

    arquivo_novo = not os.path.exists(caminho_completo)

    try:
        with open(caminho_completo, mode='a', newline='', encoding='utf-8') as file:
            escritor = csv.writer(file, delimiter=';')
            
            if arquivo_novo:
                escritor.writerow(["Nome", "Data", "Hora", "Status"])
            
            escritor.writerow([nome_aluno, data_atual, hora_atual, status])
            print(f"[SUCESSO - LOGS]: Registro salvo para {nome_aluno} às {hora_atual}.")
    except Exception as e:
        print(f"[ERRO - LOGS]: Não foi possível salvar o log: {e}")