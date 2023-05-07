from random import randint, sample
from string import ascii_letters

class ExampleGenerator:
    
    def __init__(self: __module__, fields: dict[str, str], name: str, file_type: str, samples: int, sep: str = " ") -> None:
        self._fields: dict[str, str] = fields
        self._file_name: str = f"{name}.{file_type}"
        self._serial_number: int = randint(1, 100_000)
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
                return "".join(sample(ascii_letters, 5))
            case "serial":
                return str(self._serial_number + 1)
            case "number":
                return str(randint(1, 100_000_000))
