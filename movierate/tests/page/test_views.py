from flask import url_for


class TestViews():
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == 200