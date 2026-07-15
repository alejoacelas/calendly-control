import importlib.machinery
import importlib.util
import json
import os
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


SCRIPT = Path(__file__).resolve().parents[1] / "calendly"
loader = importlib.machinery.SourceFileLoader("calendly_cli", str(SCRIPT))
spec = importlib.util.spec_from_loader(loader.name, loader)
calendly = importlib.util.module_from_spec(spec)
loader.exec_module(calendly)


class CliTests(unittest.TestCase):
    def test_safe_path_rejects_absolute_urls_and_traversal(self):
        for value in ("https://example.com/users/me", "users/me", "/users/../secrets"):
            with self.subTest(value=value), self.assertRaises(calendly.CliError):
                calendly.safe_path(value)

    def test_api_base_requires_https_origin(self):
        for value in ("http://api.calendly.com", "https://api.calendly.com/v2", "not-a-url"):
            with self.subTest(value=value), patch.dict(os.environ, {"CALENDLY_API_BASE": value}):
                with self.assertRaises(calendly.CliError):
                    calendly.api_base()

    def test_custom_api_base_requires_explicit_opt_in(self):
        with patch.dict(os.environ, {"CALENDLY_API_BASE": "https://example.com"}, clear=False):
            os.environ.pop("CALENDLY_ALLOW_CUSTOM_API_BASE", None)
            with self.assertRaisesRegex(calendly.CliError, "protect the token"):
                calendly.api_base()

    def test_parse_query_preserves_equals_in_values(self):
        self.assertEqual(calendly.parse_query(["a=b=c", "x=y"]), {"a": "b=c", "x": "y"})

    def test_validate_plan_rejects_delete_without_explicit_flag(self):
        plan = {"operations": [{"method": "DELETE", "path": "/event_types/123"}]}
        with self.assertRaisesRegex(calendly.CliError, "destructive"):
            calendly.validate_plan(plan)

    def test_validate_plan_accepts_patch(self):
        operation = {"method": "PATCH", "path": "/event_types/123", "body": {"slug": "intro"}}
        self.assertEqual(calendly.validate_plan({"operations": [operation]}), [operation])

    def test_preview_does_not_make_request(self):
        plan = {"operations": [{"method": "PATCH", "path": "/event_types/123", "body": {"slug": "intro"}}]}
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "plan.json"
            path.write_text(json.dumps(plan), encoding="utf-8")
            with patch.object(calendly, "request") as request:
                calendly.apply_plan(path, execute=False)
                request.assert_not_called()

    def test_redact_removes_nested_tokens(self):
        payload = {"token": "secret", "nested": {"access_token": "also-secret", "name": "kept"}}
        self.assertEqual(
            calendly.redact(payload),
            {"token": "[REDACTED]", "nested": {"access_token": "[REDACTED]", "name": "kept"}},
        )


if __name__ == "__main__":
    unittest.main()
