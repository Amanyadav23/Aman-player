# Adityahalder
from motor.motor_asyncio import AsyncIOMotorClient as _mongo_client_
from pymongo import MongoClient
from pyrogram import Client

from AdityaHalder.utilities import config
from AdityaHalder.console import LOGGER

TEMP_MONGODB = "mongodb+srv://aman:amanbhai2121@cluster0.eje8lmr.mongodb.net/?retryWrites=true&w=majority"


if config.MONGO_DB_URL is None:
    LOGGER(__name__).warning(
        "š„ ššØ ššØš§š šØ šš šš«š„ ššØš®š§š āØ...\n\nš¹ ššØš®š« ššØš­ šš¢š„š„ ššØš«š¤ šš§\nššš¢š­š²š'š¬ ššš­šššš¬š āØ ..."
    )
    temp_client = Client(
        "Aditya",
        bot_token=config.BOT_TOKEN,
        api_id=config.API_ID,
        api_hash=config.API_HASH,
    )
    temp_client.start()
    info = temp_client.get_me()
    username = info.username
    temp_client.stop()
    _mongo_async_ = _mongo_client_(TEMP_MONGODB)
    _mongo_sync_ = MongoClient(TEMP_MONGODB)
    mongodb = _mongo_async_[username]
    pymongodb = _mongo_sync_[username]
else:
    _mongo_async_ = _mongo_client_(config.MONGO_DB_URL)
    _mongo_sync_ = MongoClient(config.MONGO_DB_URL)
    mongodb = _mongo_async_.Aditya
    pymongodb = _mongo_sync_.Aditya
