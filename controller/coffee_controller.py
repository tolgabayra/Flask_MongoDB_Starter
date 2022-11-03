from flask import Blueprint, request
from service.coffee_service import add_coffee, get_coffee
coffee_route = Blueprint("coffee_route", __name__)

@coffee_route("/api/v1/coffee", method=['POST'])
def create():
    data = request.get_json()
    return add_coffee(data)

@coffee_route("/api/v1/coffee/<id>", method=['GET'])
def get(id):
    return get_coffee(id)