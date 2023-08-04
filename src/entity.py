from pydantic import BaseModel


class Message(BaseModel):
    chat_id: int
    file_id: str
    mime: str
    flags: list[str]