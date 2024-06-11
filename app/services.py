from typing import Dict, Type

import requests

from config import URL_AFF_NETWORK, KEY_K, URL_OFFER


def create_aff_network_keitaro(data: Dict[str, str]) -> int:
    """
    Create an affiliate network in the keitaro
    :param data: dict containing keys: name, postback_url, offer_param
    :return: id object's in the keitaro
    """
    return (requests.post(
        URL_AFF_NETWORK,
        headers={'Api-Key': KEY_K},
        data=data
    )).json()['id']


def create_offer_keitaro(data: Dict[str, int]) -> int:
    """
    Create an offer in the keitaro
    :param data: dict containing keys: name, action_payload, affiliate_network_id
    :return: id object's in the keitaro
    """

    return (requests.post(
        URL_OFFER,
        headers={'Api-Key': KEY_K},
        data=data
    )).json()['id']


async def add_keitaro_id(model: Type, current_id: int, keitaro_id: int) -> None:
    """
    Add the value - keitaro id to the database
    :param model: obj AffiliateNetwork or Offer
    :param current_id: id in database
    :param keitaro_id: id in keitaro
    """
    await model.filter(id=current_id).update(keitaro_id=keitaro_id)
