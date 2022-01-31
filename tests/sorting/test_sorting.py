from src.sorting import sort_by

import pytest


# https://stackoverflow.com/questions/23337471/how-to-properly-assert-that-an-exception-gets-raised-in-pytest
# https://docs.pytest.org/en/stable/reference.html?highlight=raises#pytest.raises
# https://github.com/tryber/sd-011-project-job-insights/pull/115/commits/831b730c0e180e09804abbf9ced44d9e5d5b70ca
# https://github.com/tryber/sd-011-project-job-insights/pull/111/files

jobs = [
    {"max_salary": 6000, "min_salary": 3000, "date_posted": "2022-01-01"},
    {"max_salary": 5000, "min_salary": 2000, "date_posted": "2021-09-09"},
    {"max_salary": 4000, "min_salary": 1000, "date_posted": "2019-12-12"},
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "ulalau", "xablau")

    sort_by(jobs, "max_salary")
    assert jobs == [
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {'max_salary': 6000, 'min_salary': 3000, 'date_posted': '2022-01-01'},
        {'max_salary': 5000, 'min_salary': 2000, 'date_posted': '2021-09-09'},
        {'max_salary': 4000, 'min_salary': 1000, 'date_posted': '2019-12-12'},
    ]
