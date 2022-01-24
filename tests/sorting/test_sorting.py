import pytest
from src.sorting import sort_by

criterias = [
    "date_posted",
    "max_salary",
    "min_salary",
]

jobs = [
    {"min_salary": '95665',
     "max_salary": '165443',
     "date_posted": '2020-05-02'},
    {"min_salary": '90665',
     "max_salary": '130000',
     "date_posted": '2020-01-01'},
    {"min_salary": '10665',
     "max_salary": '80000',
     "date_posted": '2020-10-01'},
]

jobs_min_salary = [
    {"min_salary": '10665',
     "max_salary": '80000',
     "date_posted": '2020-10-01'},
    {"min_salary": '90665',
     "max_salary": '130000',
     "date_posted": '2020-01-01'},
    {"min_salary": '95665',
     "max_salary": '165443',
     "date_posted": '2020-05-02'},
]

jobs_max_salary = [
    {"min_salary": '95665',
     "max_salary": '165443',
     "date_posted": '2020-05-02'},
    {"min_salary": '90665',
     "max_salary": '130000',
     "date_posted": '2020-01-01'},
    {"min_salary": '10665',
     "max_salary": '80000',
     "date_posted": '2020-10-01'},
]

jobs_date_posted = [
    {"min_salary": '10665',
     "max_salary": '80000',
     "date_posted": '2020-10-01'},
    {"min_salary": '95665',
     "max_salary": '165443',
     "date_posted": '2020-05-02'},
    {"min_salary": '90665',
     "max_salary": '130000',
     "date_posted": '2020-01-01'},
]


def test_sort_by_criteria():

    sort_by(jobs, "min_salary")
    assert jobs == jobs_min_salary

    sort_by(jobs, "max_salary")
    assert jobs == jobs_max_salary

    sort_by(jobs, "date_posted")
    assert jobs == jobs_date_posted

    with pytest.raises(ValueError):
        sort_by(jobs, "top_salary")
