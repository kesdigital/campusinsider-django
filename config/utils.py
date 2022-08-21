from decouple import config


def get_environment() -> str:
    environment: str = config("ENVIRONMENT", default="production")
    return environment
