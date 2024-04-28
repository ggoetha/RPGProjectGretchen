class RaiseError:

# Initializing function to pass onto the error

    def __init__(self):
        pass 

# Function that responds to the raise in the error ValueError if they user enters something else other than Y or N. Returns excited.

    def excited_error(self):
        while True:
            try:
                excited = input().lower().strip()
                if excited not in ['y','n']:
                    raise ValueError("Please give a valid answer: 'Y' or 'N'.")
            except ValueError as e:
                print(e)
                continue
            else:
                break
        return excited
