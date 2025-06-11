import marimo

__generated_with = "0.13.15"
app = marimo.App()


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        # Python Errors

         When an error arises, there will be an error message with the type of error and the line the error occured on. This notebook goes over how to handle the common types of errors and exceptions in Python.
 
         I recommend looking at the [Python tutorial page](https://docs.python.org/3/tutorial/errors.html) for more information on errors. Searching for the error message directly on Google can help the debugging process if there is an error not discussed in this page. 

        ## Syntax Error

        A **SyntaxError** occurs when the syntax of your code is incorrect. 
        """
    )
    return


app._unparsable_cell(
    r"""
    if True 
    print(\"Hello World\")
    """,
    name="_"
)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        A colon is expected after the `if` statement, which arises the syntax error. The error goes away after adding the colon.
        """
    )
    return


@app.cell
def _():
    if True:
        print("Hello World")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Name Error

        A **NameError** occurs when a variable, function, or module used does not exist. When this happens, it is usually because of a spelling error. 
        """
    )
    return


@app.cell
def _(add):
    add
    return


@app.cell
def _(string):
    string(9)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Type Error 

        A **TypeError** occurs when you input an incorrect data type for an operation or function.
        """
    )
    return


@app.cell
def _():
    "abc" + 9
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In python, you cannot add strings to integers. You can add, however, an integer to an integer or a string to a string with a `+`.
        """
    )
    return


@app.cell
def _():
    9 + 9
    return


@app.cell
def _():
    "abc" + "def"
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Zero Division Error

        A **ZeroDivisionError** occurs when you try to divide by zero. To fix this, recheck your computation. 
        """
    )
    return


@app.cell
def _():
    2 / (9 * 0)
    return


@app.cell
def _():
    #code corrected to no longer divide by zero
    (2 / 9) * 0
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Value Error

        A **ValueError** occurs when an input for a function is the correct data type but is invalid in regards to the domain of the function. This is most common with mathematical operations. 
        """
    )
    return


@app.cell
def _():
    import math

    math.sqrt(-10)
    return (math,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        In the example above, you must input a positive number into the `sqrt()` function. The negative number is still an integer, but it is not in the function's domain. 
        """
    )
    return


@app.cell
def _(math):
    math.sqrt(10)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Index Error

        An **IndexError** occurs when you try to access an item in a list with an index out of bounds. 
        """
    )
    return


@app.cell
def _():
    list = [1,2,3,4,5]
    list[5]
    return (list,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The range of a list is [0, n-1], where "n" is the length of the list. So, the list `[1,2,3,4,5]` has index elements  in the range 0-4.
        """
    )
    return


@app.cell
def _(list):
    list[4]
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Module Not Found Error 

        A **ModuleNotFoundError** occurs when you try to import a module that does not exist. It is a type of **ImportError**. To fix this error, check if you have installed the module in your python environment from the terminal command-line.
        """
    )
    return


@app.cell
def _():
    import pillow
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Catching Exceptions with Try Statements 

        You can use a `try` statement to catch errors. A `try` clause includes the code you want to run that might cause an error. If no error occurs, the `try` clause runs successfully. If an error does occur, the `except` clause runs after the line in the `try` clause that caused an error.
        """
    )
    return


@app.cell
def _():
    try:
        "abc" + 9
        print("Success")
    except:
        print("Failure to execute")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        The `except` clause above can catch any type of error. However, an `except` clause can also catch a specific type of error. There can be mulptile `except` clauses in a `try` statement to catch the different types of errors. 
        """
    )
    return


@app.cell
def _(hello):
    try:
        hello
        "abc" + 9
        print("Success")
    except TypeError:
        print("TypeError failure to execute")
    except NameError:
        print("NameError failure to execute")
    return


@app.cell
def _():
    try:
        list_1 = [1, 2, 3, 4, 5]
        list_1[5]
        print('Success')
    except TypeError:
        print('TypeError failure to execute')
    except NameError:
        print('NameError failure to execute')
    except IndexError:
        print('IndexError failure to execute')
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(
        r"""
        ## Next Steps

        These are not all the errors that might come up in your coding. If another type of error occurs, you can search the error type on Google to learn more about what has caused it. As always, remember to look at the line resulting in the error for hints on what could have gone wrong!
        """
    )
    return


@app.cell
def _():
    import marimo as mo
    return (mo,)


if __name__ == "__main__":
    app.run()
