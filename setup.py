from setuptools import setup
import sys


sys.path.append("clearpass_driver")


def get_version(path='CHANGELOG.md'):
    """
    Get latest version from a `keepachangelog` formatted file
    See also http://keepachangelog.com/en/1.0.0/
    """
    with open(path) as fd:
        for l in fd.read().split('\n'):
            version = "0.0.0"
            if l.startswith('## ['):
                version = l.split('## [')[1].split(']')[0]
                break
    if version == 'Unreleased':
        # If there's no version yet, this is the version
        version = "0.0.1"
    return version


def get_requirements(path='requirements.txt'):
    """
    Reads a standard `requirements.txt` style file (output of `pip freeze`)
    """
    with open(path) as fd:
        requirements = fd.read()
    return requirements


setup(name="clearpass-driver",
      version=get_version(),
      description="A Slack deprovisioning driver for Mozilla IAM",
      license="MPL",
      url="https://github.com/mozilla-iam/clearpass-driver",
      install_requires=get_requirements('clearpass_driver/requirements.txt'),
      tests_require=get_requirements('clearpass_driver/tests_requirements.txt')
      )
