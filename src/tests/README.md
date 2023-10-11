# Pytest

### Commands
```bash
pytest -v 
pytest -s
# To run test and see strout|strerr 
pytest -v -s 
# To run integration tests 
pytest -v --integration 

# To only run integration tests
pytest -v -m integration
```
---
`pytest -v`

> **Note:** -v (or --verbose) command line option is used to increase the verbosity of the test output when running your tests.

### Changes 
`Test Discovery Information:` 
When you run pytest with -v, it provides information about which test functions and test cases it discovered. 
This includes the names of test modules and test functions.

`Individual Test Results:` 
For each test function or test case, pytest displays detailed information 
about whether the test passed, failed, or encountered errors. 
It shows the test name, the assertion results, and any exceptions or traceback information for failed tests.

`Test Execution Order:` 
With -v, you can see the order in which pytest executes the test functions. 
It shows the sequence of tests that are run, which can help you identify any dependencies or issues in your test suite.

---
`pytest -s`
> **Note:** This will show strout to the console during execution.

---