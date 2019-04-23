from movierate.app import create_app
from movierate.extensions import db
from movierate.blueprints.user.models.models import User

app = create_app()
db.app = app

db.drop_all()
db.create_all()

# Only add seed user
user1 = User(username="abc", email="ore@st.com", password="orestone")
db.session.add(user1)
db.session.commit()
