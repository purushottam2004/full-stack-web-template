"""Seed data for auth users and public.users profiles."""

SEED_USERS = [
    {
        "email": "seed_user@gmail.com",
        "password": "password123",
        "user_metadata": {"name": "Seed User"},
        "profile": {
            "username": "seed_user",
            "display_name": "Seed User",
            "full_name": "Seed User",
        },
    },
    {
        "email": "test@example.com",
        "password": "password123",
        "user_metadata": {"name": "Test User"},
        "profile": {
            "username": "test_user",
            "display_name": "Test User",
            "full_name": "Test User",
        },
    },
]


def seed_user_emails() -> list[str]:
    return [user["email"] for user in SEED_USERS]