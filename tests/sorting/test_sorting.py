import pytest
from copy import deepcopy
from src.sorting import sort_by


DATA_JOBS = [
    {
        "title": "Full stack end developer",
        "min_salary": "1000",
        "max_salary": "2000",
        "date_posted": "2022-08-07",
    },
    {
        "title": "Back end developer",
        "min_salary": "2000",
        "max_salary": "3000",
        "date_posted": "2022-08-08",
    },
    {
        "title": "Web developer",
        "min_salary": "3000",
        "max_salary": "4000",
        "date_posted": "2022-08-09",
    },
    {
        "title": "Front end developer",
        "min_salary": "4000",
        "max_salary": "5000",
        "date_posted": "2022-08-10",
    },
]

VALID_RESPONSE_BY_CRITERIA = {
    "max_salary": [DATA_JOBS[3], DATA_JOBS[2], DATA_JOBS[1], DATA_JOBS[0]],
    "date_posted": [DATA_JOBS[3], DATA_JOBS[2], DATA_JOBS[1], DATA_JOBS[0]],
    "min_salary": [DATA_JOBS[0], DATA_JOBS[1], DATA_JOBS[2], DATA_JOBS[3]],
}


def test_sort_by_criteria():

    jobs_list = deepcopy(DATA_JOBS)
    sort_by(jobs_list, "min_salary")

    assert jobs_list == VALID_RESPONSE_BY_CRITERIA["min_salary"]

    # -------------------------------------------------------------------------
    jobs_list = deepcopy(DATA_JOBS)
    sort_by(jobs_list, "max_salary")

    assert jobs_list == VALID_RESPONSE_BY_CRITERIA["max_salary"]

    # -------------------------------------------------------------------------
    jobs_list = deepcopy(DATA_JOBS)
    sort_by(jobs_list, "date_posted")

    assert jobs_list == VALID_RESPONSE_BY_CRITERIA["date_posted"]
    # -------------------------------------------------------------------------

    jobs_list = deepcopy(DATA_JOBS)

    invalid_criteria = "testinho_maroto"
    with pytest.raises(
        ValueError, match=f"invalid sorting criteria: {invalid_criteria}"
    ):
        sort_by(jobs_list, invalid_criteria)
