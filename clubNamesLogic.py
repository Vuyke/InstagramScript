class Club:
    def __init__(self, name: str, lastPost: int):
        self.name = name
        self.lastPost = lastPost
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.__str__()

class Town:
    def __init__(self, name: str):
        self.name = name
        self.clubs = []
    def add(self, club: str):
        self.clubs.append(club)
    def __str__(self):
        s = f"{self.name}\n"
        for club in self.clubs:
            s += f"{club}\n"
        return s
    def __repr__(self):
        return self.__str__()

class Country:
    def __init__(self, name: str):
        self.name = name
        self.towns = {}
    def __str__(self):
        s = f"\n{self.name}:\n\n"
        for town in self.towns.values():
            s += f"{town}\n"
        return s
    def __repr__(self):
        return self.__str__()

def addClub(countries: dict[str, Country], country: str, town: str, club: str, lastPost: int):
    if country not in countries:
        countries[country] = Country(country)
    if town not in countries[country].towns:
        countries[country].towns[town] = Town(town)
    countries[country].towns[town].add(Club(club, lastPost))
    
def readSingleTown(country: str, town: str, lines: list[str], i: int):
    i += 1
    while i < len(lines) and lines[i] != "\n":
        curLine = lines[i].strip("\n")
        if curLine[0] == '@':
            attr2 = curLine.split("-")
            club = attr2[0].strip("@").strip()
            lastPost = attr2[1].strip()
            addClub(countries, country, town, club, lastPost)
        i += 1
    return i

def readTownsInfo(path: str, countries: dict[str, Country]):
    with open(path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        s = ""
        i = 0
        while i < len(lines):
            line = lines[i].strip()
            if line != "":
                attr = line.split(" - ")
                town = attr[0].strip()
                country = attr[1].strip(":")
                # print(country)
                i = readSingleTown(country, town, lines, i)
            i += 1
            
                    
countries = {}            
readTownsInfo("./Klubovi.txt", countries)
#print(countries.values())
print(countries["SERBIA"].towns["NOVI SAD"])
#print(countries.values())