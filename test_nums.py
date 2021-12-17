import nums

def test_program():
    assert nums.calculate_max([0, -5, 14, 4, 0]) == 14, "Not valid test [calculate_max]"
    assert nums.calculate_min([0, 0, -1, 10, -3, 6]) == -3, "Not valid test [calculate_min]"
    assert nums.calculate_sum([9, 3, 3]) == 15, "Not valid test [calculate_sum]"
    assert nums.calculate_mult([5, 3, -1, 2]) == -30, "Not valid test [calculate_mult]"
    assert nums.calculate_odds_count([7, 7, 6, 3, 10]) == 3, "Not valid test in calculate_odds_count"
    assert nums.calculate_time(nums.time_start) < 10, "Run type exceeded"
