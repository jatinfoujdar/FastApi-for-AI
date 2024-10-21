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


@app.get("/")
async def root():
    return {"Hello": "World"}


