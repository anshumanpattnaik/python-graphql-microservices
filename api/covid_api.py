import json
from flask import Blueprint, make_response, jsonify, request
from werkzeug.exceptions import abort
from models import States, Statistics
from config import Config

covid_bp = Blueprint('covid', __name__)

@covid_bp.route(Config.FETCH_STATISTICS, methods=['GET'])
def fetch_statistics():
    statistics = [json.loads(res.to_json()) for res in Statistics.objects]
    return make_response(jsonify({'success': statistics}), 200)

@covid_bp.route(Config.ADD_STATISTICS, methods=['POST'])
def add_statistics():
    try:
        for data in request.json['country_statistics']:
            country = data['country']
            code = data['code']
            flag = data['flag']
            coordinates = data['coordinates']
            confirmed = data['confirmed']
            deaths = data['deaths']
            recovered = data['recovered']

            all_states = []
            for state in data['states']:
                states = States(key=state['key'], name=state['name'],
                                address=state['address'],
                                latitude=state['latitude'],
                                longitude=state['longitude'],
                                confirmed=state['confirmed'],
                                deaths=state['deaths'],
                                recovered=state['recovered'])
                states.save()
                all_states.append(states)

            statistics = Statistics(country=country,
                                    code=code,
                                    flag=flag,
                                    coordinates=coordinates,
                                    confirmed=confirmed,
                                    deaths=deaths,
                                    recovered=recovered,
                                    states=all_states)
            statistics.save()

        return make_response(jsonify({
            "success": request.json
        }), 201)

    except KeyError:
        abort(400)


@covid_bp.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Invalid Request '+error}), 400)
