# network-diagnostic-script
Script em Python para diagnosticar e corrigir problemas de rede automaticamente.

# Network Diagnostic Script

Este repositório contém um **script em Python** projetado para diagnosticar e corrigir automaticamente problemas de conexão de rede. Ele verifica conectividade, reinicia a interface de rede e registra logs para análise detalhada.

## **Funcionalidades**
- Verifica a conectividade com o **gateway local** (roteador).
- Testa a conexão com a **Internet** usando o DNS público do Google (8.8.8.8).
- Reinicia a interface de rede para resolver problemas de IP ou conectividade.
- Registra logs detalhados em um arquivo chamado `diagnostico_rede.log` para posterior análise.

## **Requisitos**
- **Python 3.x** instalado.
- Compatível com **Windows** e **Linux** (com algumas limitações no suporte automático para Linux/Mac).

## **Como Usar**
1. Clone este repositório para o seu computador:
   ```bash
   git clone <URL_DO_REPOSITORIO>
   ```
   Substitua `<URL_DO_REPOSITORIO>` pela URL do repositório no GitHub.

2. Navegue até a pasta do repositório:
   ```bash
   cd network-diagnostic-script
   ```

3. Execute o script:
   - No Windows:
     ```bash
     python diagnostico_rede.py
     ```
   - No Linux/Mac:
     ```bash
     python3 diagnostico_rede.py
     ```

4. Verifique o arquivo `diagnostico_rede.log` para detalhes sobre as ações realizadas e problemas detectados.

## **Principais Componentes**
1. **Verificação de Conectividade**:
   - `verificar_conexao_gateway()`: Testa a conexão com o gateway local (192.168.1.1 por padrão).
   - `verificar_conexao_internet()`: Testa a conectividade com a Internet utilizando o DNS público do Google.

2. **Correção Automática**:
   - `tentar_reiniciar_conexao()`: Reinicia a interface de rede para corrigir problemas de conectividade.

3. **Logs**:
   - Todos os diagnósticos e ações são registrados no arquivo `diagnostico_rede.log`.

## **Limitações**
- Em sistemas Linux/Mac, a reinicialização da rede (`tentar_reiniciar_conexao()`) precisa ser adaptada para usar ferramentas específicas, como `nmcli`.
- O script não altera permanentemente as configurações de DNS; apenas testa conectividade com servidores DNS públicos.

## **Contribuições**
Contribuições são bem-vindas! Se você encontrar problemas ou tiver ideias para melhorias:
- Abra uma **issue** descrevendo o problema ou sugestão.
- Envie um **pull request** com sua contribuição.

## **Licença**
Este projeto está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais informações.
