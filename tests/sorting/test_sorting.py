from src.sorting import sort_by

jobs = [
    {"min_salary": 1500, "max_salary": 4000, "date_posted": "2021-02-20"},
    {"min_salary": 3680, "max_salary": 6000, "date_posted": "2022-11-11"},
    {"min_salary": 2740, "max_salary": 4500, "date_posted": "2020-02-13"},
]


def test_sort_by_criteria():
    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 3680, "max_salary": 6000, "date_posted": "2022-11-11"},
        {"min_salary": 2740, "max_salary": 4500, "date_posted": "2020-02-13"},
        {"min_salary": 1500, "max_salary": 4000, "date_posted": "2021-02-20"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1500, "max_salary": 4000, "date_posted": "2021-02-20"},
        {"min_salary": 2740, "max_salary": 4500, "date_posted": "2020-02-13"},
        {"min_salary": 3680, "max_salary": 6000, "date_posted": "2022-11-11"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 3680, "max_salary": 6000, "date_posted": "2022-11-11"},
        {"min_salary": 1500, "max_salary": 4000, "date_posted": "2021-02-20"},
        {"min_salary": 2740, "max_salary": 4500, "date_posted": "2020-02-13"},
    ]
