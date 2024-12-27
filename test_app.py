import pytest
from app import app
# Patch Werkzeug if the '__version__' attribute is missing
try:
    import werkzeug
    if not hasattr(werkzeug, '__version__'):
        werkzeug.__version__ = "patched"
except ImportError:
    raise ImportError("Werkzeug is not installed. Please ensure it's included in your dependencies.")
@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client):
    response = client.get("/")
    assert response.status_code == 200