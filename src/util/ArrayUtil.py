class ArrayUtil:

    @staticmethod
    def find_max(numbers):
        max_element = numbers[0]
        for element in numbers:
            if element < 0:
                element = element * -1
            if element > max_element:
                max_element = element
        return max_element
