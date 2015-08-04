from unittest import main, TestCase


class Price:
    def get_amount(self, days_rented):
        pass

    def get_points(self, days_rented):
        return 1


class RegularPrice(Price):
    def get_amount(self, days_rented):
        this_amount = 2
        if days_rented > 2:
            this_amount += (days_rented - 2) * 1.5
        return this_amount


class NewReleasePrice(Price):
    def get_amount(self, days_rented):
        return days_rented * 3

    def get_points(self, days_rented):
        return (days_rented > 1) + super().get_points(days_rented)


class ChildrensPrice(Price):
    def get_amount(self, days_rented):
        this_amount = 1.5
        if days_rented > 3:
            this_amount += (days_rented - 3) * 1.5
        return this_amount


class Movie:
    REGULAR = "RegularPrice"
    NEW_RELEASE = "NewReleasePrice"
    CHILDRENS = "ChildrensPrice"

    def __init__(self, title, price_code):
        self.title = title
        self.set_price(price_code)

    def get_price_code(self):
        return self.price_code

    def get_title(self):
        return self.title

    def set_price(self, price_code):
        self.price = globals()[price_code]()

    def get_amount(self, days_rented):
        return self.price.get_amount(days_rented)

    def get_points(self, days_rented):
        return self.price.get_points(days_rented)

    def get_record(self, days_rented):
        return "\t"+self.title+"\t"+str(self.get_amount(days_rented))+"\n"


class Rental:
    def __init__(self, movie, days_rented):
        self.movie = movie
        self.days_rented = days_rented

    def get_days_rented(self):
        return self.days_rented

    def get_movie(self):
        return self.movie

    def get_amount(self):
        return self.movie.get_amount(self.days_rented)

    def get_points(self):
        return self.movie.get_points(self.days_rented)

    def get_record(self):
        return self.movie.get_record(self.days_rented)


class Customer:
    def __init__(self, name):
        self.name = name
        self.rentals = []

    def add_rental(self, rental):
        self.rentals.append(rental)

    def get_name(self):
        return self.name

    def statement(self):
        total_amount = sum(map(lambda x: x.get_amount(), self.rentals))
        total_points = sum(map(lambda x: x.get_points(), self.rentals))
        total_record = "Rental Record for " + self.get_name() + "\n"
        total_record += "".join(map(lambda x: x.get_record(), self.rentals))
        total_record += "Amount owed is " + str(total_amount) + "\n"
        total_record += "You earned " + str(total_points) + \
            " frequent renter points"
        return total_record


class MyUnitTests(TestCase):
    def test_1(self):
        x = Customer("Penelope")
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "Amount owed is 0\n" +
            "You earned 0 frequent renter points")

    def test_2(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane", Movie.REGULAR), 2))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "Amount owed is 2\n" +
            "You earned 1 frequent renter points")

    def test_3(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane",     Movie.REGULAR), 2))
        x.add_rental(Rental(Movie("Red River", Movie.REGULAR), 5))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "\tRed River\t6.5\n" +
            "Amount owed is 8.5\n" +
            "You earned 2 frequent renter points")

    def test_4(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane",     Movie.REGULAR),     2))
        x.add_rental(Rental(Movie("Red River", Movie.REGULAR),     5))
        x.add_rental(Rental(Movie("Giant",     Movie.NEW_RELEASE), 1))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "\tRed River\t6.5\n" +
            "\tGiant\t3\n" +
            "Amount owed is 11.5\n" +
            "You earned 3 frequent renter points")

    def test_5(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane",     Movie.REGULAR),     2))
        x.add_rental(Rental(Movie("Red River", Movie.REGULAR),     5))
        x.add_rental(Rental(Movie("Giant",     Movie.NEW_RELEASE), 1))
        x.add_rental(Rental(Movie("2001",      Movie.NEW_RELEASE), 3))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "\tRed River\t6.5\n" +
            "\tGiant\t3\n" +
            "\t2001\t9\n" +
            "Amount owed is 20.5\n" +
            "You earned 5 frequent renter points")

    def test_6(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane",       Movie.REGULAR),     2))
        x.add_rental(Rental(Movie("Red River",   Movie.REGULAR),     5))
        x.add_rental(Rental(Movie("Giant",       Movie.NEW_RELEASE), 1))
        x.add_rental(Rental(Movie("2001",        Movie.NEW_RELEASE), 3))
        x.add_rental(Rental(Movie("Big Country", Movie.CHILDRENS),   3))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "\tRed River\t6.5\n" +
            "\tGiant\t3\n" +
            "\t2001\t9\n" +
            "\tBig Country\t1.5\n" +
            "Amount owed is 22.0\n" +
            "You earned 6 frequent renter points")

    def test_7(self):
        x = Customer("Penelope")
        x.add_rental(Rental(Movie("Shane",       Movie.REGULAR),     2))
        x.add_rental(Rental(Movie("Red River",   Movie.REGULAR),     5))
        x.add_rental(Rental(Movie("Giant",       Movie.NEW_RELEASE), 1))
        x.add_rental(Rental(Movie("2001",        Movie.NEW_RELEASE), 3))
        x.add_rental(Rental(Movie("Big Country", Movie.CHILDRENS),   3))
        x.add_rental(Rental(Movie("Spartacus",   Movie.CHILDRENS),   5))
        self.assertEqual(
            x.statement(),
            "Rental Record for Penelope\n" +
            "\tShane\t2\n" +
            "\tRed River\t6.5\n" +
            "\tGiant\t3\n" +
            "\t2001\t9\n" +
            "\tBig Country\t1.5\n" +
            "\tSpartacus\t4.5\n" +
            "Amount owed is 26.5\n" +
            "You earned 7 frequent renter points")

if __name__ == "__main__":
    main()

""" #pragma: no cover
% coverage3 run --branch Store1.py
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK



% coverage3 report -m
Name     Stmts   Miss Branch BrMiss  Cover   Missing
----------------------------------------------------
Store1      99      0     17      2    98%
"""
