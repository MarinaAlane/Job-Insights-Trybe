import pytest
from src.sorting import sort_by
from mock_test import mocked_jobs
from mock_response_jobs import mock_response_jobs


def test_sort_by_criteria():
    pass
    sort_by(mocked_jobs, "min_salary")
    assert mocked_jobs == mock_response_jobs.mock_response_jobs1

    sort_by(mocked_jobs, "max_salary")
    assert mocked_jobs == mock_response_jobs.mock_response_jobs2

    sort_by(mocked_jobs, "date_posted")
    assert mocked_jobs == mock_response_jobs.mock_response_jobs3

    with pytest.raises(ValueError):
        sort_by(mocked_jobs, "invalid_criteria")
