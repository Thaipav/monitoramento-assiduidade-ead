import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scripts.captura import executar_captura
from scripts.reconhecimento import executar_reconhecimento

INTERVALO_SEGUNDOS = 10  

print("SISTEMA DE ASSIDUIDADE EAD INICIADO! BEM-VINDO!")
print(f"O sistema fará verificações a cada {INTERVALO_SEGUNDOS} segundos.")
print("Pressione Ctrl + C no terminal para encerrar.")

try:
    ciclo = 1
    while True:
        print(f"--- INICIANDO CICLO Nº {ciclo} ---")
  
        sucesso_captura = executar_captura()
       
        if sucesso_captura:
            
            match_aluno = executar_reconhecimento()
            
            if match_aluno:
                print(f"[STATUS CICLO {ciclo}]: Presença confirmada.")
            else:
                print(f"[STATUS CICLO {ciclo}]: Presença NÃO confirmada ou rosto ausente.")
                
        else:
            print("Ciclo abortado devido a erro na captura.")
            
        print(f"Ciclo {ciclo} finalizado. Aguardando próximo intervalo...")
        print("-" * 40)
        
        ciclo += 1
        time.sleep(INTERVALO_SEGUNDOS)

except KeyboardInterrupt:
    print("\n Sistema EAD encerrado pelo usuário.")