# import pytest
import logging

logging.basicConfig(level=logging.DEBUG, filename='logs.log', filemode='a',
                    format="We have next logging message: %(asctime)s:%(levelname)s - %(message)s")

logging.info("Program start working")


class Calculate:
    def add(self, *args, **kwargs):
        result = 0
        for elem in list(args) + list(kwargs.values()):
            if isinstance(elem, (int, float, bool)):
                result += elem
            else:
                try:
                    result += float(elem)
                    continue
                except (ValueError, TypeError) as ex:
                    logging.error(ex)

        return result


def devide(a, b):
    if b == 0:
        raise ValueError("Cant be zero!")
    return a / b


# @pytest.mark.parametrize("a,b,result", [
#     (2, 3, 5),
#     (5, 5, 10),
#     (1, 1, 2)
# ])
# def test_add(a, b, result):
#     assert add(a, b) == result

calc = Calculate()
calc.add('asd', 23)

logging.info("Program end working")
