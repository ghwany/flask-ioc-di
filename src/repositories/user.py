from repositories.base import BaseRepository
from models.user import UserModel


class UserRepository(BaseRepository):
    def __init__(self) -> None:
        super().__init__(UserModel)
