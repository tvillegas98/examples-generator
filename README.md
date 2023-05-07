# Example Generator

A simple Python module to create random files to help teachers with their exercises.

In order to use this module, just import it in your file and follow this guide:

```python
from example_generator import ExampleGenerator

example_generator = ExampleGenerator(
  fields = {"Header 1": "Header Type" ... }
  name = "a file name"
  file_type = "a file extension"
  samples = an_amount_of_samples
  sep = "a field separator"
)
```
All parameters are optional except `fields`, which is required to create the file.

## Disclaimer
At the moment, we just support .txt and .csv file extension.

## Next Steps
- Add time support
- Add date support
- Add datetime support
- Add json files support
