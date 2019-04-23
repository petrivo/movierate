import click
import subprocess


@click.command()
def start_app():
    subprocess.call(
        'gunicorn -b 0.0.0.0:8000 --access-logfile - "movierate.app:create_app()"', shell=True)


@click.command()
def dbinit():
    from movierate.app import create_app
    from movierate.extensions import db
    from movierate.blueprints.user.models.models import User

    app = create_app()
    db.app = app

    db.drop_all()
    db.create_all()

    # Only add seed user
    user1 = User(email="ore@st.com", password="orestone")
    db.session.add(user1)
    db.session.commit()

    click.echo('Seed user was created')
