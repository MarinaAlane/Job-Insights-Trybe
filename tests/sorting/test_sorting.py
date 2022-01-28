from src.sorting import sort_by
import pytest


job_list = [{
      "date_posted": "2002-08-22",
      "max_salary": 3000,
      "min_salary": 5000,
    },
    {
        "date_posted": "2003-09-23",
        "max_salary": 2000,
        "min_salary": 4000,
    },
    {
        "date_posted": "2005-08-22",
        "max_salary": 1000,
        "min_salary": 2000,
    },
]

order_by_max_salary = [{
      "date_posted": "2002-08-22",
      "max_salary": 3000,
      "min_salary": 5000,
    },
    {
        "date_posted": "2003-09-23",
        "max_salary": 2000,
        "min_salary": 4000,
    },
    {
        "date_posted": "2005-08-22",
        "max_salary": 1000,
        "min_salary": 2000,
    },
]

order_by_min_salary = [{
        "date_posted": "2005-08-22",
        "max_salary": 1000,
        "min_salary": 2000,
    },
    {
        "date_posted": "2003-09-23",
        "max_salary": 2000,
        "min_salary": 4000,
    },
    {
      "date_posted": "2002-08-22",
      "max_salary": 3000,
      "min_salary": 5000,
    },
]

order_by_date_posted = [{
        "date_posted": "2005-08-22",
        "max_salary": 1000,
        "min_salary": 2000,
    },
    {
        "date_posted": "2003-09-23",
        "max_salary": 2000,
        "min_salary": 4000,
    },
    {
      "date_posted": "2002-08-22",
      "max_salary": 3000,
      "min_salary": 5000,
    },
]


def test_sort_by_criteria():

    sort_by(job_list, "max_salary")
    assert job_list == order_by_max_salary

    sort_by(job_list, "min_salary")
    assert job_list == order_by_min_salary

    sort_by(job_list, "date_posted")
    assert job_list == order_by_date_posted

    with pytest.raises(ValueError, match="invalid sorting criteria: 1234"):
        sort_by(job_list, "1234")
