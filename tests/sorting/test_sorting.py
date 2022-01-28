from src.sorting import sort_by
import pytest


@pytest.fixture
def jobs():

    return [
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2022-02-20"},
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-01-27"},
        {"min_salary": 3500, "max_salary": 8500, "date_posted": "2022-01-23"},
    ]


def test_sort_by_criteria(jobs):

    by_min_salary = [
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-01-27"},
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2022-02-20"},
        {"min_salary": 3500, "max_salary": 8500, "date_posted": "2022-01-23"},
    ]

    jobs_copy_min = jobs.copy()

    sort_by(jobs_copy_min, "min_salary")

    # "Ordenando pelo minimo"

    assert jobs_copy_min == by_min_salary

    by_max_salary = [
        {"min_salary": 3500, "max_salary": 8500, "date_posted": "2022-01-23"},
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-01-27"},
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2022-02-20"},
    ]

    jobs_copy_max = jobs.copy()

    sort_by(jobs_copy_max, "max_salary")

    # "Ordenando pelo maximo"

    assert jobs_copy_max == by_max_salary

    by_date_posted = [
        {"min_salary": 2500, "max_salary": 5500, "date_posted": "2022-02-20"},
        {"min_salary": 2000, "max_salary": 6000, "date_posted": "2022-01-27"},
        {"min_salary": 3500, "max_salary": 8500, "date_posted": "2022-01-23"},
    ]

    jobs_copy_date = jobs.copy()

    sort_by(jobs_copy_date, "date_posted")

    "Ordenamento pela data"

    assert jobs_copy_date == by_date_posted

    error = "invalid_criteria"

    with pytest.raises(ValueError, match=f"invalid sorting criteria: {error}"):

        jobs_copy = jobs.copy()

        sort_by(jobs_copy, error)
