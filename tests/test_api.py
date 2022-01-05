from unittest import TestCase
from fastapi.testclient import TestClient

from app.main import app as web_app 


class APITestCase(TestCase):

  def setUp(self):
    self.client = TestClient(web_app)
    

  def test_main_url(self):
    response = self.client