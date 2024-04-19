import tweepy
import telegram

# Twitter API credentials
consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_key = "your_access_key"
access_secret = "your_access_secret"

# Telegram Bot API credentials
bot_token = "your_bot_token"
chat_id = "your_chat_id"

# Authenticate Twitter API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# Authenticate Telegram Bot API
bot = telegram.Bot(token=bot_token)

# Twitter user to follow
twitter_user = "user_to_follow"

# Retrieve latest tweet from user's timeline
latest_tweet = api.user_timeline(screen_name=twitter_user, count=1)[0]

# Send tweet to Telegram channel
bot.send_message(chat_id=chat_id, text=latest_tweet.text)
