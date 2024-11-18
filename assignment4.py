def modify_content(content):

    return content.upper()  # Modify content as needed


def main():
    # Prompt user for a filename
    filename = input("Enter the filename to read: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()

        # Modify the content
        modified_content = modify_content(content)

        # Create a new file and write the modified content
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified_content)

        print(f"The modified content has been written to {new_filename}")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist. Please check the filename and try again.")
    except PermissionError:
        print(f"Error: Permission denied for reading the file '{filename}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()
