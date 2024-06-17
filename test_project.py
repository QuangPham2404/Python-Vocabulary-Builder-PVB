import pytest 
import csv
from project import make_word_list, make_type_list, make_definition_list, in_sheet


def test_make_word_list():
    assert make_word_list() == ['word', 'attain', 'refute', 'undergird']


def test_make_type_list():
    assert make_type_list() == ['type', 'verb', 'verb', 'verb']


def test_make_definition_list():
    assert make_definition_list() == ['definition', 'to succeed in getting something', 'to prove something is wrong', 'to support something by forming a strong base for it']


def test_in_sheet():
    assert in_sheet("repulse") == False
    assert in_sheet("attain") == True