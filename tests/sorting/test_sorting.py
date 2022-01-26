import pytest
from src.sorting import sort_by


default_jobs = [
    {
        "title": "Front end developer",
        "type": "trainee",
        "max_salary": "6000",
        "min_salary": "3000",
        "date_posted": "April 30, 2020"
    },
    {
        "title": "Back end developer",
        "type": "full time",
        "max_salary": "8000",
        "min_salary": "5000",
        "date_posted": "October 22, 2019"
    },
    {
        "title": "Full Stack developer",
        "salary": "5000",
        "type": "full time",
        "max_salary": "10000",
        "min_salary": "7000",
        "date_posted": "03/31/2020"
    },
]


mocks = {
    "max_salary": [
        {
            'title': 'Full Stack developer',
            'salary': '5000',
            'type': 'full time',
            'max_salary': '10000',
            'min_salary': '7000', 'date_posted': '03/31/2020'
        },
        {
            'title': 'Back end developer',
            'type': 'full time',
            'max_salary': '8000',
            'min_salary': '5000',
            'date_posted': 'October 22, 2019'
        },
        {
            'title': 'Front end developer',
            'type': 'trainee',
            'max_salary': '6000',
            'min_salary': '3000',
            'date_posted': 'April 30, 2020'
        }
    ],
    "min_salary": [
        {
            'title': 'Front end developer',
            'type': 'trainee',
            'max_salary': '6000',
            'min_salary': '3000',
            'date_posted': 'April 30, 2020'
        },
        {
            'title': 'Back end developer',
            'type': 'full time',
            'max_salary': '8000',
            'min_salary': '5000',
            'date_posted': 'October 22, 2019'
        },
        {
            'title': 'Full Stack developer', 'salary': '5000',
            'type': 'full time',
            'max_salary': '10000',
            'min_salary': '7000',
            'date_posted': '03/31/2020'
        }
    ],
    "date_posted": [
        {
            'title': 'Front end developer',
            'type': 'trainee',
            'max_salary': '6000',
            'min_salary': '3000',
            'date_posted': 'April 30, 2020'
        },
        {
            'title': 'Back end developer',
            'type': 'full time',
            'max_salary': '8000',
            'min_salary': '5000',
            'date_posted': 'October 22, 2019'
        },
        {
            'title': 'Full Stack developer',
            'salary': '5000',
            'type': 'full time',
            'max_salary': '10000',
            'min_salary': '7000',
            'date_posted': '03/31/2020'
        }
    ]
}


def test_sort_by_criteria():
    sort_by(default_jobs, 'max_salary')
    assert(default_jobs) == mocks['max_salary']

    sort_by(default_jobs, 'min_salary')
    assert(default_jobs) == mocks['min_salary']

    sort_by(default_jobs, 'date_posted')
    assert(default_jobs) == mocks['date_posted']

    with pytest.raises(
        ValueError,
        match="invalid sorting criteria: invalid_criteria"
    ):
        sort_by(default_jobs, 'invalid_criteria')
