import pytest
from sum import sum_of_integers

def test_sum_of_integers_with_invalid_type_throws_exception():
    with pytest.raises(TypeError) as exc_info:
        sum_of_integers("foo", 10)

    e = exc_info.value
    assert str(e.args[0]) == '"foo" is not an integer'

    with pytest.raises(TypeError) as exc_info:
        sum_of_integers(10, 'bar')

    e = exc_info.value
    assert str(e.args[0]) == '"bar" is not an integer'

@pytest.mark.parametrize("a, b, expected", [
    (0, 0, 0),              # both zero
    (-1, -1, -2),           # both negative
    (1, -1, 0),             # positive and negative that cancel
    (-100, 200, 100),       # negative + positive
    (999999999, 1, 1000000000),  # large number
    (-999999999, -1, -1000000000),  # large negative
    (int(1e9), int(1e9), int(2e9)), # very large positive values
])
def test_sum_of_integers_with_valid_values_returns_sum(a, b, expected):
    assert sum_of_integers(a, b) == expected