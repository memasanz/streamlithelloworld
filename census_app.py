import streamlit as st
import numpy as np 
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



#has to open port on application setting and make sure the port 80 was opened.

#https://docs.microsoft.com/en-us/azure/app-service/tutorial-custom-container?pivots=container-linux
# https://towardsdatascience.com/deploying-a-streamlit-web-app-with-azure-app-service-1f09a2159743
# https://towardsdatascience.com/beginner-guide-to-streamlit-deployment-on-azure-f6618eee1ba9
#https://learn.microsoft.com/en-us/azure/app-service/configure-authentication-provider-aad?tabs=workforce-tenant


# az acr build --registry acrcensusapp --resource-group CensusApp --image census-app .
# az appservice plan create --name mmAppServicePlan --resource-group CensusApp --is-linux
# az webapp create --resource-group CensusApp --plan mmAppServicePlan --name mmanotherapp --deployment-container-image-name acrcensusapp.azurecr.io/census-app:latest
# az webapp config appsettings set --resource-group CensusApp --name mmanotherapp --settings WEBSITES_PORT=80
# az webapp log config --name mmanotherapp --resource-group CensusApp --docker-container-logging filesystem
# az webapp log tail --name mmanotherapp --resource-group CensusApp
# az webapp create -g CensusApp -p CensusAppServicePlan -n xmmcensus-web-app -i xmmcensusappregistry.azurecr.io/census-app:latest
# az webapp create -g MyResourceGroup -p MyPlan -n MyUniqueAppName -i myregistry.azurecr.io/docker-image:tag



st.image(image='azure-openai.jpg',caption='https://learn.microsoft.com/en-us/azure/ai-services/openai/overview')

st.title('Hello world!')

st.sidebar.markdown("Streamlit Sample [Streamlit](https://www.streamlit.io) and [AzureOpenAI](https://learn.microsoft.com/en-us/azure/cognitive-services/openai/overview)", unsafe_allow_html=True)

