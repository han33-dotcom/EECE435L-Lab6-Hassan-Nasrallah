"""PyBuilder configuration for calculator_Hassan_Nasrallah."""

from pybuilder.core import init, use_plugin

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.distutils")

name = "calculator_Hassan_Nasrallah"
version = "1.0.0"
summary = "EECE435L Lab 6 build automation exercise"
author = "Hassan Nasrallah"
default_task = "publish"


@init
def initialize(project):
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property(
        "dir_source_unittest_python",
        "tests/unittest/calculator_Hassan_Nasrallah",
    )
    # The handout names tests test_*.py, unlike PyBuilder's *_tests default.
    project.set_property("unittest_module_glob", "test_*")
    project.set_property("dir_target", "target")
    project.set_property("distutils_commands", ["sdist", "bdist_wheel"])
