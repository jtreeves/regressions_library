from setuptools import setup, find_packages

setup(
    name='regressions',
    version='2.0.6',
    url='https://github.com/jtreeves/regressions_library',
    license='MIT',
    author='Jackson Reeves',
    author_email='jr@jacksonreeves.com',
    description='Generate regression models from data',
    packages=[
        'regressions',
        'regressions.models',
        'regressions.analyses',
        'regressions.analyses.equations',
        'regressions.analyses.derivatives',
        'regressions.analyses.integrals',
        'regressions.analyses.roots',
        'regressions.statistics',
        'regressions.matrices',
        'regressions.vectors',
        'regressions.errors'
    ],
    include_package_data=True,
    long_description=open('PYPI.md').read(),
    long_description_content_type='text/markdown',
    project_urls={
        'Documentation': 'https://regressions.readthedocs.io/en/latest/',
        'Source': 'https://github.com/jtreeves/regressions_library'
    },
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Topic :: Scientific/Engineering',
        'Topic :: Scientific/Engineering :: Mathematics',
        'Topic :: Software Development',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
    install_requires=['numpy', 'scipy']
)