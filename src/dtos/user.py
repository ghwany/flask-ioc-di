from models.user import UserModel


class CreateUserDTO:

    id: str
    name: str
    password: str

    def to_entity(self) -> UserModel:
        user = UserModel(id=self.id, name=self.name, password=self.password)
        return user

    def from_json(self, body):
        self.id = body["id"]
        self.name = body["name"]
        self.password = body["password"]
