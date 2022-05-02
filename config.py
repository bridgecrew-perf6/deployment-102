import os

class Config:
    NEWS_API_BASE_URL = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=0cff81b85884415aa6f77fb081c448f8'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')




class ProdConfig(Config):
    '''Production configuration child class 
        Args:
            Config: parent configuration class with general configuration settings
    '''
    pass

class DevConfig(Config):
    '''Development configuration chid class
        Args:
            Config:The parent config class with general config settings
    '''
    DEBUG = True

config_options ={
    'development':DevConfig,
    'production':ProdConfig
}