import pytest
from src.sorting import sort_by

jobs = [
    {
        "max_salary": "6000",
        "min_salary": "4500",
        "date_posted": "04/10/2022"
    },
    {
        "max_salary": "8000",
        "min_salary": "6500",
        "date_posted": "02/07/2021"
    },
    {
        "max_salary": "10000",
        "min_salary": "8500",
        "date_posted": "05/11/2022"
    },
]


mocks = {
    "max_salary": [
        {
            'max_salary': '10000',
            'min_salary': '8500',
            'date_posted': '05/11/2022'
        },
        {
            'max_salary': '8000',
            'min_salary': '6500',
            'date_posted': '02/07/2021'
        },
        {
            'max_salary': '6000',
            'min_salary': '4500',
            'date_posted': '04/10/2022'
        }
    ],
    "min_salary": [
        {
            'max_salary': '6000',
            'min_salary': '4500',
            'date_posted': '04/10/2022'
        },
        {
            'max_salary': '8000',
            'min_salary': '6500',
            'date_posted': '02/07/2021'
        },
        {
            'max_salary': '10000',
            'min_salary': '8500',
            'date_posted': '05/11/2022'
        }
    ],
    "date_posted": [
        {
            'max_salary': '6000',
            'min_salary': '4500',
            'date_posted': '04/10/2022'
        },
        {
            'max_salary': '8000',
            'min_salary': '6500',
            'date_posted': '02/07/2021'
        },
        {
            'max_salary': '10000',
            'min_salary': '8500',
            'date_posted': '05/11/2022'
        }
    ]
}


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert (jobs) == mocks["max_salary"]

    sort_by(jobs, "min_salary")
    assert (jobs) == mocks["min_salary"]

    sort_by(jobs, "date_posted")
    assert (jobs) == mocks["date_posted"]

    with pytest.raises(
        ValueError, match="invalid_criteria"
    ):
        sort_by(jobs, "invalid_criteria")
