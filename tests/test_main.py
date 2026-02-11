from app.main import hello_world


def test_hello_world():
    """
    Test that the serverless function returns the expected string.
    """
    assert hello_world() == "Hello, CI/CD!"
