from typing import Dict, Union, Type

from fastapi import FastAPI, Body, Request

import requests
from pydantic import BaseModel
from starlette.responses import JSONResponse, HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

from config import URL_AFF_NETWORK, URL_OFFER, KEY_K
from database import init_db
from models import AffiliateNetwork, Offer

app = FastAPI()
init_db(app)


# class Network(BaseModel):
#     name: str
#     postback_url: str
#     offer_param: str
#     offer_param: str
#     notes: str
#     keitaro_id: int

app.mount("/static", StaticFiles(directory="static"), name="static")


templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def start(request: Request):
    return templates.TemplateResponse(
        request=request, name="start.html", context={"id": id}
    )


@app.post("/aff_network")
async def create_aff_network(data: Dict[str, str] = Body()) -> int:
    """
    Create an affiliate network in the database
    :return: id object's in the database
    """
    aff_network_id = (await AffiliateNetwork.create(**data)).id
    await add_keitaro_id(AffiliateNetwork, aff_network_id, create_aff_network_keitaro(data))
    return aff_network_id


@app.get("/aff_network_keitaro")
def create_aff_network_keitaro(data: Dict[str, str]) -> int:
    """
    Create an affiliate network in the keitaro
    :return: id object's in the keitaro
    """
    return requests.post(
        URL_AFF_NETWORK,
        headers={'Api-Key': KEY_K},
        data=data
    ).json()['id']


@app.post("/offer")
async def create_offer(data: Dict[str, Union[str, int]] = Body()) -> int:
    """
    Create an offer in the database
    :return: id object's in the database
    """
    offer_id = (await Offer.create(**data)).id
    await add_keitaro_id(Offer, offer_id, create_offer_keitaro(data))
    return offer_id


@app.get("/offer_keitaro")
def create_offer_keitaro(data: Dict[str, int]) -> int:
    """
    Create an offer in the keitaro
    :return: id object's in the keitaro
    """
    return requests.post(
        URL_OFFER,
        headers={'Api-Key': KEY_K},
        data=data
    ).json()['id']


@app.post("/get_aff_network_keitaro")
def get_aff_network_keitaro(data: Dict[str, int] = Body()) -> JSONResponse:
    """
    Get detailed information about affiliate network from keitaro
    """
    id_keitaro = data['id']
    return requests.get(
        f'{URL_AFF_NETWORK}/{id_keitaro}',
        headers={'Api-Key': KEY_K}
    ).json()


@app.post("/get_offer_keitaro")
def get_offer_keitaro(data: Dict[str, int] = Body()) -> JSONResponse:
    """
    Get detailed information about offer from keitaro
    """
    id_keitaro = data['id']
    return requests.get(
        f'{URL_OFFER}/{id_keitaro}',
        headers={'Api-Key': KEY_K}
    ).json()


@app.get("/add_keitaro_id")
async def add_keitaro_id(model: Type, id_current: int, keitaro_id: int):
    await model.filter(id=id_current).update(keitaro_id=keitaro_id)