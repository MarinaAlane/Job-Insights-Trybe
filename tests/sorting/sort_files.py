jobs = [
    # 0
    {
        'min_salary': 0,
        'max_salary': 12000,
        'date_posted': '2019-12-23',
    },
    {
        'min_salary': 1500,
        'max_salary': 9000,
        'date_posted': '2019-12-20',
    },
    {
        'max_salary': 27000,
        'date_posted': '2022-01-20',
    },
    {
        'min_salary': 5000,
        'date_posted': '2022-01-07',
    },
    {
        'min_salary': 1000,
        'max_salary': 3000,
    },
]

ordenated_jobs = {
    'min_salary': [jobs[0], jobs[4], jobs[1], jobs[3], jobs[2]],
    'max_salary': [jobs[2], jobs[0], jobs[1], jobs[4], jobs[3]],
    'date_posted': [jobs[2], jobs[3], jobs[0], jobs[1], jobs[4]],
}
