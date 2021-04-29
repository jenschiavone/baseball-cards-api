import json
from app import app
from app.models.team import Team, team_schema
from flask import jsonify


@app.route('/teams')
def list_teams():
    teams = Team.query.all()
    results = []
    # TODO this is dumb; fix it
    for team in teams:
        obj = {
            'id': team.id,
            'name': team.name
        }
        results.append(obj)
    response = jsonify(results)
    response.status_code = 200
    return response
