# import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    fake_list = [
        {"date_posted": "2020-13-5", "max_salary": 3000, "min_salary": 2000},
        {"date_posted": "2020-12-5", "max_salary": 2000, "min_salary": 1000},
        {"date_posted": "2020-15-5", "max_salary": 5000, "min_salary": 4000},
        {"date_posted": "2020-14-5", "max_salary": 4000, "min_salary": 3000},
    ]

    model_list_min_salary = [
        {"date_posted": "2020-12-5", "max_salary": 2000, "min_salary": 1000},
        {"date_posted": "2020-13-5", "max_salary": 3000, "min_salary": 2000},
        {"date_posted": "2020-14-5", "max_salary": 4000, "min_salary": 3000},
        {"date_posted": "2020-15-5", "max_salary": 5000, "min_salary": 4000},
    ]

    model_list_max_salary = [
        {"date_posted": "2020-15-5", "max_salary": 5000, "min_salary": 4000},
        {"date_posted": "2020-14-5", "max_salary": 4000, "min_salary": 3000},
        {"date_posted": "2020-13-5", "max_salary": 3000, "min_salary": 2000},
        {"date_posted": "2020-12-5", "max_salary": 2000, "min_salary": 1000},
    ]

    sort_by(fake_list, "min_salary")
    assert fake_list == model_list_min_salary

    sort_by(fake_list, "max_salary")
    assert fake_list == model_list_max_salary
