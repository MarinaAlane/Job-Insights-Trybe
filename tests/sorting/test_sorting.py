from src.sorting import sort_by


# from sorting import sort_by


mocked_jobs = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
    {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
]


def test_sort_by_criteria():
    data_to_sort = mocked_jobs
    sort_by(data_to_sort, "min_salary")
    assert data_to_sort == [
        {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
        {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
    ]
