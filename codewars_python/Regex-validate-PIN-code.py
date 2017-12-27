def validate_pin(pin):
    if pin.isdigit() and (pin.__len__() == 4 or pin.__len__() == 6):
        return True
    return False