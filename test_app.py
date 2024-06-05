from fastapi.testclient import TestClient
from main import app


def test_create_aff_network():
    with TestClient(app) as client:
        aff_data = {
            "name": "467",
            "postback_url": "test_one",
            "offer_param": "test_one",
        }
        response = client.post("/aff_network", json=aff_data)
        assert response.status_code == 201


def test_create_offer():
    with TestClient(app) as client:
        offer_data = {
            "name": "57099",
            "affiliate_network_id": 28,
            "action_payload": "test_one"
        }
        response = client.post("/offer", json=offer_data)
        assert response.status_code == 201


def test_get_aff_network():
    with TestClient(app) as client:
        aff_data = {
            "id": 42
        }
        response = client.post("/get_aff_network_keitaro", json=aff_data)
        assert response.status_code == 200


def test_get_offer_keitaro():
    with TestClient(app) as client:
        offer_data = {
            "id": 19
        }
        response = client.post("/get_offer_keitaro", json=offer_data)
        assert response.status_code == 200
