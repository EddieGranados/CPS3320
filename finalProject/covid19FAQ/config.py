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
        "QnAKnowledgebaseId", "")
    QNA_ENDPOINT_KEY = os.environ.get(
        "QnAEndpointKey", "")
    QNA_ENDPOINT_HOST = os.environ.get(
        "QnAEndpointHostName", "")
