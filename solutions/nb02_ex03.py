clock = (
    moves_with_parsed_clock.hours.cast(int) * 3600
    + moves_with_parsed_clock.minutes.cast(int) * 60
    + moves_with_parsed_clock.seconds.cast(float)
)
clock