from pathlib import Path

from jarguments import __author__, __doc__, __license__, __module__, __version__
from setuptools import setup

setup(
	name=__module__,
	version=__version__,
	description=(__doc__ or '').replace('\n', ' ').strip(),
	long_description=Path('README.md').read_text(),
	long_description_content_type='text/markdown',
	url=f'https://github.com/{__author__}/{__module__}',
	author=__author__,
	include_package_data=True,
	license=__license__,
	packages=[__module__],
	package_data={},
	setup_requires=['pytest_runner'],
	python_requires='>=3.8',
	scripts=[],
	tests_require=['pytest'],
	entry_points={},
	zip_safe=True,
	classifiers=[
		'Development Status :: 4 - Beta',
		'License :: OSI Approved :: MIT License',
		'Operating System :: OS Independent',
	],
)
