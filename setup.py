import setuptools

def readme():
    with open('README.rst') as f:
        return f.read()

setuptools.setup(
    name='foowise',
    version='0.9',
    description='An implementation of Barwise-Seligman Channels',
    long_description=readme(),
    
    url='https://github.com/ben-schulz/foowise',
    author='Benjamin Schulz',
    author_email='benjamin.john.schulz@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Science/Research',
        'Natural Language :: English',
        'Topic :: Scientific/Engineering',
        ],

    packages=[
        'foowise.channels',
        'foowise.math',
        'foowise.heuristic'
    ],

    install_requires=[
        'numpy'
    ],

    entry_points={
        'console_scripts':['foowise=foowise.command_line:main']
    },

    test_suite='foowise.test.suite',

    include_package_data=True,
    zip_safe=False
)
