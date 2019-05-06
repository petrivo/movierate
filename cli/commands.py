import click
import subprocess

import os


@click.command()
def start_app():
    subprocess.call(
        'gunicorn -b 0.0.0.0:8100 --reload --access-logfile - "movierate.app:create_app()"', shell=True)


@click.command()
def loc():
    subprocess.call('git ls-files | xargs wc -l', shell=True)

@click.command()
def dbinit():
    from movierate.app import create_app
    from movierate.extensions import db
    from movierate.blueprints.user.models.user import User

    app = create_app()
    db.app = app

    db.drop_all()
    db.create_all()

    # Only add seed user
    user1 = User(email="ore@st.com", password="orestone")
    db.session.add(user1)
    db.session.commit()

    click.echo('Seed user was created')


@click.command()
@click.argument('path', default=os.path.join('movierate', 'tests'))
def tests(path):
    click.echo('test')
    cmd = 'py.test {0}'.format(path)
    return subprocess.call(cmd, shell=True)
