# %% [markdown]
# # Python 101
# 
# This is an optional notebook to get you up to speed with Python in case you are new to Python or need a refresher. The material here is a crash course in Python; I highly recommend the [official Python tutorial](https://docs.python.org/3/tutorial/) for a deeper dive. Consider reading [this page](https://docs.python.org/3/tutorial/appetite.html) in the Python docs for background on Python and bookmarking the [glossary](https://docs.python.org/3/glossary.html#glossary).
# 
# ## Basic data types
# ### Numbers
# Numbers in Python can be represented as integers (e.g. `5`) or floats (e.g. `5.0`). We can perform operations on them:

# %%
5 + 6

# %%
2.5 / 3

# %% [markdown]
# ### Booleans
# 
# We can check for equality giving us a Boolean:

# %%
5 == 6

# %%
5 < 6

# %% [markdown]
# These statements can be combined with logical operators: `not`, `and`, `or`

# %%
(5 < 6) and not (5 == 6)

# %%
False or True

# %%
True or False

# %% [markdown]
# ### Strings
# Using strings, we can handle text in Python. These values must be surrounded in quotes &mdash; single (`'...'`) is the standard, but double (`"..."`) works as well:

# %%
'hello'

# %% [markdown]
# We can also perform operations on strings. For example, we can see how long it is with `len()`:

# %%
len('hello')

# %% [markdown]
# We can select parts of the string by specifying the **index**. Note that in Python the 1<sup>st</sup> character is at index 0:

# %%
'hello'[0]

# %% [markdown]
# We can concatentate strings with `+`:

# %%
'hello' + ' ' + 'world'

# %% [markdown]
# We can check if characters are in the string with the `in` operator:

# %%
'h' in 'hello'

# %% [markdown]
# ## Variables
# Notice that just typing text causes an error. Errors in Python attempt to clue us in to what went wrong with our code. In this case, we have a `NameError` exception which tells us that `'hello'` is not defined. This means that [the Python interpreter](https://docs.python.org/3/tutorial/interpreter.html) looked for a **variable** named `hello`, but it didn't find one.

# %%
hello

# %% [markdown]
# Variables give us a way to store data types. We define a variable using the `variable_name = value` syntax:

# %%
x = 5
y = 7
x + y

# %% [markdown]
# The variable name cannot contain spaces; we usually use `_` instead. The best variable names are descriptive ones:

# %%
book_title = 'Hands-On Data Analysis with Pandas'

# %% [markdown]
# Variables can be any data type. We can check which one it is with `type()`, which is a **function** (more on that later):

# %%
type(x)

# %%
type(book_title)

# %% [markdown]
# If we need to see the value of a variable, we can print it using the `print()` function:

# %%
print(book_title)

# %% [markdown]
# ## Collections of Items
# 
# ### Lists
# We can store a collection of items in a list:

# %%
['hello', ' ', 'world']

# %% [markdown]
# The list can be stored in a variable. Note that the items in the list can be of different types:

# %%
my_list = ['hello', 3.8, True, 'Python']
type(my_list)

# %% [markdown]
# We can see how many elements are in the list with `len()`:

# %%
len(my_list)

# %% [markdown]
# We can also use the `in` operator to check if a value is in the list:

# %%
'world' in my_list

# %% [markdown]
# We can select items in the list just as we did with strings, by providing the index to select:

# %%
my_list[1]

# %% [markdown]
# Python also allows us to use negative values, so we can easily select the last one:

# %%
my_list[-1]

# %% [markdown]
# Another powerful feature of lists (and strings) is **slicing**. We can grab the middle 2 elements in the list:

# %%
my_list[1:3]

# %% [markdown]
# ... or every other one:

# %%
my_list[::2]

# %% [markdown]
# We can even select the list in reverse:

# %%
my_list[::-1]

# %% [markdown]
# Note: This syntax is `[start:stop:step]` where the selection is inclusive of the start index, but exclusive of the stop index. If `start` isn't provided, `0` is used. If `stop` isn't provided, the number of elements is used (4, in our case); this works because the `stop` is exclusive. If `step` isn't provided, it is 1.
# 
# We can use the `join()` method on a string object to concatenate all the items of a list into single string. The string we call the `join()` method on will be used as the separator, here we separate with a pipe (|):

# %%
'|'.join(['x', 'y', 'z'])

# %% [markdown]
# ### Tuples
# Tuples are similar to lists; however, they can't be modified after creation i.e. they are **immutable**. Instead of square brackets, we use parenthesis to create tuples:

# %%
my_tuple = ('a', 5)
type(my_tuple)

# %%
my_tuple[0]

# %% [markdown]
# Immutable objects can't be modified:

# %%
my_tuple[0] = 'b'

# %% [markdown]
# ### Dictionaries
# We can store mappings of key-value pairs using dictionaries:

# %%
shopping_list = {
    'veggies': ['spinach', 'kale', 'beets'],
    'fruits': 'bananas',
    'meat': 0    
}
type(shopping_list)

# %% [markdown]
# To access the values associated with a specific key, we use the square bracket notation again:

# %%
shopping_list['veggies']

# %% [markdown]
# We can extract all of the keys with `keys()`:

# %%
shopping_list.keys()

# %% [markdown]
# We can extract all of the values with `values()`:

# %%
shopping_list.values()

# %% [markdown]
# Finally, we can call `items()` to get back pairs of (key, value) pairs:

# %%
shopping_list.items()

# %% [markdown]
# ### Sets
# A set is a collection of unique items; a common use is to remove duplicates from a list. These are written with curly braces also, but notice there is no key-value mapping:

# %%
my_set = {1, 1, 2, 'a'}
type(my_set)

# %% [markdown]
# How many items are in this set?

# %%
len(my_set)

# %% [markdown]
# We put in 4 items but the set only has 3 because duplicates are removed:

# %%
my_set

# %% [markdown]
# We can check if a value is in the set:

# %%
2 in my_set

# %% [markdown]
# ## Functions
# We can define functions to package up our code for reuse. We have already seen some functions: `len()`, `type()`, and `print()`. They are all functions that take **arguments**. Note that functions don't need to accept arguments, in which case they are called without passing in anything (e.g. `print()` versus `print(my_string)`). 
# 
# *Aside: we can also create lists, sets, dictionaries, and tuples with functions: `list()`, `set()`, `dict()`, and `tuple()`*
# 
# ### Defining functions
# 
# We use the `def` keyword to define functions. Let's create a function called `add()` with 2 parameters, `x` and `y`, which will be the names the code in the function will use to refer to the arguments we pass in when calling it:

# %%
def add(x, y):
    """This is a docstring. It is used to explain how the code works and is optional (but encouraged)."""
    # this is a comment; it allows us to annotate the code
    print('Performing addition')
    return x + y

# %% [markdown]
# Once we run the code above, our function is ready to use:

# %%
type(add)

# %% [markdown]
# Let's add some numbers:

# %%
add(1, 2)

# %% [markdown]
# ### Return values
# We can store the result in a variable for later:

# %%
result = add(1, 2)

# %% [markdown]
# Notice the print statement wasn't captured in `result`. This variable will only have what the function **returns**. This is what the `return` line in the function definition did:

# %%
result

# %% [markdown]
# Note that functions don't have to return anything. Consider `print()`:

# %%
print_result = print('hello world')

# %% [markdown]
# If we take a look at what we got back, we see it is a `NoneType` object:

# %%
type(print_result)

# %% [markdown]
# In Python, the value `None` represents null values. We can check if our variable *is* `None`:

# %%
print_result is None

# %% [markdown]
# *Warning: make sure to use comparison operators (e.g. >, >=, <, <=, ==, !=) to compare to values other than `None`.*
# 
# ### Function arguments
# 
# *Note that function arguments can be anything, even other functions. We will see several examples of this in the text.* 
# 
# The function we defined requires arguments. If we don't provide them all, it will cause an error:

# %%
add(1)

# %% [markdown]
# We can use `help()` to check what arguments the function needs (notice the docstring ends up here):

# %%
help(add)

# %% [markdown]
# We will also get errors if we pass in data types that `add()` can't work with:

# %%
add(set(), set())

# %% [markdown]
# We will discuss error handling in the text.
# 
# ## Control Flow Statements
# Sometimes we want to vary the path the code takes based on some criteria. For this we have `if`, `elif`, and `else`. We can use `if` on its own:

# %%
def make_positive(x):
    """Returns a positive x"""
    if x < 0:
        x *= -1
    return x

# %% [markdown]
# Calling this function with negative input causes the code under the `if` statement to run:

# %%
make_positive(-1)

# %% [markdown]
# Calling this function with positive input skips the code under the `if` statement, keeping the number positive:

# %%
make_positive(2)

# %% [markdown]
# Sometimes we need an `else` statement as well:

# %%
def add_or_subtract(operation, x, y):
    if operation == 'add':
        return x + y
    else:
        return x - y

# %% [markdown]
# This triggers the code under the `if` statement:

# %%
add_or_subtract('add', 1, 2)

# %% [markdown]
# Since the Boolean check in the `if` statement was `False`, this triggers the code under the `else` statement:

# %%
add_or_subtract('subtract', 1, 2)

# %% [markdown]
# For more complicated logic, we can also use `elif`. We can have any number of `elif` statements. Optionally, we can include `else`.

# %%
def calculate(operation, x, y):
    if operation == 'add':
        return x + y
    elif operation == 'subtract':
        return x - y
    elif operation == 'multiply':
        return x * y
    elif operation == 'division':
        return x / y
    else:
        print("This case hasn't been handled")

# %% [markdown]
# The code keeps checking the conditions in the `if` statements from top to bottom until it finds `multiply`:

# %%
calculate('multiply', 3, 4)

# %% [markdown]
# The code keeps checking the conditions in the `if` statements from top to bottom until it hits the `else` statement:

# %%
calculate('power', 3, 4)

# %% [markdown]
# ## Loops
# ### `while` loops
# With `while` loops, we can keep running code until some stopping condition is met:

# %%
done = False
value = 2
while not done:
    print('Still going...', value)
    value *= 2
    if value > 10:
        done = True

# %% [markdown]
# Note this can also be written as, by moving the condition to the `while` statement:

# %%
value = 2
while value < 10:
    print('Still going...', value)
    value *= 2

# %% [markdown]
# ### `for` loops
# With `for` loops, we can run our code *for each* element in a collection:

# %%
for i in range(5):
    print(i)

# %% [markdown]
# We can use `for` loops with lists, tuples, sets, and dictionaries as well:

# %%
for element in my_list:
    print(element)

# %%
for key, value in shopping_list.items():
    print('For', key, 'we need to buy', value)

# %% [markdown]
# With `for` loops, we don't have to worry about checking if we have reached the stopping condition. Conversely, `while` loops can cause infinite loops if we don't remember to update variables.
# 
# ## Imports
# We have been working with the portion of Python that is available without importing additional functionality. The Python standard library that comes with the install of Python is broken up into several **modules**, but we often only need a few. We can import whatever we need: a module in the standard library, a 3rd-party library, or code that we wrote. This is done with an `import` statement:

# %%
import math

print(math.pi)

# %% [markdown]
# If we only need a small piece from that module, we can do the following instead:

# %%
from math import pi

print(pi)

# %% [markdown]
# *Warning: anything you import is added to the namespace, so if you create a new variable/function/etc. with the same name it will overwrite the previous value. For this reason, we have to be careful with variable names e.g. if you name something `sum`, you won't be able to add using the `sum()` built-in function anymore. Using notebooks or an IDE will help you avoid these issues with syntax highlighting.* 
# 
# ## Installing 3rd-party Packages
# 
# We can use [`pip`](https://pip.pypa.io/en/stable/reference/) or [`conda`](https://docs.conda.io/projects/conda/en/latest/commands.html) to install packages, depending on how we created our virtual environment. We will walk through the commands to create virtual environments with `conda`. The environment **MUST** be activated before installing the packages for this text; otherwise, it's possible they interfere with other projects on your machine or vice versa.
# 
# To install a package, we can use `conda install <package_name>` to download a package from the `default` [`conda`](https://docs.conda.io/projects/conda/en/latest/commands.html) channel. Optionally, we can provide a specific version to install `conda install pandas==0.23.4`. Even further, can define which channel that we install a package from for example we can install a package from the `conda-forge` channel by with `conda install -c conda-forge pandas=0.23.4`. Without that specification, we will get the most stable version. When we have many packages to install we will typically use a `environment.yml` or `requirements.txt` file: `conda env update -f environment.yml` from within your active environment or `conda env update -n ENVNAME -f environment.yml` if you are updating an update you are not actively in. 
# 
# *Note: running `conda env export ENVNAME > environment.yml` will send the list of platform-specific packages installed in the activate environment and their respective versions to the `environment.yml` file.*
# 
# 
# ## Classes
# 
# So far we have used Python as a functional programming language, but we also have the option to use it for **object-oriented programming**. You can think of a `class` as a way to group similar functionality together. Let's create a calculator class which can handle mathematical operations for us. For this, we use the `class` keyword and define **methods** for taking actions on the calculator. These methods are functions that take `self` as the first argument. When calling them, we don't pass in anything for that argument (example after this):

# %%
class Calculator:
    """This is the class docstring."""
    
    def __init__(self):
        """This is a method and it is called when we create an object of type `Calculator`."""
        self.on = False
        
    def turn_on(self):
        """This method turns on the calculator."""
        self.on = True
    
    def add(self, x, y):
        """Perform addition if calculator is on"""
        if self.on:
            return x + y
        else:
            print('the calculator is not on')

# %% [markdown]
# In order to use the calculator, we need to **instantiate** an instance or object of type `Calculator`. Since the `__init__()` method has no parameters other than `self`, we don't need to provide anything:

# %%
my_calculator = Calculator()

# %% [markdown]
# Let's try to add some numbers:

# %%
my_calculator.add(1, 2)

# %% [markdown]
# Oops!! The calculator is not on. Let's turn it on:

# %%
my_calculator.turn_on()

# %% [markdown]
# Let's try again:

# %%
my_calculator.add(1, 2)

# %% [markdown]
# We can access **attributes** on object with dot notation. In this example, the only attribute is `on`, and it is set in the `__init__()` method:

# %%
my_calculator.on

# %% [markdown]
# Note that we can also update attributes:

# %%
my_calculator.on = False
my_calculator.add(1, 2)

# %% [markdown]
# Finally, we can use `help()` to get more information on the object:

# %%
help(my_calculator)

# %% [markdown]
# ... and also for a method:

# %%
help(my_calculator.add)

# %% [markdown]
# ## Next Steps
# This was a crash course in Python. This isn't an exhaustive list of all of the features available to you.


