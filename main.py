from fastapi import FastAPI
# Instacia o FastAPI
app = FastAPI()
# Cria uma rota de GET com o path "/"
@app.get("/")
def read_root():
# Retorna um JSON simples com Hello World
    return {"Hello": "World!"}

# Cria uma rota de GET com o path "/items/{item_id}"
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str = None):
# Retorna um JSON com o item_id e o parâmetro q (opcional)
    return {"item_id": item_id, "q": q}