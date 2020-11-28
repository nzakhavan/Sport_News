class Sport(object):
    def __init__(self, team_name, goals):
        self.team_name = team_name
        self.goals = goals

    def __str__(self):
        return "Score of {t} is {g}".format(t = self.team_name, g = self.goals)

    def update_goal(self, new_goal):
        self.goals = new_goal

    def get_name(self):
        return self.team_name

class Date(object):
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "Date: {d}/{m}/{y}".format(d = self.day, m = self.month, y = self.year)

    def get_year(self):
        return self.year

class Magazine(Sport, Date):
    def __init__(self, team_name, goals, year, month, day, number):
        Sport.__init__(self, team_name, goals)
        Date.__init__(self, year, month, day)
        self.number = number

    def __str__(self):
        return "{t} has scored {g} goals on {d}/{m}/{y}. Magazine number: {n}".format(t=self.team_name,
        g=self.goals, d=self.day, m=self.month, y=self.year, n=self.number)

mag = Magazine("barcelona", 5, 2009, "october", 13, "1233483")
print(mag)
print(mag.get_name())
print(mag.get_year())
mag.update_goal(3)
print(mag)
