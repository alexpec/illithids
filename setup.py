from setuptools import setup, find_packages
import unittest
import os

def illithids_test_suite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('Python/illithids', pattern='test_*.py')
	return test_suite


local_path = os.path.dirname(os.path.abspath(__file__))
setup(
	name='Illithids',
	version = "1.0.0",
 	description = " Illithids - Molecular Dynamics Post-Processing Library",
 	author = "Saturn-Rings Engineering and Consulting",
 	author_email = "alexpec@gmail.com",
	package_dir = {'': 'Python'},
	packages= find_packages(where='Python', exclude=('_Tests')),
	test_suite='setup.illithids_test_suite',
)
