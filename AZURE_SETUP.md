# Configuração do Azure para CI/CD

Este documento explica como configurar o Azure para o deploy automático via GitHub Actions.

## 1. Verificar se você tem o App Service

Você já criou o App Service: `deploy-cicd-hadua2dxe6g2fcbc`

URL: https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net

## 2. Obter informações necessárias

### Encontrar o Resource Group:
1. Vá para o [Azure Portal](https://portal.azure.com)
2. Procure por "Resource groups"
3. Encontre o resource group onde está seu App Service

### Obter Subscription ID:
1. No Azure Portal, vá para "Subscriptions"
2. Copie o Subscription ID

## 3. Criar Service Principal para GitHub Actions

Abra o Azure CLI (ou Azure Cloud Shell) e execute:

```bash
# Substitua pelos seus valores
SUBSCRIPTION_ID="your-subscription-id"
RESOURCE_GROUP="your-resource-group-name"

az ad sp create-for-rbac \
  --name "GitHubActionsDeploy-FlaskApp" \
  --role contributor \
  --scopes "/subscriptions/$SUBSCRIPTION_ID/resourceGroups/$RESOURCE_GROUP" \
  --sdk-auth
```

**Importante**: Copie TODO o output JSON retornado pelo comando acima.

## 4. Configurar Secrets no GitHub

1. Vá para seu repositório no GitHub
2. Clique em **Settings** > **Secrets and variables** > **Actions**
3. Clique em **New repository secret** e adicione:

### AZURE_CREDENTIALS
- **Name**: `AZURE_CREDENTIALS`
- **Value**: Cole o JSON completo retornado pelo comando `az ad sp create-for-rbac`

### AZURE_RESOURCE_GROUP
- **Name**: `AZURE_RESOURCE_GROUP`
- **Value**: Nome do seu resource group (ex: `my-resource-group`)

### AZURE_WEBAPP_PUBLISH_PROFILE
- **Name**: `AZURE_WEBAPP_PUBLISH_PROFILE`
- **Value**: Obtenha do Azure Portal:
  1. Vá para seu App Service
  2. Clique em **Get publish profile**
  3. Abra o arquivo .PublishSettings baixado
  4. Copie o conteúdo do perfil (é um XML)

## 5. Verificar configuração

Após configurar todos os secrets, faça um push para a branch `main` para testar o deploy:

```bash
git push origin main
```

Monitore o workflow em **Actions** no GitHub.

## Troubleshooting

### Erro: "Service principal not found"
- Verifique se o JSON do `AZURE_CREDENTIALS` está correto
- Certifique-se de que o service principal não foi excluído

### Erro: "Resource group not found"
- Verifique o nome do resource group no secret `AZURE_RESOURCE_GROUP`

### Erro: "Web app not found"
- Verifique se o nome do app service no workflow está correto
- Certifique-se de que o service principal tem permissões no resource group

### Erro: "Publish profile invalid"
- Baixe novamente o publish profile do Azure Portal
- Certifique-se de que está copiando o XML completo

## Comandos úteis para debug

### Verificar se o service principal existe:
```bash
az ad sp list --display-name "GitHubActionsDeploy-FlaskApp"
```

### Verificar permissões do service principal:
```bash
az role assignment list --assignee <service-principal-id>
```

### Testar login com service principal:
```bash
az login --service-principal -u <client-id> -p <client-secret> --tenant <tenant-id>
```
