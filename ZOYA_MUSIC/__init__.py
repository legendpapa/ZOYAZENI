from ZOYA_MUSIC.core.bot import ZOYA
from ZOYA_MUSIC.core.dir import dirr
from ZOYA_MUSIC.core.git import git
from ZOYA_MUSIC.core.userbot import Userbot
from ZOYA_MUSIC.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = ZOYA()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
