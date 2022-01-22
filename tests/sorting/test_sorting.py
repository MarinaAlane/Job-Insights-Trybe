from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
        {'min_salary': 5, 'max_salary': 10, 'date_posted': '2015-01-01'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2016-01-01'},
        {'min_salary': 50, 'max_salary': 100, 'date_posted': '2017-01-01'},
        {'min_salary': 100, 'max_salary': 200, 'date_posted': '2018-01-01'},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'min_salary': 5, 'max_salary': 10, 'date_posted': '2015-01-01'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2016-01-01'},
        {'min_salary': 50, 'max_salary': 100, 'date_posted': '2017-01-01'},
        {'min_salary': 100, 'max_salary': 200, 'date_posted': '2018-01-01'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'min_salary': 100, 'max_salary': 200, 'date_posted': '2018-01-01'},
        {'min_salary': 50, 'max_salary': 100, 'date_posted': '2017-01-01'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2016-01-01'},
        {'min_salary': 5, 'max_salary': 10, 'date_posted': '2015-01-01'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'date_posted')
    assert jobs == [
        {'min_salary': 100, 'max_salary': 200, 'date_posted': '2018-01-01'},
        {'min_salary': 50, 'max_salary': 100, 'date_posted': '2017-01-01'},
        {'min_salary': 10, 'max_salary': 20, 'date_posted': '2016-01-01'},
        {'min_salary': 5, 'max_salary': 10, 'date_posted': '2015-01-01'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]
