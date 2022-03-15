from pytest import param
import pytest
from project import this_in_that


@pytest.mark.parametrize(
    ("this", "that"),
    (
        pytest.param("a", "abc", id="simple_match_1"),
        pytest.param("b", "abc", id="simple_match_2"),
        pytest.param("^$", "", id="blank_string"),
        pytest.param("(?=1)1", "1", id="lookahead_match"),
    ),
)
def test_project(this, that):
    assert this_in_that(this, that) is not None
