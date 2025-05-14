games_selected_columns.filter(
    (_.white_title == "GM") | (_.black_title == "GM")
).group_by(_.result).count()