import ccwc

def test_count_bytes():
    assert ccwc.count_bytes('test.txt') == 342190, "Should be 342190"

def test_line_count():
    assert ccwc.count_lines('test.txt') == 7145, "Should be 7145"

def test_line_words():
    assert ccwc.count_words('test.txt') == 58164, "Should be 58164"

def test_line_characters():
    assert ccwc.count_characters('test.txt') == 339292, "Should be 339292"

if __name__ == "__main__":
    test_count_bytes()
    test_line_count()
    test_line_words()
    test_line_characters()
    print("Everything passed")