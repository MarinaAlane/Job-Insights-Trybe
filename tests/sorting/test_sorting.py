import pytest
from src.sorting import sort_by


JOB_1 = {
    "min_salary": 150,
    "max_salary": 1500,
    "date_posted": "2021/02/01",
}

JOB_2 = {
    "min_salary": 250,
    "max_salary": 1000,
    "date_posted": "2021/03/01",
}

JOB_3 = {
    "min_salary": 350,
    "max_salary": 2000,
    "date_posted": "2021/01/01",
}


def test_sort_by_criteria():
    jobs = [JOB_1, JOB_2, JOB_3]

    sorted_by_min_salary = [
        JOB_1,
        JOB_2,
        JOB_3,
    ]

    sorted_by_max_salary = [
        JOB_3,
        JOB_1,
        JOB_2,
    ]

    sorted_by_date_posted = [
        JOB_2,
        JOB_1,
        JOB_3,
    ]

    assert sort_by(jobs, "min_salary") is sorted_by_min_salary
    assert sort_by(jobs, "max_salary") is sorted_by_max_salary
    assert sort_by(jobs, "date_posted") is sorted_by_date_posted
    with pytest.raises(AssertionError):
        sort_by(jobs, "ulaula")
