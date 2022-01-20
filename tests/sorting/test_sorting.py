from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {'max_salary': 10, 'min_salary': 5, 'date_posted': '2021-01-01'},
        {'max_salary': 20, 'min_salary': 1, 'date_posted': '2021-01-02'},
        {'max_salary': 30, 'min_salary': 2, 'date_posted': '2021-01-03'},
    ]
    sort_by(jobs, 'max_salary')
    assert jobs == [
        {'max_salary': 30, 'min_salary': 2, 'date_posted': '2021-01-03'},
        {'max_salary': 20, 'min_salary': 1, 'date_posted': '2021-01-02'},
        {'max_salary': 10, 'min_salary': 5, 'date_posted': '2021-01-01'},
    ]

    sort_by(jobs, 'min_salary')
    assert jobs == [
        {'max_salary': 20, 'min_salary': 1, 'date_posted': '2021-01-02'},
        {'max_salary': 30, 'min_salary': 2, 'date_posted': '2021-01-03'},
        {'max_salary': 10, 'min_salary': 5, 'date_posted': '2021-01-01'},
    ]
