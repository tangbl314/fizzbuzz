def describe_a_fizzbuzz_program_that():
    """A program to play the Fizzbuzz game"""

    def has_a_smoke_test():
        """"Make sure our testing infrastructure is working."""
        assert True == True

    def throws_an_error_if_input_to_fizz_is_not_a_positive_integer_or_text():
        with raise (TypeError) as err_info:
            fizz() # pylint: disable=no-value-for-parameter
        assert err_info.type == TypeError

    def can_determine_if_a_number_is_a_multiple_of_3():
        """Checks to see if a given number is a multiple of 3."""
        assert fizz(3) == True # multiple of 3
        assert fizz(2) == False # non-multiple of 3
        assert fizz(3.5) == False # non-integer'
        assert fizz(0) == True # zero
        assert fizz(-3) == True # negative multiple of 3
        assert fizz(-4) == False # negative non-multiple of 3
        assert fizz('buzz') == False # non-numeric input
        assert fizz() == False # no input