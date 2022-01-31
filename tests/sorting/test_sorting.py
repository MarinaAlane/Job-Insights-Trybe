from src.sorting import sort_by

jobs_min_salary = [
    {"min_salary": "3000"},
    {"min_salary": "2000"},
    {"min_salary": "1000"},
]

jobs_max_salary = [
    {"max_salary": "3000"},
    {"max_salary": "1000"},
    {"max_salary": "2000"},
]

jobs_date_posted = [
    {"date_posted": "2022-10-15"},
    {"date_posted": "2022-12-31"},
    {"date_posted": "2022-11-21"},
]


def test_sort_by_criteria():

    sort_by(jobs_min_salary, "min_salary")
    assert jobs_min_salary == [
        {"min_salary": "1000"},
        {"min_salary": "2000"},
        {"min_salary": "3000"},
    ]

    sort_by(jobs_max_salary, "max_salary")
    assert jobs_max_salary == [
        {"max_salary": "3000"},
        {"max_salary": "2000"},
        {"max_salary": "1000"},
    ]

    sort_by(jobs_date_posted, "date_posted")
    assert jobs_date_posted == [
        {"date_posted": "2022-12-31"},
        {"date_posted": "2022-11-21"},
        {"date_posted": "2022-10-15"},
    ]
