clock = (
    moves_with_parsed_clock.hours.try_cast(int) * 3600
    + moves_with_parsed_clock.minutes.try_cast(int) * 60
    + moves_with_parsed_clock.seconds.try_cast(float)
)
clock