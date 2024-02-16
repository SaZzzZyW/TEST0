import requests
import json

def test_api_returns_correct_http_status_code_for_successful_request():
    response = requests.get('https://petstore.swagger.io/')
    assert response.status_code == 200




def test_api_returns_correct_http_status_code_for_request_with_invalid_parameters():
    response = requests.get('https://petstore.swagger.io/', params={'invalid_param': 123})
    assert response.status_code == 400




def test_api_returns_correct_data_format_for_request_with_incorrect_parameters():
    try:
        response = requests.get('https://petstore.swagger.io/', params={'invalidParam': 'value'})
        
        assert response.status_code != 200
    except requests.exceptions.HTTPError as e:
        
        assert e.response.status_code == 400  
