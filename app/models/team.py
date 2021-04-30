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


class League(db.Model):
    __tablename__ = 'leagues'

    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String())


class TeamSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Team
        include_fk = True


class LeagueSchema(ma.SQLAlchemySchema):
    class Meta:
        model = League

    id = ma.auto_field()
    name = ma.auto_field()


team_schema = TeamSchema()
teams_schema = TeamSchema(many=True)
