import json
from flask import Blueprint, make_response, jsonify, request
from werkzeug.exceptions import abort
from models import Subscriber
from config import Config

subscriber_bp = Blueprint('subscriber', __name__)


@subscriber_bp.route(Config.FETCH_SUBSCRIBERS_LIST, methods=['GET'])
def fetch_subscribers():
    subscriber = [json.loads(res.to_json()) for res in Subscriber.objects]
    return make_response(jsonify(subscriber), 200)


@subscriber_bp.route(Config.SUBSCRIBE_TO_COVID_ALERT, methods=['POST'])
def subscribe():
    try:
        email = request.json['email']
        try:
            if Subscriber.objects.get(email=email):
                return make_response(jsonify({"email": email+' is already subscribed'}), 400)
        except Subscriber.DoesNotExist:
            pass

        subscribe = Subscriber(email=email)
        subscribe.save()

        return make_response(jsonify({
            "success": "Thank you for subscribing to COVID-19 alerts"
        }), 201)

    except KeyError:
        abort(400)


@subscriber_bp.errorhandler(400)
def invalid_request(error):
    return make_response(jsonify({'error': 'Invalid Request '+error}), 400)
