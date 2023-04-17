class Personnel:
    def __init__(self, firstname, lastname, ship, race):
        self.firstname = firstname
        self.lastname = lastname
        self.ship = ship
        self.race = race


class Captain(Personnel):
    def __init__(self, firstname, lastname, ship, race):
        super().__init__(firstname, lastname, ship, race)
        self.__reports_to = 'Admiral'

    def set_reports_to(self, new_reports_to):
        self.__reports_to = new_reports_to

    def get_reports_to(self):
        return self.__reports_to

    def job (self):
        return "Commands the ship"


captain1 = Captain('Kathryn', 'Janeway', 'Voyager', 'human')

captain1.set_reports_to('Vulcan')git
print(captain1.get_reports_to())