class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE_URI = 'sqlite://:memory:'
    YAHOO = "http://ichart.finance.yahoo.com/table.csv?s=AAPL&c=2014"


# lol ya right
class ProductionConfig(Config):
    ASDF = True


class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
