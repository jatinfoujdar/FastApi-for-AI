from fastapi import FastAPI
import time


# in memory tweets
tweets = [
  {
    "timestamp": "20240929101921",
    "tweet": "Hello AI",
    "user_name": "c17hawke"
  },
  {
    "timestamp": "20240929101930",
    "tweet": "Hello world!",
    "user_name": "c17hawke"
  },
  {
    "timestamp": "20240929102013",
    "tweet": "Its an amazing day!",
    "user_name": "User1"
  }
]
def get_timestamp() -> str:
    return time.strtime("%Y%m%d%H%M%S")


app = FastAPI()


@app.get("/home")
async def twittertimeline():
    return tweets

@app.get("/{user_name}")
async def user_timeline(user_name: str):
    user_tweets = [tweet for tweet in tweets if tweet["user_name"] = user_name]
    if not user_tweets:
        return {"error" : f"user: {user_name} not found"}
        return user_tweets


@app.post("/{user_name}")
async def user_timeline(user_name: str, tweet: dict):
  user_tweets = [tweet for tweet in tweets if tweet["user_name"] = user_name]
  new_tweet = {
     "timestamp": get_timestamp(),
    "tweet": tweet["tweet"],
    "user_name": user_name
  }
  tweets.append(new_tweet)
  return new_tweet