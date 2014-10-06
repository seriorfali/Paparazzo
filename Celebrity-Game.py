class Neighborhood(object):
    def __init__(self, name, places):
        self.name = name
        self.places = places
    def print_map(self):
        place_names = [[] for p in range(len(self.places))]
        for p in range(len(place_names)):
            for place in range(len(self.places[p])):
                place_names[p].insert(place, self.places[p][place].name)
            print " | ".join(place_names[p])

class Region(object):
    def __init__(self, name, neighborhoods):
        self.name = name
        self.neighborhoods = neighborhoods
    def neighborhood_map(self):
        neighborhood_map = [[] for group in range(len(self.neighborhoods))]
        for group in range(len(neighborhood_map)):
            for neighborhood in range(len(self.neighborhoods[group])):
                neighborhood_map[group].insert(neighborhood, self.neighborhoods[group][neighborhood].name)
        return neighborhood_map
    def print_map(self):
        neighborhood_map = self.neighborhood_map()
        for group in range(len(neighborhood_map)):
            print " | ".join(neighborhood_map[group])
    def neighborhood_names(self):
        neighborhood_map = self.neighborhood_map()
        neighborhood_names = []
        for group in neighborhood_map:
            for neighborhood_name in group:
                neighborhood_names.append(neighborhood_name)
        return neighborhood_names
    def neighborhood_choice(self):
        neighborhood_names = self.neighborhood_names()
        while (True):
            if celebrities == 1:
                print "There is 1 celebrity out in public in %s!" % (self.name)
                neighborhood_choice = raw_input("Which neighborhood do you think he or she is in? ")
            else:
                print "There are %s celebrities out in public in %s!" % (celebrities, self.name)
                neighborhood_choice = raw_input("Which neighborhood do you think they're in? ")
            if neighborhood_choice not in self.neighborhood_names():
                print "Oops! You can only search in the listed neighborhoods!"
            else:
                return neighborhood_choice
                break
    def print_neighborhood_map(self):
        for group in range(len(self.neighborhoods)):
            for neighborhood in range(len(self.neighborhoods[group])):
                if neighborhood_choice == self.neighborhoods[group][neighborhood].name:
                    self.neighborhoods[group][neighborhood].print_map()
                    
class RegionGroup(object):
    def __init__(self, regions):
        self.regions = regions
    def region_names(self):
        region_names = []
        for region in self.regions:
            region_names.append(region.name)
        return region_names
    def print_names(self):
        region_names = self.region_names()
        for region_name in region_names:
            print region_name
    def region_choice(self):
        while (True):
            region_choice = raw_input("Which region do you want to go to? ")
            if region_choice not in self.region_names():
                print "Oops! You can only go to the listed regions!"
            for region in self.regions:
                if region_choice == region.name:
                    return region
                    break
                    
class Place(object):
    def __init__(self, name, category):
        self.name = name
        self.category = category
    def __repr__(self):
        return self.name
        
class Category(object):
    def __init__(self, name):
        self.name = name
        
#CATEGORIES:
restaurant = Category("Restaurant")

university = Category("University")

park = Category("Park")

stroll = Category("Outdoor space")

show = Category("Show")

hospital = Category("Hospital")

grocery = Category("Grocery store")

exhibition = Category("Exhibition")

leisure = Category ("Activity")

museum = Category("Museum")

shop = Category("Shop")

event = Category("Event site")

broadcast = Category("TV shoot location")

hotel = Category("Hotel")

transit = Category("Transportation station or route")

cause = Category("Institution dedicated to a cause")

landmark = Category("Landmark")

club = Category("Nightclub")

home = Category("Residence")

speakeasy = Category("Speakeasy")

cafe = Category("Cafe")
        
#PLACES:
toms = Place("Tom's Restaurant", restaurant)

columbia = Place("Columbia University", university)

morningside_park = Place("Morningside Park", park)

m_x_blvd = Place("Malcolm X Boulevard", stroll)

sylvias = Place("Sylvia's", restaurant)

apollo_theater = Place("Apollo Theater", show)

red_rooster = Place("Red Rooster", restaurant)

raos = Place("Rao's", restaurant)

jeff_park = Place("Jefferson Park", park)

mt_sinai = Place("Mount Sinai", hospital)

uws_wf = Place("Whole Foods", grocery)

riverside_park = Place("Riverside Park", park)

lincoln_center = Place("Lincoln Center", exhibition)

masa = Place("Masa", restaurant)

per_se = Place("Per Se", restaurant)

cp_reservoir = Place("The Reservoir", park)

cp_lawn = Place("Great Lawn", park)

cp_lake = Place("The Lake", park)

cp_ice = Place("Ice Skating Rink", leisure)

met = Place("The Met", museum)

madison_ave = Place("Madison Avenue", shop)

daniel = Place("Daniel", restaurant)

barneys = Place("Barneys", shop)

lucky_strike = Place("Lucky Strike", leisure)

theatre_row = Place("Theatre Row", show)

juniors = Place("Junior's", restaurant)

broadway_show = Place("Broadway show", show)

times_square = Place("Times Square", event)

gma = Place("Good Morning America", broadcast)

nyc_nobu = Place("Nobu", restaurant)

fiftyseventh_st = Place("57th Street", shop)

fifth_ave = Place("5th Avenue", shop)

le_cirque = Place("Le Cirque", restaurant)

butter = Place("Butter", restaurant)

waldorf = Place("Waldorf-Astoria", hotel)

bryant_park = Place("Bryant Park", park)

grand_central = Place("Grand Central Terminal", transit)

tbg = Place("Turtle Bay Gardens", stroll)

un = Place("United Nations", cause)

javits = Place("Javits Center", exhibition)

msg = Place("Madison Square Garden", show)

penn_station = Place("Penn Station", transit)

nyc_macys = Place("Macy's", shop)

herald_square = Place("Herald Square", event)

empire_state = Place("Empire State Building", landmark)

park_ave = Place("Park Avenue", stroll)

mh_e_river_ferry = Place("East River Ferry", transit)

marquee = Place("Marquee", club)

chelsea_wf = Place("Whole Foods", grocery)

chelsea_piers = Place("Chelsea Piers", exhibition)

high_line = Place("The High Line", park)

avenue = Place("Avenue", club)

ace_hotel = Place("Ace Hotel", hotel)

nomad_restaurant = Place("The NoMad", restaurant)

ilili = Place("Ilili", restaurant)

gansevoort = Place("The Gansevoort", hotel)

riverpark = Place("Riverpark", restaurant)

standard = Place("The Standard", club)

fourteenth_st = Place("West 14th Street", shop)

catch = Place("Catch", club)

tao = Place("Tao Downtown", club)

dream = Place("Dream Downtown", club)

forty_40 = Place("40/40", club)

eataly = Place("Eataly", restaurant)

msp = Place("Madison Square Park", park)

shake_shack = Place("Shake Shack", restaurant)

eleven_mad = Place("Eleven Madison Park", restaurant)

fifth_ave_s = Place("5th Avenue", shop)

one_mad = Place("One Madison", home)

g_tavern = Place("Gramercy Tavern", restaurant)

g_park_hotel = Place("Gramercy Park Hotel", hotel)

g_park = Place("Gramercy Park", park)

irving = Place("Irving Place", stroll)

abc = Place("ABC Kitchen", restaurant)

u_sq_cafe = Place("Union Square Cafe", restaurant)

u_sq_park = Place("Union Square Park", park)

max_brenner = Place("Max Brenner", restaurant)

oval = Place("The Oval", park)

c_st_pier = Place("Christopher Street Pier", park)

jane = Place("The Jane", club)

spotted_pig = Place("The Spotted Pig", restaurant)

bleecker_st = Place("Bleecker Street", shop)

magnolia = Place("Magnolia Bakery", restaurant)

around_5_ave = Place("Around 5th Avenue", stroll)

strand = Place("Strand", shop)

w_sq_park = Place("Washington Square Park", park)

minetta = Place("Minetta Tavern", restaurant)

il_mulino = Place("Il Mulino", restaurant)

da_silvano = Place("Da Silvano", restaurant)

s_village = Place("South Village", stroll)

gato = Place("Gato", restaurant)

acme = Place("Acme", restaurant)

bond_st = Place("Bond Street", stroll)

smile = Place("The Smile", restaurant)

il_buco = Place("Il Buco", restaurant)

bowery_hotel = Place("The Bowery Hotel", hotel)

st_marks = Place("St. Marks Place", stroll)

alder = Place("Alder", restaurant)

pdt = Place("PDT", speakeasy)

t_sq_park = Place("Tompkins Square Park", park)

alphabet_city = Place("Alphabet City", stroll)

trump_soho = Place("Trump SoHo", hotel)

holland_tunnel = Place("Holland Tunnel", transit)

d_ansel = Place("Dominique Ansel Bakery", cafe)

sixty_thompson = Place("60 Thompson", hotel)

w_broadway = Place("West Broadway", shop)

mercer = Place("The Mercer", hotel)

lure = Place("Lure Fishbar", restaurant)

broadway = Place("Broadway", shop)

balthazar = Place("Balthazar", restaurant)

mondrian_soho = Place("Mondrian SoHo", hotel)

mcnally = Place("McNally Jackson", shop)

mulberry_st = Place("Mulberry Street", stroll)

nolita_boutiques = Place("Boutiques", shop)

public = Place("Public", restaurant)

les_wf = Place("Whole Foods", grocery)

nyc_box = Place("The Box", club)

katz = Place("Katz' Delicatessen", restaurant)

il_lab = Place("Il Laboratorio di Gelato", restaurant)

beauty_essex = Place("Beauty & Essex", speakeasy)

hud_river_park = Place("Hudson River Park", park)

locanda = Place("Locanda Verde", restaurant)

greenwich_hotel = Place("The Greenwich Hotel", hotel)

bubbys = Place("Bubby's", restaurant)

bouley = Place("Bouley", restaurant)

odeon = Place("The Odeon", restaurant)

tribeca_wf = Place("Whole Foods", grocery)

little_italy = Place("Little Italy", stroll)

canal_st = Place("Canal Street", stroll)

bk_br = Place("Brooklyn Bridge", stroll)

man_br = Place("Manhattan Bridge", transit)

goldman_alley = Place("Goldman Alley", stroll)

hud_eats = Place("Hudson Eats", restaurant)

bpc_esplanade = Place("Esplanade", park)

nine_eleven = Place("9/11 Memorial", park)

wall_st = Place("Wall Street", stroll)

bp = Place("Battery Park", park)

smorgasbar = Place("SmorgasBar", restaurant)

pier_15 = Place("Pier 15", park)


#NEIGHBORHOODS:
morningside_heights = Neighborhood("Morningside Heights", [[toms, columbia, morningside_park]])

harlem = Neighborhood("Harlem", [[m_x_blvd, sylvias], [apollo_theater, red_rooster]])

east_harlem = Neighborhood("East Harlem", [[raos], [jeff_park], [mt_sinai]])

upper_west_side = Neighborhood("Upper West Side", [[uws_wf], [riverside_park, lincoln_center, masa, per_se]])

central_park = Neighborhood("Central Park", [[cp_reservoir], [cp_lawn], [cp_lake], [cp_ice]])

upper_east_side = Neighborhood("Upper East Side", [[met, madison_ave, daniel], [barneys]])

hells_kitchen = Neighborhood("Hell's Kitchen", [[lucky_strike, theatre_row]])

theatre_district = Neighborhood("Theatre District", [[juniors, broadway_show, times_square, gma]])

midtown_east = Neighborhood("Midtown East", [[nyc_nobu, fiftyseventh_st, fifth_ave, le_cirque], [butter, waldorf], [bryant_park, grand_central]])

turtle_bay = Neighborhood("Turtle Bay", [[tbg, un]])

hudson_yards = Neighborhood("Hudson Yards", [[javits, msg, penn_station]])

garment_district = Neighborhood("Garment District", [[nyc_macys, herald_square, empire_state]])

murray_hill = Neighborhood("Murray Hill", [[park_ave, mh_e_river_ferry]])

chelsea = Neighborhood("Chelsea", [[marquee, chelsea_wf], [chelsea_piers, high_line, avenue]])

nomad = Neighborhood("NoMad", [[ace_hotel, nomad_restaurant, ilili]])

rose_hill_and_kips_bay = Neighborhood("Rose Hill and Kips Bay", [[gansevoort, riverpark]])

meatpacking_district = Neighborhood("Meatpacking District", [[standard, fourteenth_st, catch, tao, dream]])

flatiron_district = Neighborhood("Flatiron District", [[forty_40, eataly, msp, shake_shack, eleven_mad], [fifth_ave_s, one_mad, g_tavern]])

gramercy = Neighborhood("Gramercy", [[g_park_hotel], [g_park], [irving]])

union_square = Neighborhood("Union Square", [[abc], [u_sq_cafe, u_sq_park], [max_brenner]])

stuyvesant_town = Neighborhood("Stuyvesant Town", [[oval]])

west_village = Neighborhood("West Village", [[c_st_pier, jane, spotted_pig, bleecker_st, magnolia]])

greenwich_village = Neighborhood("Greenwich Village", [[around_5_ave, strand], [w_sq_park], [minetta, il_mulino], [da_silvano, s_village]])

noho = Neighborhood("NoHo", [[gato, acme, bond_st, smile, il_buco, bowery_hotel]])

east_village = Neighborhood("East Village", [[st_marks, alder, pdt, t_sq_park, alphabet_city]])

hudson_square = Neighborhood("Hudson Square", [[trump_soho], [holland_tunnel]])

soho = Neighborhood("SoHo", [[d_ansel, sixty_thompson, w_broadway, mercer, lure, broadway, balthazar, mondrian_soho]])

nolita = Neighborhood("Nolita", [[mcnally, mulberry_st, nolita_boutiques, public]])

lower_east_side = Neighborhood("Lower East Side", [[les_wf, nyc_box, katz, il_lab, beauty_essex]])

tribeca = Neighborhood("Tribeca", [[hud_river_park, locanda, greenwich_hotel, bubbys], [bouley, odeon], [tribeca_wf]])

chinatown = Neighborhood("Chinatown", [[little_italy, canal_st]])

two_bridges = Neighborhood("Two Bridges", [[bk_br, man_br]])

battery_park_city = Neighborhood("Battery Park City", [[goldman_alley], [hud_eats], [bpc_esplanade]])

financial_district = Neighborhood("Financial District", [[nine_eleven], [wall_st], [bp]])

south_street_seaport = Neighborhood("South Street Seaport", [[smorgasbar, pier_15]])

#REGION NEIGHBORHOODS:
manhattan_neighborhoods = [[morningside_heights, harlem, east_harlem], [upper_west_side, central_park, upper_east_side], [hells_kitchen, theatre_district, midtown_east, turtle_bay], [hudson_yards, garment_district, murray_hill], [chelsea, nomad, rose_hill_and_kips_bay], [meatpacking_district, flatiron_district, union_square, gramercy, stuyvesant_town], [west_village, greenwich_village, noho, east_village], [hudson_square, soho, nolita, lower_east_side], [tribeca, chinatown, two_bridges], [battery_park_city, financial_district, south_street_seaport]]

#REGIONS:
manhattan = Region("Manhattan", manhattan_neighborhoods)

#REGION GROUPS:
regions = RegionGroup([manhattan])

#GAME:
regions.print_names()

region_choice = regions.region_choice()

region_choice.print_map()

import random

from datetime import datetime

import calendar

def celebrity_number(time):
    r = random.random()
    if 0 <= calendar.weekday(time.year, time.month, time.day) <= 2:
        if 0 <= time.hour < 3:
            p1 = 0.8
            p2 = 0.15
            p3 = 0.05
        elif 3 <= time.hour < 7:
            p1 = 1
        elif 7 <= time.hour < 10:
            p1 = 0.6
            p2 = 0.3
            p3 = 0.1
        elif 10 <= time.hour < 19:
            p1 = 0.3
            p2 = 0.3
            p3 = 0.25
        elif 19 <= time.hour < 22:
            p1 = 0.2
            p2 = 0.4
            p3 = 0.3
        else:
            p1 = 0.4
            p2 = 0.35
            p3 = 0.2
    elif calendar.weekday(time.year, time.month, time.day) == 3:
        if 0 <= time.hour < 3:
            p1 = 0.8
            p2 = 0.15
            p3 = 0.05
        elif 3 <= time.hour < 7:
            p1 = 1
        elif 7 <= time.hour < 10:
            p1 = 0.65
            p2 = 0.2
            p3 = 0.1
        elif 10 <= time.hour < 19:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.4
        elif 19 <= time.hour < 22:
            p1 = 0.1
            p2 = 0.2
            p3 = 0.3
        else:
            p1 = 0.1
            p2 = 0.25
            p3 = 0.45
    elif calendar.weekday(time.year, time.month, time.day) == 4:
        if 0 <= time.hour < 3:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.8
            p2 = 0.2
        elif 7 <= time.hour < 10:
            p1 = 0.65
            p2 = 0.3
            p3 = 0.05
        elif 10 <= time.hour < 19:
            p1 = 0.15
            p2 = 0.25
            p3 = 0.45
        elif 19 <= time.hour < 22:
            p1 = 0.0
            p2 = 0.1
            p3 = 0.3
        else:
            p1 = 0.0
            p2 = 0.0
            p3 = 0.3
    elif calendar.weekday(time.year, time.month, time.day) == 5:
        if 0 <= time.hour < 3:
            p1 = 0.0
            p2 = 0.05
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.55
            p2 = 0.25
            p3 = 0.15
        elif 7 <= time.hour < 12:
            p1 = 0.8
            p2 = 0.2
        elif 12 <= time.hour < 16:
            p1 = 0.1
            p2 = 0.2
            p3 = 0.35
        elif 16 <= time.hour < 19:
            p1 = 0.25
            p2 = 0.4
            p3 = 0.3
        elif 19 <= time.hour < 22:
            p1 = 0.05
            p2 = 0.1
            p3 = 0.2
        else:
            p1 = 0.0
            p2 = 0.0
            p3 = 0.3
    else:
        if 0 <= time.hour < 3:
            p1 = 0.0
            p2 = 0.05
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.55
            p2 = 0.25
            p3 = 0.15
        elif 7 <= time.hour < 12:
            p1 = 1
        elif 12 <= time.hour < 16:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.3
        elif 16 <= time.hour < 19:
            p1 = 0.25
            p2 = 0.25
            p3 = 0.25
        elif 19 <= time.hour < 22:
            p1 = 0.2
            p2 = 0.35
            p3 = 0.35
        else:
            p1 = 0.45
            p2 = 0.35
            p3 = 0.2
    if r < p1:
        celebrities = random.randint(1, 5)
    elif r < (p1 + p2):
        celebrities = random.randint(5, 10)
    elif r < (p1 + p2 + p3):
        celebrities = random.randint(10, 15)
    else:
        celebrities = random.randint(15, 21)
    return celebrities
    
def celebrity_locations(time):
    r = random.random()
    if 0 <= calendar.weekday(time.year, time.month, time.day) <= 2:
        if 0 <= time.hour < 3:
            p1 = 0.8
            p2 = 0.15
            p3 = 0.05
        elif 3 <= time.hour < 7:
            p1 = 1
        elif 7 <= time.hour < 10:
            p1 = 0.6
            p2 = 0.3
            p3 = 0.1
        elif 10 <= time.hour < 19:
            p1 = 0.3
            p2 = 0.3
            p3 = 0.25
        elif 19 <= time.hour < 22:
            p1 = 0.2
            p2 = 0.4
            p3 = 0.3
        else:
            p1 = 0.4
            p2 = 0.35
            p3 = 0.2
    elif calendar.weekday(time.year, time.month, time.day) == 3:
        if 0 <= time.hour < 3:
            p1 = 0.8
            p2 = 0.15
            p3 = 0.05
        elif 3 <= time.hour < 7:
            p1 = 1
        elif 7 <= time.hour < 10:
            p1 = 0.65
            p2 = 0.2
            p3 = 0.1
        elif 10 <= time.hour < 19:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.4
        elif 19 <= time.hour < 22:
            p1 = 0.1
            p2 = 0.2
            p3 = 0.3
        else:
            p1 = 0.1
            p2 = 0.25
            p3 = 0.45
    elif calendar.weekday(time.year, time.month, time.day) == 4:
        if 0 <= time.hour < 3:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.8
            p2 = 0.2
        elif 7 <= time.hour < 10:
            p1 = 0.65
            p2 = 0.3
            p3 = 0.05
        elif 10 <= time.hour < 19:
            p1 = 0.15
            p2 = 0.25
            p3 = 0.45
        elif 19 <= time.hour < 22:
            p1 = 0.0
            p2 = 0.1
            p3 = 0.3
        else:
            p1 = 0.0
            p2 = 0.0
            p3 = 0.3
    elif calendar.weekday(time.year, time.month, time.day) == 5:
        if 0 <= time.hour < 3:
            p1 = 0.0
            p2 = 0.05
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.55
            p2 = 0.25
            p3 = 0.15
        elif 7 <= time.hour < 12:
            p1 = 0.8
            p2 = 0.2
        elif 12 <= time.hour < 16:
            p1 = 0.1
            p2 = 0.2
            p3 = 0.35
        elif 16 <= time.hour < 19:
            p1 = 0.25
            p2 = 0.4
            p3 = 0.3
        elif 19 <= time.hour < 22:
            p1 = 0.05
            p2 = 0.1
            p3 = 0.2
        else:
            p1 = 0.0
            p2 = 0.0
            p3 = 0.3
    else:
        if 0 <= time.hour < 3:
            p1 = 0.0
            p2 = 0.05
            p3 = 0.4
        elif 3 <= time.hour < 7:
            p1 = 0.55
            p2 = 0.25
            p3 = 0.15
        elif 7 <= time.hour < 12:
            p1 = 1
        elif 12 <= time.hour < 16:
            p1 = 0.2
            p2 = 0.3
            p3 = 0.3
        elif 16 <= time.hour < 19:
            p1 = 0.25
            p2 = 0.25
            p3 = 0.25
        elif 19 <= time.hour < 22:
            p1 = 0.2
            p2 = 0.35
            p3 = 0.35
        else:
            p1 = 0.45
            p2 = 0.35
            p3 = 0.2
    if r < p1:
        celebrities = random.randint(1, 5)
    elif r < (p1 + p2):
        celebrities = random.randint(5, 10)
    elif r < (p1 + p2 + p3):
        celebrities = random.randint(10, 15)
    else:
        celebrities = random.randint(15, 21)
    return celebrities
    
current_time = datetime.now()
    
celebrities = celebrity_number(current_time)

neighborhood_choice = region_choice.neighborhood_choice()

region_choice.print_neighborhood_map()

# CATCH IS MONDAYS
