from flask import Flask, request, session, jsonify,send_file
from flask_cors import CORS
import bcrypt
from pymongo import MongoClient
from database import get_db
from rpa import automate_browser, automate_desktop
# from mathplotlib import filtering
import time
import matplotlib.pyplot as plt
import pandas as pd
import os
import re
import json
# from machine_learning_model import linear_regression 

# frontend - reactjs and tailwinds css
# react js - its mixture of html n js
# tailwind is used as a css utility-first CSS framework used to build modern,(utility framework for css)

# flask backend
# flask for routing ( our website)
# selenium for prerform browser task
# beatifulsoup isused for - web scraping and fetching the data 
# pyautogui used for desktop task like cliking n  scrolling
# numpy and pandas used for data analysis - we r converting data into csv(excel)
# mathplotlib for converting data into graphs


import pandas as pd
global filename_
global label

filename_ = ""
label = []

app = Flask(__name__)
CORS(app, resources={
    r"/api/*": {"origins": "http://localhost:5173"},
}, supports_credentials=True)
app.config['SECRET_KEY'] = 'your-secret-key'

# connect with mongo db
db = get_db()

data_fetched = []


# ------------------> user register routes
@app.route('/api/user/register', methods=['POST'])
def register():
    print("----------------------------------")
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')

    if not name or not email or not password:
        return jsonify({'error': 'Missing required fields'}), 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    # register_()
    user = db.user_register.find_one({'email': email})
    if user:
        return jsonify({'error': 'User already registered'}), 400
    
    # Insert the new user into the database
    db.user_register.insert_one({
        'username': name,
        'email': email,
        'password': hashed_password.decode('utf-8')
    })
    

    return jsonify({'message': 'User registered successfully'}), 201


# ------------------> user login routes
@app.route('/api/user/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = db.user_register.find_one({'email': email})
    if not user:
        return jsonify({'error': 'Invalid email or password'}), 401

    if bcrypt.checkpw(password.encode('utf-8'), user['password'].encode('utf-8')):
        session["user_id"] = str(user['_id'])
        return jsonify({'message': 'Login successful', 'user': str(user['_id'])}), 200
    else:
        return jsonify({"error": "Invalid password"}), 401
    

# --------------------------> logout routes
@app.route('/api/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({'message': 'Logged out successfully'}), 200


# ---------------------------> home routes
@app.route('/api/home', methods=['GET'])
def home():
    if "user_id" in session:
        user_id = session.get("user_id")
        user = db.user_register.find_one({'_id': user_id})
        
        if user:
            return jsonify({'user': {'username': user['username'], 'email': user['email']}}), 200

    return jsonify({'error': 'User not logged in'}), 401

@app.route('/api/selenium_data', methods=['POST'])
def selenium_data():
    data = request.json
    website_name = data.get('website_name')
    parameter = data.get("custom_parameter")

    print("-----data:",parameter,website_name)
    website_data = automate_browser(website_name,parameter)
    if website_data:
        print("-sas-dasd-sad-asdas>",website_data)
    
        file_name = f"{website_name}.csv"
        df = pd.DataFrame(website_data)
        df.to_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\website_data.csv", index=False)

        return jsonify({'message': 'get data '}), 200
    else:
        return jsonify({'error': 'Failed to fetch data'}), 500


@app.route('/api/automate_desktop', methods=['POST'])
def automate_desktop_data():
    data = request.json
    website_name = data.get('website_name')
    parameter = data.get("custom_parameter")

    print("-----data:",parameter,website_name)
    website_data = automate_desktop(website_name,parameter)
    if website_data:


        time.sleep(2)


        return jsonify({"data":f"{website_data}"}), 200


# @app.route('/api/filtering', methods=['POST'])
# def filtering():
#     # Example data
#     data = pd.read_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\website_data.csv")

#     df = pd.DataFrame(data)
#     # df.to_csv('website_data.csv', index=False)  # Save as CSV for reference


    
#     df["price"] = df["price"].astype(str).replace("₹", "",regex=True)
#     df["price"] = df["price"].astype(str).replace(",", "",regex=True)
#     df["price"] = df["price"].astype(float)
    

    
#     name = df[["name"]]
#     price = df[["price"]]
#     review = df[["review"]]

#     price_ = df.price

#     # Generate graph
#     plt.bar(review, price)
#     plt.title("Price vs Review")

#     # Save graph as image
#     graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
#     print(graph_path,"-------------------------------------------<<<<<<<<<<<<<<")
#     plt.savefig(graph_path)  # Save graph

#     # linear_regression(name,review,price_)




#     return jsonify({"message": "Graph created successfully", "graph_path": graph_path}), 200
@app.route('/api/filtering', methods=['POST'])
def filtering():
    # Example data
    data = pd.read_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\website_data.csv")

    df = pd.DataFrame(data)
    # df.to_csv('website_data.csv', index=False)  # Save as CSV for reference

    df["price"] = df["price"].astype(str).replace("₹", "",regex=True)
    df["price"] = df["price"].astype(str).replace(",", "",regex=True)
    df["price"] = df["price"].astype(float)

    
    name = df[["name"]]
    price = df[["price"]]
    review = df[["review"]]

    price_ = df.price

    # Check if both review and price are not None
    if review.empty or price.empty:
        return jsonify({"error": "Review or price data is empty"}), 400

    # Generate graph
    plt.bar(review.values.flatten(), price.values.flatten())
    plt.title("Price vs Review")

    # Save graph as image
    graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
    plt.savefig(graph_path)  # Save graph

    # linear_regression(name,review,price_)


    return jsonify({"message": "Graph created successfully", "graph_path": graph_path}), 200
# ----------------------------------- how groph 
@app.route('/api/show-graph', methods=['GET'])
def show_graph():
    print("---------------------------------------> show graph")
    graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
    graph_paths = [
    r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png",
    r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipCart_history_graph.png",
    r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipCart_disocunt_graph.png"
]
    if os.path.exists(graph_path):
        return send_file(graph_paths, mimetype='image/png')
    else:
        return jsonify({"error": "Graph not found"}), 404
    


# -------------------------> ai ml model
@app.route('/api/ml-model', methods=['POST'])
def ml_model():
    if "file" not in request.files or "labels" not in request.form:
        return {"message": "File or labels missing"}, 400

    file = request.files["file"]
    labels = json.loads(request.form["labels"])  # Convert JSON string back to array

    print("filename:", file.filename)
    file_path = os.path.join(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\cdv", file.filename)
    file.save(file_path)
    
    
    from aiModel import linear_regression
    linear_regression(file_path,labels,'price')


    return {"message": f"File '{file.filename}' uploaded successfully!"}, 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)

    