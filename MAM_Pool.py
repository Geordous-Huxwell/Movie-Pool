import time
import requests
from bs4 import BeautifulSoup
import urllib


def critic(rt_url):
    
    response = requests.get(rt_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = str(soup.find(id="tomato_meter_link").find(class_="mop-ratings-wrap__percentage"))
   
    percent_pos = content_div.index("%")
    critic = content_div[percent_pos-2:percent_pos]
    
    print("Critic Score: ", int(critic), file=open("Pool Standings.txt", "a"))
    return int(critic)

def audience(rt_url):
    response = requests.get(rt_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="topSection").find(class_="media-body")
    sub_div = content_div.find(class_="meter-value")
    
    for element in sub_div.find_all("span", recursive=False):
        
        audience = element.get_text()[:-1]        

    print("Audience Score: ", int(audience), file=open("Pool Standings.txt", "a"))
    print("Audience Score: ", int(audience))
    return int(audience)

def gross(bo_url, title):
    response = requests.get(bo_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content_div = soup.find(id="movie_finances")

    box_office = content_div.find_all(class_="data")[2].get_text()
    
    ww_gross = box_office.replace("$","")
    ww_gross = ww_gross.replace(",","")
    
    # if title == "Annihilation":
    #         ww_gross = int(ww_gross) + 27500000

    try:
        print("Box Office: ", int(round((float(ww_gross)/1000000),0)), file=open("Pool Standings.txt", "a"))
        return round((float(ww_gross)/1000000),0)
    except Exception as e:
        dom_gross = content_div.find(class_="data").get_text()
        dom_gross = dom_gross.replace("$","")
        dom_gross = dom_gross.replace(",","")
        print(movie[0], file=open("Pool Standings.txt", "a"))
        

        print("Box Office: ", int(round((float(dom_gross)/1000000),0)), file=open("Pool Standings.txt", "a"))
        return round((float(dom_gross)/1000000),0)
    

def budget(bo_url, budget_backup):
    response = requests.get(bo_url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    content = soup.get_text()
    budget_content = content[content.find("Movie Details"):content.find("Domestic Releases")]
    budget = budget_content[budget_content.find("$"):budget_content.find(",")]
    budget = budget.replace("$", "")
    
    if budget == "":
        print("Budget: " + str(budget_backup), file=open("Pool Standings.txt", "a"))
        return float(budget_backup)
    else:
        print("Budget: ", int(budget), file=open("Pool Standings.txt", "a"))
        return float(budget)



def score(critic, gross, budget):

    total = ((gross-budget)*(((critic))/100))
    return round((total))



def team(team_name):
    team_total = 0
    budget_backup = 0

    for movie in team_name:
        
        title = movie[0]
        rt_url = movie[1]
        bo_url = movie[2]
        
        if len(movie) >= 4:
            if type(movie[3]) == int:
                budget_backup = movie[3]
        
        try:
                
                        print(("Movie: " + title), file=open("Pool Standings.txt", "a"))
                        if title == "Joker":
                            print(critic(rt_url))
                        movie_total = score(critic(rt_url), gross(bo_url, title), budget(bo_url, budget_backup))
                        print("Total Score: ", movie_total, file=open("Pool Standings.txt", "a"))
            

        except Exception as e:
            print(("Movie Unreleased \n"), file=open("Pool Standings.txt", "a"))
            continue
    

        team_total += movie_total

        print("\n", file=open("Pool Standings.txt", "a"))
    return team_total


# rt_url =) "https://www.rottentomatoes.com/m/black_panther_2018"
# # print("Movie: Black Panther")
# # print("Critic Scor: ", critic(rt_url))
# # print("Audience Score: ", audience(rt_url))

# bo_url = "https://www.the-numbers.com/movie/Black-Panther#tab=summary"
# print("Box Office: ", gross(bo_url))
# print("Budget: ", budget(bo_url))

# imdb_url = "http://www.imdb.com/title/tt1825683/awards?ref_=tt_awd"
# print("Oscars Bonus: ", awards(imdb_url))

# print("Total Score: ", score(gross(bo_url), budget(bo_url), critic(rt_url), audience(rt_url), awards(imdb_url)))

# wonder_woman = ("Wonder Woman", "https://www.rottentomatoes.com/m/wonder_woman_2017", "https://www.the-numbers.com/movie/Wonder-Woman-(2017)#tab=summary", "http://www.imdb.com/title/tt0451279/awards?ref_=tt_awd")
# spiderman = ("Spider-Man: Homecoming", "https://www.rottentomatoes.com/m/spider_man_homecoming", "https://www.the-numbers.com/movie/Spider-Man-Homecoming#tab=summary", "http://www.imdb.com/title/tt2250912/awards?ref_=tt_awd")
# dunkirk = ("Dunkirk", "https://www.rottentomatoes.com/m/dunkirk_2017", "https://www.the-numbers.com/movie/Dunkirk#tab)=summary", "http://www.imdb.com/title/tt5013056/awards?ref_=tt_awd")
# pirates5 = ("Pirates of the Caribbean: Dead Men Tell No Tales", "https://www.rottentomatoes.com/m/pirates_of_the_caribbean_dead_men_tell_no_tales", "http://www.boxofficemojo.com/movies/?id=potc5.htm", "http://www.imdb.com/title/tt1790809/awards?ref_=tt_awd")
# brian_team = (wonder_woman, spiderman, pirates5, dunkirk)

# alien_covnant = ("Alien: Covenant", "https://www.rottentomatoes.com/m/alien_covenant", "http://www.boxofficemojo.com/movies/?id=alienparadiselost.htm", "http://www.imdb.com/title/tt2316204/awards?ref_=tt_awd")
# all_eyez = ("All Eyez On Me", "https://www.rottentomatoes.com/m/all_eyez_on_me_2017", "http://www.boxofficemojo.com/movies/?id=tupac.htm", "http://www.imdb.com/title/tt1666185/awards?ref_=tt_awd")
# despicable3 = ("Despicable Me 3", "https://www.rottentomatoes.com/m/de)spicable_me_3", "http://www.boxofficemojo.com/movies/?id=despicableme3.htm", "http://www.imdb.com/title/tt3469046/awards?ref_=tt_awd")
# transformers5 = ("Transformers: The Last Knight", "https://www.rottentomatoes.com/m/transformers_the_last_knight_2017", "https://www.the-numbers.com/movie/Transformers-The-Last-Knight#tab=summary", "http://www.imdb.com/title/tt3371366/awards?ref_=tt_awd")
# kent_team = (alien_covenant, all_eyez, despicable3, transformers5)

# gotg2 = ("Guardians of the Galaxy Vol. 2", "https://www.rottentomatoes.com/m/guardians_of_the_galaxy_vol_2", "https://www.the-numbers.com/movie/Guardians-of-the-Galaxy-Vol-2#tab=summary", "http://www.imdb.com/title/tt3896198/awards?ref_=tt_awd")
# baywatch = ("Baywatch", "https://www.rottentomatoes.com/m/baywatch_2017", "http://www.boxofficemojo.com/movies/?id=baywatch.htm", "http://www.imdb.com/title/tt1469304/awards?ref_=tt_awd")
# mummy = ("The Mummy", "ttps://www.rottentomatoes.com/m/the_mummy_2017", "http://www.boxofficemojo.com/movies/?id=mummy2016.htm", "http://www.imdb.com/title/tt2345759/awards?ref_=tt_awd")
# war_pota = ("War for the Planet of the Apes", "https://www.rottentomatoes.com/m/war_for_the_planet_of_the_apes", "https://www.the-numbers.com/movie/War-for-the-Planet-of-the-Apes#tab=summary", "http://www.imdb.com/title/tt3450958/awards?ref_=tt_awd")
# richard_team = (gotg2, baywatch, mummy, war_pota)

# # print("Brian Total: ", team(brian_team))
# # print("Kent Total: ", team(kent_team))
# # print("Richard Total: ", team(richard_team))

# ladybird = ("Lady Bird", "https://www.rottentomatoes.com/m/lady_bird", "https://www.the-numbers.com/movie/Lady-Bird-(2017)#tab=summary", "http://www.imdb.com/title/tt4925292/awards", 10)
# ragnarok = ("Thor: Ragnarok", "https://www.rottentomatoes.com/m/thor_ragnarok_2017", "https://www.the-numbers.com/movie/Thor-Ragnarok#tab=summary", "http://www.imdb.com/title/tt3501632/awards")
# get_out = ("Get Out", "https://www.rottentomatoes.com/m/get_out/", "https://www.the-numbers.com/movie/Get-Out-(2017)#tab=summary", "http://www.imdb.com/title/tt5052448/awards?ref_=tt_awd")
# big_sick = ("The Big Sick", "https://www.rottentomatoes.com/m/the_big_sick/", "https://ww)w.the-numbers.com/movie/Big-Sick-The#tab=summary", "http://www.imdb.com/title/tt5462602/awards?ref_=tt_awd")
# water = ("The Shape of Water", "https://www.rottentomatoes.com/m/the_shape_of_water_2017", "https://www.the-numbers.com/movie/Shape-of-Water-The#tab=summary", "http://www.imdb.com/title/tt5580390/awards?ref_=tt_awd", 19.5)
# darkest_hour = ("The Darkest Hour", "https://www.rottentomatoes.com/m/darkest_hour_2017", "https://ww.the-numbers.com/movie/Darkest-Hour-(UK)#tab=summary", "http://www.imdb.com/title/tt4555426/awards?ref_=tt_awd", 30)
# last_jedi = ("The Last Jedi", "https://www.rottentomatoes.com/m/star_wars_the_last_jedi)", "https://www.the-numbers.com/movie/Star-Wars-Ep-VIII-The-Last-Jedi#tab=summary", "http://www.imdb.com/title/tt2527336/awards?ref_=tt_awd", 200)

# movies_2017 = [water, ladybird, ragnarok, get_out, big_sick, water, darkest_hour, war_pota, dunkir, transformers5, wonder_woman, spiderman, gotg2]
#print("2017 Movies: ", team(movies_2017)) 