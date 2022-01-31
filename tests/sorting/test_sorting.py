from src.sorting import sort_by

criteria = ["max_salary", "min_salary", "date_posted"]

jobs = [
    {
        "sort": 1,
        "max_salary": 500,
        "min_salary": 100,
    },
    {
        "sort": 2,
        "max_salary": 400,
        "min_salary": 110,
    },
    {
        "sort": 3,
        "max_salary": 300,
        "min_salary": 120,
    },
    {
        "sort": 4,
        "max_salary": 200,
        "min_salary": 130,
    },
    {
        "sort": 4,
        "max_salaryfg": 200,
        "min_salaryfasd": 130,
    },
]


def test_sort_by_criteria():
    assert sort_by(jobs, criteria[0]) is jobs
    assert sort_by(jobs, criteria[1]) is jobs
