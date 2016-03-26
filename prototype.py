from ConfigParser import SafeConfigParser 
import twitter 
from pprint import pprint

configFile = ".credential/.twitter_config"

config = SafeConfigParser()
config.read(configFile)

print config.get('test', 'nimei')

CONSUMER_KEY = config.get('consumer', 'consumer_key')
CONSUMER_SEC = config.get('consumer', 'consumer_secret')

TOKEN_KEY = config.get('token', 'oauth_token_key')
TOKEN_SEC = config.get('token', 'oauth_token_secret')

api = twitter.Api(consumer_key=CONSUMER_KEY,
                  consumer_secret=CONSUMER_SEC,
                  access_token_key=TOKEN_KEY,
                  access_token_secret=TOKEN_SEC
                  )
pprint(api.VerifyCredentials())

#pprint(dir(api))

