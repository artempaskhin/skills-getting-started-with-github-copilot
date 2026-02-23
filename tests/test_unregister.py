from urllib.parse import quote


def test_unregister_success(client):
    # Arrange: existing participant in Chess Club
    email = "michael@mergington.edu"
    activity = "Chess Club"
    pre = client.get("/activities").json()
    assert email in pre[activity]["participants"]

    # Act
    path = f"/activities/{quote(activity, safe='')}/participants"
    resp = client.delete(path, params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json()["message"] == f"Unregistered {email} from {activity}"
    assert email not in client.get("/activities").json()[activity]["participants"]


def test_unregister_participant_not_found(client):
    # Act
    path = f"/activities/{quote('Chess Club', safe='')}/participants"
    resp = client.delete(path, params={"email": "not_there@x.com"})

    # Assert
    assert resp.status_code == 404


def test_unregister_activity_not_found(client):
    # Act
    resp = client.delete("/activities/NoSuchActivity/participants", params={"email": "a@b.com"})

    # Assert
    assert resp.status_code == 404
