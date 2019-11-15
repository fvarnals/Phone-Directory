import py, pytest
import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../src')

from phonedirectory import PhoneDirectory

string = ("/+1-541-754-3010 156 Alphand_St. <J Steeve>\n 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;\n"
"+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573\n")

def test_initialization():
    try:
        phone_directory = PhoneDirectory(string)
    except:
        pytest.fail("Failed to initialize PhoneDirectory object")

def test_entries():
    phone_directory = PhoneDirectory(string)
    assert phone_directory.entries == ["/+1-541-754-3010 156 Alphand_St. <J Steeve>",
    " 133, Green, Rd. <E Kustur> NY-56423 ;+1-541-914-3010;", "+1-541-984-3012 <P Reed> /PO Box 530; Pollocksville, NC-28573", ""]
