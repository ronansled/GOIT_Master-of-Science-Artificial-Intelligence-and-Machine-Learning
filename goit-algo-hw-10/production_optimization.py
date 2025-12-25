from pulp import LpMaximize, LpProblem, LpVariable, value


def optimize_production() -> dict:
    model = LpProblem("Beverage_Production", LpMaximize)

    lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
    juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

    model += lemonade + juice

    model += 2 * lemonade + 1 * juice <= 100      # Water
    model += 1 * lemonade <= 50                    # Sugar
    model += 1 * lemonade <= 30                    # Lemon juice
    model += 2 * juice <= 40                       # Fruit puree

    model.solve()

    return {
        "Lemonade": int(value(lemonade)),
        "Fruit_Juice": int(value(juice)),
        "Total": int(value(lemonade + juice))
    }
