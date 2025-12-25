from production_optimization import optimize_production


def test_optimization() -> None:
    result = optimize_production()

    print("Optimization result:", result)

    assert result["Lemonade"] >= 0
    assert result["Fruit_Juice"] >= 0
    assert result["Total"] == result["Lemonade"] + result["Fruit_Juice"]

    water_used = 2 * result["Lemonade"] + 1 * result["Fruit_Juice"]
    sugar_used = result["Lemonade"]
    lemon_used = result["Lemonade"]
    puree_used = 2 * result["Fruit_Juice"]

    assert water_used <= 100
    assert sugar_used <= 50
    assert lemon_used <= 30
    assert puree_used <= 40

    print("ALL CONSTRAINTS SATISFIED")


if __name__ == "__main__":
    test_optimization()
