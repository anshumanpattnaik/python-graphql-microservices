from mongoengine import connect

class Config:
    # API Configs
    API_PATH = '/api/'
    API_VERSION = 'v1'
    BASE_URL = 'http://127.0.0.1:5000'

    # GraphQL Endpoint
    GRAPTH_QL = API_PATH+API_VERSION+'/graphql'

    # Total Covid cases Endpoint
    ADD_TOTAL_COVID_CASES = API_PATH+API_VERSION+'/add_total_cases'
    FETCH_TOTAL_COVID_CASES = API_PATH+API_VERSION+'/fetch_total_cases'

    # Statistics Endpoint
    ADD_STATISTICS = API_PATH+API_VERSION+'/add_statistics'
    FETCH_STATISTICS = API_PATH+API_VERSION+'/fetch_statistics'

    # Covid News Subscription Endpoint
    SUBSCRIBE_TO_COVID_ALERT = API_PATH+API_VERSION+'/subscribe'
    FETCH_SUBSCRIBERS_LIST = API_PATH+API_VERSION+'/fetch_subscribers'

    def connect_db():
        connect('covid-19', host='mongodb://127.0.0.1:27017', alias='default')