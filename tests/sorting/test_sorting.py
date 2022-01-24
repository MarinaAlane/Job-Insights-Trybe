import pytest
from src.sorting import sort_by

mocked_data = [
    {"date_posted": "2022-01-01", "max_salary": 1, "min_salary": 10},
    {"date_posted": "2022-02-11", "max_salary": 10, "min_salary": 100},
    {"date_posted": "2022-01-15", "max_salary": 10000, "min_salary": 200},
    {"date_posted": "2022-02-01", "max_salary": 15000, "min_salary": 1},
    {"date_posted": "2022-05-01", "max_salary": 1500, "min_salary": 1},
]


def test_sort_by_criteria():
    order_criterias = ["date_posted", "max_salary", "min_salary"]
    by_min = [
        {"date_posted": "2022-02-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2022-05-01", "max_salary": 1500, "min_salary": 1},
        {"date_posted": "2022-01-01", "max_salary": 1, "min_salary": 10},
        {"date_posted": "2022-02-11", "max_salary": 10, "min_salary": 100},
        {"date_posted": "2022-01-15", "max_salary": 10000, "min_salary": 200},
    ]
    by_max = [
        {"date_posted": "2022-02-01", "max_salary": 15000, "min_salary": 1},
        {"date_posted": "2022-01-15", "max_salary": 10000, "min_salary": 200},
        {"date_posted": "2022-05-01", "max_salary": 1500, "min_salary": 1},
        {"date_posted": "2022-02-11", "max_salary": 10, "min_salary": 100},
        {"date_posted": "2022-01-01", "max_salary": 1, "min_salary": 10},
    ]

    with pytest.raises(TypeError):
        sort_by(mocked_data, "test_01", "test_02")

    test_by_max = mocked_data.copy()
    sort_by(test_by_max, order_criterias[1])
    assert test_by_max == by_max

    test_by_min = mocked_data.copy()
    sort_by(test_by_min, order_criterias[2])
    assert test_by_min == by_min
