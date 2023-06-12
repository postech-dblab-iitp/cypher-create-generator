import random
import string
import sys

def generate_random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

def generate_cypher_create(num_properties):
    properties = {}
    for _ in range(num_properties):
        key = generate_random_string(5)
        value = generate_random_string(10)
        properties[key] = value

    cypher_statement = "CREATE (n {"
    for key, value in properties.items():
        cypher_statement += f"{key}: '{value}', "
    cypher_statement = cypher_statement.rstrip(", ")
    cypher_statement += "})"

    return cypher_statement

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <num_properties>")
        sys.exit(1)

    num_properties = int(sys.argv[1])
    cypher_statement = generate_cypher_create(num_properties)
    print(cypher_statement)
