from src.sorting import sort_by


jobs = [
    {"min_salary": 10000, "max_salary": 25000, "date_posted": "2022-01-10"},
    {"min_salary": 1100, "max_salary": 6000, "date_posted": "2022-01-15"},
    {"min_salary": 5000, "max_salary": 11000, "date_posted": "2022-01-20"},
]

mock_min_salary = [
    {"min_salary": 1100, "max_salary": 25000, "date_posted": "2022-01-20"},
    {"min_salary": 5000, "max_salary": 11000, "date_posted": "2022-01-12"},
    {"min_salary": 10000, "max_salary": 6000, "date_posted": "2022-01-10"},
]

mock_max_salary = [
    {"min_salary": 1100, "max_salary": 25000, "date_posted": "2022-01-20"},
    {"min_salary": 5000, "max_salary": 11000, "date_posted": "2022-01-12"},
    {"min_salary": 10000, "max_salary": 6000, "date_posted": "2022-01-10"},
]

mock_date_salary = [
    {"min_salary": 1100, "max_salary": 25000, "date_posted": "2022-01-20"},
    {"min_salary": 5000, "max_salary": 11000, "date_posted": "2022-01-12"},
    {"min_salary": 10000, "max_salary": 6000, "date_posted": "2022-01-10"},
]


def test_sort_by_criteria():

    assert sort_by(jobs, "min_salary") == mock_min_salary
    assert sort_by(jobs, "max_salary") == mock_max_salary
    assert sort_by(jobs, "date_posted") == mock_date_salary
