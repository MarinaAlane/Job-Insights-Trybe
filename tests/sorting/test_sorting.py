from src.sorting import sort_by


jobs = [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-10'},
        {'min_salary': -10, 'max_salary': 30, 'date_posted': '2010-10-10'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
]


def test_sort_by_criteria():
    pass
    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-10'},
        {'min_salary': -10, 'max_salary': 30, 'date_posted': '2010-10-10'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-10'},
        {'min_salary': -10, 'max_salary': 30, 'date_posted': '2010-10-10'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]

    sort_by(jobs, 'date_posted')
    assert jobs == [
        {'min_salary': 6, 'max_salary': 35, 'date_posted': '2010-10-10'},
        {'min_salary': -10, 'max_salary': 30, 'date_posted': '2010-10-10'},
        {'min_salary': '', 'max_salary': '', 'date_posted': ''},
    ]
