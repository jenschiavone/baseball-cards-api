from app import app
from app.models.team import Team, teams_schema


@app.route('/teams')
def list_teams():
    return {
        'results': teams_schema.dump(Team.query.all())
    }
