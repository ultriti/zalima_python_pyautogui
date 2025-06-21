from sklearn import linear_model
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

import pickle
import os
from pathlib import Path

# def linear_regression(filename, values, target_column):
def linear_regression(file_path):
    df = pd.read_csv(file_path)

    
    df["descount_price"] = df["descount_price"].astype(str).replace("₹", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(str).replace(",", "",regex=True)
    df["descount_price"] = df["descount_price"].astype(float)
    
    df["orginal_price"] = df["orginal_price"].astype(str).replace("₹", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(str).replace(",", "",regex=True)
    df["orginal_price"] = df["orginal_price"].astype(float)
    
    X = df[["orginal_price", "descount_price", "rating", "reviews"]]
    y = df["descount_price"]
    
    with open(r'E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\Model\model.pkl', 'rb') as f:
        model = pickle.load(f)

    
    prediction = model.predict(X)
    print("Prediction: pickel", prediction)
    
    newdf = df
    newdf["predicted Prizes"] = prediction
    
    def get_downloads_folder():
        return str(Path.home() / "Downloads")

    downloads_path = get_downloads_folder()
    
    file_path = os.path.join(downloads_path, "output.csv")
    
    df.to_csv(file_path)
    
    return file_path
    



    # def check_discount_trend(price_list):
    #     """Identify if price trend indicates future discount"""
    #     if len(price_list) >= 2 and price_list[-1] < price_list[-2]:
    #         return "Likely to get further discount"
    #     return "Stable or Increasing Price"

    # df["Future Discount Likely"] = df["Price Trend"].apply(check_discount_trend)

    # # Display Products Likely to Get Discounts
    # discount_predictions = df[df["Future Discount Likely"] == "Likely to get further discount"]
    
    
    # print("\nProducts Likely to Get Further Discounts:")
    # print(discount_predictions[["Product Name", "Base Price", "Discounted Price", "Price History"]])

    
# linear_regression()