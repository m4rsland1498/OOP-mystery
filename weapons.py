class Weapon:
    instances = []
    def __init__(self, weapon_name):
        self.name = weapon_name
        Weapon.instances.append(self)

    def get_name(self):
        return self.name
