from typing import Union, List, Dict

from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    try:
        jobs = read(path)
        salaries = [
            int(job['max_salary'])
            for job in jobs
            if job['max_salary'].isdigit()
            ]

        max_salary = max(salaries)

    except OSError:
        raise Exception('Error system')

    else:
        return max_salary


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    try:
        jobs = read(path)
        salaries = [
            int(job['min_salary'])
            for job in jobs
            if job['min_salary'].isdigit()
            ]

        min_salary = min(salaries)

    except OSError:
        raise Exception('Error system')

    else:
        return min_salary


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    if (
        'max_salary' not in job
        or 'min_salary' not in job
    ):
        raise ValueError

    elif (
        type(job['max_salary']) != int
        or type(job['min_salary']) != int
    ):
        raise ValueError

    elif (
        int(job['min_salary']) > int(job['max_salary'])
        or not str(salary).lstrip('-.')
    ):
        raise ValueError

    else:
        return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    jobs_list = list()
    for job in jobs:
        if matches_salary_range(job, salary):
            jobs_list.append(job)

    return jobs_list

    # try:
    #     jobs_list = list()
    #     for job in jobs:
    #         if matches_salary_range(job, salary):
    #             jobs_list.append(job)
    #
    # exception Assertion?
