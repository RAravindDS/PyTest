# Why Unit Test? 
* It reduces bug in the new featuers. 
* Tests are good documentation. 
* Faster Debugging, development, testing, and desing. 

### Unit Testing Frameworkds: 
* Unittest - Python standard library
* nose - It's not in standard library. 
* pytest - not in the python standard library but it's more popular. 

### Installing pytest: 
```python 
pip install pytest 
```

**To Start with ask help from pytest**
```python 
pytest -h 
```
* It will return the lot of flags and commands used for the pytest library. 

### Notes: 
* In order to use pytest you need to call your testing function prefix as `test` because it automatically recogonized by the test. 
* You can also create a py file prefix with `test` to test everything inside the file. See the [**test_main.py**](test_main.py)
* After written the test just write this command to execute the terminal `pytest`. 


```python 
pytest -v  # This will give more information about the test -v for verbose. 
pytest filename -v  # You can also specify the filename for the pytest.
pytest test_main.py::test_add  # If you want to test one sinlge funciton. 
pytest -v -k "add"  # -k for keyword, it willl execute the function contains the keyword. 
pytest -v -k "add or product"  # -k for keyword, it will execute either add or product function. 
pytest -v -k "add and product" 
pytest -v -m number  # you can use pytest decorator to mark function with anything like number, string or whatever you want! 
pytest -v -x  # -x means exit first -> If any assertion wrong it will break the overall pytest and stop the execution at the same time. 
pytest -v -x --tb=no # If you don't want to see any error in the terminal just use this tace brace command. 
pytst -v --maxfail--2 # we are expecting to occur 2 failures to exit from the testing. 
@pytest.mark.skip(reason = "do not run this functio") # If you want to skip any function to not run on pytest. 
@pytest.mark.skipif( sys.version_info < (3, 3), reason = "This is bellow 3.3")
pytest -v -s # if you want to print any print statement inside the testing function (NOTE! -> This needs to be have a print function)
pytest -q  # quiet mode 
```