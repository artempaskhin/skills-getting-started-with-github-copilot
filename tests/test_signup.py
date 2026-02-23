from urllib.parse import quote


def test_signup_success(client):
    # Arrange
    email = "new_student@mergington.edu"
    activity = "Chess Club"

    # Act
    path = f"/activities/{quote(activity, safe='')}/signup"
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Signed up {email} for {activity}"
    assert email in client.get("/activities").json()[activity]["participants"]


def test_signup_duplicate(client):
    # Arrange: use existing participant
    email = "michael@mergington.edu"
    activity = "Chess Club"
    path = f"/activities/{quote(activity, safe='')}/signup"

    # Act
    resp = client.post(path, params={"email": email})

    # Assert
    assert resp.status_code == 400


def test_signup_activity_not_found(client):
    # Act
    resp = client.post("/activities/NoSuchActivity/signup", params={"email": "x@x.com"})

    # Assert
    assert resp.status_code == 404
