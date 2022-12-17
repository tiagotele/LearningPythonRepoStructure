import json


class Partner:
    def __init__(self, name, company):
        self.name = name
        self.company = company


class Person:
    def __init__(self, file_path) -> None:
        if file_path is None:
            raise AttributeError("Required argument file_path")
        self.file_path = file_path
        self.partners = []
        self._parse_principal()

    def _parse_principal(self):
        p = json.load(open(self.file_path))
        self.name = p["name"]
        self.company_name = p["company"]
        self._parse_partner(p["partners"])

    def _parse_partner(self, partners_list):
        for p in partners_list:
            partner = Partner(name=p.get("name"), company=p.get("company"))
            self.partners.append(partner)
