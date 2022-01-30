import pytest
from src.sorting import sort_by


@pytest.fixture
def jobs_for_sort_by():
    return [
        {
            "id": 1,
            "industry": "agriculture",
            "date_posted": "2020-01-01",
            "min_salary": 100,
            "max_salary": 1000,
        },
        {
            "id": 2,
            "industry": "finances",
            "date_posted": "2020-02-01",
            "min_salary": 200,
            "max_salary": 2000,
        },
        {
            "id": 3,
            "industry": "solar energy",
            "date_posted": "2020-03-01",
            "min_salary": 300,
            "max_salary": 3000,
        },
        {
            "id": 4,
            "industry": "bank",
            "date_posted": "2020-04-01",
            "min_salary": 400,
            "max_salary": 40000,
        },
    ]


def test_sort_by_criteria(jobs_for_sort_by):
    with pytest.raises(ValueError):
        sort_by(jobs_for_sort_by, "anyString")

    result_min_salary = sort_by(jobs_for_sort_by, "min_salary")
    result_max_salary = sort_by(jobs_for_sort_by, "max_salary")
    result_date_posted = sort_by(jobs_for_sort_by, "date_posted")

    assert result_min_salary[0]["id"] == 4
    assert result_max_salary[0]["id"] == 4
    assert result_date_posted[1]["id"] == 3
