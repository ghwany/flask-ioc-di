from models.user import UserModel
from repositories.user import UserRepository
from dtos.user import CreateUserDTO


class UserService:
    def __init__(self, repository: UserRepository) -> None:
        self.repository = repository

    def create(self, dto: CreateUserDTO) -> UserModel:
        user = dto.to_entity()
        self.repository.save(user)
        return user

    def get_by_id(self, id: str) -> UserModel:
        user = self.repository.findOne(id=id)
        return user

    def get_all(self) -> list:
        users = self.repository.find()
        return users
