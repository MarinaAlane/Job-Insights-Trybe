from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs_test = [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "1988-09-11"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "1988-09-10"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "1988-09-09"},
    ]

    sort_by(jobs_test, "min_salary")
    assert jobs_test == [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "1988-09-11"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "1988-09-10"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "1988-09-09"},
    ]

    sort_by(jobs_test, "max_salary")
    assert jobs_test == [
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "1988-09-09"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "1988-09-10"},
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "1988-09-11"},
    ]

    sort_by(jobs_test, "date_posted")
    assert jobs_test == [
        {"min_salary": 1000, "max_salary": 3000, "date_posted": "1988-09-11"},
        {"min_salary": 2000, "max_salary": 4000, "date_posted": "1988-09-10"},
        {"min_salary": 3000, "max_salary": 5000, "date_posted": "1988-09-09"},
    ]
