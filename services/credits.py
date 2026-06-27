from services.database import connection, cursor

FREE_CREDITS = 3


def initialize_user(user_id: int):
    cursor.execute(
        """
        SELECT *
        FROM users
        WHERE user_id = ?
        """,
        (user_id,)
    )

    user = cursor.fetchone()

    if user is None:
        cursor.execute(
            """
            INSERT INTO users (user_id, credits)
            VALUES (?, ?)
            """,
            (user_id, FREE_CREDITS)
        )
        connection.commit()


def get_balance(user_id: int) -> int:
    initialize_user(user_id)

    cursor.execute(
        """
        SELECT credits
        FROM users
        WHERE user_id = ?
        """,
        (user_id,)
    )

    result = cursor.fetchone()

    return result[0] if result else 0


def has_credits(user_id: int) -> bool:
    return get_balance(user_id) > 0


def deduct_credits(user_id: int) -> bool:
    initialize_user(user_id)

    if get_balance(user_id) <= 0:
        return False

    cursor.execute(
        """
        UPDATE users
        SET credits = credits - 1
        WHERE user_id = ? AND credits > 0
        """,
        (user_id,)
    )

    connection.commit()

    return True


def add_credits(user_id: int, amount: int):
    initialize_user(user_id)

    cursor.execute(
        """
        UPDATE users
        SET credits = credits + ?
        WHERE user_id = ?
        """,
        (amount, user_id)
    )

    connection.commit()