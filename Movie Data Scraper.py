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
    # content_div = soup.find(class_="mp_box_content").table
    # box_office = content_div.get_text()
    # ww_gross = (box_office[box_office.find("Worldwide:")+13:])

    content_div = soup.find(id="movie_finances")
    box_office = content_div.get_text()
    ww_gross = box_office[box_office.find("Worldwide Box Office")+22:box_office.find("Further")]
    ww_gross = ww_gross.replace(",","")
    return round((float(ww_gross)/1000000),0)

def budget(bo_url):
    response = requests.get(bo_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text()
    #budget = content[content.find("Production Budget:"):content.find(" million")]
    #budget = budget.replace("Production Budget: $", "")
    #print(type(content))
    budget_content = content[content.find("Movie Details"):content.find("Domestic Releases")]
    budget = budget_content[budget_content.find("$"):budget_content.find(",")]
    budget = budget.replace("$", "")
    return float(budget)

def awards(imdb_url):
    response = requests.get(imdb_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    wins = 0
    noms = 0
    bp_bonus = 0

    if str(soup).find("Academy") != -1:
        content_div = soup.find(id="main").find(class_="article listo").find("table")
        content = content_div.get_text()
        win_text = content[:content.find("Nominated")]
        nom_text = content[content.find("Nominated"):]

        wins = win_text.count("Best")

        if win_text.find("Best Picture") == 1:
            bp_bonus += 50

        noms = nom_text.count("Best")

    return (wins*50)+(noms*10)+bp_bonus

def score(gross, budget, critic, audience, awards=0):

    total = ((gross-budget)*(((critic+audience)/2)/100))+awards
    return round((total))

def team(team_name):
    team_total = 0
    for movie in team_name:
        title = movie[0]
        rt_url = movie[1]
        bo_url = movie[2]
        imdb_url = movie[3]
        print("Movie: " + title)
        print("Critic Score: ", critic(rt_url))
        print("Audience Score: ", audience(rt_url))
        print("Box Office: ", int(gross(bo_url)))
        print("Budget: ", int(budget(bo_url)))
        print("Oscars Bonus: ", awards(imdb_url))
        movie_total = score(gross(bo_url), budget(bo_url), critic(rt_url), audience(rt_url), awards(imdb_url))
        print("Total Score: ", movie_total)
        team_total += movie_total
        print("\n")
    return team_total

rt_url = "https://www.rottentomatoes.com/m/black_panther_2018"
print("Movie: Black Panther")
print("Critic Score: ", critic(rt_url))
print("Audience Score: ", audience(rt_url))

bo_url = "https://www.the-numbers.com/movie/Black-Panther#tab=summary"
print("Box Office: ", gross(bo_url))
print("Budget: ", budget(bo_url))

imdb_url = "http://www.imdb.com/title/tt1825683/awards?ref_=tt_awd"
print("Oscars Bonus: ", awards(imdb_url))

print("Total Score: ", score(gross(bo_url), budget(bo_url), critic(rt_url), audience(rt_url), awards(imdb_url)))

wonder_woman = ("Wonder Woman", "https://www.rottentomatoes.com/m/wonder_woman_2017", "http://www.boxofficemojo.com/movies/?id=wonderwoman.htm", "http://www.imdb.com/title/tt0451279/awards?ref_=tt_awd")
spiderman = ("Spider-Man: Homecoming", "https://www.rottentomatoes.com/m/spider_man_homecoming", "http://www.boxofficemojo.com/movies/?id=spiderman2017.htm", "http://www.imdb.com/title/tt2250912/awards?ref_=tt_awd")
dunkirk = ("Dunkirk", "https://www.rottentomatoes.com/m/dunkirk_2017", "http://www.boxofficemojo.com/movies/?id=chrisnolan2017.htm", "http://www.imdb.com/title/tt5013056/awards?ref_=tt_awd")
pirates5 = ("Pirates of the Caribbean: Dead Men Tell No Tales", "https://www.rottentomatoes.com/m/pirates_of_the_caribbean_dead_men_tell_no_tales", "http://www.boxofficemojo.com/movies/?id=potc5.htm", "http://www.imdb.com/title/tt1790809/awards?ref_=tt_awd")
brian_team = (wonder_woman, spiderman, pirates5, dunkirk)

alien_covenant = ("Alien: Covenant", "https://www.rottentomatoes.com/m/alien_covenant", "http://www.boxofficemojo.com/movies/?id=alienparadiselost.htm", "http://www.imdb.com/title/tt2316204/awards?ref_=tt_awd")
all_eyez = ("All Eyez On Me", "https://www.rottentomatoes.com/m/all_eyez_on_me_2017", "http://www.boxofficemojo.com/movies/?id=tupac.htm", "http://www.imdb.com/title/tt1666185/awards?ref_=tt_awd")
despicable3 = ("Despicable Me 3", "https://www.rottentomatoes.com/m/despicable_me_3", "http://www.boxofficemojo.com/movies/?id=despicableme3.htm", "http://www.imdb.com/title/tt3469046/awards?ref_=tt_awd")
transformers5 = ("Transformers: The Last Knight", "https://www.rottentomatoes.com/m/transformers_the_last_knight_2017", "http://www.boxofficemojo.com/movies/?id=transformers5.htm", "http://www.imdb.com/title/tt3371366/awards?ref_=tt_awd")
kent_team = (alien_covenant, all_eyez, despicable3, transformers5)

gotg2 = ("Guardians of the Galaxy Vol. 2", "https://www.rottentomatoes.com/m/guardians_of_the_galaxy_vol_2", "http://www.boxofficemojo.com/movies/?id=marvel17a.htm", "http://www.imdb.com/title/tt3896198/awards?ref_=tt_awd")
baywatch = ("Baywatch", "https://www.rottentomatoes.com/m/baywatch_2017", "http://www.boxofficemojo.com/movies/?id=baywatch.htm", "http://www.imdb.com/title/tt1469304/awards?ref_=tt_awd")
mummy = ("The Mummy", "https://www.rottentomatoes.com/m/the_mummy_2017", "http://www.boxofficemojo.com/movies/?id=mummy2016.htm", "http://www.imdb.com/title/tt2345759/awards?ref_=tt_awd")
war_pota = ("War for the Planet of the Apes", "https://www.rottentomatoes.com/m/war_for_the_planet_of_the_apes", "http://www.boxofficemojo.com/movies/?id=planetoftheapes16.htm", "http://www.imdb.com/title/tt3450958/awards?ref_=tt_awd")
richard_team = (gotg2, baywatch, mummy, war_pota)

# print("Brian Total: ", team(brian_team))
# print("Kent Total: ", team(kent_team))
# print("Richard Total: ", team(richard_team))
