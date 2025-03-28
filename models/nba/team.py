class Team:
    def __init__(self, name, location, abbreviation):
        self.name = name
        self.location = location
        self.abbreviation = abbreviation
    def get_full_name(self):
        return f"{self.location} {self.name}"
