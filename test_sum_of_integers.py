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