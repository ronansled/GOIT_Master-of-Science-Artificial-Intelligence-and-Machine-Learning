import math

from dice_simulation import simulate_two_dice, analytical_probabilities


def test_simulation_close_to_analytical():
    n_rolls = 100_000
    _, sim_probs = simulate_two_dice(n_rolls)
    ana_probs = analytical_probabilities()

    # Перевіряємо, що Monte Carlo близько до аналітики
    for s in range(2, 13):
        assert math.isclose(
            sim_probs[s],
            ana_probs[s],
            rel_tol=0.15,  # допускаємо ~15% відносне відхилення
            abs_tol=0.015,  # або 1.5% абсолютне
        )
