# Sample Streamlit App Deploying to Azure

## Reference Material:
- https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux
- https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743
- https://towardsdatascience.com/beginner-guide-to-streamlit-deployment-on-azure-f6618eee1ba9
- https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant

## Commands
```
az login --tenant "XXXX-YYYY-ZZZZ-111-aaaaaaaaa"

az acr build --registry mmxarc --resource-group mmx-cog-search-rg --image census-app .

az appservice plan create --name mmAppServicePlan --resource-group mmx-cog-search-rg --is-linux

az webapp create --resource-group mmx-cog-search-rg --plan mmAppServicePlan --name mmanotherapp --deployment-container-image-name mmxarc.azurecr.io/census-app:latest

az webapp config appsettings set --resource-group mmx-cog-search-rg --name mmanotherapp --settings WEBSITES_PORT=80


#Access Diagnostic Logs:
https://learn.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux&tabs=azure-cli#viii-access-diagnostic-logs

az webapp log tail --name mmanotherapp --resource-group mmx-cog-search

az webapp log config --name mmanotherapp --resource-group mmx-cog-search --docker-container-logging filesystem

#inspect log files by going to:
https://mmanotherapp.scm.azurewebsites.net/api/logs/docker

```