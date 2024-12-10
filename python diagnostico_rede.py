import os
import platform
import time

# Função para registrar mensagens no log
def registrar_mensagem(mensagem):
    try:
        with open("diagnostico_rede.log", "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {mensagem}\n")
    except Exception as e:
        print(f"Erro ao registrar log: {e}")

# Verifica a conectividade com o gateway local (roteador)
def verificar_conexao_gateway():
    gateway = "192.168.1.1"  # IP do roteador (ajuste conforme necessário)
    sistema = platform.system().lower()
    comando_ping = f"ping -n 1 {gateway}" if sistema == "windows" else f"ping -c 1 {gateway}"

    resposta = os.system(comando_ping)
    if resposta == 0:
        registrar_mensagem("Conexão com a rede local está funcionando.")
        return True
    else:
        registrar_mensagem("Erro: Sem conexão com a rede local.")
        return False

# Verifica a conectividade com a internet usando o Google DNS (8.8.8.8)
def verificar_conexao_internet():
    sistema = platform.system().lower()
    comando_ping = "ping -n 1 8.8.8.8" if sistema == "windows" else "ping -c 1 8.8.8.8"

    resposta = os.system(comando_ping)
    if resposta == 0:
        registrar_mensagem("Conexão com a Internet está funcionando.")
        return True
    else:
        registrar_mensagem("Erro: Sem conexão com a Internet.")
        return False

# Tenta reiniciar a rede e obter um novo IP
def tentar_reiniciar_conexao():
    sistema = platform.system().lower()
    try:
        if sistema == "windows":
            registrar_mensagem("Tentando reiniciar a conexão de rede...")
            os.system("ipconfig /release")  # Solta o IP atual
            os.system("ipconfig /renew")    # Solicita um novo IP
            time.sleep(5)  # Aguarda 5 segundos para reiniciar a rede
            if verificar_conexao_gateway() and verificar_conexao_internet():
                registrar_mensagem("Conexão de rede reiniciada com sucesso.")
                return True
        else:
            registrar_mensagem("Sistema não suportado para reiniciar conexão automaticamente.")
    except Exception as e:
        registrar_mensagem(f"Erro ao tentar reiniciar a conexão: {e}")
    return False

# Verifica o status da interface de rede
def verificar_driver_de_rede():
    sistema = platform.system().lower()
    try:
        if sistema == "windows":
            comando = "ipconfig"
        else:
            comando = "ifconfig"  # Para Linux/Mac

        resposta = os.system(comando)
        if resposta == 0:
            registrar_mensagem("Interface de rede está respondendo.")
            return True
        else:
            registrar_mensagem("Erro ao verificar a interface de rede.")
            return False
    except Exception as e:
        registrar_mensagem(f"Erro ao verificar a interface de rede: {e}")
        return False

# Testa a conectividade com DNS público (apenas para teste)
def testar_dns_para_teste():
    registrar_mensagem("Testando a conectividade com o DNS público 8.8.8.8...")
    comando_ping = "ping -n 1 8.8.8.8" if platform.system().lower() == "windows" else "ping -c 1 8.8.8.8"
    try:
        resposta = os.system(comando_ping)
        if resposta == 0:
            registrar_mensagem("Conectividade com o DNS Google (8.8.8.8) está funcionando.")
            return True
        else:
            registrar_mensagem("Erro ao conectar com o DNS 8.8.8.8.")
            return False
    except Exception as e:
        registrar_mensagem(f"Erro ao testar o DNS: {e}")
        return False

# Executa todas as soluções automáticas de rede
def tentar_solucoes_automáticas():
    try:
        if not verificar_conexao_gateway() or not verificar_conexao_internet():
            if tentar_reiniciar_conexao():
                return True

        if not verificar_driver_de_rede():
            registrar_mensagem("Possível falha no driver de rede.")
            return False

        if not testar_dns_para_teste():
            registrar_mensagem("Se o problema persistir, verifique a configuração do DNS.")
            return False

        registrar_mensagem("Conexão resolvida com sucesso!")
        return True
    except Exception as e:
        registrar_mensagem(f"Erro ao executar soluções automáticas: {e}")
        return False

# Função principal
if __name__ == "__main__":
    tentar_solucoes_automáticas()

