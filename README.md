# Análise de Sentimentos no Reddit

Este projeto realiza a análise de sentimentos de postagens no Reddit com base em um termo de pesquisa fornecido pelo usuário. Utiliza a API do Reddit através do PRAW, biblioteca VADER para determinar a polaridade dos textos e a biblioteca de interface gráfica Tkinter.

## Pré-requisitos

Certifique-se de ter as seguintes bibliotecas Python instaladas:

- `praw`
- `vaderSentiment`

Você pode instalá-las utilizando o `pip`:

```pip install praw vaderSentiment```

## Além disso, é necessário configurar as credenciais de acesso à API do Reddit. Você precisará dos seguintes dados:

- CLIENT_ID
- CLIENT_SECRET
- USER_AGENT

### Configuração das Credenciais do Reddit
**Crie um Aplicativo no Reddit:**

1. Acesse Reddit Apps e faça login com sua conta Reddit.
2. Clique em "Create App" ou "Create Another App" na parte inferior da página e Preencha o formulário com as informações do seu aplicativo:
- Nome: Escolha um nome para o seu aplicativo.
- Descreva: Opcional, você pode descrever brevemente seu aplicativo.
- Sobre URL: Opcional, deixe em branco.
- Permissões de Redirecionamento: Para fins de desenvolvimento, você pode definir como http://localhost:8000.
- Tipo de Aplicativo: Selecione "script".
- Clique em "Create app" para criar seu aplicativo.
- Obtenha suas Credenciais:

Após criar o aplicativo, você verá uma seção com suas credenciais.
Anote o client_id, client_secret, e configure o user_agent como desejar (ex.: "my-reddit-app").

## Configure suas Credenciais no Projeto:

**O arquivo config.py na pasta config tem o seguinte conteúdo:**
- CLIENT_ID = 'seu_client_id_aqui'
- CLIENT_SECRET = 'seu_client_secret_aqui'
- USER_AGENT = 'sua_user_agent_aqui'

**Estrutura do Projeto**

├── config/  
 
│   └── config.py  

├── sentiment_analysis.py  

└── README.md  

### Como Executar:
 **Clone este repositório para o seu ambiente local:**

```git clone https://github.com/seu-usuario/reddit-sentiment-analysis.git```

**Navegue até o diretório do projeto:**

``` cd reddit-sentiment-analysis``` 
**Execute o script principal:**

```python sentiment_analysis.py```
**Insira o termo de pesquisa quando solicitado e veja a análise de sentimento dos posts relevantes.**

###  Funcionalidades:
- Conexão ao Reddit usando PRAW.
- Busca de posts com base em um termo de pesquisa fornecido pelo usuário.
- Análise de sentimento dos títulos e corpos dos posts usando VADER.
- Interação contínua com o usuário para realizar múltiplas buscas.
### Contribuição: 
Contribuições são bem-vindas! Se você tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou um pull request.

### Licença:
Este projeto é licenciado sob a MIT License.
