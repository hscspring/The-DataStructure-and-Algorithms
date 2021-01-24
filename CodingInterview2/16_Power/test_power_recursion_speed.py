from power import power_recursion


def power_recursion_big():
    power_recursion(8, 30)

def test_power_recursion_speed(benchmark):
    benchmark(power_recursion_big)