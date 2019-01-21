from unittest import TestCase

from semantics import analyze_command


class TestSemantics(TestCase):
    def test_analyze_splits_to_and_from_correctly(self):
        command = "rondo ofiar katynia w kierunku miasteczko studenckie AGH"

        self.assertEqual(
            analyze_command(command),
            ("rondo ofiar katynia", "miasteczko studenckie AGH"),
        )

    def test_analyze_recognizes_numbers(self):
        command = "rondo ofiar katynia w kierunku obozowa dwadzieścia sześć"

        self.assertEqual(
            analyze_command(command),
            ("rondo ofiar katynia", "obozowa 26"),
        )

    def test_analyze_recognizes_multiple_numbers(self):
        command = "radzikowskiego sto czterdzieści w kierunku obozowa dwadzieścia sześć"

        self.assertEqual(
            analyze_command(command),
            ("radzikowskiego 140", "obozowa 26"),
        )
