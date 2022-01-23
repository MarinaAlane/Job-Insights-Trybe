from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": ""},
        {"min_salary": 10},
        {"min_salary": 30},
        {"min_salary": 20},
        {"min_salary": 5},
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": ""},
        {"min_salary": 5},
        {"min_salary": 10},
        {"min_salary": 20},
        {"min_salary": 30},
    ]
