from flask import url_for


class TestLogin():

    def test_login_view(self, client):
        response = client.get(url_for('user.login'))
        assert response.status_code == 200

    def test_login_user(self, client):
        response = login(client)
        # response = client.get('/signout', follow_redirects=True)
        print(response.data)
        assert b'Hi admin@local.host' in response.data

    # def test_logout(self, client):
    #     login(client)
    #     response = client.get('/signout', follow_redirects=True)
    #     assert b'You have been signed out' in response.data


def login(client, username='admin@local.host', password='password'):
    data = dict(email=username, password=password)

    response = client.post('/login', data=data, follow_redirects=True)

    return response
