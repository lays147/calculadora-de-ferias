from .constants import BIG_NUMBER
from .range import Range

LEAO = [
    {
        "percent": 0,
        "deduction": 0,
        "range": Range(floor=0, upper=float(2212.20)),
    },
    {
        "percent": float(0.075),
        "deduction": float(158.40),
        "range": Range(floor=float(2212.01), upper=float(2826.65)),
    },
    {
        "percent": float(0.15),
        "deduction": float(370.40),
        "range": Range(floor=float(2826.66), upper=float(3751.05)),
    },
    {
        "percent": float(0.225),
        "deduction": float(651.73),
        "range": Range(floor=float(3751.06), upper=float(4664.68)),
    },
    {
        "percent": float(0.275),
        "deduction": float(884.96),
        "range": Range(floor=float(4664.69), upper=float(BIG_NUMBER)),
    },
]


def lion_discount(salary: float, inss_discount: float) -> float:
    for f in LEAO:
        if f["range"].floor <= salary <= f["range"].upper:
            percent = f["percent"]
            deduction = f["deduction"]
            return ((salary - inss_discount) * percent) - deduction
    return float(0)
