from flask import Blueprint, request
from services.user import UserService
from dtos.user import CreateUserDTO
from dependency_injector.wiring import inject, Provide
from container import Container
from util.serialize import http_code


blueprint = Blueprint("api_users", __name__, url_prefix="/api")


@blueprint.route("/users", methods=["GET"])
@http_code(code=200)
@inject
def get_users(service: UserService = Provide[Container.user_service]):
    return [u.to_dict() for u in service.get_all()]


@blueprint.route("/users", methods=["POST"])
@http_code(code=201)
@inject
def create_user(service: UserService = Provide[Container.user_service]):
    dto = CreateUserDTO()
    dto.from_json(request.get_json(silent=True))
    return service.create(dto).to_dict()
