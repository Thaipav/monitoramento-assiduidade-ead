import time
import sys
import os

sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from scripts.captura import executar_captura

# LARA : IMPORTA A SUA FUNÇÃO DE RECONHECIMENTO AQUI EMBAIXO!
# Exemplo: from scripts.reconhecimento import executar_reconhecimento

INTERVALO_SEGUNDOS = 10  

print("SISTEMA DE ASSIDUIDADE EAD INICIADO!")
print(f"O sistema fará verificações a cada {INTERVALO_SEGUNDOS} segundos.")
print("Pressione Ctrl + C no terminal para encerrar.")

try:
    ciclo = 1
    while True:
        print(f"--- INICIANDO CICLO Nº {ciclo} ---")
  
        sucesso_captura = executar_captura()
       
        if sucesso_captura:
      
            # LARA (Aluno A): COLOQUE A SUA CHAMADA DE FUNÇÃO AQUI EMBAIXO!
            # Substitua o print abaixo pela sua função que analisa o 'temp_frame.jpg'
        
            print("Aguardando integração do código de reconhecimento da Lara...")
            
        else:
            print("Ciclo abortado devido a erro na captura.")
            
        print(f"Ciclo {ciclo} finalizado. Aguardando próximo intervalo...")
        print("-" * 40)
        
        ciclo += 1
        time.sleep(INTERVALO_SEGUNDOS)

except KeyboardInterrupt:
    print("\n Sistema EAD encerrado pelo usuário.")