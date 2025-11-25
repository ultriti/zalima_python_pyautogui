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
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


global filename_
global label

filename_ = ""
label = []

app = Flask(__name__)
# CORS(
#     app,
#     supports_credentials=True,
#     origins=["http://localhost:5173", "http://localhost:5173/autoMate"],
# )
CORS(app, resources={
    r"/api/*": {
        "origins": [
            "http://localhost:5173",
            "http://localhost:5173/autoMate"
        ]
    }
}, supports_credentials=True)

# app.config['SECRET_KEY'] = 'your-secret-key'

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

import os
import pandas as pd
from flask import request, jsonify

@app.route('/api/selenium_data', methods=['POST'])
def selenium_data():
    data = request.json
    website_name = data.get('website_name')
    parameter = data.get("custom_parameter")

    print("-----data:", parameter, website_name)
    website_data = automate_browser(website_name, parameter)
    if website_data:
        print("Fetched website data:", website_data)

        file_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data_.csv"

        # ✅ Delete file if it exists
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Deleted old file: {file_path}")

        # Save new CSV
        df = pd.DataFrame(website_data)
        df.to_csv(file_path, index=False)

        return jsonify({'message': 'Data fetched and saved'}), 200
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
    # Load CSV
    data = pd.read_csv(
        r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data_.csv"
    )
    df = pd.DataFrame(data)

    # Clean numeric columns
    df["discount_price"] = (
        df["discount_price"].astype(str)
        .str.replace("₹", "", regex=True)
        .str.replace(",", "", regex=True)
        .astype(float)
    )
    df["original_price"] = (
        df["original_price"].astype(str)
        .str.replace("₹", "", regex=True)
        .str.replace(",", "", regex=True)
        .astype(float)
    )
    df["discount_percent"] = (
        df["discount_percent"].astype(str).str.extract(r"(\d+)").astype(float)
    )
    
    def extract_ratings(val):
        val = str(val).replace(",", "")
        numbers = re.findall(r"\d+", val)
        return int(numbers[0]) if len(numbers) > 0 else 0

    def extract_reviews(val):
        val = str(val).replace(",", "")
        numbers = re.findall(r"\d+", val)
        return int(numbers[1]) if len(numbers) > 1 else 0

    df["ratings_count"] = df["review"].apply(extract_ratings)
    df["reviews_count"] = df["review"].apply(extract_reviews)

    # Features and target
    X = df[["original_price", "discount_price", "ratings_count", "reviews_count"]]
    y = df["discount_price"]

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Train model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Predictions
    y_pred = model.predict(X_test)

    # Error metric
    mae = mean_absolute_error(y_test, y_pred)
    print(f"Mean Absolute Error: {mae:.2f}")

    # Graph path
    graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
    if os.path.exists(graph_path):
        os.remove(graph_path)
        print(f"Deleted old file ---> {graph_path}")

    # Scatter plot: Original vs Discounted, colored by discount_percent
    plt.figure(figsize=(10, 6))
    scatter = plt.scatter(
        df["original_price"],
        df["discount_price"],
        c=df["discount_percent"],
        cmap="coolwarm",
        alpha=0.7,
        edgecolors="w",
    )
    plt.xlabel("Original Price (₹)")
    plt.ylabel("Discounted Price (₹)")
    plt.title("Price Reduction Analysis")
    cbar = plt.colorbar(scatter)
    cbar.set_label("Discount Percent (%)")

    # Save graph
    plt.tight_layout()
    plt.savefig(graph_path)
    plt.close()

    return jsonify(
        {"message": "Graph created successfully", "graph_path": graph_path}
    ), 200


# ----------------------------------- how groph 
@app.route('/api/show-graph', methods=['GET'])
def show_graph():
    print("-------> show graph request")
    

    # Allow dynamic graph selection via query parameter
    graph_name = request.args.get("name", "graph.png")  
    graph_dir = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data"
    graph_path = os.path.join(graph_dir, graph_name)

    if os.path.exists(graph_path):
        return send_file(graph_path, mimetype='image/png')
    else:
        return jsonify({"error": f"Graph '{graph_name}' not found"}), 404
    



def get_top_products(products, top_n=5):
    """
    Filter and return the best products based on lowest price and highest reviews.
    """
    cleaned = []
    for p in products:
        try:
            price = int("".join(filter(str.isdigit, str(p.get("descount_price", "")))) or 0)
            reviews = int("".join(filter(str.isdigit, str(p.get("reviews", "")))) or 0)
            rating = float(str(p.get("rating", "0")).replace(",", ".") or 0)

            cleaned.append({
                "name": p.get("name"),
                "price": price,
                "reviews": reviews,
                "rating": rating,
                "original_price": p.get("orginal_price"),
                "discount_percent": p.get("descount_Percent"),
            })
        except Exception as e:
            print("Skipping product due to parse error:", e)

    sorted_products = sorted(
        cleaned,
        key=lambda x: (x["price"], -x["reviews"], -x["rating"])
    )
    return sorted_products[:top_n]


# @app.route('/api/get_info', methods=['GET'])
@app.route('/api/get_info', methods=['GET'])
def getInfo():
    import pandas as pd
    import re
    import json   # <-- add this

    print("------------------------------------------------>")
    # Load CSV file
    file_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data_.csv"
    df = pd.read_csv(file_path)

    # --- Clean numeric columns ---
    df["discount_price"] = (
        df["discount_price"].astype(str)
        .str.replace("₹", "", regex=True)
        .str.replace(",", "", regex=True)
    )
    df["discount_price"] = pd.to_numeric(df["discount_price"], errors="coerce")

    df["original_price"] = (
        df["original_price"].astype(str)
        .str.replace("₹", "", regex=True)
        .str.replace(",", "", regex=True)
    )
    df["original_price"] = pd.to_numeric(df["original_price"], errors="coerce")

    # --- Clean discount_percent like "29% off" ---
    def clean_discount(val):
        match = re.search(r"(\d+)", str(val))
        return int(match.group(1)) if match else 0

    df["discount_percent"] = df["discount_percent"].apply(clean_discount)

    # --- Clean review column like "1,514 Ratings&124 Reviews" ---
    def extract_ratings(val):
        val = str(val).replace(",", "")
        numbers = re.findall(r"\d+", val)
        return int(numbers[0]) if len(numbers) > 0 else 0

    def extract_reviews(val):
        val = str(val).replace(",", "")
        numbers = re.findall(r"\d+", val)
        return int(numbers[1]) if len(numbers) > 1 else 0

    df["ratings_count"] = df["review"].apply(extract_ratings)
    df["reviews_count"] = df["review"].apply(extract_reviews)

    # Drop rows with missing critical values
    df = df.dropna(subset=["discount_price", "original_price", "ratings_count", "reviews_count"])

    # --- Analysis ---
    cheapest_product = df.loc[df["original_price"].idxmin()] if not df.empty else None
    most_expensive_product = df.loc[df["original_price"].idxmax()] if not df.empty else None
    most_reviews = df.loc[df["reviews_count"].idxmax()] if not df.empty else None
    highest_rated = df.loc[df["ratings_count"].idxmax()] if not df.empty else None

    products = df.to_dict(orient="records")
    top_products = get_top_products(products, top_n=5)

    # Prepare response data safely
    data_array = []

    if cheapest_product is not None:
        data_array.append({"type": "Cheapest", **cheapest_product.to_dict()})

    if most_expensive_product is not None:
        data_array.append({"type": "Most Expensive", **most_expensive_product.to_dict()})

    if most_reviews is not None:
        data_array.append({"type": "Most Reviewed", **most_reviews.to_dict()})

    if highest_rated is not None:
        data_array.append({"type": "Highest Rated", **highest_rated.to_dict()})

    for prod in top_products:
        data_array.append({"type": "Top Product", **prod})

    # Optional: save to file
    fileName_txt = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\frontend\public\text file\info.txt"
    if os.path.exists(fileName_txt):
            os.remove(fileName_txt)
            print(f"Deleted old file--->\n: {fileName_txt}")
    
    with open(fileName_txt, "w", encoding="utf-8") as f:
        f.write(json.dumps(data_array, indent=2))

    return jsonify({"infoData": data_array}), 200






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

    