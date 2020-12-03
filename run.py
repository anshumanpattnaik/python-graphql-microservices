from api.subscriber_api import subscriber_bp
from api.total_covid_cases_api import total_covid_cases_bp
from api.covid_api import covid_bp
from flask import Flask
from flask_graphql import GraphQLView
from config import Config
from schema import schema

app = Flask(__name__)
app.debug = True

app.register_blueprint(covid_bp)
app.register_blueprint(total_covid_cases_bp)
app.register_blueprint(subscriber_bp)

app.add_url_rule(
    Config.GRAPTH_QL,
    view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True)
)

if __name__ == '__main__':
    Config.connect_db()
    app.run()