"""
This contains the classes for parsing the input from the Google Hash Code
pizza problem.
"""

class Customer:
    """
    This defines a customer by the ingredients that one likes and dislikes.
    """
    def __init__(
        self,
        n_likes: int,
        likes: tuple,
        n_dislikes: int,
        dislikes: tuple
    ):
        """
        Initializes a user and defines its attributes.

        Arguments:
            n_likes (int): number of ingredients that the customer likes.
            likes (tuple[str]): list of ingredients that the customer likes.
            n_dislikes (int): number of ingredients that the customer dislikes.
            dislikes (tuple[str]): list of ingredients that the customer dislikes.

        Note:
            Although n_likes and n_dislikes could be obtained from the likes and dislikes,
            we are not verifying the input file and just reporting its contents here.
        """
        self.n_likes = n_likes
        self.likes = likes
        self.n_dislikes = n_dislikes
        self.dislikes = dislikes

    def __repr__(self):
        """
        Defines the string representation of the user, providing information
        about its attributes.
        """
        return f"""
            <Customer>:
            likes {self.n_likes} ingredients: {self.likes}
            dislikes {self.n_dislikes} ingredients: {self.dislikes}
        """


class ParsedContents:
    """
    Parses the contents of an input file into an object with the attributes:
    filename (str), ingredients (set[str]), likes (set[set]), dislikes(set[str]).
    """
    def __init__(self, filename: str):
        """
        Instantiates ParsedContents.
        Reads and parse the contents of the filename.

        Arguments:
            filename (str): local (path to and) input file name.
        """
        self.filename = filename
        self.ingredients = set()
        self.likes = set()
        self.dislikes = set()
        self.read_file()

    def read_file(self):
        """
        Reads the content of the file.
        Sets the attributes:
            n_customers (int)
            ingredients (set[str])
        """

        with open(self.filename, 'r') as content:
            lines = content.readlines()
            n_customers =  int(lines[0].strip())
            self.n_customers = n_customers

        customers = []
        ingredients = set()
        for index in range(self.n_customers):
            customers.append(
                self.form_customer(
                    lines[1 + 2 * index],
                    lines[2 + 2 * index]))
        self.customers = tuple(customers)

    @staticmethod
    def read_line(line):
        tokens = line.split()
        if len(tokens) == 1 and tokens[0] == '0':
            return (0, set())
        else:
            return (int(tokens[0]), set(tokens[1:]))

    def form_customer(self, like_line, dislike_line):
        n_likes, likes = self.read_line(like_line)
        self.ingredients.update(likes)
        self.likes.update(likes)
        n_dislikes, dislikes = self.read_line(dislike_line)
        self.ingredients.update(dislikes)
        self.dislikes.update(dislikes)
        return Customer(
            n_likes=n_likes,
            likes=likes,
            n_dislikes=n_dislikes,
            dislikes=dislikes)
