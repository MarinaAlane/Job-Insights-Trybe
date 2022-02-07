from src.sorting import sort_by

jobs = [
    {
        "min_salary": "900",
        "max_salary": "4800",
        "date_posted": "2022-03-12"
    },
    {
        "min_salary": "1000",
        "max_salary": "5000",
        "date_posted": "2022-03-13"
    },
    {
        "min_salary": "1100",
        "max_salary": "5200",
        "date_posted": "2022-03-14"
    }
]


def test_sort_by_criteria():
    pass
    job_list_min_salary_mock = [
        {
            "min_salary": "900",
            "max_salary": "4800",
            "date_posted": "2022-03-12"
        },
        {
            "min_salary": "1000",
            "max_salary": "5000",
            "date_posted": "2022-03-13"
        },
        {
            "min_salary": "1100",
            "max_salary": "5200",
            "date_posted": "2022-03-14"
        }
    ]

    job_list_date_posted_mock = [
        {
            "min_salary": "900",
            "max_salary": "4800",
            "date_posted": "2022-03-12"
        },
        {
            "min_salary": "1000",
            "max_salary": "5000",
            "date_posted": "2022-03-13"
        },
        {
            "min_salary": "1100",
            "max_salary": "5200",
            "date_posted": "2022-03-14"
        }
    ]

    sort_by(jobs, "min_salary")
    assert jobs == job_list_min_salary_mock

    sort_by(jobs, "date_posted")
    assert jobs == job_list_date_posted_mock
