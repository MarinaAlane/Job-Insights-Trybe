import pytest
from src.sorting import sort_by
from src.jobs import read

criterias = [
    "date_posted",
    "max_salary",
    "min_salary",
]


def test_sort_by_criteria():
    jobs_list = read("src/jobs.csv")

    with pytest.raises(ValueError):
        sort_by(jobs_list, "top_salary")
