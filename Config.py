import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17713634"))
    API_HASH = os.environ.get("API_HASH", "a8c943a69022fef3ac66accc7ba8ce6b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443029397:AAFLghTQUsS1oohwMA6O_4CNC-DhTDiOPns")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQAtV1fEhl3iexzF4dMp0kv_q8CuVyTVdSwLz6e9DUsgQdWJDiv5ek_kB0Qj6BLJLeeXmqeVjyS_QDcemzMuUQEj4Ri_lOquqiRJoDnK90SWU7sRBAVmnfsOjLRe3YafnWMEo95QLOPrNAYVObx43_3LLru2Rue0K54AcKTG6upq8y1mDqGV4qBr2jNvG7YHR4DHd_FBDI-jbsZZUPcukzxyKYyzzHNBDP0U2b_Nnrq1W4ZGSXjkq4gXQKyMyAT4WWnXYUXSDCxd5FDoHZREIr-1_GVpZZXoxJtbyK8E35k-SD3DKq6ZuAmh2iSibuwijxvrUMH4q3Pxsuy4qV9rFF1kAAAAAYxVunwA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "MoniMineBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/3d8ecee0ba7dddfc6fce4.jpg")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6649395836")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
