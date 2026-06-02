import time
import os
import shutil
from scripts.captura import executar_captura
from scripts.reconhecimento import executar_reconhecimento
from scripts.logs import registrar_presenca
from scripts.tela import AppAssiduidade # Importa a tela principal

INTERVALO_MINUTOS = 5 

print("SISTEMA INICIADO - SALVANDO NA PASTA CADASTRO")

while True:
    print("[SISTEMA]: Abrindo interface de aviso...")
    app = AppAssiduidade()
    app.mainloop()

    if executar_captura():
        
        resultado = executar_reconhecimento()
        
        if not resultado:
            print("[ALERTA]: Rosto não detectado ou diferente. Abrindo aviso...")
            aviso_app = AppAssiduidade() 
            aviso_app.mostrar_aviso_ausencia()
  
        registrar_presenca(resultado)
        
        atual = "Cadastro/captura_atual.jpg"
        passada = "Cadastro/captura_passada.jpg"
        
        if os.path.exists(atual):
            shutil.copy(atual, passada)
            print("[SISTEMA]: Foto atualizada para a próxima comparação.")
    else:
        print("[ERRO]: Câmera não encontrada.")
        app_erro = AppAssiduidade()
        app_erro.mostrar_avilo_ausencia()

    print(f"Aguardando {INTERVALO_MINUTOS} minutos para o próximo ciclo...")
    time.sleep(INTERVALO_MINUTOS * 60)