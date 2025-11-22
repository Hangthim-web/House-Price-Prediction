import os 


class config:
    SECRET_KEY = os.environ.get('SECRET_KEY','dev-secret') # change in production 
    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL','sqlite:///house_price_predictor.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=FALSE
    MODEL_PATH = os.environ.get('MODEL_PATH','model_artifacts/model.pkl') 