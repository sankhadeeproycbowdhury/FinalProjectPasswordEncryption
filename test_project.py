from project import check_arg,get_dob,get_key,encrypt
import pytest

def test_check_arg():
    with pytest.raises(SystemExit):
         check_arg()


def test_get_dob():
    assert get_dob("12/12/2003") == "12122003"
    assert get_dob("24/12/2004") == "24122004"
    with pytest.raises(SystemExit):
         get_dob("12/13/2003")
         get_dob("12.12.2004")
         get_dob("12/2/2004")


def test_get_key():
    assert get_key("sasasasa","11111111") == "11111111"
    assert get_key("sasa","24122003") == "2412"
    assert get_key("1234qwerty","12122005") == "1212200512"

def test_encrypt():
     assert encrypt("12345","11111") == "23456"
     assert encrypt("1234qwer","24122003") == "3646sweu"
     assert encrypt("12345qwerty@#","2412200324122") == "36467qwhtxzB%"


