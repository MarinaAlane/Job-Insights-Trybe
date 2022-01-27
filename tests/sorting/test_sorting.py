from src.sorting import sort_by
from pytest import raises, fixture
import src.jobs as jobs


@fixture
def jobs__unsorted():
    return jobs.read('tests/sorting/fixtures/jobs__unsorted.csv')


@fixture
def jobs__sorted_by_max_salary():
    return jobs.read('tests/sorting/fixtures/jobs__sorted_by_max_salary.csv')


@fixture
def jobs__sorted_by_min_salary():
    return jobs.read('tests/sorting/fixtures/jobs__sorted_by_min_salary.csv')


@fixture
def jobs__sorted_by_date_posted():
    return jobs.read('tests/sorting/fixtures/jobs__sorted_by_date_posted.csv')


def test_sort_by_criteria(jobs__unsorted,
                          jobs__sorted_by_max_salary,
                          jobs__sorted_by_min_salary,
                          jobs__sorted_by_date_posted):
    invalid_criterias = ['job_type', 'industry', 'company', 'state', 'city',
                         'job_desc', 'rating', 'valid_until', 'id']

    for criteria in invalid_criterias:
        with raises(ValueError,
                    match=f'invalid sorting criteria: {criteria}'):
            sort_by(jobs__unsorted, criteria)

    assert(sort_by(jobs__unsorted, 'max_salary')) == jobs__sorted_by_max_salary
    assert(sort_by(jobs__unsorted, 'min_salary')) == jobs__sorted_by_min_salary
    assert(sort_by(jobs__unsorted, 'date_posted')) \
        == jobs__sorted_by_date_posted
    pass
