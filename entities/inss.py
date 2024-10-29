from .constants import BIG_NUMBER
from .range import Range

INSS = [
    {
        "percent": float(0.0750),
        "deduction": float(0.00),
        "range": Range(floor=0, upper=float(1412.00)),
    },
    {
        "percent": float(0.09),
        "deduction": float(21.18),
        "range": Range(floor=float(1412.01), upper=float(2666.68)),
    },
    {
        "percent": float(0.12),
        "deduction": float(101.18),
        "range": Range(floor=float(2666.69), upper=float(4000.03)),
    },
    {
        "percent": float(0.14),
        "deduction": float(181.18),
        "range": Range(floor=float(4000.04), upper=float(7786.02)),
    },
    {
        "percent": float(0),
        "deduction": float(908.85),
        "range": Range(floor=float(7786.03), upper=BIG_NUMBER),
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
