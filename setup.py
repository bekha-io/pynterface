from setuptools import setup, find_packages

setup(
    name='pynterfacelib',
    version='1.0.0',
    description='Library for checking interface compliance in Python',
    long_description='''pynterface is a library that provides a mechanism for enforcing strict adherence to interfaces in Python. It allows you to define interfaces and ensures that all implementing classes properly implement the required methods defined in the interface.''',
    author='Bekhruz Iskandarzoda',
    author_email='iskandarzoda@outlook.com',
    url='https://github.com/bekha-io/pynterface',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='interface checker development',
    license='MIT',
    python_requires='>=3.6',
)