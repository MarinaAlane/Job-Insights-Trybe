from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {"min_salary": 2500, "max_salary": 3000, "date_posted": "1992-04-29"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "1992-04-28"},
        {"min_salary": 4000, "max_salary": 5000, "date_posted": "1992-04-27"},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 2500, "max_salary": 3000, "date_posted": "1992-04-29"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "1992-04-28"},
        {"min_salary": 4000, "max_salary": 5000, "date_posted": "1992-04-27"},
    ]

    sort_by(jobs, "max_salary")
    assert jobs == [
        {"min_salary": 4000, "max_salary": 5000, "date_posted": "1992-04-27"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "1992-04-28"},
        {"min_salary": 2500, "max_salary": 3000, "date_posted": "1992-04-29"},
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {"min_salary": 2500, "max_salary": 3000, "date_posted": "1992-04-29"},
        {"min_salary": 3000, "max_salary": 4000, "date_posted": "1992-04-28"},
        {"min_salary": 4000, "max_salary": 5000, "date_posted": "1992-04-27"},
    ]
