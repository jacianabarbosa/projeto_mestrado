from typing import List

from fastapi import HTTPException
from openai import APIError
from pydantic import BaseModel

from factory import create_app
from utils import load_base_instructions, load_openai_client

base_instructions = load_base_instructions()
openai_client = load_openai_client()

app = create_app()


class Message(BaseModel):
    role: str
    content: str


class ChatInput(BaseModel):
    messages: List[Message]


base_instructions = "This is your assistant speaking."


@app.get("/")
async def root():
    return {"message": "API is ready to receive requests."}


@app.post("/ask-gpt")
async def gpt_response(chat_input: ChatInput):
    # Processa as mensagens para garantir que as roles estão corretas
    processed_messages = [
        "assistant" if msg.role == "gpt" else msg.role for msg in chat_input.messages
    ]

    messages = [{"role": "system", "content": base_instructions}] + processed_messages

    try:
        completion = openai_client.chat.completions.create(
            model="gpt-3.5-turbo",
            response_format={"type": "json_object"},
            messages=messages,
        )

        return {"response": completion.choices[0].message}
    except APIError as e:
        error_info = e.response.json()
        error_message = error_info["error"]["message"]

        print(error_message)

        return {"response": "testing!"}
        raise HTTPException(status_code=e.response.status_code, detail=error_message)
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500, detail="An unexpected error occurred")
