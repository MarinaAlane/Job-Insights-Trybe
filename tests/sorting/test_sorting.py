from src.sorting import sort_by


def test_sort_by_criteria():
    pass


job_test = [
     {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
     {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
     {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]


sort_by(job_test, "min_salary")
assert job_test == [
     {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
     {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
     {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]


sort_by(job_test, "max_salary")
assert job_test == [
     {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
     {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
     {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
]


sort_by(job_test, "date_posted")
assert job_test == [
     {"min_salary": 100, "max_salary": 300, "date_posted": "2021-05-03"},
     {"min_salary": 200, "max_salary": 400, "date_posted": "2021-05-02"},
     {"min_salary": 300, "max_salary": 500, "date_posted": "2021-05-01"},
]
