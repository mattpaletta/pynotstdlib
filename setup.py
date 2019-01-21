from setuptools import setup, find_packages

setup(
    name="pynotstdlib",
    version="0.0.1",
    url='https://github.com/mattpaletta/pynotstdlib',
    packages=find_packages(),
    include_package_data=True,
    install_requires=["threadlru"],
    setup_requires=[],
    author="Matthew Paletta",
    author_email="mattpaletta@gmail.com",
    description="Extra useful functions and datatypes",
    license="BSD",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Communications',
    ]
)