from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='pysocviz',
        version='0.3.0',
        url='https://github.com/Gedevan-Aleksizde/pysocviz',
        license='',
        author='Katagiri, Satoshi',
        packages=find_packages(),
        install_requires=[
            'adjustText >= 1.1.1',
            'gapminder >= 0.1',
            'geopandas >= 0.14.3',
            'mizani >= 0.11.0',
            'numpy >= 1.26.4',
            'pandas >= 2.2.1',
            'scikit-misc >= 0.1.4',
            'statsmodels >= 0.12.2',
            'plotnine >= 0.13.2'
        ],
        package_data={'pysocviz': ['data/*.csv', 'data/schema.json']},
        author_email='katagiri.stsh@gmail.com',
        description='Unofficial python version of socviz by K. Healy',
        python_requires = '>3.7.1',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
            'Programming Language :: Python :: 3.10'
        ]
    )
