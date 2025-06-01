def count_alphanumeric(mystring):
    alphanumeric_count = 0
    for char in mystring:
        if char.isalnum():
            alphanumeric_count += 1
    return alphanumeric_count


if __name__ == "__main__":
    example_string = "Hello World! 123"
    print(f"Number of alphanumeric characters: {count_alphanumeric(example_string)}")
