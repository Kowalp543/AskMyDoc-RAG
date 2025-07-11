import os
import pytest


@pytest.fixture(autouse=True)
def set_env_vars_for_tests():

    os.environ["ENV_FILE"] = ".env.test"
    yield
    os.environ.pop("ENV_FILE", None)
