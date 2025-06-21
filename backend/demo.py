import pandas as pd

# Define product data (more than 20 entries)
data = {
    "Product Name": [
        "Wireless Mouse", "Mechanical Keyboard", "Gaming Monitor", "Bluetooth Headphones", 
        "USB-C Hub", "Laptop Stand", "Portable SSD", "Smartphone Tripod", "Wireless Earbuds",
        "Gaming Chair", "Smartwatch", "HD Webcam", "Desk Lamp", "Noise-Canceling Headphones",
        "Phone Holder", "Mechanical Pencil", "Wireless Charger", "External Hard Drive", 
        "Microphone", "VR Headset", "Gaming Laptop", "Smart TV", "Power Bank", "Fitness Tracker"
    ],
    "Product URL": [f"http://flipkart.com/product-{i}" for i in range(1, 25)],
    "Product Description": [
        "Ergonomic design with long battery life", "RGB backlit gaming keyboard with tactile switches",
        "High refresh rate 144Hz display", "Noise cancellation with HD sound",
        "Compact multi-port hub for Type-C devices", "Adjustable stand for comfortable laptop use",
        "Fast NVMe storage with high-speed transfers", "Stable tripod for smartphone photography",
        "True wireless earbuds with deep bass", "Premium ergonomic gaming chair",
        "Smartwatch with fitness tracking", "1080p HD webcam for video calls",
        "LED desk lamp with adjustable brightness", "Wireless headphones with noise cancellation",
        "Universal phone holder with adjustable grip", "Graphite mechanical pencil for smooth writing",
        "Fast wireless charging pad", "External HDD with backup software",
        "Professional microphone for streaming", "VR headset with immersive experience",
        "High-performance gaming laptop", "4K Smart TV with built-in streaming apps",
        "20,000mAh power bank for fast charging", "Wearable fitness tracker with heart rate monitoring"
    ],
    "Category": [
        "Electronics", "Gaming", "Gaming", "Audio", "Accessories", "Accessories", "Storage", 
        "Photography", "Audio", "Furniture", "Wearable", "Computing", "Home Decor", "Audio",
        "Accessories", "Stationery", "Accessories", "Storage", "Audio", "Gaming",
        "Computing", "Entertainment", "Power", "Wearable"
    ],
    "Base Price": [25.99, 89.99, 199.99, 59.99, 39.99, 34.99, 129.99, 19.99, 74.99, 
                   159.99, 199.99, 49.99, 22.99, 179.99, 15.99, 9.99, 39.99, 89.99, 
                   129.99, 299.99, 799.99, 999.99, 29.99, 99.99],
    "Discounted Price": [22.49, 85.49, 195.99, 54.99, 38.49, 33.99, 132.99, 21.49, 
                         78.99, 162.99, 198.99, 51.99, 23.49, 182.99, 16.49, 10.99, 
                         41.49, 92.99, 135.99, 310.99, 820.99, 970.99, 32.99, 95.99],
    "Competitor Price": [27.49, 95.99, 210.99, 62.99, 38.49, 33.99, 132.99, 21.49, 
                         78.99, 162.99, 198.99, 51.99, 23.49, 182.99, 16.49, 10.99, 
                         41.49, 92.99, 135.99, 310.99, 820.99, 970.99, 32.99, 95.99],
    "Price History": [
        "[25.99, 24.99, 22.49]", "[89.99, 88.99, 85.49]", "[199.99, 210.99, 195.99]",
        "[59.99, 58.99, 54.99]", "[39.99, 38.99, 38.49]", "[34.99, 33.99, 33.49]", "[129.99, 132.99, 131.49]",
        "[19.99, 21.49, 19.49]", "[74.99, 78.99, 76.49]", "[159.99, 162.99, 157.99]", "[199.99, 198.99, 200.49]",
        "[49.99, 51.99, 48.99]", "[22.99, 23.49, 23.49]", "[179.99, 182.99, 181.49]", "[15.99, 16.49, 15.49]",
        "[9.99, 10.99, 9.49]", "[39.99, 41.49, 40.49]", "[89.99, 92.99, 91.49]", "[129.99, 135.99, 127.99]",
        "[299.99, 310.99, 305.49]", "[799.99, 820.99, 810.49]", "[999.99, 970.99, 985.49]", "[29.99, 32.99, 30.49]",
        "[99.99, 95.99, 97.49]"
    ],
    "Rating": [4.5, 4.7, 4.6, 4.2, 4.3, 4.4, 4.8, 4.1, 4.6, 4.5, 4.2, 4.3, 4.0, 4.7, 4.1, 3.9, 4.4, 4.5, 4.3, 4.8, 4.6, 4.9, 4.1, 4.2],
    "Number of Reviews": [1200, 3400, 1800, 2800, 900, 1500, 2200, 800, 3100, 1700, 2400, 1000, 600, 2800, 700, 400, 1300, 2100, 900, 3200, 1200, 4000, 1000, 2100],
    "Seller Name": ["BestTech", "GameGear", "DisplayMasters", "SonicTech", "USBWorks", "LaptopWorld", "StoragePro", "CameraExperts",
                    "AudioXperts", "GamingZone", "WearableTech", "WebCamCo", "HomeEssentials", "AudioMasters", "MobileGears",
                    "StationeryHub", "ChargingPro", "StorageKing", "ProMicStore", "VirtualRealityInc", "FastComputers",
                    "SmartScreenStore", "PowerBoost", "FitTech"],
    "Stock Availability": ["In Stock"] * 20 + ["Out of Stock"] * 4,
    "Shipping Details": ["Free Shipping"] * 24,
    "Delivery Time Estimate": ["3-5 Days"] * 12 + ["5-7 Days"] * 12
}

# Create DataFrame
df = pd.DataFrame(data)

# Save as CSV
df.to_csv("flipkart_products.csv", index=False)

print("CSV file with 24 products saved successfully!")
