from src.sorting import sort_by


def test_sort_by_criteria():
    unordened_jobs = [
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2022-02-02'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2021-12-15'},
        {'min_salary': 0, 'max_salary': 5, 'date_posted': '2020-10-20'},
        {'min_salary': 101, 'max_salary': 50000, 'date_posted': '2019-09-19'},
    ]

    ordened_job_by_min_salary = [{
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
        {'min_salary': 0, 'max_salary': 5, 'date_posted': '2020-10-20'},
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2022-02-02'},
        {'min_salary': 101, 'max_salary': 50000, 'date_posted': '2019-09-19'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2021-12-15'},
    }]
    sort_by(unordened_jobs, "min_salary")
    assert unordened_jobs == ordened_job_by_min_salary

    ordened_job_by_max_salary = [{
        {'min_salary': 101, 'max_salary': 50000, 'date_posted': '2019-09-19'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2021-12-15'},
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2022-02-02'},
        {'min_salary': 0, 'max_salary': 5, 'date_posted': '2020-10-20'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    }]
    sort_by(unordened_jobs, "max_salary")
    assert unordened_jobs == ordened_job_by_max_salary

    ordened_job_by_date_posted = [{
        {'min_salary': 100, 'max_salary': 1000, 'date_posted': '2022-02-02'},
        {'min_salary': 1000, 'max_salary': 2000, 'date_posted': '2021-12-15'},
        {'min_salary': 0, 'max_salary': 5, 'date_posted': '2020-10-20'},
        {'min_salary': 101, 'max_salary': 50000, 'date_posted': '2019-09-19'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    }]

    sort_by(unordened_jobs, "date_posted")
    assert unordened_jobs == ordened_job_by_date_posted

