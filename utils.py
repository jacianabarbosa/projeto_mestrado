import os

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def load_base_instructions():
    try:
        with open("base_instructions.txt") as file:
            return file.read().strip()
    except Exception as e:
        raise IOError("Failed to load base instructions: {}".format(e))


def load_openai_client():
    _openai_api_key = os.getenv("OPENAI_API_KEY")
    if not _openai_api_key:
        raise ValueError("The 'OPENAI_API_KEY' environment variable must be set.")

    return OpenAI(api_key=_openai_api_key)
