def test_get_activities(client):
    # Arrange: `reset_activities` fixture ensures pristine state

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    # Known activities from src/app.py
    assert "Chess Club" in data
    assert "Programming Class" in data
