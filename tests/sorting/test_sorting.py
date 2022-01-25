from src.sorting import sort_by


def test_sort_by_criteria():
    jobs_values = [
        {"min_salary": 100},
        {"min_salary": 700},
        {"min_salary": 250},
        {"min_salary": 800},
        {"min_salary": 340},
    ]
    sort_by(jobs_values, "min_salary")
    assert jobs_values == [
        {"min_salary": 100},
        {"min_salary": 250},
        {"min_salary": 340},
        {"min_salary": 700},
        {"min_salary": 800},
    ]
