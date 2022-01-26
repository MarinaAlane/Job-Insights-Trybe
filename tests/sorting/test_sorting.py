# from src.sorting import sort_by
import pytest


@pytest.fixture()
def jobs():
    return [
        {
            "title": "Arquiteto de depende",
            "max_salary": 29000,
            "min_salary": 9000,
            "date_posted": "2023-04-01",
        },
        {
            "title": "Analista de bug",
            "max_salary": 35000,
            "min_salary": 12000,
            "date_posted": "2023-01-19",
        },
        {
            "title": "Testador de teste",
            "max_salary": 25500,
            "min_salary": 7000,
            "date_posted": "2022-07-15",
        },
        {
            "title": "Ajudante de Junior",
            "max_salary": 3000,
            "min_salary": 1500,
            "date_posted": "2022-12-30",
        },
    ]


min_salary_criteria = [
    {
        "title": "Ajudante de Junior",
        "max_salary": 3000,
        "min_salary": 1500,
        "date_posted": "2022-12-30",
    },
    {
        "title": "Testador de teste",
        "max_salary": 25500,
        "min_salary": 7000,
        "date_posted": "2022-07-15",
    },
    {
        "title": "Arquiteto de depende",
        "max_salary": 29000,
        "min_salary": 9000,
        "date_posted": "2023-04-01",
    },
    {
        "title": "Analista de bug",
        "max_salary": 35000,
        "min_salary": 12000,
        "date_posted": "2023-01-19",
    },
]

max_salary_criteria = [
    {
        "title": "Analista de bug",
        "max_salary": 35000,
        "min_salary": 12000,
        "date_posted": "2023-01-19",
    },
    {
        "title": "Arquiteto de depende",
        "max_salary": 29000,
        "min_salary": 9000,
        "date_posted": "2023-04-01",
    },
    {
        "title": "Testador de teste",
        "max_salary": 25500,
        "min_salary": 7000,
        "date_posted": "2022-07-15",
    },
    {
        "title": "Ajudante de Junior",
        "max_salary": 3000,
        "min_salary": 1500,
        "date_posted": "2022-12-30",
    },
]

date_posted_criteria = [
    {
        "title": "Arquiteto de depende",
        "max_salary": 29000,
        "min_salary": 9000,
        "date_posted": "2023-04-01",
    },
    {
        "title": "Analista de bug",
        "max_salary": 35000,
        "min_salary": 12000,
        "date_posted": "2023-01-19",
    },
    {
        "title": "Ajudante de Junior",
        "max_salary": 3000,
        "min_salary": 1500,
        "date_posted": "2022-12-30",
    },
    {
        "title": "Testador de teste",
        "max_salary": 25500,
        "min_salary": 7000,
        "date_posted": "2022-07-15",
    },
]
