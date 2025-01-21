O código foi reorganizado para atender aos padrões propostos pelo framework [Guara(https://github.com/douglasdcm/guara/tree/main)] e está sendo utilizado como parte dos experimentos realizados pela equipe para validar as capacidades da ferramenta. O principal objetivo é estruturar o fluxo de automação de forma modular e reutilizável, separando as responsabilidades em transações específicas como abrir o Google, realizar login e finalizar a execução.

Isso facilita a legibilidade, a manutenção e a escalabilidade do código, permitindo que cada etapa do processo seja tratada como uma unidade independente. Caso tenha sugestões ou precise de ajustes, fico à disposição!

Explicação da Reorganização do Código

O código foi reorganizado seguindo o padrão Page Transactions, um modelo que separa cada etapa do processo de automação em transações independentes e bem definidas. Abaixo está o detalhamento das principais mudanças realizadas:
1. Organização em Transações

Cada parte do fluxo foi encapsulada em uma classe derivada de AbstractTransaction, representando uma transação com uma responsabilidade específica:

    AbrirGoogle: Responsável por abrir o site do Google.
    RealizarLogin: Lida com o fluxo completo de login, incluindo a validação de email e senha incorretos.
    FecharDriver: Finaliza a execução do WebDriver.

Essa abordagem modular facilita a reutilização do código e melhora sua organização, tornando-o mais legível e de fácil manutenção.
2. Introdução do Framework Guara

O framework Guara foi utilizado para organizar e gerenciar as transações, permitindo a execução sequencial e desacoplada de cada etapa do fluxo. O objeto Application gerencia o driver e executa as transações com o método at, passando os argumentos necessários.

Por exemplo:

app.at(AbrirGoogle, url="https://google.com/")
app.at(RealizarLogin, email=email_usuario, senha=senha_usuario)

3. Separação de Responsabilidades

Ao invés de ter todo o código em um único bloco, as responsabilidades foram separadas em transações:

    A abertura do navegador e a navegação para o site foram movidas para a transação AbrirGoogle.
    A validação de credenciais (email e senha) foi incorporada na transação RealizarLogin, com loops específicos para tratar erros de autenticação.
    O encerramento do WebDriver foi isolado na transação FecharDriver.

4. Melhorias de Leitura e Manutenção

O código ficou mais claro e organizado:

    Cada transação possui uma função específica, documentada e reutilizável.
    O uso do framework facilita a adaptação de novas transações, como automações adicionais ou diferentes fluxos de login.
    Torna mais fácil identificar e corrigir erros em partes específicas do fluxo, já que o código está dividido em blocos menores.