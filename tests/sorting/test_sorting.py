from src.sorting import sort_by


mocked_test = [
    {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
    {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
    {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
]


def test_sort_by_criteria():
    data = mocked_test
    sort_by(data, "min_salary")
    assert data == [
        {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
        {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
    ]

    data = mocked_test
    sort_by(data, "max_salary")
    assert data == [
        {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
        {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
    ]
    
    data = mocked_test
    sort_by(data, "date_posted")
    assert data == [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "2022-01-23"},
        {"min_salary": 800, "max_salary": 4000, "date_posted": "2022-01-20"},
        {"min_salary": 1200, "max_salary": 3500, "date_posted": "2022-01-01"},
    ]