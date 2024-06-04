from typing import Dict, Type

from fastapi import FastAPI, Request, Form

import requests
from starlette import status
from starlette.responses import JSONResponse, HTMLResponse
from starlette.templating import Jinja2Templates

from config import URL_AFF_NETWORK, URL_OFFER, KEY_K
from database import init_db
from models import AffiliateNetwork, Offer

app = FastAPI()
init_db(app)
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def load_start_page(request: Request) -> HTMLResponse:
    """
    Render start html-page
    """
    return templates.TemplateResponse(
        request=request,
        name="network.html"
    )


@app.post("/aff_network", status_code=status.HTTP_201_CREATED)
async def create_aff_network(
        request: Request,
        name: str = Form(),
        postback_url: str = Form(),
        offer_param: str = Form()
) -> HTMLResponse:
    """
    Create an affiliate network in the database
    :return: id object's in the database
    """
    data_aff_network = {
        'name': name,
        'postback_url': postback_url,
        'offer_param': offer_param
    }
    aff_network_id = (await AffiliateNetwork.create(**data_aff_network)).id
    await add_keitaro_id(
        AffiliateNetwork,
        aff_network_id,
        create_aff_network_keitaro(data_aff_network)
    )
    return templates.TemplateResponse(
        request=request,
        name="offer.html",
        context={'network_id': aff_network_id}
    )


@app.get("/aff_network_keitaro", status_code=status.HTTP_201_CREATED)
def create_aff_network_keitaro(data: Dict[str, str]) -> int:
    """
    Create an affiliate network in the keitaro
    :return: id object's in the keitaro
    """
    response = requests.post(
        URL_AFF_NETWORK,
        headers={'Api-Key': KEY_K},
        data=data
    )
    return response.json()['id']


@app.get("/add_keitaro_id", status_code=status.HTTP_201_CREATED)
async def add_keitaro_id(model: Type, current_id: int, keitaro_id: int) -> None:
    """
    Add the value - keitaro id to the database
    :param model: obj AffiliateNetwork or Offer
    :param current_id: id in database
    :param keitaro_id: id in keitaro
    """
    await model.filter(id=current_id).update(keitaro_id=keitaro_id)


@app.post("/offer", status_code=status.HTTP_201_CREATED)
async def create_offer(
        request: Request,
        name: str = Form(),
        affiliate_network_id: int = Form(),
        action_payload: str = Form()) -> HTMLResponse:
    """
    Create an offer in the database
    :return: id object's in the database
    """
    data_offer = {
        'name': name,
        'affiliate_network_id': affiliate_network_id,
        'action_payload': action_payload
    }
    offer_id = (await Offer.create(**data_offer)).id
    await add_keitaro_id(Offer, offer_id, create_offer_keitaro(data_offer))
    return templates.TemplateResponse(
        request=request,
        name="search.html",
        context={'offer_id': offer_id}
    )


@app.get("/offer_keitaro", status_code=status.HTTP_201_CREATED)
def create_offer_keitaro(data: Dict[str, int]) -> int:
    """
    Create an offer in the keitaro
    :return: id object's in the keitaro
    """
    response = requests.post(
        URL_OFFER,
        headers={'Api-Key': KEY_K},
        data=data
    )
    return response.json()['id']


@app.post("/get_aff_network_keitaro", status_code=status.HTTP_200_OK)
async def get_aff_network_keitaro(
        request: Request,
        network_id: int = Form()) -> JSONResponse:
    """
    Get detailed information about affiliate network from keitaro
    """
    keitaro_id = await AffiliateNetwork.filter(id=network_id).values('keitaro_id')
    response = requests.get(
        f'{URL_AFF_NETWORK}/{keitaro_id}',
        headers={'Api-Key': KEY_K}
    )
    return response.json()


@app.post("/get_offer_keitaro", status_code=status.HTTP_200_OK)
async def get_offer_keitaro(
        request: Request,
        offer_id: int = Form()) -> JSONResponse:
    """
    Get detailed information about offer from keitaro
    """
    keitaro_id = await Offer.filter(id=offer_id).values('keitaro_id')
    response = requests.get(
        f'{URL_OFFER}/{keitaro_id}',
        headers={'Api-Key': KEY_K}
    )
    return response.json()


