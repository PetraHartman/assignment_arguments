# Do not modify these lines
__winc_id__ = '7b9401ad7f544be2a23321292dd61cb6'
__human_name__ = 'arguments'

# Add your code after this line

""" Part 1: Greet Template

Define a function greet in main.py that takes these arguments, in this order:

- A name (str)
- A greeting template (str). Set this template parameter to 'Hello, <name>!' by
  default.
- greet should return a string where <name> in the greeting template is
  replaced by the name given in the first parameter.
  For example:

    greet('Doc')
    'Hello, Doc!'

    greet('Bob', "What's up, <name>!")
    "What's up, Bob!"
You do not need to handle the case where <name> is not in the greeting
template string. """


def greet(name, template_greet="Hello, <name>!"):
    replace_greet = template_greet.replace("<name>", name)
    return replace_greet


"""Part 2: Force

Read this up to and including "Example:
how much force to hold an apple with a mass of 0.1 kg?":

* Math Is Fun -- Gravity(opens in a new tab)
https://www.mathsisfun.com/physics/gravity.html
You should now understand the formula:

force = mass x gravity

Open up this page for reference:
https://nssdc.gsfc.nasa.gov/planetary/factsheet/
Planetary Facts Sheet(opens in a new tab)

Write a function force that takes two arguments:

- mass (float)
- body (str), with 'earth' as its default.
  Your implementation should support all 11 bodies listed on the reference
  website given above (in lowercase). Make sure you process these bodies
  with the correlated gravity factor in a dictionary.
  Before using the gravity of a celestial body round its gravity factor to 1
  decimal.
  You can "hardcode" this, for example: the gravity of Earth becomes 9.8.

The arguments should be named exactly as listed so that we can call them
with keyword arguments.
Force should return the force that is exerted given the mass and body."""

# het lijkt erop dat de website waarnaar verwezen wordt voor deze opdracht
# niet de goede waarden weergeeft
# heb waarden opgehaald van slack om het tot het goedgekeurderesultaat te
# komen


def force(mass, body="earth"):
    planets = {
        "sun": round(274, 1),
        "mercury": round(3.7, 1),
        "venus":  round(8.87, 1),
        "earth": round(9.81, 1),
        "moon": round(1.62, 1),
        "mars": round(3.711, 1),
        "jupiter": round(24.79, 1),
        "saturn": round(10.44, 1),
        "uranus": round(8.69, 1),
        "neptune": round(11.15, 1),
        "pluto": round(0.58, 1)
    }
    gravity = planets.get(body)
    force = mass * gravity
    force_rounded = round(force, 1)

    return force_rounded


"""Part 3: Gravity

Read on from "But What Is Gravity?" on the same page as previously:

Math Is Fun -- Gravity(opens in a new tab)
You should now understand the formula:

pull = G x ((m1 x m2)/d2)

Recall that in Python you can express powers with **,
for example: x5 would be x ** 5 in Python.

Write a function pull that takes three arguments:

- m1 An object's mass in kg (float)
- m2 Another object's mass in kg (float)
- d Their distance in meters (float)
pull should return the gravitional pull that these two objects
have on each other.
You can test your function by entering in the examples given on the website."""


def pull(m1, m2, d):
    g = 6.674e-11
    gravitational_pull = g * ((m1 * m2) / (d**2))
    return gravitational_pull
