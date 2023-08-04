from pathlib import Path
from pydantic import SecretStr
from pydantic_settings import BaseSettings


class BotSettings(BaseSettings):
    token: SecretStr = SecretStr("6495793463:AAFz1HbAlKdohMbPAkocrfjbMtPRu3rXalU")
    
class StaticSettings(BaseSettings):
    path: Path = Path("/home/kiortir/projects/photobot/static")
