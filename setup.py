from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(
    name='rule34-api',
    version='0.0.2',
    description='valzkai ae rule 34 api',
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    url='https://github.com/akashktesla/rule34-api',
    author='akashktesla',
    author_email='akashktesla@gmail.com',
    keywords='rule34_image,rule34_number',
    license='MIT',
    install_requires=['requests', 'beautifulsoup4', 'lxml'],
    include_package_data=True,
    zip_safe=False
)