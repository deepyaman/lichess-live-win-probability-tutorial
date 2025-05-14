expr = games_selected_columns.mutate(
    winner_margin=games_selected_columns.result.cases(
        (
            "0-1",
            games_selected_columns.black_rating - games_selected_columns.white_rating,
        ),
        (
            "1-0",
            games_selected_columns.white_rating - games_selected_columns.black_rating,
        ),
    )
).order_by(_.winner_margin)