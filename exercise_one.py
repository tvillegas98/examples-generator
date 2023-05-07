from example_generator import ExampleGenerator

headers = {"Nombre": "str", "Apellido": "str", "Padrón": "serial", "DNI": "serial"}
example_generator = ExampleGenerator(headers)
example_generator.generate_file()
