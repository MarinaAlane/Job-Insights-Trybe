import pytest
from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"max_salary": 10000, "min_salary": 100, 'date_posted': '2021-01-02'},
        {"max_salary": 1000, "min_salary": 200, 'date_posted': '2019-01-02'},
        {"max_salary": 200, "min_salary": 50, 'date_posted': '2019-04-02'},
    ]

    expected = [[
        {"max_salary": 200, "min_salary": 50, 'date_posted': '2019-04-02'},
        {"max_salary": 10000, "min_salary": 100, 'date_posted': '2021-01-02'},
        {"max_salary": 1000, "min_salary": 200, 'date_posted': '2019-01-02'},
    ], [
        {"max_salary": 10000, "min_salary": 100, 'date_posted': '2021-01-02'},
        {"max_salary": 1000, "min_salary": 200, 'date_posted': '2019-01-02'},
        {"max_salary": 200, "min_salary": 50, 'date_posted': '2019-04-02'},
    ], [
        {"max_salary": 10000, "min_salary": 100, 'date_posted': '2021-01-02'},
        {"max_salary": 200, "min_salary": 50, 'date_posted': '2019-04-02'},
        {"max_salary": 1000, "min_salary": 200, 'date_posted': '2019-01-02'},
    ]]

    criteria = ['min_salary', 'max_salary', 'date_posted']

    for index in range(len(criteria)):
        jobsCp = jobs.copy()
        sort_by(jobsCp, criteria[index])
        assert jobsCp == expected[index]

    with pytest.raises(ValueError):
        sort_by(jobs, 'title')
