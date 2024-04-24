- Adicione sua API KEY do chat gpt em um arquivo ".env"

Ele deve estar na sintaxe:

```
OPENAI_API_KEY="sua_openai_key"
```

- Crie um ambiente virtual e instale as dependências

```sh
python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt
```

- Rode o aplicativo (desenvolvimento)

```sh
uvicorn main:app --reload

py -m uvicorn main:app --reload
```
