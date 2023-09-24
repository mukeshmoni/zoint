import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "17713634"))
    API_HASH = os.environ.get("API_HASH", "a8c943a69022fef3ac66accc7ba8ce6b")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6443029397:AAFLghTQUsS1oohwMA6O_4CNC-DhTDiOPns")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BVtsOKoBux1pq9BK9Mzb0NtEIqMh7mgAocKNu1u7SsoVStsK0HPkGWzYROHTk1_zAAM3-WXsc_A2I3j7aYZKE252PrAPI8Qc7_55TKIXb90DrXtfTbPvKwST0ZSVU3lP1E5pRuqiH5PY1gfiNooH4yXG78OlFT5Fsy2p0VCEMxeCZ5ImNogXjFYA2snz_rkLLZdqdddRe6hK0msq4drRGANh1FVfjL2xzMEsMK02F_0P0EZ-PH4BJi7jpSOdeFfHDSen_bY-GAAlB8lZ7wTzldaVQ6bD3iv9eqs7fu6yuXI2NrblFC_0CLwuYA8UHst3mGy7eTftvLaD9vDa1HtA1N96g2OMG3o=")
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
