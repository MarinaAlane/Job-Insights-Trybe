import pytest
from mock_test import mock_t
from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    sort_by(mock_t, "max_salary")
    assert mock_t == [
        {"min_salary": 8000, "max_salary": 9000, "date_posted": "2022-04-22"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2019-12-30"},
        {"min_salary": 0, "max_salary": 2000, "date_posted": "2020-08-07"},
    ]

    sort_by(mock_t, "date_posted")
    assert mock_t == [
        {"min_salary": 3000, "max_salary": 8000, "date_posted": "2020-03-01"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2020-02-01"},
        {"min_salary": 7000, "max_salary": 8000, "date_posted": "2020-01-01"},
    ]

    sort_by(mock_t, "min_salary")
    assert mock_t == [
        {"min_salary": 1000, "max_salary": 9000, "date_posted": "2022-04-22"},
        {"min_salary": 2000, "max_salary": 8000, "date_posted": "2019-12-30"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "2020-08-07"},
    ]

    with pytest.raises(ValueError):
        sort_by(mock_t, "fail criteria")
