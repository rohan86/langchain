# SnowBot ❄️


## Description

The querybot leverages Azure Open AI to help generate ANSI standard SQL queries from user input provided in natural langauge. Further leveraging Langchain framework quries are submitted to Snowflake and output is rendered on UI that is built with Streamlit 

## Getting Started

### Pre Reqs

Please ensure you have the following:

An Azure Open AI service account with a deployed GPT-3.5 model.The OpenAI Key and OpenAI URL for your Azure Open AI service deployment.
If you haven't set up an Azure Open AI service account and deployed the GPT-3.5 model, follow these steps:

Sign in to the Azure portal at https://portal.azure.com.
Refer to the Microsoft Learn guide for detailed steps on deploying the GPT-3.5 model.
Retrieve the OpenAI Key and OpenAI URL from your Azure Open AI service account.

### Installing

```
pip install -r requirements.txt
```

### Executing program

```
steamlit main.py
```

## Version History

* 0.1
    * Initial Release

