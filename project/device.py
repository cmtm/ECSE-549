import parameters as p

class Interface(object):

	def __init__(name = [], params = []):
		self.name = name
		self.params = params
		self.specializations = []

	def specialize(name, params):
		specialized = Interface()
		specialized.name = self.name.append(name)
		specialized.params = self.params += params
		self.specializations.append(specialized)

		return specialized

general = Interface([], [p.power, p.frequency])

electrical = general.specialize("electrical", [p.voltage, p.current, p.theveninResistance])
dc = electrical.specialize("DC", [])
ac = electrical.specialize("AC", [])

mechanical = specialize("mechanical", [])
rotational = specialize("rotational", [p.torque])
linear = specialize("linear", [p.force, p.actuationLength, p.velocity])


# system has 2 interfaces
# it constains system parameters
# it can solve equations about itself
class System:
	# these are the parameters all systems share
	params = [p.maxDimension, p.mass, p.efficiency, p.heatOutput, p.cost]

	def __init__():
		self.input = None
		self.output = None
