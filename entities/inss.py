from .constants import BIG_NUMBER
from .range import Range

INSS = [
    {
        "percent": float(0.0750),
        "deduction": float(0.00),
        "range": Range(floor=0, upper=float(1212.00)),
    },
    {
        "percent": float(0.09),
        "deduction": float(18.18),
        "range": Range(floor=float(1212.01), upper=float(2427.35)),
    },
    {
        "percent": float(0.12),
        "deduction": float(91.00),
        "range": Range(floor=float(2427.36), upper=float(3641.03)),
    },
    {
        "percent": float(0.14),
        "deduction": float(163.82),
        "range": Range(floor=float(3641.04), upper=float(7807.22)),
    },
    {
        "percent": float(0),
        "deduction": float(828.38),
        "range": Range(floor=float(7807.23), upper=BIG_NUMBER),
    },
]


def inss_discount(salary: float) -> float:
    for i in INSS:
        if i["range"].floor <= salary <= i["range"].upper:
            percent = i["percent"]
            if percent != 0:
                return (salary * i["percent"]) - i["deduction"]
            return i["deduction"]
    return float(0)
