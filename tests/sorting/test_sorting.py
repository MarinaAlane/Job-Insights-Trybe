import pytest
from src.sorting import sort_by

jobs = [
    {
        "Title": "Senior Salesforce Developer",
        "Company": "National Debt Relief",
        "Industry": "Finance",
        "Type": "FULL_TIME",
        "min_salary": 44587,
        "max_salary": 82162,
        "date_posted": "2022-01-10"
    },
    {
        "Title": "Emergency Veterinarian - NYC",
        "Company": "Veterinary Emergency Group",
        "Industry": "Health Care",
        "Type": "FULL_TIME",
        "min_salary": 94715,
        "max_salary": 103279,
        "date_posted": "2022-01-11"
    },
    {
        "Title": "Construction Project Manager",
        "Company": "The LiRo Group",
        "Industry": "Construction, Repair & Maintenance",
        "Type": "FULL_TIME",
        "min_salary": 54991,
        "max_salary": 143860,
        "date_posted": "2022-01-12"
    },
]


def test_sort_by_criteria():
    with pytest.raises(TypeError):
        sort_by(jobs, "salary", "remote")

    sort_by(jobs, "max_salary")
    assert jobs == [
        {
            "Title": "Construction Project Manager",
            "Company": "The LiRo Group",
            "Industry": "Construction, Repair & Maintenance",
            "Type": "FULL_TIME",
            "min_salary": 54991,
            "max_salary": 143860,
            "date_posted": "2022-01-12"
        },
        {
            "Title": "Emergency Veterinarian - NYC",
            "Company": "Veterinary Emergency Group",
            "Industry": "Health Care",
            "Type": "FULL_TIME",
            "min_salary": 94715,
            "max_salary": 103279,
            "date_posted": "2022-01-11"
        },
        {
            "Title": "Senior Salesforce Developer",
            "Company": "National Debt Relief",
            "Industry": "Finance",
            "Type": "FULL_TIME",
            "min_salary": 44587,
            "max_salary": 82162,
            "date_posted": "2022-01-10"
        },
    ]

    sort_by(jobs, "min_salary")
    assert jobs == [
        {
            "Title": "Senior Salesforce Developer",
            "Company": "National Debt Relief",
            "Industry": "Finance",
            "Type": "FULL_TIME",
            "min_salary": 44587,
            "max_salary": 82162,
            "date_posted": "2022-01-10"
        },
        {
            "Title": "Construction Project Manager",
            "Company": "The LiRo Group",
            "Industry": "Construction, Repair & Maintenance",
            "Type": "FULL_TIME",
            "min_salary": 54991,
            "max_salary": 143860,
            "date_posted": "2022-01-12"
        },
        {
            "Title": "Emergency Veterinarian - NYC",
            "Company": "Veterinary Emergency Group",
            "Industry": "Health Care",
            "Type": "FULL_TIME",
            "min_salary": 94715,
            "max_salary": 103279,
            "date_posted": "2022-01-11"
        },
    ]

    sort_by(jobs, "date_posted")
    assert jobs == [
        {
            "Title": "Construction Project Manager",
            "Company": "The LiRo Group",
            "Industry": "Construction, Repair & Maintenance",
            "Type": "FULL_TIME",
            "min_salary": 54991,
            "max_salary": 143860,
            "date_posted": "2022-01-12"
        },
        {
            "Title": "Emergency Veterinarian - NYC",
            "Company": "Veterinary Emergency Group",
            "Industry": "Health Care",
            "Type": "FULL_TIME",
            "min_salary": 94715,
            "max_salary": 103279,
            "date_posted": "2022-01-11"
        },
        {
            "Title": "Senior Salesforce Developer",
            "Company": "National Debt Relief",
            "Industry": "Finance",
            "Type": "FULL_TIME",
            "min_salary": 44587,
            "max_salary": 82162,
            "date_posted": "2022-01-10"
        },
    ]
