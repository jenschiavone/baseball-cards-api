from app import db
from app import ma


class Team(db.Model):
    __tablename__ = 'teams'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String())
    locale = db.Column(db.String())
    league_id = db.Column(db.String())

    def __init__(self, name, locale, league_id):
        self.name = name
        self.locale = locale
        self.league_id = league_id


class TeamSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Team

    id = ma.auto_field
    name = ma.auto_field
    locale = ma.auto_field
    league_id = ma.auto_field


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
