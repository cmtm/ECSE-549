import parameters as p

class Interface:

	def __init__(name, params, specialization = None):
		self.name = name
		self.params = params
		self.specialization = specialization


dc = Interface("DC", [])
ac = Interface("AC", [])
electrical = Interface("electrical", [p.voltage, p.current, p.theveninResistance], [ac, dc])

rotational = Interface("rotational", [p.torque])
linear = Interface("linear", [p.force, p.actuationLength, p.velocity])
mechanical = Interface("mechanical", [], [rotational, mechanical])

general = Interface("general", [p.power, p.frequency], [mechanical, electrical])


# system has 2 interfaces
# it constains system parameters
# it can solve equations about itself
class System:

	def __init__(
