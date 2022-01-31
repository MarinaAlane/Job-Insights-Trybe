from src.sorting import sort_by


fake_jobs = [
    {
        'min_salary': 2200,
        'max_salary': 5600,
        'date_posted': '2022-01-30'
    },
    {
        'min_salary': 1800,
        'max_salary': 3500,
        'date_posted': '2022-01-31'
    },
    {
        'min_salary': 7000,
        'max_salary': 14000,
        'date_posted': '2022-02-01'
    },
]


def test_sort_by_criteria():
    sort_by(fake_jobs, 'min_salary')
    assert fake_jobs == [
        {'min_salary': 1800, 'max_salary': 3500, 'date_posted': '2022-01-31'},
        {'min_salary': 2200, 'max_salary': 5600, 'date_posted': '2022-01-30'},
        {'min_salary': 7000, 'max_salary': 14000, 'date_posted': '2022-02-01'}
    ]
    sort_by(fake_jobs, 'max_salary')
    assert fake_jobs == [
        {'min_salary': 7000, 'max_salary': 14000, 'date_posted': '2022-02-01'},
        {'min_salary': 2200, 'max_salary': 5600, 'date_posted': '2022-01-30'},
        {'min_salary': 1800, 'max_salary': 3500, 'date_posted': '2022-01-31'}
    ]
    sort_by(fake_jobs, 'date_posted')
    assert fake_jobs == [
        {'min_salary': 7000, 'max_salary': 14000, 'date_posted': '2022-02-01'},
        {'min_salary': 1800, 'max_salary': 3500, 'date_posted': '2022-01-31'},
        {'min_salary': 2200, 'max_salary': 5600, 'date_posted': '2022-01-30'}
    ]
