# 🔓 API de Desbloqueio Control iD
Esta API permite automatizar o processo de desbloqueio de equipamentos da Control iD via navegador utilizando Selenium. O usuário envia os dados da empresa e do equipamento por meio de uma requisição POST, e a API retorna o código de desbloqueio gerado automaticamente pelo site oficial da Control iD.

# 🚀 Tecnologias Utilizadas
Flask — Microframework para criação da API.

Flask-CORS — Habilita CORS para comunicação com outras aplicações.

Selenium — Automatiza a navegação no site da Control iD.

Webdriver Manager — Gerencia o download e instalação do WebDriver automaticamente.

# 📦 Instalação

```bash
pip install -r requirements.txt
```

# ⚙️ Como usar
Inicie a API:

```bash
python3 api_desbloqueio.py
```

A API ficará disponível em http://localhost:5000.

Para que funcione com o flutter web hospedado é preciso estar rodando com https, por isso configurado para rodar no ngrok

`snap run ngrok http 5000`

Faça uma requisição POST para o endpoint `/desbloquear`:

Exemplo de payload:

```json
{
  "rsocial": "Nome da Empresa LTDA",
  "cnpj": "12345678000199",
  "serial": "ID123456789",
  "senha": "suasenha"
}

```
A resposta será um JSON com o código de desbloqueio:

```json
{
  "codigo": "123456"
}
```
