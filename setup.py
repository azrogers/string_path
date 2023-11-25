from setuptools import setup

setup(
	name='string_path',
	version='1.0.0',
	description='Calculates the path between two strings based on edit distance',
	author='Ashley Rogers',
	author_email='ashley@rogers.cafe',
	packages=['string_path'],
	install_requires=['editdistance']
)