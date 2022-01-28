import pytest
from src.sorting import sort_by

mockingbird = [
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-03-28"},
    {"min_salary": 4000, "max_salary": 9000, "date_posted": "2022-01-28"},
    {"min_salary": 6000, "max_salary": 5000, "date_posted": "2022-02-28"},
]

min_salary_mock = [
    {"min_salary": 4000, "max_salary": 9000, "date_posted": "2022-01-28"},
    {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-03-28"},
    {"min_salary": 6000, "max_salary": 5000, "date_posted": "2022-02-28"},
]

max_salary_mock = [
      {"min_salary": 4000, "max_salary": 9000, "date_posted": "2022-01-28"},
      {"min_salary": 6000, "max_salary": 8000, "date_posted": "2022-02-28"},
      {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-03-28"},
]

date_posted_mock = [
      {"min_salary": 5000, "max_salary": 7000, "date_posted": "2022-03-28"},
      {"min_salary": 6000, "max_salary": 8000, "date_posted": "2022-02-28"},
      {"min_salary": 4000, "max_salary": 9000, "date_posted": "2022-01-28"},
]


def test_sort_by():
    pass
    sort_by(mockingbird, "min_salary")
    assert mockingbird == min_salary_mock

    with pytest.raises(ValueError):
        sort_by(mockingbird, "invalid")
