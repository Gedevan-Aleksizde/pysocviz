from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='pysocviz',
        version='0.2',
        url='https://github.com/Gedevan-Aleksizde/pysocviz',
        license='',
        author='Katagiri, Satoshi',
        packages=find_packages(),
        install_requires=[
            'adjustText >= 0.7.3',
            'gapminder >= 0.1',
            'geopandas >= 0.9.0',
            'mizani >= 0.7.3',
            'numpy >= 1.20.3',
            'pandas >= 1.2.4',
            'scikit-misc >= 0.1.4',
            'statsmodels >= 0.12.2',
            'plotnine >= 0.8'
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
