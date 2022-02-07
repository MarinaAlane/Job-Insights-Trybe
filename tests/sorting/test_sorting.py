from src.sorting import sort_by

jobs = [
    {
        "min_salary": 900,
        "max_salary": 4800,
        "date_posted": "2022-03-12"
    },
    {
        "min_salary": 1000,
        "max_salary": 5000,
        "date_posted": "2022-03-13"
    },
    {
        "min_salary": 1100,
        "max_salary": 5200,
        "date_posted": "2022-03-14"
    }
]

mock = {
    "min_salary": [
        {
            "min_salary": 900,
            "max_salary": 4800,
            "date_posted": "2022-03-12"
        },
        {
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-03-13"
        },
        {
            "min_salary": 1100,
            "max_salary": 5200,
            "date_posted": "2022-03-14"
        },
        ],
    "max_salary": [
        {
            "min_salary": 1100,
            "max_salary": 5200,
            "date_posted": "2022-03-14"
        },
        {
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-03-13"
        },
        {
            "min_salary": 900,
            "max_salary": 4800,
            "date_posted": "2022-03-12"
        },
        ],
    "date_posted": [
       {
            "min_salary": 1100,
            "max_salary": 5200,
            "date_posted": "2022-03-14"
        },
        {
            "min_salary": 1000,
            "max_salary": 5000,
            "date_posted": "2022-03-13"
        },
        {
            "min_salary": 900,
            "max_salary": 4800,
            "date_posted": "2022-03-12"
        },
        ],
}


def test_sort_by_criteria():

    sort_by(jobs, "min_salary")
    assert jobs == mock["min_salary"]

    sort_by(jobs, "max_salary")
    assert jobs == mock["max_salary"]

    sort_by(jobs, "date_posted")
    assert jobs == mock["date_posted"]
