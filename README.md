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

## 🚀 CI/CD Pipeline Inteligente

O projeto possui um pipeline avançado de CI/CD com jobs separados e otimizações:

### 📋 Jobs do Pipeline:

1. **🔨 Build & Lint** - Compila, testa sintaxe e faz linting
2. **🧪 Integration Tests** - Testa endpoints da API em tempo real
3. **🚀 Deploy** - Só executa se os testes passarem (apenas em main)

### ⚡ Otimizações:

- **Cache inteligente** de dependências Python
- **Deploy condicional** - só acontece em push para main
- **Path filtering** - ignora mudanças em docs
- **Testes de integração** - valida funcionamento real da API
- **Verificação pós-deploy** - confirma que a app está rodando

> 📖 **Para instruções detalhadas de configuração do Azure, consulte [AZURE_SETUP.md](AZURE_SETUP.md)**

### Pré-requisitos para deploy:

1. Criar repositório no GitHub
2. Configurar o secret `AZURE_WEBAPP_PUBLISH_PROFILE`:
   - **Settings** > **Secrets and variables** > **Actions**
   - **New secret**: `AZURE_WEBAPP_PUBLISH_PROFILE`
   - **Value**: Publish profile XML do Azure App Service
3. Push para main dispara automaticamente: Build → Test → Deploy

#### Como obter o Publish Profile:

1. [Azure Portal](https://portal.azure.com) → App Service `deploy-cicd`
2. **Get publish profile** → Download `.PublishSettings`
3. Copiar conteúdo XML completo → Colar no secret GitHub
4. ⚠️ **Importante**: O nome interno do app é `deploy-cicd` (não o nome completo da URL)

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

## 🧪 Testando com Postman

Para facilitar os testes da API, foram criadas coleções completas do Postman:

- **📁 Pasta**: `postman/`
- **📋 Coleção**: `postman/postman_collection.json`
- **🌐 Environment Produção**: `postman/postman_environment_production.json`
- **🏠 Environment Local**: `postman/postman_environment_local.json`
- **📖 Documentação**: `postman/POSTMAN_README.md`

### Como usar:
1. Importe os arquivos na pasta `postman/` no Postman
2. Selecione o environment apropriado (produção/local)
3. Execute os testes automaticamente ou manualmente
