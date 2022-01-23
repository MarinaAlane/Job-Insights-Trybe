from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {
            'title': 'Web developer',
            'max_salary': 2500,
            'min_salary': 1200,
            'date_posted': '2018-05-10'
        },
        {
            'title': 'Back end developer',
            'max_salary': 1500,
            'min_salary': 1500,
            'date_posted': '2018-04-03'
        },
        {
            'title': 'Full stack developer',
            'max_salary': 9000,
            'min_salary': 2700,
            'date_posted': '2018-10-15'
        },
    ]
    sort_by(jobs, 'max_salary')
    assert jobs == [
        {
            'title': 'Full stack developer',
            'max_salary': 9000,
            'min_salary': 2700,
            'date_posted': '2018-10-15'
        },
        {
            'title': 'Web developer',
            'max_salary': 2500,
            'min_salary': 1200,
            'date_posted': '2018-05-10'
        },
        {
            'title': 'Back end developer',
            'max_salary': 1500,
            'min_salary': 1500,
            'date_posted': '2018-04-03'
        },
    ]
    sort_by(jobs, 'min_salary')
    assert jobs == [
        {
            'title': 'Web developer',
            'max_salary': 2500,
            'min_salary': 1200,
            'date_posted': '2018-05-10'
        },
        {
            'title': 'Back end developer',
            'max_salary': 1500,
            'min_salary': 1500,
            'date_posted': '2018-04-03'
        },
        {
            'title': 'Full stack developer',
            'max_salary': 9000,
            'min_salary': 2700,
            'date_posted': '2018-10-15'
        },
    ]
    sort_by(jobs, 'date_posted')
    assert jobs == [
        {
            'title': 'Full stack developer',
            'max_salary': 9000,
            'min_salary': 2700,
            'date_posted': '2018-10-15'
        },
        {
            'title': 'Web developer',
            'max_salary': 2500,
            'min_salary': 1200,
            'date_posted': '2018-05-10'
        },
        {
            'title': 'Back end developer',
            'max_salary': 1500,
            'min_salary': 1500,
            'date_posted': '2018-04-03'
        },
    ]
