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

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


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
        df.to_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data_.csv", index=False)

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


@app.route('/api/filtering', methods=['POST'])
def filtering():
    data = pd.read_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data.csv")

    df = pd.DataFrame(data)

    df["descount_price"] = df["descount_price"].astype(str).replace("₹", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(str).replace(",", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(float)
    
    df["orginal_price"] = df["orginal_price"].astype(str).replace("₹", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(str).replace(",", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(float)
    


    X = df[["orginal_price", "descount_price", "rating", "reviews"]]
    y = df["descount_price"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f}")

    # Save graph as image
    graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
    # plt.savefig(graph_path)  # Save graph


    return jsonify({"message": "Graph created successfully", "graph_path": graph_path}), 200


# ----------------------------------- how groph 
@app.route('/api/show-graph', methods=['GET'])
def show_graph():
    print("---------------------------------------> show graph")
    graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
#     graph_paths = [
#     r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png",
#     r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipCart_history_graph.png",
#     r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipCart_disocunt_graph.png"
# ]
    if os.path.exists(graph_path):
        return send_file(graph_path, mimetype='image/png')
    else:
        return jsonify({"error": "Graph not found"}), 404
    

# ----------------- csv file info
@app.route('/api/get_info', methods=['GET'])
def getInfo():
    # Load CSV file
    file_path = r"E:/python/ptautomateai/project/Zalima_Pyautogui_project/backend/all_data/flipkart_website_data.csv"
    df = pd.read_csv(file_path)
    
    df["descount_price"] = df["descount_price"].astype(str).replace("₹", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(str).replace(",", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(float)
    
    df["orginal_price"] = df["orginal_price"].astype(str).replace("₹", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(str).replace(",", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(float)

    # Display basic information
    print("Column Names:", df.columns.tolist())
    print("\nData Types:", df.dtypes)
    print("\nMissing Values:", df.isnull().sum())
    print("\nBasic Statistics:")
    print(df.describe())

    # Find Cheapest & Most Expensive Products
    cheapest_product = df.loc[df["orginal_price"].idxmin()]
    most_expensive_product = df.loc[df["orginal_price"].idxmax()]
    print("\nCheapest Product:\n", cheapest_product)
    print("\nMost Expensive Product:\n", most_expensive_product)

    # Price Analysis
    print("\nPrice Range Distribution:")
    df["orginal_price"] = df["orginal_price"].astype(int)
    df["descount_price"] = df["descount_price"].astype(int)
    df["descount_Percent"] = pd.to_numeric(df["descount_Percent"], errors='coerce')

    
    price_ranges = pd.cut(df["orginal_price"], bins=[0, 5000, 10000, 20000, 50000, 100000], labels=["Very Cheap", "Cheap", "Moderate", "Expensive", "Luxury"])
    print(price_ranges.value_counts())

    # Discount Analysis
    df["descount_Percent"] = ((df["orginal_price"] - df["descount_Percent"]) / df["orginal_price"]) * 100
    df["descount_Percent"] = df["descount_Percent"].round(2)
    top_discounts = df.nlargest(5, "descount_Percent")
    print("\nTop 5 Best Discounts:\n", top_discounts[["name", "orginal_price", "descount_price", "descount_Percent"]])

    # Most Reviewed & Highest-Rated Products
    most_reviews = df.loc[df["reviews"].idxmax()]
    highest_rated = df.loc[df["rating"].idxmax()]
    print("\nMost Reviewed Product:\n", most_reviews)
    print("\nHighest Rated Product:\n", highest_rated)
    print(df)
    
    
    print("----------------------------------------------------")
    print(
        f"description: {df.describe()} , \nCheapestPrice :{cheapest_product}, \nMostExpensiveProduct :{most_expensive_product} , \nPriceRangeDistribution: {price_ranges.value_counts()} ,\nMostReviewedProduct:{most_reviews},\nHighestRatedProduct:{highest_rated}", 
        
    )
    
  
    
    data ={
        "CheapestPrice":[cheapest_product], 
        "MostExpensiveProduct":[most_expensive_product],
        # "PriceRangeDistribution":{price_ranges.value_counts()},
        "MostReviewedProduct":[most_reviews],
        "HighestRatedProduct":[highest_rated ]
    }
    fileName_txt = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\frontend\public\text file\info.txt"
    with open(fileName_txt,"w+") as f:
        f.write(str(data))
        f.close
    

    
   
    return jsonify({"infoData":fileName_txt}), 200
 
    # "Discount":top_discounts[["name", "orginal_price", "descount_price", "descount_Percent"]]


# -------------------------> ai ml model
@app.route('/api/ml_model', methods=['POST'])
def ml_model():

    if 'csv' not in request.files:
            return jsonify({'error': 'CSV file missing'}), 400

    file = request.files['csv']
    
    from aiModel import linear_regression
    file_path = linear_regression(file)
    
    return jsonify({"message": f"File saved at {file_path}","fileInfo":file_path}), 200


if __name__ == '__main__':
    app.run(debug=True, port=8000)

    