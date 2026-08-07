def main():
    """
    Main function to demonstrate the normalization of field names.
    """
    field_name = input("Enter a field name: ")
    normalized_name = normalize_field_name(field_name)
    print(f"Normalized field name: {normalized_name}")   


def normalize_field_name(name):
    """
    Normalize a field name by converting it to lowercase and replacing spaces with underscores.

    Args:
        name (str): The field name to normalize.

    Returns:
        str: The normalized field name.
    """
    return name.lower().replace(' ', '_')
main()