from copy import copy
from src.sorting import sort_by
import pytest


@pytest.fixture
def mocked_jobs():
    return [
        {
            "date_posted": "2020-05-08",
            "max_salary": "80000",
            "min_salary": "40000",
        },
        {
            "date_posted": "2021-05-08",
            "max_salary": "90000",
            "min_salary": "50000",
        },
        {
            "date_posted": "2019-05-08",
            "max_salary": "70000",
            "min_salary": "30000",
        },
        {
            "date_posted": "2017-05-08",
            "max_salary": "50000",
            "min_salary": "10000",
        },
        {
            "date_posted": "2018-05-08",
            "max_salary": "60000",
            "min_salary": "20000",
        },
        {},
    ]


mocked_max_salary = [
    {
        "date_posted": "2021-05-08",
        "max_salary": "90000",
        "min_salary": "50000",
    },
    {
        "date_posted": "2020-05-08",
        "max_salary": "80000",
        "min_salary": "40000",
    },
    {
        "date_posted": "2019-05-08",
        "max_salary": "70000",
        "min_salary": "30000",
    },
    {
        "date_posted": "2018-05-08",
        "max_salary": "60000",
        "min_salary": "20000",
    },
    {
        "date_posted": "2017-05-08",
        "max_salary": "50000",
        "min_salary": "10000",
    },
    {},
]

mocked_min_salary = [
    {
        "date_posted": "2017-05-08",
        "max_salary": "50000",
        "min_salary": "10000",
    },
    {
        "date_posted": "2018-05-08",
        "max_salary": "60000",
        "min_salary": "20000",
    },
    {
        "date_posted": "2019-05-08",
        "max_salary": "70000",
        "min_salary": "30000",
    },
    {
        "date_posted": "2020-05-08",
        "max_salary": "80000",
        "min_salary": "40000",
    },
    {
        "date_posted": "2021-05-08",
        "max_salary": "90000",
        "min_salary": "50000",
    },
    {},
]

mocked_date_posted = [
    {
        "date_posted": "2021-05-08",
        "max_salary": "90000",
        "min_salary": "50000",
    },
    {
        "date_posted": "2020-05-08",
        "max_salary": "80000",
        "min_salary": "40000",
    },
    {
        "date_posted": "2019-05-08",
        "max_salary": "70000",
        "min_salary": "30000",
    },
    {
        "date_posted": "2018-05-08",
        "max_salary": "60000",
        "min_salary": "20000",
    },
    {
        "date_posted": "2017-05-08",
        "max_salary": "50000",
        "min_salary": "10000",
    },
    {},
]


def test_sort_by_criteria(mocked_jobs):
    copied_mock = copy(mocked_jobs)
    sort_by(copied_mock, "max_salary")
    assert (copied_mock) == mocked_max_salary

    copied_mock = copy(mocked_jobs)
    sort_by(copied_mock, "date_posted")
    assert (copied_mock) == mocked_date_posted

    copied_mock = copy(mocked_jobs)
    sort_by(copied_mock, "min_salary")
    assert (copied_mock) == mocked_min_salary

    with pytest.raises(ValueError, match="invalid sorting criteria: invalid"):
        copied_mock = copy(mocked_jobs)
        sort_by(copied_mock, "invalid")
