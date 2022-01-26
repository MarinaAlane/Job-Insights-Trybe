from src.sorting import sort_by
import pytest


def test_sort_by_criteria():
    first_job = {
        "job_title": "Chief Marketing Officer (CMO)",
        "min_salary": 1000,
        "max_salary": 5000,
        "date_posted": "2020-05-08",
    }

    second_job = {
        "job_title": "Registered Nurse",
        "min_salary": 800,
        "max_salary": 4000,
        "date_posted": "2020-04-25",
    }

    third_job = {
        "job_title": "Dental Hygienist",
        "min_salary": 500,
        "max_salary": 2500,
        "date_posted": "2020-05-02",
    }

    jobs_list = [first_job, second_job, third_job]
    min_salary = [third_job, second_job, first_job]
    max_salary = [first_job, second_job, third_job]
    date_posted = [first_job, third_job, second_job]

    sort_by(jobs_list, "min_salary")
    assert jobs_list == min_salary

    sort_by(jobs_list, "max_salary")
    assert jobs_list == max_salary

    sort_by(jobs_list, "date_posted")
    assert jobs_list == date_posted

    with pytest.raises(
        ValueError, match="invalid sorting criteria: other_criteria"
    ):
        sort_by(jobs_list, "other_criteria")