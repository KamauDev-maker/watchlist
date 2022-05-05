import os

class Config:
    """
    """
    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://oscar:4321@localhost/watchlist'
    
class ProdConfig(Config):
    """_summary_

    Args:
        Config (_type_): _description_
    """
    pass
class DevConfig(Config):
    """_summary_

    Args:
        config (_type_): _description_
    """
    DEBUG = True 
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}