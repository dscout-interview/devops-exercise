from app import app


def test_hello():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Hello, dscout!"


def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}


def test_login_calls_elixscout(mocker):
    mock_resp = mocker.Mock()
    mock_resp.json.return_value = {"authenticated": True}
    mocker.patch("app.requests.get", return_value=mock_resp)

    client = app.test_client()
    response = client.get("/login")
    assert response.status_code == 200
    assert response.get_json() == {"authenticated": True}
