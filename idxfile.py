import pprint

pp = pprint.PrettyPrinter(indent=4)


def test_sort_by_criteria():
    invalid_jobs = [
        [{"min_salary": 10, "date_posted": "2019-01-01"}],
        [{"max_salary": 10, "date_posted": "2019-01-01"}],
        [{"max_salary": 10, "min_salary": 10}],
    ]
    criteria = ["max_salary", "min_salary", "date_posted"]

    jobs = [
        {"max_salary": 10000, "min_salary": 200},
        {"max_salary": 1500, "min_salary": 0},
    ]

    for i, job_list in enumerate(invalid_jobs):
        pp.pprint([criteria[i], job_list])


test_sort_by_criteria()
