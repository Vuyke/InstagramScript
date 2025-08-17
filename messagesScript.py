#poslati klubovima notifikacije
from TownUtils import getDistance
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver import Edge
import time

SESSION_FILE = "session.json"

def getMessage():# here we implement Aleksa's message
    return "De si Sale!!!"

def loginConf() -> Edge:
    edge_options = Options()
    edge_options.use_chromium = True
    edge_driver_path = "C:\EdgeDriver\msedgedriver.exe"
    service = Service(executable_path=edge_driver_path)
    return webdriver.Edge(service=service, options=edge_options)

def login() -> Edge:
    driver = loginConf()
    driver.get("https://www.instagram.com")
    time.sleep(45) # login yourself
    return driver
    
    
def sendToClubs(clubs):
    driver = login()
    for club in clubs:
        driver.get(f"https://www.instagram.com/{club.name}")
        time.sleep(10)
        message_button = driver.find_element(By.XPATH, "//*[text()='Message']")
        message_button.click()
        time.sleep(10)
        msg_box = driver.find_element(By.XPATH, "//div[@role='textbox']")
        msg_box.click()
        msg_box.send_keys(getMessage())
        msg_box.send_keys("\n")
        time.sleep(60)
        
        
def sendNotifications(countries, currentCity: str, km: int):
    clubs = []
    for country in countries.values():
        print(country)
        for town in country.towns.values():
            if getDistance(currentCity, town.name) <= km:
                print("VAMOS")
                for club in town.clubs:
                    clubs.append(club)
    sendToClubs(clubs)
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
username = "vanjavujovic"
password = "4Negro511"