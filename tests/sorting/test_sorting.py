import pytest
from src.sorting import sort_by


def jobs_unsorted(key, key2='date_posted'):
    return [
        {key: 3000, key2: '2015-03-12'},
        {key: 1000, key2: '2009-05-08'},
        {key: 1200, key2: '2018-08-13'},
        {key: '', key2: '2018-12-13'},
        {key: 5000, key2: '2021-01-15'},
        {key: 4000, key2: '2013-08-13'},
    ]


def jobs_asc_sorted(key, key2='date_posted'):
    return [
        {key: 1000, key2: '2009-05-08'},
        {key: 1200, key2: '2018-08-13'},
        {key: 3000, key2: '2015-03-12'},
        {key: 4000, key2: '2013-08-13'},
        {key: 5000, key2: '2021-01-15'},
        {key: '', key2: '2018-12-13'},
    ]


def jobs_desc_sorted_by_max_salary(key, key2='date_posted'):
    return [
        {key: 5000, key2: '2021-01-15'},
        {key: 4000, key2: '2013-08-13'},
        {key: 3000, key2: '2015-03-12'},
        {key: 1200, key2: '2018-08-13'},
        {key: 1000, key2: '2009-05-08'},
        {key: '', key2: '2018-12-13'},
    ]


def jobs_desc_sorted_by_date_posted(key, key2='date_posted'):
    return [
        {key: 3000, key2: '2021-01-15'},
        {key: 1000, key2: '2018-12-13'},
        {key: 1200, key2: '2018-08-13'},
        {key: '', key2: '2015-03-12'},
        {key: 5000, key2: '2013-08-13'},
        {key: 4000, key2: '2009-05-08'},
    ]


def test_sort_by_criteria():
    criterias = ['min_salary', 'max_salary', 'date_posted']

    for criteria in criterias:
        jobs = jobs_unsorted(criteria)
        sort_by(jobs, criteria)

        if criteria == 'min_salary':
            assert jobs == jobs_asc_sorted(criteria)
        elif criteria == 'max_salary':
            assert jobs == jobs_desc_sorted_by_max_salary(criteria)
        else:
            assert jobs == jobs_desc_sorted_by_date_posted(criteria)

    with pytest.raises(ValueError):
        sort_by(jobs, 'invalid')
        assert f'invalid sorting criteria: {criteria}'
