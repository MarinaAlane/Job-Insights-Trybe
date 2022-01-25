import pytest
from src.sorting import sort_by

# FAKE_CRITERIA = "max"
DEFAULT_JOBS = [
    {"min_salary": 1000, "max_salary": 2500, "date_posted": "2021-01-01"},
    {"min_salary": 5000, "max_salary": 6000, "date_posted": "2023-01-01"},
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2022-01-01"},
]

JOBS_DATA_BY_MIN_SALARY = [
    {"min_salary": 1000, "max_salary": 2500, "date_posted": "2021-01-01"},
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 5000, "max_salary": 6000, "date_posted": "2023-01-01"},
]

JOBS_DATA_BY_MAX_SALARY = [
    {"min_salary": 5000, "max_salary": 6000, "date_posted": "2023-01-01"},
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 1000, "max_salary": 2500, "date_posted": "2021-01-01"},
]

JOBS_DATA_BY_DATE = [
    {"min_salary": 5000, "max_salary": 6000, "date_posted": "2023-01-01"},
    {"min_salary": 1500, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 1000, "max_salary": 2500, "date_posted": "2021-01-01"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError,
                       match="takes 2 positional arguments but 3 were given"):
        sort_by([], [], [])

    # with pytest.raises(ValueError,
    #                    match=f"invalid sorting criteria: {FAKE_CRITERIA}"):
    #     sort_by(DEFAULT_JOBS, FAKE_CRITERIA)

    jobs = list(DEFAULT_JOBS)
    sort_by(jobs, "min_salary")
    assert jobs == JOBS_DATA_BY_MIN_SALARY

    jobs = list(DEFAULT_JOBS)
    sort_by(jobs, "max_salary")
    assert jobs == JOBS_DATA_BY_MAX_SALARY

    jobs = list(DEFAULT_JOBS)
    sort_by(jobs, "date_posted")
    assert jobs == JOBS_DATA_BY_DATE
