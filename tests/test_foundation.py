import unittest
from unittest.mock import patch

from a2_bridge.config import Settings
from a2_bridge.domain.models import EngineeringObject
from a2_bridge.services.exchange import preview_exchange


class FoundationTests(unittest.TestCase):
    def test_missing_configuration_fails(self):
        with patch.dict("os.environ", {}, clear=True):
            with self.assertRaises(ValueError):
                Settings.from_env()

    def test_valid_configuration(self):
        with patch.dict("os.environ", {
            "A2_AVEVA_BASE_URL": "https://aveva.example.invalid/",
            "A2_ARAS_BASE_URL": "https://aras.example.invalid/Innovator/",
        }, clear=True):
            settings = Settings.from_env()
            self.assertEqual(settings.aras_base_url, "https://aras.example.invalid/Innovator")

    def test_insecure_or_credential_urls_fail(self):
        for url in ("http://example.invalid", "https://user:secret@example.invalid", "https://[", "https://example.invalid:bad"):
            with self.subTest(url=url), patch.dict("os.environ", {
                "A2_AVEVA_BASE_URL": url,
                "A2_ARAS_BASE_URL": "https://aras.example.invalid",
            }, clear=True):
                with self.assertRaises(ValueError):
                    Settings.from_env()

    def test_preview_collects_source_objects(self):
        item = EngineeringObject("sample-1", "example")

        class Source:
            def read_objects(self):
                yield item

        self.assertEqual(preview_exchange(Source()), [item])
