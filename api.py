import json
import flask
from flask import jsonify
from flask import request

# read and parse
with open('wine-detailed-data.json', 'r') as json_file:
    json_str=json_file.read()
all_wines = json.loads(json_str)

app = flask.Flask(__name__)
app.config["DEBUG"] = True

def extract_food_names():
    food_names_set = set(())

    for wine in all_wines:
        if "food_names" in wine:
            if wine['food_names'] != None:
                temp_food_names_list = wine['food_names'].split('|')
                food_names_set.update(temp_food_names_list)
    
    food_names_list = list(food_names_set)
    food_names_list.sort()
    
    return food_names_list

def extract_grape_names():
    grape_names_set = set(())

    for wine in all_wines:
        if "grape_names" in wine:
            if wine['grape_names'] != None:
                temp_grape_names_list = wine['grape_names'].split('|')
                grape_names_set.update(temp_grape_names_list)
    
    grape_names_list = list(grape_names_set)
    grape_names_list.sort()
    
    return grape_names_list

def extract_country_names():
    country_names_set = set(())

    for wine in all_wines:
        if "country_name" in wine:
            if wine['country_name'] != None:
                country_names_set.add(wine['country_name'])
    
    country_names_list = list(country_names_set)
    country_names_list.sort()
    
    return country_names_list

food_names = extract_food_names()
grape_names = extract_grape_names()
country_names = extract_country_names()

@app.route('/', methods=['GET'])
def home():
    return "HEY"

@app.route('/wine/all', methods=['GET'])
def wine_all():
    return jsonify(all_wines)

@app.route('/wine/foods', methods=['GET'])
def wine_foods():
    return jsonify(food_names)

@app.route('/wine/countries', methods=['GET'])
def wine_countries():
    return jsonify(country_names)

@app.route('/wine/grapes', methods=['GET'])
def wine_grapes():
    return jsonify(grape_names)

@app.route('/wine/search', methods=['GET'])
def wine_search():
    food_name = request.args["food_name"] if "food_name" in request.args else False
    country_name = request.args["country_name"] if "country_name" in request.args else False
    grape_name = request.args["grape_name"] if "grape_name" in request.args else False
    price_min = float(request.args["price_min"]) if "price_min" in request.args else False
    price_max = float(request.args["price_max"]) if "price_max" in request.args else False
    has_price = price_min and price_max

    wines_with_food_name = list(filter(lambda wine: wine['food_names'] != None and food_name in wine['food_names'], all_wines)) if food_name else all_wines
    wines_with_country_name = list(filter(lambda wine: wine['country_name'] != None and country_name == wine['country_name'], wines_with_food_name)) if country_name else wines_with_food_name
    wines_with_grape_name = list(filter(lambda wine: wine['grape_names'] != None and grape_name in wine['grape_names'], wines_with_country_name)) if grape_name else wines_with_country_name
    wines_with_price = list(filter(lambda wine: wine['price_eur'] != None and wine['price_eur'] >= price_min and wine['price_eur'] <= price_max, wines_with_grape_name)) if has_price else wines_with_grape_name

    return jsonify(wines_with_price)

# dev mode
app.run() 

# prod mode
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
