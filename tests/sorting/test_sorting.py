from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    jobs = [
        {
            "max_salary": 100000,
            "min_salary": 50000,
            "date_posted": "2020-01-01",
        },
        {
            "max_salary": 200000,
            "min_salary": 30000,
            "date_posted": "2020-01-02",
        },
        {
            "max_salary": 400000,
            "min_salary": 20000,
            "date_posted": "2020-01-03",
        },
        {
            "max_salary": 300000,
            "min_salary": 10000,
            "date_posted": "2020-01-04",
        },
    ]

    assert sort_by(jobs, "max_salary") == [
        {
            "max_salary": 400000,
            "min_salary": 20000,
            "date_posted": "2020-01-03",
        },
        {
            "max_salary": 300000,
            "min_salary": 10000,
            "date_posted": "2020-01-04",
        },
        {
            "max_salary": 200000,
            "min_salary": 30000,
            "date_posted": "2020-01-02",
        },
        {
            "max_salary": 100000,
            "min_salary": 50000,
            "date_posted": "2020-01-01",
        },
    ]

    assert sort_by(jobs, "min_salary") == [
        {
            "max_salary": 300000,
            "min_salary": 10000,
            "date_posted": "2020-01-04",
        },
        {
            "max_salary": 400000,
            "min_salary": 20000,
            "date_posted": "2020-01-03",
        },
        {
            "max_salary": 200000,
            "min_salary": 30000,
            "date_posted": "2020-01-02",
        },
        {
            "max_salary": 100000,
            "min_salary": 50000,
            "date_posted": "2020-01-01",
        },
    ]

    assert sort_by(jobs, "date_posted") == [
        {
            "max_salary": 300000,
            "min_salary": 10000,
            "date_posted": "2020-01-04",
        },
        {
            "max_salary": 200000,
            "min_salary": 30000,
            "date_posted": "2020-01-02",
        },
        {
            "max_salary": 400000,
            "min_salary": 20000,
            "date_posted": "2020-01-03",
        },
        {
            "max_salary": 100000,
            "min_salary": 50000,
            "date_posted": "2020-01-01",
        },
    ]

    invalid_criterias = ["title", "industry"]
    for criteria in invalid_criterias:
        with pytest.raises(
            ValueError, match=f"invalid sorting criteria: {criteria}"
        ):
            sort_by(jobs, invalid_criterias)
