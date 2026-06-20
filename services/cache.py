import os

from redis import Redis
from dotenv import load_dotenv

load_dotenv()

redis_client = Redis(
    host=os.getenv("REDIS_HOST"),
    port=int(os.getenv("REDIS_PORT")),
    decode_responses=True
)
