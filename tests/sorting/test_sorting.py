from src.sorting import sort_by
import pytest

mocked_data = [
    {"min_salary": 400, "max_salary": 1000, "date_posted": "2022-02-01"},
    {"min_salary": 200, "max_salary": 2000, "date_posted": "2022-08-01"},
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2022-04-01"},
    {"min_salary": 300, "max_salary": 4000, "date_posted": "2022-10-01"},
]

data_sorted_by_max_salary = [
    {"min_salary": 300, "max_salary": 4000, "date_posted": "2022-10-01"},
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2022-04-01"},
    {"min_salary": 200, "max_salary": 2000, "date_posted": "2022-08-01"},
    {"min_salary": 400, "max_salary": 1000, "date_posted": "2022-02-01"},
]

data_sorted_by_min_salary = [
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2022-04-01"},
    {"min_salary": 200, "max_salary": 2000, "date_posted": "2022-08-01"},
    {"min_salary": 300, "max_salary": 4000, "date_posted": "2022-10-01"},
    {"min_salary": 400, "max_salary": 1000, "date_posted": "2022-02-01"},
]

data_sorted_by_date_posted = [
    {"min_salary": 400, "max_salary": 1000, "date_posted": "2022-02-01"},
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2022-04-01"},
    {"min_salary": 200, "max_salary": 2000, "date_posted": "2022-08-01"},
    {"min_salary": 300, "max_salary": 4000, "date_posted": "2022-10-01"},
]


def test_sort_by_criteria():
    sorted_by_date = sort_by(mocked_data, "date_posted")
    assert sorted_by_date == data_sorted_by_date_posted

    sorted_by_max_salary = sort_by(mocked_data, "max_salary")
    assert sorted_by_max_salary == data_sorted_by_max_salary

    sorted_by_min_salary = sort_by(mocked_data, "min_salary")
    assert sorted_by_min_salary == data_sorted_by_min_salary

    with pytest.raises(ValueError, match="invalid sorting criteria"):
        sort_by(mocked_data, "invalid_param")
