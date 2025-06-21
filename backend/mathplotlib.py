import matplotlib.pyplot as plt
import pandas as pd



df = pd.read_csv(r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\flipkart_website_data.csv")

df["descount_price"] = df["descount_price"].astype(str).replace("₹", "",regex=True)
df["descount_price"] = df["descount_price"].astype(str).replace(",", "",regex=True)
df["descount_price"] = df["descount_price"].astype(float)

df["orginal_price"] = df["orginal_price"].astype(str).replace("₹", "",regex=True)
df["orginal_price"] = df["orginal_price"].astype(str).replace(",", "",regex=True)
df["orginal_price"] = df["orginal_price"].astype(float)

df["descount_Percent"] = df["descount_Percent"].astype(str).replace("off", "")
print(df["descount_Percent"],"---------2")
df["descount_Percent"] = df["descount_Percent"].astype(float)
print(df["descount_Percent"],"---------3")



plt.figure(figsize=(8,5))
plt.scatter(df["orginal_price"], df["descount_price"], c=df["descount_Percent"], cmap='coolwarm', alpha=0.75)
plt.colorbar(label="Discount Percent (%)")
plt.xlabel("Original Price (₹)")
plt.ylabel("Discounted Price (₹)")
plt.title("Price Reduction Analysis")
plt.grid(True)
# Save graph as image
graph_path = r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\graph.png"
plt.savefig(graph_path)  # Save graph
