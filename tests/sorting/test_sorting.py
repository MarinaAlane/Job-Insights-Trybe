import pytest
from src.sorting import sort_by

# Foi utilizado um gerador de datas para o 'date_posted'
# https://www.random.org/calendar-dates/?num=5&start_day=21&start_month=1&start_year=2022&end_day=31&end_month=12&end_year=2022&mondays=on&tuesdays=on&wednesdays=on&thursdays=on&fridays=on&display=2&format=html&rnd=new


@pytest.fixture
def jobs():
    return [
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
    ]


def test_sort_by_criteria(jobs):
    order_by_min_salary = [
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
    ]
    assert sort_by(jobs, "min_salary") == order_by_min_salary

    order_by_max_salary = [
        {"min_salary": 1500, "max_salary": 25000, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 15000, "date_posted": "2022-07-05"},
        {"min_salary": 500, "max_salary": 10000, "date_posted": "2022-06-27"},
    ]
    assert sort_by(jobs, "max_salary") == order_by_max_salary

    order_by_date_posted = [
        {"min_salary": 1500, "max_salary": 2500, "date_posted": "2022-09-13"},
        {"min_salary": 1000, "max_salary": 1500, "date_posted": "2022-07-05"},
        {"min_salary": 500, "max_salary": 1000, "date_posted": "2022-06-27"},
    ]
    assert sort_by(jobs, "date_posted") == order_by_date_posted

    not_a_criteria = "not_a_criteria"
    with pytest.raises(
        ValueError, match="invalid sorting criteria: not_a_criteria"
    ):
        sort_by(jobs, not_a_criteria)
