def server_starts(client):
    assert client.get('/spurious-url').status_code == 404
