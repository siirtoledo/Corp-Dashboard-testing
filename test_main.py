import pytest
import json
import requests

ENDPOINT = "https://demo.api.payer.serenity.health"


def test_login():
    url = f"{ENDPOINT}/v1/login/access-token"
    headers = {'accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded'}
    # print(url)
    response = requests.post(
        url,
        headers=headers,
        data={
            "grant_type": "",
            "username": "ronald@example.com",
            "password": "string232",
            "scope": "",
            "client_id": "",
            "client_secret": "",

        }
    )
    # print(response.status_code)
    # print(response)
    assert response.status_code == 200
    assert response.json()


def test_for_invalid_credential_login():
    url = f"{ENDPOINT}/v1/login/access-token"
    headers = {'accept': 'application/json',
               'Content-Type': 'application/x-www-form-urlencoded'}
    # print(url)
    response = requests.post(
        url,
        headers=headers,
        data={
            "grant_type": "",
            "username": "ronald23@example.com",
            "password": "string32",
            "scope": "",
            "client_id": "",
            "client_secret": "",

        }
    )
    # print(response.status_code)
    # print(response)
    assert response.status_code == 400
    assert response.json()

