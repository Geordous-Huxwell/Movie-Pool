import time
import requests
from bs4 import BeautifulSoup
import urllib

def critic(rt_url):
    response = requests.get(rt_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="all-critics-numbers").find(class_="meter-value superPageFontColor")
    
    for element in content_div.find_all("span", recursive=False):
        
        critic = element.get_text()
                
        return int(critic)

def audience(rt_url):
    response = requests.get(rt_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="topSection").find(class_="media-body")
    sub_div = content_div.find(class_="meter-value")
    
    for element in sub_div.find_all("span", recursive=False):
        
        audience = element.get_text()[:-1]        

    return int(audience)

def gross(bo_url):
    response = requests.get(bo_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(class_="mp_box_content").table
    box_office = content_div.get_text()
    ww_gross = (box_office[box_office.find("Worldwide:")+13:])
    ww_gross = ww_gross.replace(",","")
    return round((float(ww_gross)/1000000),0)

def budget(bo_url):
    response = requests.get(bo_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text()
    budget = content[content.find("Production Budget:"):content.find(" million")]
    budget = budget.replace("Production Budget: $", "")
    return float(budget)

def awards(imdb_url):
    response = requests.get(imdb_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="main").find(class_="article listo").find("table")
    content = content_div.get_text()
    win_text = content[:content.find("Nominated")]
    nom_text = content[content.find("Nominated"):]
    wins = win_text.count("Best")
    bp_bonus = 0
    if win_text.find("Best Picture"):
        bp_bonus += 50
    noms = nom_text.count("Best")
    return (wins*50)+(noms*10)+bp_bonus
    

rt_url = "https://www.rottentomatoes.com/m/get_out"
#print("Movie: Get Out")
#print("Critic Score: ", critic(rt_url))
#print("Audience Score: ", audience(rt_url))

bo_url = "http://www.boxofficemojo.com/movies/?id=forrestgump.htm"
print("Box Office: ", gross(bo_url))
#print("Budget: ", budget(bo_url))

imdb_url = "http://www.imdb.com/title/tt1895587/awards?ref_=tt_awd"
print("Oscars Bonus: ", awards(imdb_url))
