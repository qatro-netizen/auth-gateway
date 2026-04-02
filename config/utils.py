import os
import logging
import secrets
import string
from typing import Optional

def configure_logging(level: str = "INFO") -> None:
    """
    Configures basic logging for the application.
    """
    numeric_level = getattr(logging, level.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level}")

    logging.basicConfig(
        level=numeric_level,
        format="%(asctime)s - %(levelname)s - %(module)s - %(message)s",
    )

def generate_secret_key(length: int = 32) -> str:
    """
    Generates a cryptographically secure random secret key.

    Args:
        length: The desired length of the secret key.

    Returns:
        A string containing the generated secret key.
    """
    alphabet = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(alphabet) for _ in range(length))


def get_environment_variable(name: str, default: Optional[str] = None) -> str:
    """
    Retrieves an environment variable.

    Args:
        name: The name of the environment variable.
        default: The default value to return if the variable is not set.

    Returns:
        The value of the environment variable, or the default value if not set.

    Raises:
        ValueError: If the environment variable is not set and no default is provided.
    """
    value = os.environ.get(name)
    if value is None:
        if default is not None:
            return default
        raise ValueError(f"Environment variable {name} not set.")
    return value

def validate_email(email: str) -> bool:
  """
  Basic email validation.  Does not guarantee email exists
  but checks for a valid structure.

  Args:
    email: The email address to validate.

  Returns:
    True if the email is valid, False otherwise.
  """
  import re
  email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
  return bool(re.match(email_regex, email))