from chess.pgn import CLOCK_REGEX

moves_with_parsed_clock = (
    moves.alias("moves")
    .sql(
        f"""
        SELECT
          *,
          REGEXP_EXTRACT(
            comment,
            '{CLOCK_REGEX.pattern}',
            ['prefix', 'hours', 'minutes', 'seconds', 'suffix']
          ) AS clock
        FROM moves
        """
    )
    .unpack("clock")
)
moves_with_parsed_clock