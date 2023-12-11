class DataValidator:
    def __init__(self):
        self.valid_integers = []

    def validate_and_add_integers(self, input_list):
        for input_str in input_list:
            if self._is_valid_positive_integer(input_str):
                self.valid_integers.append(int(input_str))

        return self.valid_integers

    def _is_valid_positive_integer(self, input_str):
        try:
            number = int(input_str)
            return number > 0
        except ValueError:
            return False


# Example Usage:
user_inputs = ["12", "abc", "45", "-3", "100"]
validator = DataValidator()
valid_integers = validator.validate_and_add_integers(user_inputs)

print("Original User Inputs:", user_inputs)
print("Valid Positive Integers:", valid_integers)