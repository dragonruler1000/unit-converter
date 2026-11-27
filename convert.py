length = "length"
# Base unit for length is the meter
# Base unit for area is the square meter
# Base unit for time is the second
# Base unit for electric current is ampere
# Base unit for temperature is kelven
# Base unit for luminous intensity is candela
# Base unit for mass is kilogram
UNITS = {
    "smoot": {
        "dim": "length",
        "to_base": lambda x: x * 1.7018,
        "from_base": lambda x: x / 1.7018,
    },
    "beard second": {
        "dim": "length",
        "to_base": lambda x: x * 5e-9,
        "from_base": lambda x: x / 5e-9,
    },
    "inch": {
        "dim": "length",
        "to_base": lambda x: x / 39.3700787402,
        "from_base": lambda x: x * 39.3700787402,
    },
    "square meter": {
        "dim": "area",
        "to_base": lambda x: x * 1,
        "from_base": lambda x: x / 1,
    },
    "square kilometer": {
        "dim": "area",
        "to_base": lambda x: x * 1000,
        "from_base": lambda x: x * 0.001,
    },
    "exameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e19,
        "from_base": lambda x: x / 1e19,
    },
    "petameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e16,
        "from_base": lambda x: x / 1e16,
    },
    "terameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e13,
        "from_base": lambda x: x / 1e13,
    },
    "gigameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e10,
        "from_base": lambda x: x / 1e10,
    },
    "megameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e7,
        "from_base": lambda x: x / 1e7,
    },
    "kilometer": {
        "dim": "length",
        "to_base": lambda x: x * 1000,
        "from_base": lambda x: x / 1000,
    },
    "hectometer": {
        "dim": "length",
        "to_base": lambda x: x * 100,
        "from_base": lambda x: x / 100,
    },
    "decameter": {
        "dim": "length",
        "to_base": lambda x: x * 10,
        "from_base": lambda x: x / 10,
    },
    "meter": {
        "dim": "length",
        "to_base": lambda x: x * 1,
        "from_base": lambda x: x / 1,
    },
    "decimeter": {
        "dim": "length",
        "to_base": lambda x: x * 0.1,
        "from_base": lambda x: x / 0.1,
    },
    "centimeter": {
        "dim": "length",
        "to_base": lambda x: x * 0.01,
        "from_base": lambda x: x / 0.01,
    },
    "milimeter": {
        "dim": "length",
        "to_base": lambda x: x * 0.001,
        "from_base": lambda x: x / 0.001,
    },
    "micrometer": {
        "dim": "length",
        "to_base": lambda x: x * 1e-7,
        "from_base": lambda x: x / 1e-7
    },
    "nanometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-10,
        "from_base": lambda x: x / 1e-10
    },
    "picometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-13,
        "from_base": lambda x: x / 1e-13
    },
    "femtometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-16,
        "from_base": lambda x: x / 1e-16
    },
    "attometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-19,
        "from_base": lambda x: x* 1e-19
    },
    "zeptometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-22,
        "from_base": lambda x: x / 1e-22
    },
    "quacometer": {
        "dim": length,
        "to_base": lambda x: x * 1e-24,
        "from_base": lambda x: x / 1e-24
    },
    "mile": {
        "dim": length,
        "to_base": lambda x: x * 1609.344,
        "from_base": lambda x: x / 1609.344
    },
    "yard": {
        "dim": length,
        "to_base": lambda x: x * 0.9144,
        "from_base": lambda x: x / 0.9144
    },
    "break": {
        "dim": length,
        "to_base": lambda x: x * 1e31,
        "from_base": lambda x: x / 1e31
    },
    "lightyear": {
        "dim": length,
        "to_base": lambda x: x * 9460730472580044,
        "from_base": lambda x: x / 9460730472580044
    }
}

ERRORS = {
    frozenset({"length", "area"}): "Area can't be converted to length.",
    frozenset(
        {"length", "time"}
    ): "Length and time are different things, unless you're a beard.",
    frozenset(
        {"power", "energy"}
    ): "Power is energy per time. You can't convert them without knowing how long.",
}


def convert(x, src, dst):
    s, d = UNITS[src], UNITS[dst]
    if s["dim"] != d["dim"]:
        return ERRORS.get(frozenset({s["dim"], d["dim"]}), "These can't be converted.")
    return d["from_base"](s["to_base"](x))
