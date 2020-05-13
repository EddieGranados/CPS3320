#!/usr/bin/env python3
import os

class DefaultConfig:
    # """ Bot Configuration """

    # PORT = 3978
    # APP_ID = os.environ.get("MicrosoftAppId", "")
    # APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")
    
    """ Bot Configuration """
    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "")

    QNA_KNOWLEDGEBASE_ID = os.environ.get(
        "QnAKnowledgebaseId", "3274199d-4739-4dfa-b21b-ffdc4afe6b7d")
    QNA_ENDPOINT_KEY = os.environ.get(
        "QnAEndpointKey", "cb523b38-0d94-4600-a423-58b2061c9e0f")
    QNA_ENDPOINT_HOST = os.environ.get(
        "QnAEndpointHostName", "https://myfirstqnaeg.azurewebsites.net/qnamaker")
