from typing import Any


class Version:
    def __init__(self, version: str):
        version = version + ".0.0"
        tuple_version = tuple(i for i in version.split("."))[:3]
        self.major = int(tuple_version[0]) if tuple_version[0] != '' else 0
        self.minor = int(tuple_version[1]) if tuple_version[1] != '' else 0
        self.patch = int(tuple_version[2]) if tuple_version[2] != '' else 0
        self.version = (self.major, self.minor, self.patch)

    def __lt__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            return False
        return self.version < other.version

    def __gt__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            return False
        return self.version > other.version

    def __eq__(self, other: Any) -> bool:
        if not isinstance(other, Version):
            return False
        return self.version == other.version


def comparison_version(version_a: str, version_b: str) -> int:
    v1 = Version(version_a)
    v2 = Version(version_b)
    return int(v1 > v2) or -(v1 < v2) or 0


if __name__ == "__main__":
    print(comparison_version('1.1', '1.2'))
    print(comparison_version('1.1', '0.2'))
    print(comparison_version('1.0', '1.'))
    # assert Version("a") > Version("1.0.0")
    # assert Version("1.1,2") > Version("1.0.0")
    assert Version("1.1.2") > Version("1.0.0")
    assert Version("1.0.1") > Version("1.0.0")
    assert Version("1.0.1") == Version("1.0.1")
    assert Version("1.1.") > Version("1.0.0")
    assert Version("1.1") > Version("1.0.0")
    assert Version("1.") > Version("0.1.0")
    assert Version("1") > Version("0.1.")
    assert Version("0") == Version("0")
    assert Version("1.0.0") < Version("1.1.")
    assert Version("1.0.0") < Version("1.1")
    assert Version("0.1.0") < Version("1.")
    assert Version("0.1.") < Version("1")
    assert comparison_version('1.10', '1.1.0') == 1
    assert comparison_version('1.1', '1.1.0') == 0
    assert comparison_version('1.0', '1.1.0') == -1
    assert comparison_version('1.1', '1.1.') == 0
    assert comparison_version('1', '0') == 1
    assert comparison_version('1.10', '1.1.0') == 1
