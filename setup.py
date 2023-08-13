from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
    
with open('requirements.txt') as f:
    required = f.read().splitlines()

VERSION = '0.0.1.9'
DESCRIPTION = 'The official gpt4free repository | various collection of powerful language models'

# Setting up
setup(
    name="g4f",
    version=VERSION,
    author="Tekky",
    author_email="<support@g4f.ai>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=required,
    keywords=['python', 'chatbot', 'reverse-engineering', 'openai', 'chatbots', 'gpt', 'language-model', 'gpt-3', 'gpt3', 'openai-api', 'gpt-4', 'gpt4', 'chatgpt', 'chatgpt-api', 'openai-chatgpt', 'chatgpt-free', 'chatgpt-4', 'chatgpt4','chatgpt4-api', 'free', 'free-gpt', 'gpt4free', 'g4f'],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)