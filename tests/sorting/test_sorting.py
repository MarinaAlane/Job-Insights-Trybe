import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    """
    Test sort_by() with various criteria.
    """
    jobs = [
        {
            "max_salary": "10000",
            "min_salary": "5000",
            "date_posted": "2019-01-01"
        },
        {
            "max_salary": "9600",
            "min_salary": "4000",
            "date_posted": "2019-01-02"
        },
        {
            "max_salary": "7890",
            "min_salary": "2000",
            "date_posted": "2019-01-03"
        },
    ]

    # invalid criteria
    with pytest.raises(ValueError):
        sort_by(jobs, "invalid")
