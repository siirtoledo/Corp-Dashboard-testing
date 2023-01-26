import requests
from fastapi import status


#from .main import app

#client = TestClient(app)
ENDPOINT = "https://demo.api.payer.serenity.health"


#client = TestClient(ENDPOINT)

def test_signup_returns_correct():
    url = f"{ENDPOINT}/v1/users/sign-up"
    response = requests.post(
        url,
        json={
            "first_name": "onyed",
            "last_name": "onyed",
            "full_name": "onyed onyed",
            "last_used_organization_name": "Serenity",
            "last_used_organization_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "mobile": "+233506948022",
            "national_mobile_number": "+233506948022",
            "email": "onyed@gmail.com",
            "uuid": "726a7bef-4aa4-4faf-a0da-dc0ebbb558f7",
            "password": "string098",
            "created_at": "2023-01-25T07:53:37.937844",
            "updated_at": "2023-01-25T07:53:37.937848"})
   # print(response)
    print(response.status_code)
    assert response.status_code == status.HTTP_200_OK
    assert response.json()


def test_signup_for_existing_credential_returns_correct():
    url = f"{ENDPOINT}/v1/users/sign-up"
    response = requests.post(
        url,
        json={
            "first_name": "onyed",
            "last_name": "onyed",
            "full_name": "onyed onyed",
            "last_used_organization_name": "Serenity",
            "last_used_organization_id": "3fa85f64-5717-4562-b3fc-2c963f66afa6",
            "mobile": "+233506948022",
            "national_mobile_number": "+233506948022",
            "email": "onyed@gmail.com",
            "uuid": "726a7bef-4aa4-4faf-a0da-dc0ebbb558f7",
            "password": "string098",
            "created_at": "2023-01-25T07:53:37.937844",
            "updated_at": "2023-01-25T07:53:37.937848"})
   # print(response)
    # print(response.status_code)
    assert response.status_code == 400
    assert response.json()