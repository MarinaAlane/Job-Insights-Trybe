import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    mock = [
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2022-01-02"},
        {"min_salary": 1502, "max_salary": 3002, "date_posted": "2022-01-03"},
        {"min_salary": 1501, "max_salary": 3001, "date_posted": "2022-01-01"},
    ]

    mock_min_salary = [
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2022-01-02"},
        {"min_salary": 1501, "max_salary": 3001, "date_posted": "2022-01-01"},
        {"min_salary": 1502, "max_salary": 3002, "date_posted": "2022-01-03"},
    ]

    mock_max_salary = [
        {"min_salary": 1502, "max_salary": 3002, "date_posted": "2022-01-03"},
        {"min_salary": 1501, "max_salary": 3001, "date_posted": "2022-01-01"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2022-01-02"},
    ]

    mock_date_posted = [
        {"min_salary": 1502, "max_salary": 3002, "date_posted": "2022-01-03"},
        {"min_salary": 1500, "max_salary": 3000, "date_posted": "2022-01-02"},
        {"min_salary": 1501, "max_salary": 3001, "date_posted": "2022-01-01"},
    ]

    assert sort_by(mock, "min_salary") == mock_min_salary
    assert sort_by(mock, "max_salary") == mock_max_salary
    assert sort_by(mock, "date_posted") == mock_date_posted

    with pytest.raises(
        ValueError,
            match="invalid sorting criteria: invalid criteria"):
        sort_by(mock, 'invalid')
