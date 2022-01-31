import pytest
from src.sorting import sort_by

criteria = ["max_salary", "min_salary", "date_posted", "random"]

jobs = [
    {"max_salary": 400, "min_salary": 110, "date_posted": 2},
    {"max_salary": 300, "min_salary": 120, "date_posted": 3},
    {"max_salary": 500, "min_salary": 100, "date_posted": 1},
    {"max_sal": 200, "min_sal": 130, "date_post": 5},
    {"max_salary": 200, "min_salary": 130, "date_posted": 4},
]

correctReturn = [
    {"max_salary": 500, "min_salary": 100, "date_posted": 1},
    {"max_salary": 400, "min_salary": 110, "date_posted": 2},
    {"max_salary": 300, "min_salary": 120, "date_posted": 3},
    {"max_salary": 200, "min_salary": 130, "date_posted": 4},
    {"max_sal": 200, "min_sal": 130, "date_post": 5},
]


def test_sort_by_criteria():
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {criteria[-1]}"
    ):
        sort_by(jobs, criteria[-1])
