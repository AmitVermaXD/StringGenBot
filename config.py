from os import getenv
from dotenv import load_dotenv

load_dotenv()

API_ID = int(getenv("27890167"))
API_HASH = getenv("f31f6f41da08fc767c626931eade82c9")

BOT_TOKEN = getenv("6670342404:AAHwMhGtlwGdl7ys4vcF_w03jviSgO7EYxM")
OWNER_ID = int(getenv("6227452199"))

MONGO_DB_URI = getenv("mongodb+srv://kaushalxraja:JSck0@cluster0.dfvemtb.mongodb.net/?retryWrites=true&w=majority")
MUST_JOIN = getenv("MUST_JOIN", None)
