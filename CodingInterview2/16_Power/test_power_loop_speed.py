from power import power


def power_big():
    power(8, 30)

def test_power_loop_speed(benchmark):
    benchmark(power_big)