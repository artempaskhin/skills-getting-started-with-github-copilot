import copy
import pytest
from fastapi.testclient import TestClient

import src.app as app_module


# Capture a pristine copy of the in-memory activities to restore between tests
_PRISTINE_ACTIVITIES = copy.deepcopy(app_module.activities)


@pytest.fixture(autouse=True)
def reset_activities():
    # Arrange: restore pristine state before each test
    app_module.activities = copy.deepcopy(_PRISTINE_ACTIVITIES)
    yield
    # Cleanup: ensure state is pristine afterwards as well
    app_module.activities = copy.deepcopy(_PRISTINE_ACTIVITIES)


@pytest.fixture()
def client():
    # Provide a TestClient for the FastAPI app
    with TestClient(app_module.app) as c:
        yield c
