from environs import Env


env = Env()
env.read_env()

CACHALOT_ENABLED = env.bool("CACHALOT_ENABLED")
CACHALOT_ONLY_CACHABLE_TABLES = env.list("CACHALOT_ONLY_CACHABLE_TABLES", [])
CACHALOT_MODE = env.str("CACHALOT_MODE", "default")
SWAGGER_ENABLE = env.bool("SWAGGER_ENABLE", False)


def install_cachalot():
    global CACHALOT_ONLY_CACHABLE_TABLES
    global CACHALOT_MODE

    if CACHALOT_MODE == "full":
        CACHALOT_ONLY_CACHABLE_TABLES = []

    elif CACHALOT_ONLY_CACHABLE_TABLES:
        # Please avoid to add tables with more than 50 modifications per minute
        # to this list, as described here:
        # https://django-cachalot.readthedocs.io/en/latest/limits.html
        CACHALOT_ONLY_CACHABLE_TABLES = CACHALOT_ONLY_CACHABLE_TABLES
    else:
        CACHALOT_ONLY_CACHABLE_TABLES = [
            "database_user",
            "django_content_type",
            "database_room",
        ]

    CACHALOT_TIMEOUT = env.int("CACHALOT_TIMEOUT", 60 * 60 * 24 * 7)
