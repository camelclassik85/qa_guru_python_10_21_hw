import os
from dotenv import load_dotenv
from utils.resource import path
from pydantic import BaseModel

dotenv_path = path('.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    load_dotenv()


class Config(BaseModel):
    user_name: str
    access_key: str
    base_url: str
    timeout: float


config = Config(
    user_name=os.getenv('USER_NAME'),
    access_key=os.getenv('ACCESS_KEY'),
    base_url=os.getenv('BASE_URL'),
    timeout=float(os.getenv('TIMEOUT'))
)
