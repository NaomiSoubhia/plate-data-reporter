from functions import isValidPlate

def test_valid_plate():
    assert isValidPlate("ABC123") == True

def test_invalid_plate_letters():
    assert isValidPlate("AB123") == False

def test_invalid_plate_numbers():
    assert isValidPlate("ABC12") == False

def test_empty_plate():
    assert isValidPlate("") == False
