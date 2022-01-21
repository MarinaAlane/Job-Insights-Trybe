import pytest
from src.sorting import sort_by

jobs_mock_base = [
    {"min_salary": 1, "max_salary": 3, "date_posted": "2021-01-01"},
    {"min_salary": 3, "max_salary": 5, "date_posted": "2022-01-01"},
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-01-01"},
]

jobs_sorted_by_max_salary = [
    {"min_salary": 3, "max_salary": 5, "date_posted": "2022-01-01"},
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-01-01"},
    {"min_salary": 1, "max_salary": 3, "date_posted": "2021-01-01"},
]

jobs_sorted_by_min_salary = [
    {"min_salary": 1, "max_salary": 3, "date_posted": "2021-01-01"},
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-01-01"},
    {"min_salary": 3, "max_salary": 5, "date_posted": "2022-01-01"},
]

jobs_sorted_by_date_posted = [
    {"min_salary": 3, "max_salary": 5, "date_posted": "2022-01-01"},
    {"min_salary": 1, "max_salary": 3, "date_posted": "2021-01-01"},
    {"min_salary": 2, "max_salary": 4, "date_posted": "2020-01-01"},
]


def test_sort_by_criteria():
    with pytest.raises(
        TypeError,
        match="takes 2 positional arguments but 3 were given",
    ):
        sort_by([], "param2", "param3")

    data_to_assert = jobs_mock_base.copy()
    sort_by(data_to_assert, "max_salary")
    assert data_to_assert == jobs_sorted_by_max_salary

    data_to_assert = jobs_mock_base.copy()
    sort_by(data_to_assert, "min_salary")
    assert data_to_assert == jobs_sorted_by_min_salary

    data_to_assert = jobs_mock_base.copy()
    sort_by(data_to_assert, "date_posted")
    assert data_to_assert == jobs_sorted_by_date_posted
