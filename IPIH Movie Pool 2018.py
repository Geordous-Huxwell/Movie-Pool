import Movie_Pool as mp
import operator

panther = ("Black Panther", "https://www.rottentomatoes.com/m/black_panther_2018", "https://www.the-numbers.com/movie/Black-Panther#tab=summary", "http://www.imdb.com/title/tt1825683/awards")
wrinkle = ("A Wrinkle In Time", "https://www.rottentomatoes.com/m/a_wrinkle_in_time_2018", "https://www.the-numbers.com/movie/Wrinkle-in-Time-A-(2018)#tab=summary", "https://www.imdb.com/title/tt1620680/awards")
red_sparrow = ("Red Sparrow", "https://www.rottentomatoes.com/m/red_sparrow", "https://www.the-numbers.com/movie/Red-Sparrow#tab=summary", "http://www.imdb.com/title/tt2873282/awards") 
creed2 = ("Creed 2", "https://www.rottentomatoes.com/m/creed_ii", "https://www.the-numbers.com/movie/Creed-2#tab=summary", "http://www.imdb.com/title/tt6343314/awards")
mortal_engines = ("Mortal Engines", "https://www.rottentomatoes.com/m/mortal_engines", "https://www.the-numbers.com/movie/Mortal-Engines#tab=summary", "http://www.imdb.com/title/tt1571234/awards", 'BOMB')

nick = (panther, wrinkle, red_sparrow, creed2, mortal_engines)

ready = ("Ready Player One", "https://www.rottentomatoes.com/m/ready_player_one", "https://www.the-numbers.com/movie/Ready-Player-One#tab=summary", "http://www.imdb.com/title/tt1677720/awards")
fiftyshades = ("50 Shades Freed", "https://www.rottentomatoes.com/m/fifty_shades_freed", "https://www.the-numbers.com/movie/Fifty-Shades-Freed#tab=summary", "https://www.imdb.com/title/tt4477536/awards")
annihilation = ("Annihilation", "https://www.rottentomatoes.com/m/annihilation", "https://www.the-numbers.com/movie/Annihilation#tab=summary", "http://www.imdb.com/title/tt2798920/awards")
forever_young = ("Forever Young", "https://www.rottentomatoes.com/m/forever_young_2018", "www.boxofficemojo.com/movies/intl/?page=&wk=2018W1&id=_fFOREVERYOUNG202", "http://www.imdb.com/title/tt2401825/awards", 16.3)
alpha = ("Alpha", "https://www.rottentomatoes.com/m/alpha_2018", "https://www.the-numbers.com/movie/Alpha-(2017)#tab=summary", "http://www.imdb.com/title/tt4244998/awards", 'BOMB')

patrick = (ready, fiftyshades, annihilation, forever_young, alpha)

isle = ("Isle of Dogs", "https://www.rottentomatoes.com/m/isle_of_dogs_2018", "https://www.the-numbers.com/movie/Isle-of-Dogs-(2018)#summary", "http://www.imdb.com/title/tt5104604/awards")
pacific_rim = ("Pacific Rim Uprising", "https://www.rottentomatoes.com/m/pacific_rim_uprising", "https://www.the-numbers.com/movie/Pacific-Rim-Uprising#tab=summary", "http://www.imdb.com/title/tt2557478/awards")
love_simon = ("Love, Simon", "https://www.rottentomatoes.com/m/love_simon", "https://www.the-numbers.com/movie/Love-Simon#tab=summary", "http://www.imdb.com/title/tt5164432/awards")
bohemian = ("Bohemian Rhapsody", "https://www.rottentomatoes.com/m/bohemian_rhapsody", "https://www.the-numbers.com/movie/Bohemian-Rhapsody-(2018)#tab=summary", "http://www.imdb.com/title/tt1727824/awards")
mary_poppins = ("Mary Poppins Returns", "https://www.rottentomatoes.com/m/mary_poppins_returns", "https://www.the-numbers.com/movie/Mary-Poppins-Returns#tab=summary", "http://www.imdb.com/title/tt5028340/awards", 'BOMB')

aaron = (isle, pacific_rim, love_simon, bohemian, mary_poppins)

infinity = ("Avengers: Infinity War", "https://www.rottentomatoes.com/m/avengers_infinity_war", "https://www.the-numbers.com/movie/Avengers-Infinity-War#tab=summary", "http://www.imdb.com/title/tt4154756/awards")
jurassic = ("Jurassic World: Fallen Kingdom", "https://www.rottentomatoes.com/m/jurassic_world_fallen_kingdom", "https://www.the-numbers.com/movie/Jurassic-World-Fallen-Kingdom#tab=summary", "http://www.imdb.com/title/tt4881806/?ref_=nv_sr_1")
antman = ("Ant-Man and The Wasp", "https://www.rottentomatoes.com/m/ant_man_and_the_wasp", "https://www.the-numbers.com/movie/Ant-Man-and-the-Wasp#tab=summary", "http://www.imdb.com/title/tt5095030/awards")
first_man = ("First Man", "https://www.rottentomatoes.com/m/first_man", "https://www.the-numbers.com/movie/First-Man#tab=summary", "http://www.imdb.com/title/tt1213641/awards")
english3 = ("Johnny English 3", "https://www.rottentomatoes.com/m/johnny_english_3", "https://www.the-numbers.com/movie/Johnny-English-3#tab=summary", "http://www.imdb.com/title/tt6921996/awards", 'BOMB')

joel = (infinity, jurassic, antman, first_man, english3)

mary = ("Mary, Queen of Scots", "https://www.rottentomatoes.com/m/mary_queen_of_scots", "https://www.the-numbers.com/movie/Mary-Queen-of-Scots-(UK)#tab=summary", "http://www.imdb.com/title/tt2328900/awards")
incredibles2 = ("Incredibles 2", "https://www.rottentomatoes.com/m/incredibles_2", "https://www.the-numbers.com/movie/Incredibles-2-The#tab=summary", "http://www.imdb.com/title/tt3606756/awards")
mammamia2 = ("Mamma Mia 2: Here We Go Again", "https://www.rottentomatoes.com/m/mamma_mia_here_we_go_again", "https://www.the-numbers.com/movie/Mamma-Mia-Here-We-Go-Again#tab=summary", "http://www.imdb.com/title/tt6911608/awards")
chris_robin = ("Christopher Robin", "https://www.rottentomatoes.com/m/christopher_robin", "https://www.the-numbers.com/movie/Christopher-Robin-(2018)#tab=summary", "http://www.imdb.com/title/tt4575576/awards")
aquaman = ("Aquaman", "https://www.rottentomatoes.com/m/aquaman_2018", "https://www.the-numbers.com/movie/Aquaman#tab=summary", "http://www.imdb.com/title/tt1477834/awards", 'BOMB')

elliot = (mary, incredibles2, mammamia2, chris_robin, aquaman)

dp2 = ("Deadpool 2", "https://www.rottentomatoes.com/m/deadpool_2/", "https://www.the-numbers.com/movie/Untitled-Deadpool-Sequel#tab=summary", "http://www.imdb.com/title/tt5463162/awards")
boy_erased = ("Boy Erased", "https://www.rottentomatoes.com/m/boy_erased", "https://www.the-numbers.com/movie/Boy-Erased#tab=summary", "http://www.imdb.com/title/tt7008872/awards")
sorry_to_bother = ("Sorry to Bother You", "https://www.rottentomatoes.com/m/sorry_to_bother_you_2018/", "https://www.the-numbers.com/movie/Sorry-to-Bother-You#tab=summary", "http://www.imdb.com/title/tt5688932/awards")
star_is_born = ("A Star is Born", "https://www.rottentomatoes.com/m/a_star_is_born_2018", "https://www.the-numbers.com/movie/Star-is-Born-A-(2018)#tab=summary", "http://www.imdb.com/title/tt1517451/awards")
proud_mary = ("Proud Mary", "https://www.rottentomatoes.com/m/proud_mary", "https://www.the-numbers.com/movie/Proud-Mary#tab=summary", "http://www.imdb.com/title/tt6421110/awards", 14, 'BOMB')

melissa = (dp2, boy_erased, sorry_to_bother, star_is_born, proud_mary)

solo = ("Solo", "https://www.rottentomatoes.com/m/solo_a_star_wars_story", "https://www.the-numbers.com/movie/Solo-A-Star-Wars-Story#tab=summary", "http://www.imdb.com/title/tt3778644/awards")
tomb_raider = ("Tomb Raider", "https://www.rottentomatoes.com/m/tomb_raider_2018", "https://www.the-numbers.com/movie/Tomb-Raider-(2018)#tab=summary", "http://www.imdb.com/title/tt1365519/awards")
winchester = ("Winchester", "https://www.rottentomatoes.com/m/winchester/", "https://www.the-numbers.com/movie/Winchester#tab=summary", "http://www.imdb.com/title/tt1072748/awards")
maze_runner = ("Maze Runner: The Death Cure", "https://www.rottentomatoes.com/m/maze_runner_the_death_cure", "https://www.the-numbers.com/movie/Maze-Runner-The-Death-Cure#tab=summary", "http://www.imdb.com/title/tt4500922/awards")
meg = ("The Meg", "https://www.rottentomatoes.com/m/the_meg", "https://www.the-numbers.com/movie/Meg-The#tab=summary", "http://www.imdb.com/title/tt4779682/awards", 'BOMB')

dougkate = (solo, tomb_raider, winchester, maze_runner, meg)

alita = ("Alita: Battle Angel", "https://www.rottentomatoes.com/m/alita_battle_angel", "https://www.the-numbers.com/movie/Alita-Battle-Angel#tab=summary", "http://www.imdb.com/title/tt0437086/awards")
predator = ("The Predator", "https://www.rottentomatoes.com/m/the_predator", "https://www.the-numbers.com/movie/Predator-The-(2018)#tab=summary", "http://www.imdb.com/title/tt3829266/awards")
dark_phoenix = ("X-Men: Dark Phoenix", "https://www.rottentomatoes.com/m/x_men_dark_phoenix", "https://www.the-numbers.com/movie/X-Men-Dark-Phoenix-(2018)#tab=summary", "http://www.imdb.com/title/tt6565702/awards")
scarface = ("Scarface", "https://www.rottentomatoes.com/m/scarface_2018", "https://www.the-numbers.com/movie/Scarface-(2018)#tab=summary", "http://www.imdb.com/title/tt2066055/awards")
samson = ("Samson", "https://www.rottentomatoes.com/m/samson_2018", "https://www.the-numbers.com/movie/Samson-(2018)#tab=summary", "http://www.imdb.com/title/tt6951892/awards", 4, 'BOMB')

dara = (alita, predator, dark_phoenix, scarface, samson)

##print("Nick Total: ", mp.team(nick))
#print("Joel Total: ", mp.team(joel))
#print("Patrick Total: ", mp.team(patrick))
#print("Elliot Total: ", mp.team(elliot))
#print("Melissa Total: ", mp.team(melissa))
#print("DougKate Total: ", mp.team(dougkate))
#print("Dara Total: ", mp.team(dara)) 

def standings(players, pools):
	standings_dict = {}
	for player, pool in zip(players, pools):
		standings_dict[player] = mp.team(pool)
	
	bomb_winner = min(mp.bombs.keys(), key=(lambda k: mp.bombs[k]))
	print("Bomb Winner: ", bomb_winner)
	for team in pools:
		for element in team:
			if bomb_winner in element:
				bomb_bonus_team = team
	for team in list(zip(players,pools)):
		if bomb_bonus_team in team:
			bomb_bonus_player_name = team[0]
	
	standings_dict[bomb_bonus_player_name] += 500

	sorted_standings = sorted(standings_dict.items(), key=operator.itemgetter(1),reverse=True)
	for pair in sorted_standings:
		print(pair[0] + ": " + str(pair[1]))
	return
##	
##
players = ["Nick", "Patrick", "Joel", "Aaron", "Elliot", "Melissa", "DougKate", "Dara"]
pools = [nick, patrick, joel, aaron, elliot, melissa, dougkate, dara]

# players = ["Melissa", "Dara"]
# pools = [dara, melissa]

print(standings(players,pools))
