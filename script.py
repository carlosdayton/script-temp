import os
import shutil

# Função que limpa a pasta "Temp"
def limpar_temp():
    pastas_para_limpar = [
        r"C:\Windows\Temp",  # Caminho da pasta Temp
        r"C:\Windows\Prefetch",# Caminho da pasta Prefetch
        os.path.join(os.environ['USERPROFILE'], r"AppData\Local\Temp")  # Caminho da pasta temp local
    ]
    
    for pasta_temp in pastas_para_limpar:
        print(f"Iniciando a limpeza da pasta: {pasta_temp}")
        
        try:
            # Verifica se o diretório realmente existe
            if not os.path.exists(pasta_temp):
                print(f"A pasta {pasta_temp} não foi encontrada")
                continue
            
            # Lista os arquivos e diretórios dentro da pasta
            for nome_arquivo in os.listdir(pasta_temp):
                caminho_arquivo = os.path.join(pasta_temp, nome_arquivo)  # Caminho completo do arquivo ou pasta
                try:
                    # Verifica se é um arquivo
                    if os.path.isfile(caminho_arquivo):  
                        print(f"Tentando remover arquivo: {caminho_arquivo}")
                        os.remove(caminho_arquivo)  # Remove o arquivo
                        print(f"Arquivo removido: {caminho_arquivo}")
                    # Verifica se é uma pasta
                    elif os.path.isdir(caminho_arquivo):  
                        print(f"Tentando remover pasta: {caminho_arquivo}")
                        shutil.rmtree(caminho_arquivo)  # Remove a pasta e todo seu conteúdo
                        print(f"Pasta removida: {caminho_arquivo}")
                except PermissionError:
                    print(f"Permissão negada para o arquivo/pasta: {caminho_arquivo}")
                except Exception as e:
                    print(f"Erro ao tentar remover {caminho_arquivo}: {e}")
            
            print(f"Arquivos da pasta {pasta_temp} limpos com sucesso!")
        except Exception as e:
            print(f"Ocorreu um erro ao limpar a pasta {pasta_temp}: {e}")

# Rodando a função de limpeza assim que o script é executado
if __name__ == "__main__":
    limpar_temp()
