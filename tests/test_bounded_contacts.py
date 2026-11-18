import unittest

from bounded_contacts import extract_emails


class ContactExtractionTest(unittest.TestCase):
    def test_extracts_explicit_text_and_mailto_without_duplicates(self):
        markup = """
        <div>
          <a href="mailto:kontakt@studio.example?subject=Oferta">Napisz</a>
          Kontakt: KONTAKT(at)studio.example
          <p>Biuro: biuro&#64;poradnia.example</p>
          <p>Pomoc: SUPPORT@operacje.example</p>
          <script>const fake = "internal@hidden.example";</script>
        </div>
        """
        self.assertEqual(extract_emails(markup), [
            "biuro@poradnia.example",
            "kontakt@studio.example",
            "support@operacje.example",
        ])

    def test_does_not_construct_an_address_from_a_company_site(self):
        self.assertEqual(extract_emails("Firma: Pracownia (https://studio.example)."), [])
