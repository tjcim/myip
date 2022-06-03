import requests

from myip import myip


def test_get_public_ip(requests_mock):
    requests_mock.get(myip.API, json={"ip": "10.0.0.1"})
    resp = myip.get_public_ip()
    assert resp == "10.0.0.1"


def test_get_public_ip_timeout(requests_mock):
    requests_mock.get(myip.API, exc=requests.exceptions.Timeout)
    resp = myip.get_public_ip()
    assert resp == "Request Timed Out"


def test_get_public_ip_error(requests_mock):
    requests_mock.get(myip.API, exc=requests.exceptions.ConnectionError)
    resp = myip.get_public_ip()
    assert resp == "An error occurred during the request."
