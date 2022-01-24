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
    {"min_salary": 300, "max_salary": 4000, "date_posted": "2022-10-01"},
    {"min_salary": 200, "max_salary": 2000, "date_posted": "2022-08-01"},
    {"min_salary": 100, "max_salary": 3000, "date_posted": "2022-04-01"},
    {"min_salary": 400, "max_salary": 1000, "date_posted": "2022-02-01"},
]


def test_sort_by_criteria():
    data_copy = mocked_data.copy()
    sort_by(data_copy, "date_posted")
    assert data_copy == data_sorted_by_date_posted

    data_copy = mocked_data.copy()
    sort_by(data_copy, "max_salary")
    assert data_copy == data_sorted_by_max_salary

    data_copy = mocked_data.copy()
    sort_by(data_copy, "min_salary")
    assert data_copy == data_sorted_by_min_salary

    with pytest.raises(ValueError, match="invalid sorting criteria"):
        sort_by(mocked_data, "invalid_param")
