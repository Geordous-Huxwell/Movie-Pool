import MAM_Pool as mp
import operator
import os

starwars = ("Star Wars: Rise of Skywalker", "https://www.rottentomatoes.com/m/star_wars_the_rise_of_skywalker", "https://www.the-numbers.com/movie/Star-Wars-The-Rise-of-Skywalker-(2019)#tab=summary")
lionking = ("The Lion King", "https://www.rottentomatoes.com/m/the_lion_king_2019", "https://www.the-numbers.com/movie/Lion-King-The-(Live-Action)-(2019)#tab=summary", 260)
lego2 = ("The Lego Movie 2", "https://www.rottentomatoes.com/m/the_lego_movie_2_the_second_part", "https://www.the-numbers.com/movie/Lego-Movie-2-The-Second-Part-The-(2019)#tab=summary")
hobbsandshaw = ("Hobbs and Shaw", "https://www.rottentomatoes.com/m/fast_and_furious_presents_hobbs_and_shaw", "https://www.the-numbers.com/movie/Fast-and-Furious-Presents-Hobbs-and-Shaw-(2019)#tab=summary")
hollywood = ("Once Upon A Time In Hollywood", "https://www.rottentomatoes.com/m/once_upon_a_time_in_hollywood", "https://www.the-numbers.com/movie/Once-Upon-A-Time-In-Hollywood-(2019)#tab=summary")
joker = ("The Joker", "https://www.rottentomatoes.com/m/joker_2019", "https://www.the-numbers.com/movie/Joker-(2019)#tab=summary")
aladdin = ("Aladdin", "https://www.rottentomatoes.com/m/aladdin", "https://www.the-numbers.com/movie/Aladdin-(2019)#tab=summary")
johnwick3 = ("John Wick 3", "https://www.rottentomatoes.com/m/john_wick_chapter_3_parabellum", "https://www.the-numbers.com/movie/John-Wick-Chapter-3-Parabellum-(2019)#tab=summary")

richard = (starwars, lionking, lego2, hobbsandshaw, hollywood, joker, aladdin, johnwick3)

toystory4 = ("Toy Story 4", "https://www.rottentomatoes.com/m/toy_story_4", "https://www.the-numbers.com/movie/Toy-Story-4-(2019)#tab=summary", 200)
spiderman2 = ("Spider-Man: Far From Home", "https://www.rottentomatoes.com/m/spider_man_far_from_home", "https://www.the-numbers.com/movie/Spider-Man-Far-From-Home-(2019)#tab=summary")
traindragon3 = ("How to Train Your Dragon: The Hidden World", "https://www.rottentomatoes.com/m/how_to_train_your_dragon_the_hidden_world", "https://www.the-numbers.com/movie/How-to-Train-Your-Dragon-The-Hidden-World-(2019)#tab=summary")
frozen2 = ("Frozen 2", "https://www.rottentomatoes.com/m/frozen_2", "https://www.the-numbers.com/movie/Frozen-II-(2019)#tab=summary")
jumanji3 = ("Jumanji 3", "https://www.rottentomatoes.com/m/untitled_jumanji_welcome_to_the_jungle_sequel", "https://www.the-numbers.com/movie/Jumanji-3-(2019)#tab=summary")
meninblack = ("Men in Black International", "https://www.rottentomatoes.com/m/men_in_black_international", "https://www.the-numbers.com/movie/Men-in-Black-International-(2019)#tab=summary")
godzilla = ("Godzilla: King of Monsters", "https://www.rottentomatoes.com/m/godzilla_king_of_the_monsters_2019", "https://www.the-numbers.com/movie/Godzilla-King-of-the-Monsters-(2019)#tab=summary")
hellboy = ("Hellboy", "https://www.rottentomatoes.com/m/hellboy_2019", "https://www.the-numbers.com/movie/Hellboy-(2019)#tab=summary")

brian = (toystory4, spiderman2, traindragon3, frozen2, jumanji3, meninblack, godzilla, hellboy)

endgame = ("Avengers: Endgame", "https://www.rottentomatoes.com/m/avengers_endgame", "https://www.the-numbers.com/movie/Avengers-Endgame-(2019)#tab=summary", 356)
captain_marvel = ("Captain Marvel", "https://www.rottentomatoes.com/m/captain_marvel", "https://www.the-numbers.com/movie/Captain-Marvel-(2019)#tab=summary")
it2 = ("It: Chapter 2", "https://www.rottentomatoes.com/m/it_chapter_two", "https://www.the-numbers.com/movie/It-Chapter-Two-(2019)#tab=summary")
pikachu = ("Detective Pikachu", "https://www.rottentomatoes.com/m/pokemon_detective_pikachu", "https://www.the-numbers.com/movie/Pokemon-Detective-Pikachu-(2019)#tab=summary")
us = ("Us", "https://www.rottentomatoes.com/m/us_2019", "https://www.the-numbers.com/movie/Us-(2019)#tab=summary")
shazam = ("Shazam!", "https://www.rottentomatoes.com/m/shazam", "https://www.the-numbers.com/movie/Shazam-(2019)#tab=summary")
zombieland2 = ("Zombieland: Double Tap", "https://www.rottentomatoes.com/m/zombieland_double_tap", "https://www.the-numbers.com/movie/Zombieland-Double-Tap-(2019)#tab=summary")
downton = ("Downton Abbey", "https://www.rottentomatoes.com/m/downton_abbey", "https://www.the-numbers.com/movie/Downton-Abbey-(UK)-(2019)#tab=summary", 80)

kent = (endgame, captain_marvel, it2, pikachu, us, shazam, zombieland2, downton)



def standings(players, pools):
	standings_dict = {}
	for player, pool in zip(players, pools):
		standings_dict[player] = mp.team(pool)
	
	
	sorted_standings = sorted(standings_dict.items(), key=operator.itemgetter(1),reverse=True)
	for pair in sorted_standings:
		print(pair[0] + ": " + str(pair[1]), file=open("Pool Standings.txt", "a"))
	

players = ["Richard", "Brian", "Kent"]
pools = [richard, brian, kent]


def update_file(fileData):
	with open("Pool Standings.txt", "a") as file:
	
		file.write(str(fileData))
		file.close()

with open("Pool Standings.txt", "w+"):
	print(standings(players,pools))

