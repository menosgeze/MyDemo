"""
This script contains the class in charge of grading the submission output line.
"""

class Grading:
    """
    Takes a submission line and the list of customers, and counts how many
    would like the pizza served.
    """
    def __init__(self, submission_line, customers):
        """
        Instantiates and sets attributes.

        Arguments:
            submission_line (str): space separated list of ingredients in the pizza.
            customers (list[Customer]): list of Customers in the input file.
        """
        submission_line = self.read_line(submission_line)
        self.n_ingredients = submission_line[0]
        self.ingredients = submission_line[1]
        self.grade(customers)

    @staticmethod
    def read_line(line):
        """
        Takes a line of the form:
        <number of ingredients> <ingredient1> <ingredient2> ...
        And parses the number of ingredients to an integer,
        and the list of ingredients to a tuple[str].

        Arguments:
            line (str): number of ingredients and list of ingredients
                separated by spaces.
        """
        tokens = line.split()
        if len(tokens) == 1 and tokens[0] == '0':
            return (0, tuple())
        else:
            return (int(tokens[0]), tuple(tokens[1:]))

    def grade(self, customers):
        """
        Loops over the customers and counts how many will like our pizza and
        how many will not.

        Sets the attributes: my_customers (will like our pizza), my_leaves (won't like it),
        and grade (length of my_customers).

        Arguments:
            customers (list[Customer]): list of (potential) customers.
        """
        my_customers = []
        my_leaves = []
        for index, customer in enumerate(customers):
            if (
                customer.likes.issubset(self.ingredients)
                and customer.dislikes.isdisjoint(self.ingredients)
            ):
                my_customers.append(index)
            else:
                my_leaves.append(index)

        self.my_customers = tuple(my_customers)
        self.my_leaves = tuple(my_leaves)
        self.grade = len(my_customers)
        print(f"The grade is {self.grade}={round(100.0 * self.grade / len(customers), 2)}%")

