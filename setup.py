from setuptools import setup, find_packages

setup(
    name="myblog",
    version="1.0",
    url="https://github.com/zhang-da-miao/Myblog",
    license="MIT",
    author="zhou yiguang",
    author_email="zhouyig180@gmail.com",
    description="It has the function of login and registration",
    packages=find_packages(include=('*',)),
    include_package_data=True,
    install_requires=[]
)
