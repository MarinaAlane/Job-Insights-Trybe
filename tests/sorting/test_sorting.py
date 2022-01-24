import pytest
from src.sorting import sort_by
from tests.sorting.sort_files import jobs, ordenated_jobs


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs)

    with pytest.raises(TypeError):
        sort_by('max_salary')

    criterias = ['min_salary', 'max_salary', 'date_posted']

    for criteria in criterias:
        sort_by(jobs, criteria)
        assert jobs == ordenated_jobs[criteria]
