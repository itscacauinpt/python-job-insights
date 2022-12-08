from functools import lru_cache
from typing import List, Dict

import csv


@lru_cache
def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    try:
        with open(path, encoding="utf-8") as file:
            jobs_file = csv.DictReader(file, delimiter=",")
            jobs_archive = []
            for job in jobs_file:
                jobs_archive.append(job)

    except not path.endswith(('.csv')):
        raise Exception('Must be a csv file')

    except OSError:
        raise Exception('Could not read file')

    else:
        return jobs_archive


def get_unique_job_types(path: str) -> List[str]:
    """Checks all different job types and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique job types
    """
    try:
        jobs_file = read(path)
        unique_jobs_archive = set()
        for job_type in jobs_file:
            unique_jobs_archive.add(job_type['job_type'])

    except AttributeError:
        raise Exception('Could not attribute references or assignments')

    else:
        return unique_jobs_archive


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
