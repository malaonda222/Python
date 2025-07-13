def print_info(**kwargs):
    if kwargs:
        print("Informazioni:")
        for key, value in kwargs.items():
            print(f"{key}: {value}")
    else:
        print("Nessuna informazione")

print_info(Name="Alice", Age=30, City="Florence")

