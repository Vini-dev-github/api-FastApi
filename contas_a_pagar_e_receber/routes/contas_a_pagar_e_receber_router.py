from fastapi import APIRouter
from pydantic import BaseModel
from decimal import Decimal
from typing import List

router = APIRouter(prefix="/contas_a_pagar_e_receber")

class ContaPagarReceberResponse(BaseModel):
    id: int
    descricao: str
    valor: Decimal
    tipo: str #Pagar, Receber

class ContaPagarReceberRequest(BaseModel):
    descricao: str
    valor: Decimal
    tipo: str #Pagar, Receber

@router.get("/", response_model=List[ContaPagarReceberResponse])
def listar_contas():
    return [
        ContaPagarReceberResponse(
            id= 1,
            descricao= "Aluguel",
            valor= 1000,
            tipo= "PAGAR",
        ),
        ContaPagarReceberResponse(
            id= 2,
            descricao= "Salario",
            valor= 5000,
            tipo= "RECEBER",
        ),
    ]

@router.post("/", response_model=ContaPagarReceberResponse, status_code= 201)
def criar_conta(conta: ContaPagarReceberRequest):
    return ContaPagarReceberResponse(
        id=3,
        descricao= conta.descricao,
        valor= conta.valor,
        tipo= conta.tipo

    )
