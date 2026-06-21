import csv
import os
import sys
from datetime import datetime

def registrar_presenca(sucesso):
    pasta_logs = "Logs"
    arquivo_csv = os.path.join(pasta_logs, "frequencia.csv")
    
    if not os.path.exists(pasta_logs):
        os.makedirs(pasta_logs)
        
    status_texto = "Presente" if sucesso else "Ausente"
    agora = datetime.now()
    
    try:
        with open(arquivo_csv, mode='a', newline='', encoding='utf-8') as f:
            escritor = csv.writer(f)
            if not os.path.exists(arquivo_csv) or os.path.getsize(arquivo_csv) == 0:
                escritor.writerow(["Data", "Hora", "Status"])
            escritor.writerow([agora.strftime("%d/%m/%Y"), agora.strftime("%H:%M:%S"), status_texto])
            
            print(f"[LOG ATUALIZADO]: {agora.strftime('%H:%M:%S')} - {status_texto}")
            sys.stdout.flush() 
    except Exception as e:
        print(f"[ERRO NO LOG]: {e}")
        sys.stdout.flush()