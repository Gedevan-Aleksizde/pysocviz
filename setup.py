from setuptools import setup, find_packages

if __name__ == '__main__':
    setup(
        name='pysocviz',
        version='0.1',
        url='',
        license='',
        author='Katagiri, Satoshi',
        packages=find_packages(),
        install_requires=open('requirements.txt', 'r').readlines(),
        package_data={'pysocviz': ['data/*.csv', 'data/schema.json']},
        author_email='katagiri.stsh@gmail.com',
        description='Unofficial python version of socviz by K. Healy',
        python_requires = '>3.7.1',
        classifiers=[
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.7',
            'Programming Language :: Python :: 3.8',
            'Programming Language :: Python :: 3.9'
        ]
    )
