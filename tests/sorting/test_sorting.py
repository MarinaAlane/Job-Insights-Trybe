from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2021-01-09"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-09"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-09"},
    ]
    sort_by(jobs, "min_salary")

    assert jobs == [
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2021-01-09"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-09"},
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-09"},
    ]
    sort_by(jobs, "max_salary")

    assert jobs == [
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-09"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-09"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2021-01-09"},
    ]
    sort_by(jobs, "date_posted")

    assert jobs == [
        {"min_salary": 2000, "max_salary": 3000, "date_posted": "2021-01-09"},
        {"min_salary": 1000, "max_salary": 2000, "date_posted": "2021-01-09"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2021-01-09"},
    ]
