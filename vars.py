

from os import environ

API_ID = int(environ.get("API_ID", "29777466"))
API_HASH = environ.get("API_HASH", "a04b3df726520026f207079aec2f9879")
BOT_TOKEN = environ.get("BOT_TOKEN", "8677808521:AAFOPTxHetOquXBBI5byQf6c7FRzsa440NY")


# Admin Configuration
ADMINS = list(map(int, environ.get("ADMINS", "8399557684").split()))

# Optional: Bot Owner ID
OWNER_ID = int(environ.get("OWNER_ID", "8399557684"))

# Database URL (if you want to add database support later)
DATABASE_URL = environ.get("DATABASE_URL", "mongodb+srv://girnarimaharaj01_db_user:KsxBY4eoUBwRKXXw@cluster0.6firafk.mongodb.net/?appName=Cluster0")




