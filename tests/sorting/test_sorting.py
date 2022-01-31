import pytest
from src.sorting import sort_by

data_jobs_fake = [
    {
        "title": "Front end developer",
        "min_salary": 1000,
        "max_salary": 4000,
        "date_posted": "2022-01-23"
    },
    {
        "title": "Back end developer",
        "min_salary": 3000,
        "max_salary": 6000,
        "date_posted": "2022-01-25"
    },
    {
        "title": "Full stack end developer",
        "min_salary": 4000,
        "max_salary": 8000,
        "date_posted": "2022-01-21"
    }
]

jobs_by_min_salary = [
        data_jobs_fake[0],
        data_jobs_fake[1],
        data_jobs_fake[2]
    ]

jobs_by_max_salary = [
        data_jobs_fake[2],
        data_jobs_fake[1],
        data_jobs_fake[0]
    ]

jobs_by_date_posted = [
        data_jobs_fake[1],
        data_jobs_fake[0],
        data_jobs_fake[2]
    ]


def test_sort_by_criteria():
    sort_by(data_jobs_fake, "min_salary")
    assert data_jobs_fake == jobs_by_min_salary

    sort_by(data_jobs_fake, "max_salary")
    assert data_jobs_fake == jobs_by_max_salary

    sort_by(data_jobs_fake, "date_posted")
    assert data_jobs_fake == jobs_by_date_posted

    with pytest.raises(ValueError):
        sort_by(data_jobs_fake, "invalid")
