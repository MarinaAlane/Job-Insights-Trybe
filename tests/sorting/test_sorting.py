from src.sorting import sort_by

jobs = [
    {"min_salary": 100, "max_salary": 300, "date_posted": "2022-02-05"},
    {"min_salary": 400, "max_salary": 600, "date_posted": "2022-01-05"},
    {"min_salary": 700, "max_salary": 900, "date_posted": "2022-02-01"},
]


def test_sort_by_criteria():

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 100, "max_salary": 300, "date_posted": "2022-02-05"},
        {"min_salary": 400, "max_salary": 600, "date_posted": "2022-01-05"},
        {"min_salary": 700, "max_salary": 900, "date_posted": "2022-02-01"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 700, "max_salary": 900, "date_posted": "2022-02-01"},
        {"min_salary": 400, "max_salary": 600, "date_posted": "2022-01-05"},
        {"min_salary": 100, "max_salary": 300, "date_posted": "2022-02-05"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 100, "max_salary": 300, "date_posted": "2022-02-05"},
        {"min_salary": 700, "max_salary": 900, "date_posted": "2022-02-01"},
        {"min_salary": 400, "max_salary": 600, "date_posted": "2022-01-05"},
    ]
