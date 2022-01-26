import pytest
from src.sorting import sort_by


jobs = [
    {
        'date_posted': '2020-03-01',
        'min_salary': 1100,
        'max_salary': 2000,
    },
    {
        'date_posted': '2020-05-15',
        'min_salary': 2500,
        'max_salary': 5000,
    },
    {
        'date_posted': '2021-12-23',
        'min_salary': 1500,
        'max_salary': 2150,
    },
    {
        'date_posted': '2022-01-18',
        'min_salary': 5000,
        'max_salary': 15000,
    },
]

jobs_ordered = {
    'min_salary': [
        jobs[0],
        jobs[2],
        jobs[1],
        jobs[3],
    ],
    'max_salary': [
        jobs[3],
        jobs[1],
        jobs[2],
        jobs[0],
    ],
    'date_posted': [
        jobs[3],
        jobs[2],
        jobs[1],
        jobs[0],
    ],
}


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs)

    criterias = ['min_salary', 'max_salary', 'date_posted']

    for criteria in criterias:
        sort_by(jobs, criteria)
        assert jobs == jobs_ordered[criteria]
