from dice_simulation import simulate_two_dice, analytical_probabilities


def format_probability_table(simulated, analytical) -> str:
    headers = "| Сума | Monte Carlo, % | Аналітична, % | Різниця (абс.), % |\n"
    sep = "|-----|----------------|---------------|--------------------|\n"
    rows = []

    for s in range(2, 13):
        sim_p = simulated.get(s, 0.0) * 100
        ana_p = analytical.get(s, 0.0) * 100
        diff = abs(sim_p - ana_p)
        rows.append(
            f"| {s:>3} | {sim_p:>14.3f} | {ana_p:>13.3f} | {diff:>18.3f} |"
        )

    return headers + sep + "\n".join(rows)


def main() -> None:
    n_rolls = 200_000  # можна змінити при потребі

    counts, simulated_probs = simulate_two_dice(n_rolls)
    analytical_probs = analytical_probabilities()

    print(f"Кількість кидків: {n_rolls}")
    print("Абсолютні частоти сум:")
    for s in range(2, 13):
        print(f"Сума {s:>2}: {counts.get(s, 0)}")

    print("\nТаблиця ймовірностей (Monte Carlo vs аналітика):\n")
    table_md = format_probability_table(simulated_probs, analytical_probs)
    print(table_md)

    # Короткий текстовий висновок
    avg_abs_diff = sum(
        abs(simulated_probs[s] - analytical_probs[s]) for s in range(2, 13)
    ) / 11
    print(
        f"\nСереднє абсолютне відхилення між Monte Carlo "
        f"та аналітичними ймовірностями: {avg_abs_diff * 100:.3f}%"
    )


if __name__ == "__main__":
    main()



