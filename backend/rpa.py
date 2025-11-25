from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
import pyautogui

# Global product list
data = []

def automate_browser(website: str, parameter: str):
    """Automate search and scraping from Amazon or Flipkart."""
    print("------------------------->")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    print("------------------------->")
    urls = {
        "amazon": "https://www.amazon.in",
        "flipkart": "https://www.flipkart.com",
    }

    if website.lower() not in urls:
        print(f"Website '{website}' not supported!")
        driver.quit()
        return []

    driver.get(urls[website.lower()])
    time.sleep(3)

    if website.lower() == "amazon":
        scrape_amazon(driver, parameter)
    elif website.lower() == "flipkart":
        scrape_flipkart(driver, parameter)

    driver.quit()
    return data


def scrape_amazon(driver, search_query: str):
    """Scrape product data from Amazon search results."""
    
    print(search_query)
    try:
        search_box = driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(3)
    except Exception as e:
        print("Error interacting with Amazon search box:", e)
        return

    soup = BeautifulSoup(driver.page_source, "html.parser")

    titles = soup.select("h2.a-size-medium.a-spacing-none.a-color-base")
    prices = soup.select("span.a-price-whole")
    reviews = soup.select("div.a-row.a-size-small")

    for title, price, review in zip(titles, prices, reviews):
        add_product(
            title=title.get_text(strip=True),
            discount_price=price.get_text(strip=True),
            original_price=None,
            discount_percent=None,
            review=review.get_text(strip=True),
            rating=None,
            reviews_stars=None,
        )


def scrape_flipkart(driver, search_query: str):
    """Scrape product data from Flipkart search results."""
    try:
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(search_query)
        search_box.send_keys(Keys.RETURN)
        time.sleep(5)
    except Exception as e:
        print("Error interacting with Flipkart search box:", e)
        return

    soup = BeautifulSoup(driver.page_source, "html.parser")
    products = soup.find_all("div", {"class": "tUxRFH"})

    for idx, pro in enumerate(products[:20]):  # Limit to 20 items
        title = pro.find("div", class_=["KzDlHZ", "wjcEIp"]) 
        discounted_price = pro.find("div", {"class": "Nx9bqj"})
        original_price = pro.find("div", {"class": "yRaY8j"})
        discount_percent = pro.find("div", {"class": "UkUFwK"})
        review = pro.find("span", {"class": "Wphh3N"})
        rating_stars = pro.find("div", {"class": "XQDdHH"})
        
        print({
        "title": title.get_text(strip=True) if title else None,
        "discount_price": discounted_price.get_text(strip=True) if discounted_price else None,
        "original_price": original_price.get_text(strip=True) if original_price else None,
        "discount_percent": discount_percent.get_text(strip=True) if discount_percent else None,
        "review": review.get_text(strip=True) if review else None,
        "rating": None,
        "reviews_stars": rating_stars.get_text(strip=True) if rating_stars else None,
        })


        add_product(
            title=title.get_text(strip=True) if title else None,
            discount_price=discounted_price.get_text(strip=True) if discounted_price else None,
            original_price=original_price.get_text(strip=True) if original_price else None,
            discount_percent=discount_percent.get_text(strip=True) if discount_percent else None,
            review=review.get_text(strip=True) if review else None,
            rating=None,  # Flipkart rating parsing can be added separately
            reviews_stars=rating_stars.get_text(strip=True) if rating_stars else None,
        )


def add_product(title, discount_price, original_price, discount_percent, review, rating, reviews_stars):
    """Append product details to global data list."""
    product = {
        "name": title,
        "discount_price": discount_price,
        "original_price": original_price,
        "discount_percent": discount_percent,
        "review": review,
        "rating": rating,
        "reviews_stars": reviews_stars,
    }
    data.append(product)


# Example usage:
# if __name__ == "__main__":
    # results = automate_browser("flipkart", "laptop")
    # for item in results:
    #     print(item)




def automate_desktop():
    """
    Simulates desktop-based actions: closes popup and scrolls the webpage.
    """
    print("Simulating desktop interactions...")
    time.sleep(1)  # Delay for observation

    # Move to Flipkart login popup close button (coordinates may vary)
    pyautogui.moveTo(1100, 300, duration=1)  # Coordinates for close button
    pyautogui.click()  # Close the popup

    # Scroll through the page using PyAutoGUI
    print("Scrolling through the webpage...")
    pyautogui.scroll(-500)  # Scroll down
    time.sleep(1)
    pyautogui.scroll(-500)  # Scroll further
    time.sleep(1)

    # Display a simulated message
    pyautogui.alert(text='Desktop automation simulated!', title='PyAutoGUI', button='OK')

if __name__ == "__main__":
    print("Starting Flipkart automation...")

    # Run browser automation
    automate_browser()

    # Run desktop automation
    automate_desktop()

    print("Flipkart automation completed successfully!")

