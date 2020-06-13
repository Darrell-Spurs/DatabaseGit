def name2key(name):
    ind = name.find(" ")
    while ind!=-1:
        name = name[:ind]+"+"+name[ind+1:]
        ind = name.find(" ")
    return name

player = "Donny van de beek"
searchkey = name2key(player)
url="https://www.transfermarkt.com/schnellsuche/ergebnis/schnellsuche?query=%s&x=0&y=0"%searchkey
print(url)