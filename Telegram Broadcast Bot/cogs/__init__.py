# cogs/__init__.py

from . import Text
from . import Image
from . import Delete
from . import Video
from . import Broadcast
from . import Subscribe
from . import List
from . import Help
from . import Download

def register_handlers(bot):
    Broadcast.register_handlers(bot)
    Text.register_handlers(bot)
    Image.register_handlers(bot)
    Delete.register_handlers(bot)
    Video.register_handlers(bot)
    Subscribe.register_handlers(bot)
    List.register_handlers(bot)
    Help.register_handlers(bot)
    Download.register_handlers(bot)
  