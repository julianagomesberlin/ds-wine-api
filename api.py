import json
import flask
from flask import jsonify

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
def print_all():
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

# dev mode
app.run() 

# prod mode
# if __name__ == "__main__":
#     from waitress import serve
#     serve(app, host="0.0.0.0", port=5000)
