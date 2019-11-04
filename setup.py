import distutils.command.build
import distutils.command.sdist
import os
import subprocess

from setuptools import Command, find_packages, setup

REQS = ["python-socketio==4.3.1", "aiohttp==3.5.4", "aiohttp-devtools==0.13.1"]


class build_assets(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        base_dir = os.path.abspath(os.path.dirname(__file__))
        renderer_dir = os.path.join(base_dir, "webimgui-renderer")
        package_dir = os.path.join(base_dir, "webimgui")
        dist_dest = os.path.join(package_dir, "dist")

        subprocess.check_call(["yarn", "build", "--dest", dist_dest], cwd=renderer_dir)


class build(distutils.command.build.build):
    _sub_command = ("build_assets", None)
    _sub_commands = distutils.command.build.build.sub_commands
    sub_commands = [_sub_command] + _sub_commands


class sdist(distutils.command.sdist.sdist):
    _sub_command = ("build_assets", None)
    _sub_commands = distutils.command.sdist.sdist.sub_commands
    sub_commands = [_sub_command] + _sub_commands


with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="webimgui",
    version="0.0.2",
    author="Elnard Utiushev",
    author_email="elnardu2@gmail.com",
    packages=find_packages(exclude=["tests"]),
    include_package_data=True,
    license="MIT",
    description="Python framework for simple webapps and dashboards",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=REQS,
    url="https://github.com/elnardu/webimgui",
    python_requires=">=3.6",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3 :: Only",
    ],
    cmdclass={"build_assets": build_assets, "build": build, "sdist": sdist},
)
