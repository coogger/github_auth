from setuptools import setup

setup(
    name="github_auth",
    version='0.0.5',
    description='A django application to login via github.',
    author='hakancelik96',
    author_email='hakancelik96@outlook.com',
    packages=["github_auth"],
    include_package_data=True,
    install_requires=[],
    url="https://github.com/djangoapps/github_auth",
    license='MIT',
    zip_safe=False,
    keywords="github, django github, login github",
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
