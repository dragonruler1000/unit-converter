# the base unit for length is meters
UNITS = {
    "smoot": {
        "dim": "length",
        "to_base": lambda x: x * 1.7018,
        "from_base": lambda x: x / 1.7018,
    },
    "beard second": {
        "dim": "length",
        "to_base": lambda x: x * 5e-9,
        "from_base": lambda x: x / 5e-9
    },
}

def convert(x, src, dst):
    s, d = UNITS[src], UNITS[dst]
    if s["dim"] != d["dim"]:
        return ERRORS.get((s["dim"], d["dim"]), "These can't be converted.")
    return d["from_base"](s["to_base"](x))
