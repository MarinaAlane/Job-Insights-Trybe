from src.sorting import sort_by
    
job_list = [{
      "date_posted": "2002-08-22",
      "max_salary": 3000,
      "min_salary": 5000,
    },
    {
        "date_posted": "2003-09-23",
        "max_salary": 2000,
        "min_salary": 4000,
    },
    {
        "date_posted": "2001-08-22",
        "max_salary": 1000,
        "min_salary": 2000,
    },
]

order_by_max_salary = {"max_salary": [job_list[0], job_list[1], job_list[2]]},


def test_sort_by_criteria():
    sort_by(job_list, "max_salary")
    assert job_list == order_by_max_salary[""]
    