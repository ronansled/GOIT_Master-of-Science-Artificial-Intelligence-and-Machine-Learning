from budget_opt import items, greedy_algorithm, dynamic_programming, summary


def pretty_print(selection):
    sel_list = sorted(selection.keys())
    s = ", ".join(sel_list) if sel_list else "(none)"
    return s


def test_compare(budget: int):
    greedy_sel = greedy_algorithm(items, budget)
    dp_sel = dynamic_programming(items, budget)

    greedy_sum = summary(greedy_sel, items)
    dp_sum = summary(dp_sel, items)

    print(f"\nBUDGET = {budget}")
    print("Greedy selection:", pretty_print(greedy_sel))
    print("Greedy totals:", greedy_sum)
    print("DP selection    :", pretty_print(dp_sel))
    print("DP totals       :", dp_sum)

    # Перевірки: вартість не перевищує бюджету
    assert greedy_sum["total_cost"] <= budget
    assert dp_sum["total_cost"] <= budget

    # DP має не гірший результат по калоріям (оптимальність)
    assert dp_sum["total_calories"] >= greedy_sum["total_calories"]


if __name__ == "__main__":
    # Тестові бюджети
    test_compare(60)
    test_compare(80)
    test_compare(100)
    test_compare(120)
    print("\nAll tests completed.")
