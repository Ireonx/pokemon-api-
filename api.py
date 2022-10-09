import requests
import json
import random
import sys
import copy
import os


url = 'https://pokeapi.co/api/v2/pokemon'


user_ch = None
used = False
cur_menu = {}
toprint = """
Select characteristics
    1.Abilities
    2.Base expreience
    3.Defense
    4.Attack
    5.Speed
    6.Hp
    7.Approve
"""
response = requests.get(url)
pokemon_dic = response.json()
list_of_pokemons = []
characteristics_list = ["name"]
previous_list = []
current_list = []
chr_l = ["name"]
payload = {"limit" : 1,"offset": None}
just_name = False
def PokListGenerator():
    list_of_pokemons.clear()
    current_list.clear()
    for i in range(5):
        pokemon_num = random.randint(1,1050)
        if pokemon_num not in list_of_pokemons:
            list_of_pokemons.append(pokemon_num)
            payload["offset"] = pokemon_num
            response = requests.get(url, params=payload)
            current_list.append(response.json()['results'][0]['url'])

characteristics = {
    "1" : "abilities",
    "2" : "base_experience",
    "3" : "defense",
    "4" : "attack",
    "5" : "speed",
    "6" : "hp",
}

chr = {
    "1" : """
ab = characteristics["1"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "2" : """
ab = characteristics["2"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "3" : """
ab = characteristics["3"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "4" : """
ab = characteristics["4"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "5" : """
ab = characteristics["5"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "6" : """
ab = characteristics["6"]
if ab not in chr_l:
    chr_l.append(ab)
elif ab in chr_l:
    chr_l.remove(ab)
user_ch,cur_menu = add_crst()
    """,
    "7" : """
os.system("cls")
user_ch,cur_menu = mm()  
    """
}

main_menu = {
    "1" : """
os.system("cls")
PokListGenerator()
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
user_ch,cur_menu = lm()
""",
    "2" : """
os.system("cls")
print(toprint)
user_ch,cur_menu = add_crst()
    """,
    "3" : "sys.exit()"
}

list_menu = {
    "11" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[0]
ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "12" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[1]
ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "13" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[2]
ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "14" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[3]
ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "15" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[4]
ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "21" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[0]
pics(pokemon)
user_ch,cur_menu = lm()  
    """,
    "22" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[1]
pics(pokemon)
user_ch,cur_menu = lm()  
    """,
    "23" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[2]
pics(pokemon)
user_ch,cur_menu = lm()  
    """,
    "24" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[3]
pics(pokemon)
user_ch,cur_menu = lm()  
    """,
    "25" : """
os.system("cls")
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
pokemon = current_list[4]
pics(pokemon)
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "3" : """
os.system("cls")
current_list = copy.deepcopy(previous_list)
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
user_ch,cur_menu = lm()  
    """,
    "4" : """
os.system("cls")
previous_list.clear()
previous_list = copy.deepcopy(current_list)
PokListGenerator()
for pokemon in current_list:
    just_name = True
    ShowCrst(pokemon)
user_ch,cur_menu = lm()  
""",
    "5" : "user_ch,cur_menu = mm()",
    "6" : "sys.exit()"
}

def ShowCrst(pokemon):
    global just_name
    response = requests.get(pokemon)
    if not just_name:
        c_l = chr_l
    else:
        c_l = characteristics_list
    for characteristic in c_l:
        if characteristic==characteristics["1"]:
            data = response.json()["abilities"]
            print("Pokemon abilities:")
            print(len(data))
            if len(data)>0:
                for i in range(0, len(data)):
                    data = response.json()["abilities"][i]["ability"]
                    try:
                        data = f"{data['name']}\nDescription:\n{requests.get(data['url']).json()['effect_entries'][1]['effect']}"
                    except IndexError:
                        data = f"{data['name']}\nDescription:\n{requests.get(data['url']).json()['effect_entries'][0]}"
                    print(data)
        elif characteristic==characteristics["2"]:
            data = response.json()["base_experience"]
            print(data)
        elif characteristic==characteristics["3"]:
            data = response.json()["stats"][2]["base_stat"]
            print(data)
        elif characteristic==characteristics["4"]:
            data = response.json()["stats"][1]["base_stat"]
            print(data)
        elif characteristic==characteristics["5"]:
            data = response.json()["stats"][5]["base_stat"]
            print(data)
        elif characteristic==characteristics["6"]:
            data = response.json()["stats"][0]["base_stat"]
            print(data)
        else:
            data = response.json()["name"]
            data = json.dumps(data, indent=2)
            print(data)
    just_name = False

def pics(ur):
    response = requests.get(ur)
    responsename = response
    name = responsename.json()["name"]
    data = response.json()["sprites"]["other"]["official-artwork"]["front_default"]
    if data == None:
        data = response.json()["sprites"]["front_default"]
    if data != None:
        response = requests.get(data)
        with open(f'pokemons\\{name}.png', 'wb') as f:
            f.write(response.content)
            f.close()


def add_crst():
    cur_menu = chr
    user_ch = input()
    return user_ch, cur_menu

def mm():
    cur_menu = main_menu
    print("""Main menu
    1.Show list
    2.Change characteristics 
    3.Exit program
    """)
    user_ch = input()
    return user_ch, cur_menu

def lm():
    cur_menu = list_menu
    print("""List 
    1.Show pokemon's characteristics
    2.Save pokemon's picture
    3.Previous list
    4.New list
    5.Maim menu
    6.Exit program
    """)
    user_ch = input()
    return user_ch, cur_menu

if not os.path.exists("pokemons"):
    os.makedirs("pokemons")

user_ch,cur_menu = mm()
while True:
    exec(cur_menu[f"{user_ch}"])
