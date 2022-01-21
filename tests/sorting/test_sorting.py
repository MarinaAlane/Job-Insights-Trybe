import pytest
from src.sorting import sort_by


def test_returns_typeerror_whith_unexpected_params():
    with pytest.raises(
        TypeError,
        match="takes 2 positional arguments but 3 were given",
    ):
        sort_by([], "param2", "param3")
