from random import randint, sample
from string import ascii_letters
MAX_SERIAL_NUMBER_LENGTH = 6
class ExampleGenerator:
    """
    A simple python class that allows teachers
    to create random files for exercises with just a dictionary.
    The dictionary should be structured like this:
    {
        "header name 1": "header 1's type"
        ...
        "header name n": "header n's type"
    }
    Where header's type could be one of these:
    "str" -> a random string generated with ascii letters
    "serial" -> random serial numbers that starts with zeros
    "number" -> random numbers between 1 and 100_000
    """
    default_name = "sample"
    default_type = "txt"
    default_samples = 100_000
    default_sep = " "

    def __init__(self: __module__, 
                fields: dict[str, str], 
                name: str = default_name, 
                file_type: str = default_type,
                samples: int = default_samples, 
                sep: str = default_sep) -> __module__:
        self._fields: dict[str, str] = fields
        self._file_name: str = f"{name}.{file_type}"
        self._samples: int = samples
        self._sep = sep
    
    def generate_file(self: __module__) -> None:
        headers = tuple(self._fields.keys())
        with open(self._file_name, 'w') as file:
            file.write(self._sep.join(headers) + '\n')
            for i in range(self._samples):
                sample_line = []
                for _, type in self._fields.items():
                    sample_line.append(self._create_sample(type))
                line = self._sep.join(sample_line)
                file.write(line + '\n')

    def _create_sample(self: __module__, type: str) -> str:
        match type:
            case "str":
                return self.__generate_str_sample()
            case "serial":
                return self.__generate_serial_sample()
            case "number":
                return self.__generate_number_sample()

    def __generate_str_sample(self: __module__):
        return "".join(sample(ascii_letters, 5))

    def __generate_serial_sample(self: __module__):
        serial_number = f"{randint(1, 10_000)}"
        return serial_number.zfill(MAX_SERIAL_NUMBER_LENGTH)

    def __generate_number_sample(self: __module__):
        return str(randint(1, 100_000))
