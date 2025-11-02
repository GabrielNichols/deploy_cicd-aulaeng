# Configuração Simples do Azure para CI/CD

Este documento explica como configurar o deploy automático usando apenas o publish profile.

## ✅ Seu Ambiente Azure

- **App Service**: `deploy-cicd-hadua2dxe6g2fcbc`
- **Resource Group**: `Engenharia_de_Software`
- **URL**: https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net
- **Subscription ID**: `012f0e50-fa82-4ade-a8f6-c82683e6cb90`

## 📋 Configuração Necessária

### 1. Obter o Publish Profile

1. Vá para o [Azure Portal](https://portal.azure.com)
2. Procure pelo seu App Service: `deploy-cicd-hadua2dxe6g2fcbc`
3. No menu lateral esquerdo, clique em **Get publish profile**
4. Baixe o arquivo `.PublishSettings`
5. Abra o arquivo com um editor de texto (Notepad++, VS Code, etc.)
6. **Copie TODO o conteúdo XML** (é um arquivo grande com várias linhas)
7. ⚠️ **IMPORTANTE**: Certifique-se de copiar do `<publishData>` até `</publishData>`

### 2. Verificar o Publish Profile

Antes de colar no GitHub, verifique se o XML contém:
- `publishUrl` com seu domínio Azure
- `userName` e `userPWD` válidos
- `destinationAppUrl` apontando para `https://deploy-cicd-hadua2dxe6g2fcbc.azurewebsites.net`

### 3. Configurar Secret no GitHub

1. Vá para seu repositório no GitHub
2. Clique em **Settings** > **Secrets and variables** > **Actions**
3. Clique em **New repository secret**
4. Configure:
   - **Name**: `AZURE_WEBAPP_PUBLISH_PROFILE`
   - **Value**: Cole o conteúdo XML completo do arquivo .PublishSettings

### 4. ⚠️ Troubleshooting Publish Profile

Se der erro "Publish profile is invalid":

1. **Baixe novamente** o publish profile do Azure Portal
2. **Verifique se copiou tudo** - às vezes editores cortam o final
3. **Confirme o app name** no workflow: `deploy-cicd-hadua2dxe6g2fcbc`
4. **Teste o publish profile** localmente (opcional):
   ```bash
   # Instale Azure CLI
   az webapp deployment source config-zip --resource-group Engenharia_de_Software --name deploy-cicd-hadua2dxe6g2fcbc --src <arquivo-zip>
   ```

### 3. Testar o Deploy

Após configurar o secret, faça push para a branch main:

```bash
git push origin main
```

Monitore o workflow em **Actions** no GitHub.

## 🐛 Troubleshooting

### Erro: "Publish profile is invalid"
- Verifique se copiou TODO o conteúdo do arquivo .PublishSettings
- Certifique-se de que não há quebras de linha extras no secret
- Tente baixar o publish profile novamente do Azure Portal

### Erro: "Deployment Failed"
- Verifique se o nome do App Service no workflow está correto: `deploy-cicd-hadua2dxe6g2fcbc`
- Certifique-se de que o App Service está no estado "Running"

### Verificar se o App Service está funcionando:
1. Vá para o Azure Portal
2. Procure pelo App Service `deploy-cicd-hadua2dxe6g2fcbc`
3. Verifique se está "Running" e não há erros

## ✅ Próximos Passos

1. Configure o secret `AZURE_WEBAPP_PUBLISH_PROFILE`
2. Faça push do código
3. Monitore o deploy em GitHub Actions
4. Teste a aplicação na URL: https://deploy-cicd-hadua2dxe6g2fcbc.eastus2-01.azurewebsites.net
