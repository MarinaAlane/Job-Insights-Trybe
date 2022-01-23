from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2019-02-02'},
        {'min_salary': 6, 'max_salary': 30, 'date_posted': '2017-03-20'},
        {'min_salary': -30, 'max_salary': 90, 'date_posted': '2014-05-05'},
        {'min_salary': 300, 'max_salary': 600, 'date_posted': '2021-01-01'},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'min_salary': -30, 'max_salary': 90, 'date_posted': '2014-05-05'},
        {'min_salary': 6, 'max_salary': 30, 'date_posted': '2017-03-20'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2019-02-02'},
        {'min_salary': 300, 'max_salary': 600, 'date_posted': '2021-01-01'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'min_salary': 300, 'max_salary': 600, 'date_posted': '2021-01-01'},
        {'min_salary': -30, 'max_salary': 90, 'date_posted': '2014-05-05'},
        {'min_salary': 6, 'max_salary': 30, 'date_posted': '2017-03-20'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2019-02-02'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'date_posted')
    assert jobs == [
        {'min_salary': 300, 'max_salary': 600, 'date_posted': '2021-01-01'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2019-02-02'},
        {'min_salary': 6, 'max_salary': 30, 'date_posted': '2017-03-20'},
        {'min_salary': -30, 'max_salary': 90, 'date_posted': '2014-05-05'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]
