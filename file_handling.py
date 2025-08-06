def modify_content(content):
  
    return content.upper()

def main():
    filename = input("Enter the filename to read: ")

    try:
        with open(filename, 'r') as file:
            content = file.read()
        modified = modify_content(content)
        new_filename = f"modified_{filename}"
        with open(new_filename, 'w') as new_file:
            new_file.write(modified)

        print(f"\nModified content saved to: {new_filename}")

    except FileNotFoundError:
        print("❌ Error: The file does not exist.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
