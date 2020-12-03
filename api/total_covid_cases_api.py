import json
from flask import Blueprint, make_response, jsonify, request
from werkzeug.exceptions import abort
from models import TotalCases
from config import Config

total_covid_cases_bp = Blueprint('total_covid_cases', __name__)


@total_covid_cases_bp.route(Config.FETACH_TOTAL_COVID_CASES, methods=['GET'])
def fetch_total_covid_cases():
    total_cases = [json.loads(res.to_json()) for res in TotalCases.objects]
    return make_response(jsonify(total_cases), 200)


@total_covid_cases_bp.route(Config.ADD_TOTAL_COVID_CASES, methods=['POST'])
def add_total_covid_cases():
    try:
        total_confirmed = request.json['total_confirmed']
        total_deaths = request.json['total_deaths']
        total_recovered = request.json['total_recovered']
        last_date_updated = request.json['last_date_updated']

        total_cases = TotalCases(total_confirmed=total_confirmed,
                                total_deaths=total_deaths,
                                total_recovered=total_recovered,
                                last_date_updated=last_date_updated)
        total_cases.save()

        return make_response(jsonify({
            "success": request.json
        }), 201)

    except KeyError:
        abort(400)


@total_covid_cases_bp.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Invalid Request '+error}), 400)
