from setuptools import setup


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="CS Helper",
    version="0.1",
    description="CS Helper, Here to Help",
    url="https://github.com/CS-Helper-Helpers/cs_helper",
    author="Team 3 AI Masters",
    author_email="flyingcircus@example.com",
    license="NA",
    packages=[
        "cs_helper",
        "database",
        "gui",
        "input",
        "intent_classifier",
        "phone",
        "slots",
    ],
    install_requires=[
        "gtts",
        "tensorflow",
        "nltk",
        "playsound",
        "speechrecognition",
        "SQLAlchemy",
        "PyAudio",
        "pymysql",
    ],
    zip_safe=False,
    test_suite="nose.collector",
    tests_require=["nose"],
)
