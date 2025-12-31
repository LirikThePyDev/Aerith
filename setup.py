from setuptools import setup, find_packages

setup(
    name='aerith',
    version='0.1.0',
    author='Abdulrahman Faris',
    author_email='lirikthepythondev@gmail.com',
    description='Python 3.15-level language interpreter implemented in Python',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/LirikThePyDev/Aerith',
    packages=find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
