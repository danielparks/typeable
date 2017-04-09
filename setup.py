import setuptools

setuptools.setup(
    name = "typeable",
    version = "0.0.1",

    description = "Calculate how hard it is to type a given string",
    author = "Daniel Parks",
    author_email = "typeable@demonhorse.net",
    url = "http://github.com/danielparks/typeable",
    license = "BSD",
    long_description = open("README.rst").read(),

    classifiers = [
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
    ],

    packages = [ "typeable" ],
    install_requires = [
        'click',
    ],

    include_package_data = True,
    entry_points = {
        "console_scripts": [
            "typeable = typeable.cli:main"
        ]
    }
)
