import fastapi

api = fastapi.FastAPI()

response = {"Ответ": "Который возвращает сервер"}


@api.get('/')
def index():
    return response
