from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime
from . import db


class UserRole:
    USER = 0
    ADMIN = 1
    MONIT = 2
    QUEST = 3


class UserModel(db.Model):
    __tablename__ = "user"

    id = Column(
        String(100),
        primary_key=True,
    )

    name = Column(String(50), nullable=False)
    password = Column(String(128))

    role = Column(Integer, default=UserRole.USER, nullable=False)

    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return dict(id=self.id, name=self.name, role=self.role)
