from setuptools import setup, find_packages
import unittest

def illithids_test_suite():
	test_loader = unittest.TestLoader()
	test_suite = test_loader.discover('Python', pattern='test_*.py')
	return test_suite




setup(
	name='Python',
	packages=find_packages(),
	test_suite='setup.illithids_test_suite',
)
