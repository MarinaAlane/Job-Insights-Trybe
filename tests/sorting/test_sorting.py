import pytest
from src.sorting import sort_by

jobs_list = [
    {
     'date_posted': '2020-01-28',
     'max_salary': '100000',
     'min_salary': '10000',
    },
    {
     'max_salary': '200000',
     'date_posted': '2019-01-28',
     'min_salary': '20000',
    },
    {
     'min_salary': '30000',
     'max_salary': '300000',
     'date_posted': '2021-01-28'
    },
]

max_salary_list = [
    {
     'max_salary': '300000',
     'min_salary': '30000',
     'date_posted': '2021-01-28'
    },
    {
     'max_salary': '200000',
     'date_posted': '2019-01-28',
     'min_salary': '20000',
    },
    {
     'max_salary': '100000',
     'date_posted': '2020-01-28',
     'min_salary': '10000',
    },
]

min_salary_list = [
    {
     'min_salary': '10000',
     'max_salary': '100000',
     'date_posted': '2020-01-28',
    },
    {
     'min_salary': '20000',
     'max_salary': '200000',
     'date_posted': '2019-01-28',
    },
    {
     'min_salary': '30000',
     'max_salary': '300000',
     'date_posted': '2021-01-28'
    },
]

date_posted_list = [
    {
     'date_posted': '2021-01-28',
     'max_salary': '300000',
     'min_salary': '30000',
    },
    {
     'date_posted': '2020-01-28',
     'max_salary': '100000',
     'min_salary': '10000',
    },
    {
     'date_posted': '2019-01-28',
     'max_salary': '200000',
     'min_salary': '20000',
    },
]


def test_sort_by_criteria():
    sort_by(jobs_list, "max_salary")
    assert jobs_list == max_salary_list
    sort_by(jobs_list, "min_salary")
    assert jobs_list == min_salary_list
    sort_by(jobs_list, "date_posted")
    assert jobs_list == date_posted_list

    with pytest.raises(ValueError, match='invalid sorting criteria: criteria'):
        sort_by(jobs_list, 'criteria')
