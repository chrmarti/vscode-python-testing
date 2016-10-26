See [documentation](https://github.com/DonJayamanne/pythonVSCode/wiki) for details.

#### Prereqs

* Install / update to the latest Python extension from Don
* Install Python 3.5 and Python 2.7 (if not preinstalled with your OS)
* Install default linter `pip install pylint`
* Install default formatter `pip install autopep8`

#### Setup

* Use `Select Workspace Interpreter` to configure the Python version to run against
  * Use setting `"python.pythonPath"` if not listed.

#### IntelliSense

* Verify that IntelliSense is working
  * With standard libraries
  * With custom modules

#### Linting

* Verify linting is working
  * With the default linter (Pylint)
  * With one other supported linter

#### Formatting

* Verify formatting is working with the default formatter (AutoPep8)

#### Refactoring

* Verify refactorings work as expected
  * Rename (affecting one or multiple files)
  * Sort import
  * Extract variable
  * Extract method

#### Debugging

* Verify debugging a console app or any other flavour listed in the documentation works
  * Verify that the debugger stops at breakpoints
  * Verify you can step into / over / out of any line of code

#### Unit tests

* Run a simple unit test with the built-in library UnitTests

#### Jupyter integration

* Install Jupyter prereqs and run some examples (See [documentation](https://github.com/DonJayamanne/pythonVSCode/wiki/Jupyter-(IPython)))
