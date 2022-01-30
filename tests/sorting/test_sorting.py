from src.sorting import sort_by


def test_sort_by_criteria():
    jobs = [{"min_salary": 1000}, {"min_salary": 2000}, {"min_salary": 500}]

    sort_by(jobs, "min_salary")

    assert jobs == [
        {"min_salary": 500},
        {"min_salary": 1000},
        {"min_salary": 2000},
    ]
