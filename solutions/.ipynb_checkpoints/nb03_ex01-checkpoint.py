lichess_recipe = ml.Recipe(
    ml.DropZeroVariance(ml.everything()),
    ml.Drop(ml.string()),
    ml.Cast(ml.everything(), "float64")
)