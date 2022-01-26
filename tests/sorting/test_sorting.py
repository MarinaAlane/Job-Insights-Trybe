import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    with pytest.raises(
        ValueError,
        match="invalid sorting criteria: invalid_criteria"
    ):
        sort_by(jobs=[], criteria="invalid_criteria")
