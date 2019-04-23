from movierate.extensions import db


class ResourceMixin():
    def save(self):
        db.session.add(self)
        db.session.commit()
