import random

from gen.sam.group_generator import GroupGenerator


class LHAGroupGenerator(GroupGenerator):

    def __init__(self, game, ground_object, faction):
        super(LHAGroupGenerator, self).__init__(game, ground_object)
        self.faction = faction

    def generate(self):

        # Add carrier
        if len(self.faction.helicopter_carrier) > 0:
            carrier_type = random.choice(self.faction.helicopter_carrier)
            self.add_unit(carrier_type, "LHA", self.position.x, self.position.y, self.heading)

        # Add destroyers escort
        if len(self.faction.destroyers) > 0:
            dd_type = random.choice(self.faction.destroyers)
            self.add_unit(dd_type, "DD1", self.position.x + 1250, self.position.y + 1450, self.heading)
            self.add_unit(dd_type, "DD2", self.position.x + 1250, self.position.y - 1450, self.heading)

        self.get_generated_group().points[0].speed = 20