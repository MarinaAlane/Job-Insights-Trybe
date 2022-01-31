from src.sorting import sort_by


def test_sort_by_criteria():
    pass
    jobs = [
        {
            "max_salary": 0,
            "min_salary": 10,
            "date_posted": "2020-05-16"
        },
        {
            "max_salary": 10,
            "min_salary": 20,
            "date_posted": "2020-05-17"
        },
        {
            "max_salary": -1,
            "min_salary": 30,
            "date_posted": "2020-05-18"
        },
    ]
    expected = [
        {
            "max_salary": -1,
            "min_salary": 30,
            "date_posted": "2020-05-18"
        },
        {
            "max_salary": 10,
            "min_salary": 20,
            "date_posted": "2020-05-17"
        },
        {
            "max_salary": 0,
            "min_salary": 10,
            "date_posted": "2020-05-16"
        },
    ]
    assert sort_by(jobs, "max_salary") is expected
