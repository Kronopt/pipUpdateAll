#!python2
# coding: utf-8

"""
PIPUPDATEALL
Updates outdated python modules using pip
Checks outdated modules using "pip list --outdated --format columns", parses that column to only show relevant
information (name, current version, new version) and then updates all detected modules using "pip install -U" followed
by each module's name

DEPENDENCIES:
    - Python 2.7
    - pip

HOW TO RUN:
    - Directly, by double clicking the script.
"""

import subprocess
import sys
from time import sleep

__author__ = 'Pedro HC David, https://github.com/Kronopt'
__credits__ = ['Pedro HC David']
__version__ = '1.0'
__date__ = '02:40h, 16/12/2016'
__status__ = 'Finished'


def pip_list_columns_parser(pip_list_columns_format_output):
    """
    Parses the output of "pip list --outdated --format columns" into a dictionary

    PARAMETERS:
        pip_list_columns_format_output : str
            output of "pip list --outdated --format columns"

    RETURNS: {{module_name : (current_version, new_version)}
        Module_name associated with its current_version and new_version
    """
    # Column format:
    #
    # Package       Version   Latest    Type
    # ------------- --------- --------- ----
    # module_1_name version_1 version_2 type
    # module_2_name version_1 version_2 type
    final_dictionary = {}

    # removes "Package", "Version", etc and "----"
    modules_and_versions = pip_list_columns_format_output.split()[8:]
    number_of_modules = len(modules_and_versions)/4

    # parses list
    for module_number in xrange(number_of_modules):
        list_position = module_number*4
        final_dictionary[modules_and_versions[list_position]] = (modules_and_versions[list_position+1],
                                                                 modules_and_versions[list_position+2])

    return final_dictionary


if __name__ == '__main__':
    # location of python executable, avoids dependency on windows PATH
    python_executable = sys.executable

    # checking if pip is installed
    try:
        pip_version_output = subprocess.check_output([python_executable, "-m", "pip", "--version"])
        pip_version = pip_version_output.split()[1]
    except subprocess.CalledProcessError:
        print "Python cannot locate pip..."
        sys.exit()

    print "Modules to be updated using pip version", pip_version + ":"

    # Get modules out of date
    modules_to_update_columns = subprocess.check_output(
        [python_executable, "-m", "pip", "list", "--outdated", "--format", "columns"])

    # dictionary in the format {module_name : (current_version, new_version)}
    modules_to_update = pip_list_columns_parser(modules_to_update_columns)

    if len(modules_to_update) > 0:
        module_names = []
        # shows modules out of date and each respective current versions and new versions
        for module_name, (current_version, new_version) in sorted(modules_to_update.iteritems()):
            print module_name + ":", current_version, "->", new_version
            module_names.append(module_name)

        print

        no_correct_answer_given_yet = True
        while no_correct_answer_given_yet:
            answer = raw_input("Do you wish to continue (y/n)? ")

            if answer == "y":
                # call "pip install -U" with every outdated module name as parameters
                subprocess.call([python_executable, "-m", "pip", "install", "--upgrade"] + module_names)
                no_correct_answer_given_yet = False
            elif answer == "n":
                print "Update canceled"
                no_correct_answer_given_yet = False
    else:
        print "All modules are up to date"

    sleep(2)
