def convert_meters(meters: float, to: str = "cm") -> float:
    if to.lower() == "cm":
        return meters * 100
    elif to.lower() == "km":
        return meters / 1000


def convert_kilogram(kilogram_that_convert_to_gram: float) -> float:
    return kilogram_that_convert_to_gram * 1000


def convert_centimetre(cm: float, to: str = "m") -> float:
    if to.lower() == "m":
        return cm * 100
    elif to.lower() == "km":
        return cm / (convert_meters(cm) * 1000)


def convert_gram(gram_that_convert_to_kilogram: float) -> float:
    return gram_that_convert_to_kilogram / 1000


def convert_liter(liter_to_ml: float) -> float:
    return liter_to_ml / 1000


def convert_milliliter(milliliter_to_liter: float) -> float:
    return milliliter_to_liter * 1000


def convert_kilometre(kilometre_to_metre: float) -> float:
    return kilometre_to_metre * 1000
