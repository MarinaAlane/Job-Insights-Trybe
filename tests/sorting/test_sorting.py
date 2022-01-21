from src.sorting import sort_by


def test_sort_by_criteria():
    var = [{
            "min_salary": 100,
            "max_salary": 10000,
            "date_posted": "2003-03-23"
        },
        {
            "min_salary": 200,
            "max_salary": 20000,
            "date_posted": "2001-01-23"
        },
        {
            "min_salary": 400,
            "max_salary": 40000,
            "date_posted": "2006-03-23"
        }]
    sort_by(var, "min_salary")
    assert var == [{
            "min_salary": 100,
            "max_salary": 10000,
            "date_posted": "2003-03-23"
        },
        {
            "min_salary": 200,
            "max_salary": 20000,
            "date_posted": "2001-01-23"
        },
        {
            "min_salary": 400,
            "max_salary": 40000,
            "date_posted": "2006-03-23"
        }]
    sort_by(var, "max_salary")
    assert var == [{
            "min_salary": 400,
            "max_salary": 40000,
            "date_posted": "2006-03-23"
        },
        {
            "min_salary": 200,
            "max_salary": 20000,
            "date_posted": "2001-01-23"
        },
        {
            "min_salary": 100,
            "max_salary": 10000,
            "date_posted": "2003-03-23"
        }]
    sort_by(var, "date_posted")
    assert var == [{
            "min_salary": 400,
            "max_salary": 40000,
            "date_posted": "2006-03-23"
        },
        {
            "min_salary": 100,
            "max_salary": 10000,
            "date_posted": "2003-03-23"
        },
        {
            "min_salary": 200,
            "max_salary": 20000,
            "date_posted": "2001-01-23"
        }]
    pass
