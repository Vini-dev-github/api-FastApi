
import uvicorn
from fastapi import FastAPI
from contas_a_pagar_e_receber.routes import contas_a_pagar_e_receber_router


app = FastAPI()

@app.get("/")
def sou_programador():
    return "Hell-o world"

app.include_router(contas_a_pagar_e_receber_router.router)

if __name__ == "main":
    uvicorn.run(app, host="127.0.0.1", port=8000)
