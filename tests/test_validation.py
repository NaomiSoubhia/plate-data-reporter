from functions import isValidPlate

def test_valid_plate():
    assert isValidPlate("ABC123")


def test_invalid_plate_letters():
    assert not isValidPlate("AB123")


def test_invalid_plate_numbers():
    assert not isValidPlate("ABC12")


def test_empty_plate():
    assert not isValidPlate("")
