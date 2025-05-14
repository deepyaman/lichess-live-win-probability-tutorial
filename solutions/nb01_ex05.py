games_selected_columns.filter(
    (_.white_title.isnull()) & (_.black_title.isnull())
).group_by(_.result).count()
