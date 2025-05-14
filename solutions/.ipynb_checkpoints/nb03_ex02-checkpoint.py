xgb_steps = (
    ml.Mutate(
        relative_clock_diff=(_.white_clock - _.black_clock)
        / (_.base_time + _.increment * NUM_MOVES)
    ),
    ml.Mutate(elo_diff=_.white_elo - _.black_elo),
)