import pytest
from src.sorting import sort_by

# reference https://docs.pytest.org/en/6.2.x/fixture.html


@pytest.fixture
def jobs():
    return [
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2022-01-20"},
        {"min_salary": 1500, "max_salary": 2000, "date_posted": "2022-01-21"},
        {"min_salary": 2500, "max_salary": 3000, "date_posted": "2022-01-22"},
        {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-23"},
    ]


ordered_by_min = [
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2022-01-20"},
    {"min_salary": 1500, "max_salary": 2000, "date_posted": "2022-01-21"},
    {"min_salary": 2500, "max_salary": 3000, "date_posted": "2022-01-22"},
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-23"},
]

ordered_by_max = [
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-23"},
    {"min_salary": 2500, "max_salary": 3000, "date_posted": "2022-01-22"},
    {"min_salary": 1500, "max_salary": 2000, "date_posted": "2022-01-21"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2022-01-20"},
]

ordered_by_date = [
    {"min_salary": 3500, "max_salary": 5000, "date_posted": "2022-01-23"},
    {"min_salary": 2500, "max_salary": 3000, "date_posted": "2022-01-22"},
    {"min_salary": 1500, "max_salary": 2000, "date_posted": "2022-01-21"},
    {"min_salary": 500, "max_salary": 1000, "date_posted": "2022-01-20"},
]


def has_salary_data(job):
    if "min_salary" in job and "max_salary" in job:
        return True
    return False


def has_correct_salary_type(job):
    if isinstance(job["min_salary"], int) and isinstance(
        job["max_salary"], int
    ):
        return True
    return False


def min_less_than_max(job):
    if job["min_salary"] > job["max_salary"]:
        return False
    return True


def salary_between_range(job, salary):

    if not isinstance(salary, int):
        return False

    min, max = job["min_salary"], job["max_salary"]

    return (
        has_salary_data(job)
        and has_correct_salary_type(job)
        and min <= salary <= max
    )


def test_sort_by_criteria(jobs):
    sort_by(jobs, "max_salary")
    assert jobs == ordered_by_max

    sort_by(jobs, "min_salary")
    assert jobs == ordered_by_min

    sort_by(jobs, "date_posted")
    assert jobs == ordered_by_date

    with pytest.raises(ValueError, match="invalid sorting criteria: job_type"):
        jobs_copy = jobs.copy()
        sort_by(jobs_copy, "job_type")

    invalid_criteria = ""

    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
    ):
        jobs_copy = jobs.copy()
        sort_by(jobs_copy, invalid_criteria)
