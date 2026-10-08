from text_tools import is_palindrome


def test_level_is_palindrome():
	assert is_palindrome("level") is True


def test_python_is_not_palindrome():
	assert is_palindrome("python") is False


def test_empty_string_is_palindrome():
	assert is_palindrome("") is True
