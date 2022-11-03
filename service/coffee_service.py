from model.coffee import Coffee
from flask import make_response
import json
from utils.jwt_verify import validate_token

@validate_token
def add_coffee(coffee_data):
    try:
        name = coffee_data['name']
        description = coffee_data['description']
        image = coffee_data['image']
        quantity = coffee_data['quantity']

        coffee = Coffee(
            name = name,
            description = description,
            iamge = image,
            quantity = quantity
        )
        coffee.save()
        return make_response({'message': 'Created coffee'}, 201)
    except Exception(e):
        return make_response({'message': str(e)},500)

def get_coffee(id):
    result_coffee = []
    try:
        for coffe in Coffee.objects(id=id):
            result_coffe.append(coffee.data)
        
        return make_response({result_coffee}, 200)
    except Exception(e):
        return make_response({'message:': str(e)},500)