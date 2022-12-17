import json
from src.json_parsing.person_schema import Person
import pytest


@pytest.fixture
def create_simple_person():
    file_path = "src/json_parsing/sample_data/sample_person.json"
    person = Person(file_path)
    return person


def test_person_exists(create_simple_person):
    assert create_simple_person is not None


def test_person_need_json_file_as_parameters():
    with pytest.raises(AttributeError):
        person = Person(None)


def test_person_company_is_optional_value(create_simple_person):
    assert create_simple_person.company_name is not None
    create_simple_person.company_name = None
    assert create_simple_person.company_name is None


def test_person_has_required_fields(create_simple_person):
    assert create_simple_person.name is not None
    assert len(create_simple_person.name) > 0
    assert len(create_simple_person.partners) > 0
    for partner in create_simple_person.partners:
        assert partner.name is not None
        assert len(partner.name) > 0
