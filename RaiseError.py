class RaiseError:
    def __init__(self):
        pass 

    def excited_error(self):
        while True:
            try:
                excited = input.lower().strip()
                print(type(excited))
                if excited not in ['y','n']:
                    raise ValueError("Please give a valid answer: 'Y' or 'N'.")
            except ValueError as e:
                print(e)
                continue
            else:
                break
