from models import db


class BaseRepository:
    def __init__(self, model) -> None:
        self._model = model

    def save(self, model_object) -> object:
        db.session.add(model_object)
        db.session.commit()
        return model_object

    def find(self, **kwags) -> list:
        query = self._model.query
        if kwags:
            query = query.filter_by(kwags)
        return query.order_by("id").all()

    def findOne(self, **kwags) -> object:
        query = self._model.query
        if kwags:
            query = query.filter_by(kwags)
        return query.first()
