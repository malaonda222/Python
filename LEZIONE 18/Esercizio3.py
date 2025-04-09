try: 
    with open('example.txt', 'r') as file:
        try:
            content = file.read()
            print(content)
        except IOError as e:
            print(f"Errore nella lettura del file {e}.")

except FileNotFoundError:
    print("The file does not exist")

except IOError as e:
    print(f"An error occurred while opening the file {e}.")

