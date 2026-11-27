# The base unit for length is meters
# The base unit for area is square meters
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
    "meter": {
        "dim": "length",
        "to_base": lambda x: x * 1,
        "from_base": lambda x: x / 1,
    },
    "inch": {
        "dim": "length",
        "to_base": lambda x: x / 39.3700787402,
        "from_base": lambda x: x * 39.3700787402,
    },
    "centimeter": {
        "dim": "length",
        "to_base": lambda x: x * 0.01,
        "from_base": lambda x: x * 100,
    },
    "milimeter": {
        "dim": "length",
        "to_base": lambda x: x * 0.001,
        "from_base": lambda x: x * 1000,
    },
    "kilometer": {
        "dim": "length",
        "to_base": lambda x: x * 1000,
        "from_base": lambda x: x * 0.001,
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
        "from_base": lambda x: x / 1e16
    },
    "terameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e13,
        "from_base": lambda x: x / 1e13
    },
    "gigameter": {
        "dim": "length",
        "to_base": lambda x: x * 1e10,
        "from_base": lambda x: x / 1e10
    },
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
