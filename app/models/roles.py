from sqlalchemy.sql import func

from app import db

# helpers
from .helpers import Helpers

helper = Helpers()


class Role(db.Model):
    """
    Defines properties for an event to generate an event table in the database
    """
    __tablename__ = 'roles'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    created_at = db.Column(db.DateTime(), server_default=func.now())

    def __init__(
        self,
        name='',
        created_at=func.now(),
    ):
        self.name = name
        self.created_at = created_at

    def __str__(self):
        return "Role(id='%s')" % self.id

    def get_role(self, *args):
        role = Role.query.all()
        if len(args) > 0:
            role = Role.query.filter_by(id=args[0])
        return helper.unpack_query_roles_object(role)

    def add_role(self, data):
        role = Role(
            name=data.get('name'),
        )
        db.session.add(role)
        db.session.commit()
        print(role)

    def delete_role(self, role_id):
        role = Role.query.filter_by(id=role_id).first()
        db.session.delete(role)
        db.session.commit()
