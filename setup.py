from setuptools import setup

setup(
    name="hubgridcloud",
    version="0.0.4",
    description="The SimplyStack API allows you to manage Stacklets and resources within the SimplyStack cloud in a simple, programmatic way using conventional HTTP requests.",
    long_description="The SimplyStack API allows you to manage Stacklets and resources within the SimplyStack cloud in a simple, programmatic way using conventional HTTP requests. The endpoints are intuitive and powerful, allowing you to easily make calls to retrieve information or to execute actions.",
    keywords="python, cloud, hubgridcloud, server",
    author="Kalinin Dmitry <kalinin.mitko@gmail.com>",
    url="https://github.com/null-none/python-hubgridcloud",
    license="MIT",
    packages=["src"],
    zip_safe=False,
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
    ],
    install_requires=["requests==2.27.1", "schema==0.7.5"],
)
