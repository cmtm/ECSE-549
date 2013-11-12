import sympy.physics.units as Units
import math


class Parameter:
	def __init__(name, glyph, units, domain = [0,float("inf")], description = ""):
		self.name = name
		self.glyph = glyph
		self.units = units 
		self.domain = domain

# --- Interfaces -------------------
#
# electrical
voltage = Parameter("voltage", "V", "V", "In the case of AC, the voltage is the rms amplitude")
current = Parameter("current", "I", "A", "In the case of AC, the current is the rms amplitude")
theveninResistance = Parameter("theveninResistance", "R", "ohms", "The input or output resistance")

# mechanical rotational
# rotational speed is an analogue of frequency, I might just get rid of this
# I'm using it to avoid having to implement a full units system
# as motor rotation is usually measure in rpm or in rad/s
rotationalSpeed = Parameter("rotational speed", "omega", 'rad/s')
torque = Parameter("torque", "tau", 'Nm')

# mechanical linear
actuationLength = Parameter("actuation length", "l", "m")
forceAtEnds = Parameter("force at end", "Fe", "N", "The force created in when the actuator is at the end of it's range of motion")
forceAtMid = Parameter("force at mid point", "Fm", "N", "The force created in when the actuator is at the mid point of it's range of motion")

# general
power = Parameter("power", "P", "W")
frequency = Parameter("frequency", "f", "Hz")


# --- System parameters ------------
#
maxDimension = Parameter("max dimension", "d", "m", "The longest edge of a box inscribing the device")
mass = Parameter("mass", "m", "kg")
efficiency = Parameter("efficiency", "Eta", "", "(power out)/(power in)")
heatOutput = Parameter("heat output", "H", "W", "Waste heat produced by inefficiencies in the energy conversion")
cost = Parameter("cost", "C", "$")


