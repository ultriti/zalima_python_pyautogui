import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

import pickle 


def linear_regression():
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
    
    print("vlaues goin to preducts:\n",X_test)
    
    x_to_predict = np.array([[22999.0,18999.0,7,4]])

    y_pred = model.predict(x_to_predict)
    
    print("predicted value -->\n",y_pred)

    # mae = mean_absolute_error(y_test, y_pred)
    # print(f"Mean Absolute Error: {mae:.2f}")
    
    # with open(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\Model\model.pkl", "wb") as f:
    #     pickle.dump(model, f)

linear_regression()