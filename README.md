# pipUpdateAll
The missing "pip install --upgrade ALL" feature missing from pip

This script basically checks for outdated modules using `pip list --outdated`, parses the output to only show relevant
information (specifically `name`, `current_version` and `new_version`) and then updates all detected modules using `pip install -U module_1 module_2 ...`

There are lots of ways to achieve this, as can be seen in this discussion https://stackoverflow.com/questions/2720014/upgrading-all-packages-with-pip. This script is just my take on the matter.

At the time of this writing, there still was a debate about wether to add an option like this to pip (at https://github.com/pypa/pip/issues/59). So while that option isn't officialy implemented, feel free to use pipUpdateAll

#### Dependencies
* Python 2.7
* pip

#### How to run
Double click pipUpdateAll.py to update every outdated python module

#### Note
If you get a pip related error it's probably because you have an outdated version of pip. Outdated versions may still not have implemented the necessary options for this script to work
