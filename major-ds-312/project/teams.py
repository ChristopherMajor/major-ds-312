class Team():
    def __init__(self, name, city, sport=None):
        self.name = name
        self.city = city
        self.sport = sport
    
    @property
    def full_name(self):
        return f"{team.city} {team.name}"


if __name__ =="__main__":

    teams = [
    {'name': 'Yankees', 'city': 'New York'},
    {'name': 'Mets', 'city': 'New York'},
    {'name': 'Nationals', 'city': 'Washington'}
    ]

    for d in teams:
        team = Team(d['name'], d['city'])
        print(team.name)
        print(team.full_name)