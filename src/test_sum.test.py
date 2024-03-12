def test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("Python is awesome") == "Pythn s wsm"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("") == ""
    assert remove_vowels("12345") == "12345"

test_remove_vowels() test_remove_vowels():
    assert remove_vowels("Hello World") == "Hll Wrld"
    assert remove_vowels("Python is awesome") == "Pythn s wsm"
    assert remove_vowels("AEIOU") == ""
    assert remove_vowels("") == ""
    assert remove_vowels("12345") == "12345"
    assert remove_vowels("abcdefghijklmnopqrstuvwxyz") == "bcdfghjklmnpqrstvwxyz"
    assert remove_vowels("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == "BCDFGHJKLMNPQRSTVWXYZ"
    assert remove_vowels("Hello, how are you?") == "Hll, hw r y?"
    assert remove_vowels("I love programming") == " lv prgrmmng"
    assert remove_vowels("This is a test") == "Ths s tst"

test_remove_vowels()