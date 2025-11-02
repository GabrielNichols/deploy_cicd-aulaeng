# Flask Hello World com CI/CD

Uma aplicação Flask simples com API RESTful e deploy automático no Azure App Service.

## Funcionalidades

- Página "Hello World" básica
- API RESTful com endpoints para usuários e produtos
- Endpoint de health check
- Endpoint echo para testes POST
- CI/CD automático via GitHub Actions

## Endpoints da API

### GET /
Página inicial com "Hello World"

### GET /api/health
Verifica se a API está funcionando
```json
{
  "status": "healthy",
  "message": "API is running",
  "timestamp": "2025-11-02T21:00:00.000000"
}
```

### GET /api/users
Lista todos os usuários
```json
{
  "users": [...],
  "count": 2
}
```

### GET /api/users/{id}
Retorna um usuário específico

### GET /api/products
Lista todos os produtos

### GET /api/products/{id}
Retorna um produto específico

### POST /api/echo
Echo endpoint para testes
```json
// Request
{
  "message": "Hello"
}

// Response
{
  "received": {
    "message": "Hello"
  },
  "timestamp": "2025-11-02T21:00:00.000000",
  "method": "POST"
}
```

## Configuração do CI/CD

O projeto está configurado com GitHub Actions para deploy automático no Azure App Service.

### Pré-requisitos para deploy:

1. Criar repositório no GitHub
2. Configurar os seguintes secrets no GitHub (Settings > Secrets and variables > Actions):
   - `AZURE_CREDENTIALS`: Credenciais de service principal do Azure (JSON format)
   - `AZURE_RESOURCE_GROUP`: Nome do resource group onde está o App Service
   - `AZURE_WEBAPP_PUBLISH_PROFILE`: Publish profile do Azure App Service
3. Push do código para a branch main dispara o deploy automático

#### Como criar as credenciais do Azure:

1. No Azure CLI, execute:
   ```bash
   az ad sp create-for-rbac --name "GitHubActionsDeploy" --role contributor --scopes /subscriptions/YOUR_SUBSCRIPTION_ID/resourceGroups/YOUR_RESOURCE_GROUP --sdk-auth
   ```

2. Copie o output JSON e adicione como secret `AZURE_CREDENTIALS`

3. Adicione o nome do seu resource group como secret `AZURE_RESOURCE_GROUP`

## Como executar localmente

1. Instalar dependências:
```bash
pip install -r requirements.txt
```

2. Executar a aplicação:
```bash
python app.py
```

3. Acessar http://localhost:5000

## Deploy no Azure

O deploy é feito automaticamente via GitHub Actions quando há push para a branch main.

URL do App Service: https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net

## Testando a API com Postman

### Exemplos de requests:

1. **Health Check**
   - Method: GET
   - URL: `https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net/api/health`

2. **Listar Usuários**
   - Method: GET
   - URL: `https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net/api/users`

3. **Echo Test**
   - Method: POST
   - URL: `https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net/api/echo`
   - Headers: `Content-Type: application/json`
   - Body:
   ```json
   {
     "test": "Hello from Postman"
   }
   ```
