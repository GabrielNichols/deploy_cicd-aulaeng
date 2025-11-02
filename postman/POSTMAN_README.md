# 🧪 Testando a API com Postman

Este guia explica como testar a API Flask usando as coleções do Postman incluídas neste projeto.

## 📦 Arquivos Incluídos

- `postman_collection.json` - Coleção com todos os endpoints da API
- `postman_environment_production.json` - Environment para testar em produção
- `postman_environment_local.json` - Environment para testar localmente

## 🚀 Como Importar no Postman

### Passo 1: Abrir o Postman
1. Abra o Postman Desktop ou Web
2. Clique em **Import** (botão no topo esquerdo)

### Passo 2: Importar Coleção
1. Clique em **Upload Files**
2. Selecione o arquivo `postman_collection.json`
3. Clique em **Import**

### Passo 3: Importar Environments
1. Clique novamente em **Import**
2. Selecione os arquivos:
   - `postman_environment_production.json`
   - `postman_environment_local.json`
3. Clique em **Import**

## 🌐 Configurando Environments

### Para Produção:
1. No Postman, clique no dropdown de environments (canto superior direito)
2. Selecione **"Flask CI/CD API - Production"**
3. A URL base será automaticamente configurada para: `https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net`

### Para Desenvolvimento Local:
1. Selecione **"Flask CI/CD API - Local Development"**
2. A URL base será: `http://localhost:5000`
3. Certifique-se de que sua aplicação Flask está rodando localmente

## 📋 Endpoints Disponíveis

### ✅ GET Endpoints

| Endpoint | Descrição |
|----------|-----------|
| `GET /` | Página inicial (HTML) |
| `GET /api/health` | Health check da API |
| `GET /api/users` | Lista todos os usuários |
| `GET /api/users/{id}` | Busca usuário específico |
| `GET /api/products` | Lista todos os produtos |
| `GET /api/products/{id}` | Busca produto específico |

### 📤 POST Endpoints

| Endpoint | Descrição |
|----------|-----------|
| `POST /api/echo` | Endpoint de teste que retorna os dados enviados |

## 🧪 Como Testar

### 1. Health Check
- Método: `GET`
- URL: `{{base_url}}/api/health`
- **Esperado**: Status 200 com JSON de saúde

### 2. Listar Usuários
- Método: `GET`
- URL: `{{base_url}}/api/users`
- **Esperado**: Status 200 com lista de usuários

### 3. Echo Test
- Método: `POST`
- URL: `{{base_url}}/api/echo`
- Headers: `Content-Type: application/json`
- Body:
```json
{
  "message": "Teste do Postman",
  "user": "tester",
  "timestamp": "2024-01-01"
}
```

## 🔍 Verificando Respostas

### Resposta Esperada - Health Check:
```json
{
  "status": "healthy",
  "message": "API is running",
  "timestamp": "2025-11-02T21:00:00.000000"
}
```

### Resposta Esperada - Users:
```json
{
  "users": [
    {
      "id": 1,
      "name": "João Silva",
      "email": "joao@example.com"
    },
    {
      "id": 2,
      "name": "Maria Santos",
      "email": "maria@example.com"
    }
  ],
  "count": 2
}
```

### Resposta Esperada - Echo:
```json
{
  "received": {
    "message": "Teste do Postman",
    "user": "tester",
    "timestamp": "2024-01-01"
  },
  "timestamp": "2025-11-02T21:00:00.000000",
  "method": "POST"
}
```

## 🐛 Troubleshooting

### Erro: "Could not get any response"
- **Produção**: Verifique se a aplicação está deployada corretamente
- **Local**: Certifique-se de que `python app.py` está rodando

### Erro: "Connection refused"
- Verifique se a URL do environment está correta
- Para local: Certifique-se de que a porta 5000 não está bloqueada

### Erro: Status 500
- Verifique os logs da aplicação no Azure Portal (para produção)
- Verifique o terminal onde está rodando a app (para local)

## 📱 Test Runner

Você pode executar todos os testes automaticamente:

1. Na coleção, clique com botão direito
2. Selecione **Run collection**
3. Configure o environment correto
4. Clique em **Run Flask CI/CD API**

Isso executará todos os endpoints automaticamente e mostrará um relatório de sucesso/falha.

## 🔄 Atualizando a Coleção

Quando adicionar novos endpoints à API:

1. Atualize o arquivo `postman_collection.json`
2. Importe novamente no Postman (sobrescrever a existente)
3. Teste os novos endpoints

---

🎯 **Dica**: Use o environment correto para não confundir URLs de produção e desenvolvimento!
