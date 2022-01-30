from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [
        {"min_salary": 1500},
        {"min_salary": 2100},
        {"min_salary": 1200},
        {"min_salary": 1800},
        {"min_salary": 1100},
    ]
    sort_by(jobs, "min_salary")
    assert jobs == [
        {"min_salary": 1100},
        {"min_salary": 1200},
        {"min_salary": 1500},
        {"min_salary": 1800},
        {"min_salary": 2100},
    ]
