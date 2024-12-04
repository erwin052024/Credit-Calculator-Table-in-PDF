# Credit-Calculator-Table-in-PDF

    # credit calculator
    #### Description:
    I'd like to introduce you to the credit calculator of mine with a fixed capital installment and decreasing credit installments.
    You will be asked for certain financial data in order to create a credit repayment schedule.
    The credit repayment schedule includes such components as a number of period, current credit balance, interest amount and total credit installment due for each period.
    I had tried to create this program as user-friendly as it's possible in the element of user inputs.
    I allow the program to accept some minor spelling errors with a letter s at the end of nouns in inputs.
    If you make a mistake during inputting the data asked for, you will be asked to enter this data again with the information to enter the data in the correct format.
    Remember to stick to the proper input data format. I add below additional informations about that.
    You can enter the credit amount with a comma, e.g. 100,000 or as a single number without spaces.
    Enter the annual interest rate with or without the percentage sign, e.g. 10%, 10.75, 10 percent, 10percent.
    For the credit term, you can enter it as:
    - a number of payment periods
    - a number of months, e.g., 12 months, 12months, 12m, or 12 m
    - a combination of years and months, e.g., 1 year 2 months; 1year2month; 1 y 2 m; 1y,2m
      (In this case, remember! Instead of entering 12 months, add 1 year to the credit term.) 
    After starting up the program, the introduction message is displayed to its user with some tips how to properly use it.
    The user than enters a credit amount, an annual interest rate and a credit term.
    Based on provided financial information by the user, the program is able to conduct numerical operations for example an extraction, multiplication or division.
    In the resul of this actions and thanks to the tabulate library the user is served with a complete credit payment schedule presented in a properly manner.
    Additionally the user is asked if the credit payment schedule is needed to be created as a pdf file on the desktop and if you enter "y" or "yes", your pdf file is going to be at your disposal on the desktop. Be sure to look at the top of every page because every page starts with the set up header.
    It's completely normal that a project is containded in a file called project.py, necesarry tests in test_project.py, the list of used repositories/libraries in a file requirements.txt and the description you're reading right now in README.md.
    What was interesting for me in the aspects of testing using pytest. The usage of the unittest.mock library helped me a lot because I fused inputs with functions containing them inside these functions. That's one of the additional things I've learned during constructing my final project. The patch function of the unittest.mock library allowed me to feed my functions with mock_inputs while serving them lists of side effects in the process of testing these functions. I was impressed how that worked. That was really helpful for me because I hadn't to throw out inputs outside the functions. Those of side effects that don't match up with regular expressions I created are checked by pytest but aren't given a transformation effect by functions because they force functions to continue their loops and these functions just ask for another input from the user. The testing continues to work until it catches up with a side effect that allows a function to return transformed value. What is written in assertion lines.



   
