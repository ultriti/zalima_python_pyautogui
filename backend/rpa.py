from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pyautogui
from bs4 import BeautifulSoup
import time
import requests

from fake_useragent import UserAgent

data = []

def automate_browser(website,parameter):
        print("-------------->website",website)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

       
        # Define URLs for specific websites
        urls = {
            "amazon": "https://www.amazon.in",
            "flipkart": "https://www.flipkart.com",
            # "zalando": "https://www.zalando.com",
            # "ebay": "https://www.ebay.in",
            # "walmart": "https://www.walmart.com",

        }

        # Check if the input website exists in the predefined URLs
        if website.lower() in urls:
            url = urls[website.lower()]
        else:
            print(f"Website '{website}' not supported!")
            return

        # print("url:",url)
        # Open the website using Selenium
        driver.get(url)
        time.sleep(3)  

        print("_---------------_____________________________________________")
        # Close login popup if it appears
        # try:
        #     close_button = driver.find_element(By.XPATH, "//button[contains(text(), '✕')]")
        #     close_button.click()
        # except Exception as e:
        #     print("No login popup appeared:", e)

        # Perform a search operation
        
     
        if website.lower() == "amazon":
            search_query = f"{parameter}"
            search_box = driver.find_element(By.ID, "twotabsearchtextbox") 
            try:
                search_box = driver.find_element(By.ID, "twotabsearchtextbox") 
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.RETURN)
                time.sleep(3)  # Wait for search results to load
            except Exception as e:
                print("Error interacting with the search box:", e)


            page_source = driver.page_source
            # print("print aource",page_source)


            soup = BeautifulSoup(page_source, 'html.parser')

            print("-=-=-=-=-=-=-=-=-:",website.lower())
        
            print("------------------------------------>amazon")
            s = soup.select("h2.a-size-medium.a-spacing-none.a-color-base")
            p = soup.select("span.a-price-whole")
            r = soup.select("div.a-row.a-size-small")

            # print("data ---------->name:",s)
            # print("\n\n data ---------->price:\n",p)
            # print("\n\n---------------------->reweiw\n",r)
            # print("------------------------------------>amazon")


            for title, price ,review in zip(s, p, r):
                # print(f"Product: {title.string}, \nPrice: {price.string}, \nreview: {review.span.text}")
                add_product(title.string, price.string, review.text)
        
        # ------------------> flip kart 

        elif website.lower() == "flipkart":
            search_query = f"{parameter}"
            try:
                search_box = driver.find_element(By.NAME, "q")
                search_box.send_keys(search_query)
                search_box.send_keys(Keys.RETURN)
                time.sleep(10)  # Wait for search results to load
            except Exception as e:
                print("Error interacting with the search box:", e)

            page_source = driver.page_source


            soup = BeautifulSoup(page_source, 'html.parser')
            
            products = soup.find_all("div",{"class":"tUxRFH"})  # Flipkart's product container class
            
            # with open (r"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\scrapped data\text.txt",'w',encoding='utf-8') as file:
            #     file.write(soup) 
        
            print("------------------------------------>flipkart data")
            # print(products,"------------------->")
            
            page =0 
            for pro in products:
                if page >= 20:
                     break  # Stop the loop after 20 items
                
                print("------------------------------------------------------------------------------------")
                title = pro.find("div",{"class":"KzDlHZ"})
                print(title.text)
                descounted_price = pro.find("div",{"class":"Nx9bqj"})
                print(descounted_price.text)
                original_Price = pro.find("div",{"class":"yRaY8j"})
                print(descounted_price.text)
                discount_Percent = pro.find("div",{"class":"UkUFwK"})
                if(discount_Percent.string):
                    print(discount_Percent.string)
                else:
                    print(discount_Percent.text)                    
                pro_review = pro.find("span",{"class":"Wphh3N"})
                print(pro_review.text.split('&')[1].strip(),"-------------->")
                
                pro_rating = pro.find("span",{"class":"Wphh3N"})
                print(pro_rating.text.split('&')[0].strip(),"-------------->")
                
                # pro_reviews = pro.find("div",{"class":"Wphh3N"})
                pro_rating_starts = pro.find("div",{"class":"XQDdHH"})
                print("reviews : ------------------>",pro_rating_starts.text)
                
                for title, descounted_price,original_Price,pro_review,pro_rating,pro_rating_starts in zip(title,descounted_price,original_Price,pro_review.text.split('&')[1].strip(),pro_rating.text.split('&')[0].strip(),pro_rating_starts.text):
                    print(f"Product: {title.text}, original Price: {original_Price.text},descounted: {descounted_price.text}, rating: {pro_rating}, review: {pro_review}, reviews: {pro_rating_starts} \n\n")
                    
                    add_product(title.text, descounted_price.text, original_Price.text,discount_Percent.text,pro_review,pro_rating,pro_rating_starts)
                page += 1
            
            # try:
            #     file =0
            #     for product in products:
            #         d = product
            #         print("-------------------- html data of prodycts\n\n",d)
            #         with open (f"E:\python\ptautomateai\project\Zalima_Pyautogui_project\backend\all_data\scrapped data\flipcart data\{search_query}_{file}.html",'w',encoding='utf-8') as file:
            #             file.write(d) 
            #             file += 1
                    

     
            # except Exception as e:
            #     print("-----------------------------------------------------------------------------------------------------------------------------error\n",e)
            #     pass
                
        
    
        # print("data:-------->",data)
        driver.quit()
        return data

def add_product(title,descount_price, orginal_price,discount_Percent,pro_review,pro_rating,reviews_stars):

    
    data.append({"name": title,"descount_price":descount_price,"orginal_price":orginal_price,"descount_Percent":discount_Percent,"review":pro_review,"reviews":reviews_stars,"rating":pro_rating})
    print(f"------------->data appended: Discounted Price: {descount_price}, Original Price: {orginal_price}, Discount Percent: {discount_Percent}, Review: {pro_review}, Rating: {pro_rating}, Reviews Stars: {reviews_stars}\n\n")
    



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

