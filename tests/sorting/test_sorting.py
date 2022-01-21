from src.sorting import sort_by
import pytest

JOBS_SORTED_MAX_SALARY = [
    {"max_salary": 15000, "min_salary": 0, "date_posted": "20-12-2003"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "20-12-2002"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "20-12-2004"},
    {"max_salary": 1220, "min_salary": 100, "date_posted": "20-12-2001"},
    {"max_salary": 110, "min_salary": 10, "date_posted": "20-12-2000"},
]

JOBS_SORTED_MIN_SALARY = [
    {"max_salary": 15000, "min_salary": 0, "date_posted": "20-12-2003"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "20-12-2004"},
    {"max_salary": 110, "min_salary": 10, "date_posted": "20-12-2000"},
    {"max_salary": 1220, "min_salary": 100, "date_posted": "20-12-2001"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "20-12-2002"},
]

JOBS_SORTED_DATE_POSTED = [
    {"max_salary": 110, "min_salary": 10, "date_posted": "20-12-2000"},
    {"max_salary": 1220, "min_salary": 100, "date_posted": "20-12-2001"},
    {"max_salary": 10000, "min_salary": 200, "date_posted": "20-12-2002"},
    {"max_salary": 15000, "min_salary": 0, "date_posted": "20-12-2003"},
    {"max_salary": 1500, "min_salary": 0, "date_posted": "20-12-2004"},
]


@pytest.fixture()
def jobs():
    return [
        {"max_salary": 110, "min_salary": 10, "date_posted": "20-12-2000"},
        {"max_salary": 1220, "min_salary": 100, "date_posted": "20-12-2001"},
        {"max_salary": 10000, "min_salary": 200, "date_posted": "20-12-2002"},
        {"max_salary": 15000, "min_salary": 0, "date_posted": "20-12-2003"},
        {"max_salary": 1500, "min_salary": 0, "date_posted": "20-12-2004"},
    ]


def test_sort_by_criteria(jobs):
    # sort by max salary
    sort_by(jobs, "max_salary")
    assert jobs == JOBS_SORTED_MAX_SALARY

    # sort by min salary:
    sort_by(jobs, "min_salary")
    assert jobs == JOBS_SORTED_MIN_SALARY

    # sort_by(jobs, "date_posted")
    # assert jobs == JOBS_SORTED_DATE_POSTED
    with pytest.raises(ValueError):
        sort_by(jobs, "job_title")
