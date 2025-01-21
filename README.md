# Automação de Login no Google com Selenium

Este projeto utiliza a biblioteca [Selenium](https://www.selenium.dev/) para realizar a automação de login no Google de maneira simulada, interagindo com o navegador Chrome. O script implementa validações para o e-mail e senha, garantindo que os dados sejam inseridos corretamente antes de realizar as ações de login.

## 📋 Funcionalidades

- Validação de e-mail e senha com regex e verificações manuais.
- Automação de preenchimento de campos de login e senha no Google.
- Tratamento de erros em caso de credenciais inválidas (e-mail ou senha incorretos).
- Interação direta com elementos da página usando identificadores como `ID`, `CLASS_NAME` e `XPATH`.
- Configuração personalizada do navegador para ocultar que ele está sendo controlado por uma ferramenta automatizada.

## 🛠️ Requisitos

### Hardware Necessário
- **Sistema Operacional**: Windows, macOS ou Linux.
- **Processador**: Dual-core ou superior.
- **Memória RAM**: Pelo menos 4 GB (recomendado 8 GB ou mais).
- **Espaço em Disco**: 500 MB livres para instalação do navegador Chrome e dependências.

### Software Necessário

1. **Python 3.7 ou superior**
   - Baixe e instale o Python a partir do [site oficial](https://www.python.org/downloads/).
2. **Google Chrome**
   - Baixe e instale o navegador Google Chrome a partir do [site oficial](https://www.google.com/chrome/).
3. **ChromeDriver compatível**
   - Faça o download da versão do ChromeDriver compatível com a sua versão do Chrome em [ChromeDriver Downloads](https://chromedriver.chromium.org/downloads).
4. **Pacotes Python**:
   - Instale os pacotes necessários executando o seguinte comando no terminal:
     ```bash
     pip install selenium pygetwindow pyautogui
     ```

## 📂 Estrutura do Projeto

- `index.py`: Script principal contendo o código de automação.
- `chromedriver.exe`: Arquivo necessário para controlar o navegador Chrome.

## 🚀 Como Executar

1. **Clone o Repositório**
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um Ambiente Virtual (.venv)**
   - No terminal, execute o seguinte comando para criar um ambiente virtual:
     ```bash
     python -m venv .venv
     ```
   - Ative o ambiente virtual:
     - **Windows**: `source .venv\Scripts\activate`
     - **macOS/Linux**: `source .venv/bin/activate`

3. **Configure o Caminho do ChromeDriver**
   - Verifique o caminho correto do arquivo `chromedriver.exe` em sua máquina.
   - Atualize a variável `caminho` no script `index.py`:
     ```python
     caminho = "./chromedriver-win64/chromedriver.exe"
     ```

4. **Execute o Script**
   - No terminal, execute:
     ```bash
     python index.py
     ```

5. **Siga as Instruções no Terminal**
   - Insira o e-mail e senha quando solicitado.
   - Caso os dados estejam incorretos, você terá a oportunidade de corrigir.

## ⚠️ Observações Importantes

- **Segurança**: Evite compartilhar seu e-mail e senha. Este script foi desenvolvido para aprendizado e não deve ser usado para propósitos maliciosos.
- **Restrições do Google**: O Google pode bloquear o acesso automatizado, mesmo com as configurações para mascarar a automação. Use este script com moderação.
- **Compatibilidade**: Certifique-se de que a versão do ChromeDriver seja compatível com sua versão do Google Chrome.

## 📄 Licença
Este projeto está licenciado sob a [MIT License](LICENSE). Sinta-se à vontade para usar, modificar e distribuir.

---

### 💡 Dúvidas?
Se tiver alguma dúvida ou problema, entre em contato ou abra uma issue no repositório!
