from aiogram import Bot, Dispatcher
from data import config
from baza.postgresql import Database

ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS
MOVIE_CHANNEL = config.MOVIE_CHANNEL

bot = Bot(TOKEN)
db = Database()
dp = Dispatcher()