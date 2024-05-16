'Setup script for the jarguments package.'

from pathlib import Path

from jarguments import (
	__author__,
	__doc__,
	__license__,
	__module_name__,
	__python_version__,
	__version__,
)
from setuptools import setup

setup(
	name=__module_name__,
	version=__version__,
	description=__doc__,
	long_description=Path('README.md').read_text(),
	long_description_content_type='text/markdown',
	url=f'https://github.com/{__author__}/{__module_name__}',
	author=__author__,
	include_package_data=True,
	license=__license__,
	packages=[__module_name__],
	package_data={},
	setup_requires=['pytest_runner'],
	python_requires=f'>={__python_version__}',
	scripts=[],
	tests_require=['pytest'],
	entry_points={},
	zip_safe=True,
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 3.8',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python',
		'Topic :: Software Development :: Libraries :: Python Modules',
		'Topic :: Software Development :: Libraries',
	],
)
