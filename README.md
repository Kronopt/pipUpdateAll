# pipUpdateAll
The missing "pip install --upgrade ALL" feature missing from pip

This script basically checks for outdated modules using `pip list --outdated`, parses the output to only show relevant
information (specifically `name`, `current_version` and `new_version`) and then updates all detected modules using `pip install -U module_1 module_2 ...`

#### Dependencies
* Python 2.7
* pip

#### How to run
Double click pipUpdateAll.py to update every outdate python module
