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

app = FastAPI()


@app.get("/home")
async def twittertimeline():
    return tweets

@app.get("/{user_name}")
async def twittertimeline(user_name: str):
    user_tweets = [tweet for tweet in tweets if tweet["user_name"] = user_name]
    if not user_tweets:
        return {"error" : f"user: {user_name} not found"}
        return user_tweets
