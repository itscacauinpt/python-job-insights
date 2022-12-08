from typing import List, Dict

from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    try:
        jobs = read(path)
        unique_ind = {job['industry'] for job in jobs if job['industry'] != ''}

    except AttributeError:
        raise Exception('Could not attribute references or assignments')

    else:
        return unique_ind


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    try:
        filtered = [job for job in jobs if job['industry'] == industry]

    except KeyError:
        raise Exception('Key error')

    else:
        return filtered
