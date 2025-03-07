import os
import time
import tweepy
from dotenv import load_dotenv

# Load env variables
load_dotenv()

# Twitter API Credentials
CONSUMER_KEY = os.getenv("CONSUMER_KEY")
CONSUMER_SECRET = os.getenv("CONSUMER_SECRET")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
ACCESS_TOKEN_SECRET = os.getenv("ACCESS_TOKEN_SECRET")
TWEET_ID = os.getenv("TWEET_ID")

# Initialize client with OAuth 1.0a
client = tweepy.Client(
    consumer_key=CONSUMER_KEY,
    consumer_secret=CONSUMER_SECRET,
    access_token=ACCESS_TOKEN,
    access_token_secret=ACCESS_TOKEN_SECRET
)

# Verify authentication
def verify_authentication():
    try:
        user = client.get_me()
        print(f"Authenticated @{user.data.username}")
        return True
    except tweepy.TweepyException as e:
        print(f"Authentication failed: {e}")
        return False

# Like tweet
def like_tweet(tweet_id):
    for attempt in range(3):
        try:
            response = client.like(tweet_id=tweet_id)
            if response.data['liked']:
                print(f"Successfully liked!")
                return
        except tweepy.TooManyRequests as e:
            print(f"Rate limited. Waiting 60 seconds...")
            time.sleep(60)
        except tweepy.Forbidden as e:
            print(f"Permission error: {e}")
            break
        except tweepy.NotFound as e:
            print(f"Tweet not found: {e}")
            break
        except tweepy.TweepyException as e:
            print(f"Error: {e}")
            break
    print(f"Failed to like tweet!")

# Verify credentials first
if not verify_authentication():
    exit(1)

like_tweet(TWEET_ID)