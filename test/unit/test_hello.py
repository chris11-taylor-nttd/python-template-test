import pytest

from hello import hello


class TestHello:
    def test_hello_no_arguments(self):
        """Test the happy path of the main function, where no arguments are passed."""
        assert hello.main() == "Hello python-template-test!"

    @pytest.mark.parametrize("name", ["Alice", "Bob", "Charlie"])
    def test_hello_name(self, name):
        """Test the happy path of the main function, where a person is greeted.

        Args:
            name (_type_): Name of the person to greet.
        """
        assert hello.main(name) == f"Hello {name}!"

    @pytest.mark.parametrize("not_a_string", [None, False, -1, list(), dict(), set()])
    def test_hello_failure(self, not_a_string):
        """Tests the main function with a non-string argument expecting a failure.

        Args:
            not_a_string (_type_): Any non-string value.
        """
        with pytest.raises(NotImplementedError):
            hello.main(not_a_string)
