from src.pre_built.sorting import sort_by

jobs_fake = [
        {
            'title': 'Web developer',
            'min_salary': '3000',
            'max_salary': '7000',
            'date_posted': '2020-05-08'
        },
        {
            'title': 'Front end developer',
            'min_salary': '1000',
            'max_salary': '5000',
            'date_posted': '2020-05-10'
        },
        {
            'title': 'Back end developer',
            'min_salary': '1000',
            'max_salary': '3000',
            'date_posted': '2020-02-05'
        },
        {
            'title': 'Full stack end developer',
            'min_salary': '4000',
            'max_salary': '8000',
            'date_posted': '2020-05-01'
        }
    ]

mock_max_salary = [
    {
        'title': 'Full stack end developer',
        'min_salary': '4000',
        'max_salary': '8000',
        'date_posted': '2020-05-01'
    },
    {
        'title': 'Web developer',
        'min_salary': '3000',
        'max_salary': '7000',
        'date_posted': '2020-05-08'
    },
    {
        'title': 'Front end developer',
        'min_salary': '1000',
        'max_salary': '5000',
        'date_posted': '2020-05-10'
    },
    {
        'title': 'Back end developer',
        'min_salary': '1000',
        'max_salary': '3000',
        'date_posted': '2020-02-05'
    }
]

mock_min_salary = [
    {
        'title': 'Front end developer',
        'min_salary': '1000',
        'max_salary': '5000',
        'date_posted': '2020-05-10'
    },
    {
        'title': 'Back end developer',
        'min_salary': '1000',
        'max_salary': '3000',
        'date_posted': '2020-02-05'
    },
    {
        'title': 'Web developer',
        'min_salary': '3000',
        'max_salary': '7000',
        'date_posted': '2020-05-08'
    },
    {
        'title': 'Full stack end developer',
        'min_salary': '4000',
        'max_salary': '8000',
        'date_posted': '2020-05-01'
    }
]

mock_date_posted = [
    {
        'title': 'Front end developer',
        'min_salary': '1000',
        'max_salary': '5000',
        'date_posted': '2020-05-10'
    },
    {
        'title': 'Web developer',
        'min_salary': '3000',
        'max_salary': '7000',
        'date_posted': '2020-05-08'
    },
    {
        'title': 'Full stack end developer',
        'min_salary': '4000',
        'max_salary': '8000',
        'date_posted': '2020-05-01'
    },
    {
        'title': 'Back end developer',
        'min_salary': '1000',
        'max_salary': '3000',
        'date_posted': '2020-02-05'
    }
]


def test_sort_by_criteria():
    sort_by(jobs_fake, 'date_posted')
    assert jobs_fake == mock_date_posted

    sort_by(jobs_fake, 'max_salary')
    assert jobs_fake == mock_max_salary

    sort_by(jobs_fake, 'min_salary')
    assert jobs_fake == mock_min_salary
