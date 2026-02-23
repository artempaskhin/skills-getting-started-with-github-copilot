def test_root_redirect(client):
    # Act: do not follow redirects so we can assert the Location header
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code in (301, 302, 307, 308)
    assert resp.headers.get("location") == "/static/index.html"
