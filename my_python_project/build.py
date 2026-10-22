"""PyBuilder configuration for my_python_project."""

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "my_python_project"
version = "1.0.0"
summary = "EECE435L Lab 6 build automation exercise"
author = "Hassan Nasrallah"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    # The handout names tests test_*.py, unlike PyBuilder's *_tests default.
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("dir_target", "target")
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
