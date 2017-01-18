import os

# configuration
MY_CONSUMER_KEY = os.environ["CONSUMER_KEY"]
MY_CONSUMER_SECRET = os.environ["CONSUMER_SECRET"]
MY_ACCESS_TOKEN_KEY = os.environ["ACCESS_TOKEN_KEY"]
MY_ACCESS_TOKEN_SECRET = os.environ["ACCESS_TOKEN_SECRET"]

# A list of comma-separated, quote-enclosed Twitter handles of account that you'll generate tweets based on. 
# It should look like ["account1", "account2"]. If you want just one account, no comma needed.
SOURCE_ACCOUNTS = list(filter(lambda x: x, os.environ.get("SOURCE_ACCOUNTS", "").split(","))) 
ODDS = int(os.environ.get("ODDS", 8)) # How often do you want this to run? 1/8 times?
ORDER = int(os.environ.get("ORDER", 2)) # How closely do you want this to hew to sensical? 1 is low and 3 is high.
DEBUG = bool(os.environ.get("DEBUG", False)) # Set this to False to start Tweeting live
STATIC_TEST = bool(os.environ.get("STATIC_TEST", False)) # Set this to True if you want to test Markov generation from a static file instead of the API.
TEST_SOURCE = os.environ.get("TEST_SOURCE", "testcorpus.txt") # The name of a text file of a string-ified list for testing. To avoid unnecessarily hitting Twitter API. You can use the included testcorpus.txt, if needed.
TWEET_ACCOUNT = os.environ.get("TWEET_ACCOUNT", "") # The name of the account you're tweeting to.
