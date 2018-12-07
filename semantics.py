import re


def analyze_command(command):
    delimiters = "do", "w kierunku", "kierunku"

    for delimiter in delimiters:
        if delimiter in command:
            start, destination = command.split(delimiter)
            return start, destination


def cleanup_direction(direction):
    pass


class CommandPattern:
    command: str

    def get_start(self):
        return re.search(self.pattern, self.command).groupdict().get("start", None)

    def get_destination(self):
        return re.search(self.pattern, self.command).groupdict().get("destination", None)

    def is_valid(self):
        return re.match(self.pattern, self.command)


class BothDirectionsSpecified(CommandPattern):
    delimiter: str

    @property
    def pattern(self):
        return r"(?P<start>.+){delimiter}(?P<destination>.+)".format(delimiter=self.delimiter)


class WKierunku(BothDirectionsSpecified):
    delimiter = "w kierunku"


class Do(BothDirectionsSpecified):
    delimiter = "do"
