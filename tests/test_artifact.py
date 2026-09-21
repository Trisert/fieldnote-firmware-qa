from pathlib import Path
import unittest
import zipfile

ROOT = Path(__file__).parents[1]


class ArtifactTests(unittest.TestCase):
    def test_landing_page_has_real_offer_and_compliance_copy(self):
        page = (ROOT / "site" / "index.html").read_text()
        self.assertIn("STM32 Embedded Firmware QA Starter Kit", page)
        self.assertIn("No certification", page)
        self.assertIn("checkout-url", page)
        self.assertIn("free", page.lower())

    def test_kit_has_the_core_deliverables(self):
        required = [
            "kit/README.md",
            "kit/checklists/firmware-qa-checklist.md",
            "kit/templates/requirements-traceability.csv",
            "kit/templates/test-plan.md",
            "kit/templates/bug-report.yml",
            "kit/templates/issue-template.md",
            "kit/templates/ci-stm32.yml",
            "kit/examples/README.md",
            "kit/LICENSE",
        ]
        for relative in required:
            with self.subTest(relative=relative):
                self.assertTrue((ROOT / relative).is_file())

    def test_public_sample_does_not_expose_private_repo_details(self):
        sample = (ROOT / "site" / "sample-checklist.md").read_text()
        self.assertNotIn("/home/hermes", sample)
        self.assertNotIn("/root/", sample)
        self.assertNotIn("JOS", sample)

    def test_bundle_exists_and_contains_required_files(self):
        bundle = ROOT / "dist" / "embedded-firmware-qa-starter-kit-v0.1.0.zip"
        self.assertTrue(bundle.is_file())
        with zipfile.ZipFile(bundle) as archive:
            names = set(archive.namelist())
        self.assertIn("embedded-firmware-qa-starter-kit/README.md", names)
        self.assertIn("embedded-firmware-qa-starter-kit/templates/ci-stm32.yml", names)

    def test_preview_pages_inline_styles_for_file_preview(self):
        for relative in ["site/index.html", "site/kit-preview.html"]:
            with self.subTest(relative=relative):
                page = (ROOT / relative).read_text()
                self.assertIn("<style>", page)
                self.assertIn("--bg: #0b0e12", page)


if __name__ == "__main__":
    unittest.main()
