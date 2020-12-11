def game_summary(game_name, game_console, game_year, game_genre, game_publisher):
    if str(game_year) == "nan":
        string = f"{game_name} is an incredible {game_genre} game for {game_console} published by {game_publisher}."
    else:
        game_year = int(game_year)
        string = f"{game_name} is an incredible {game_genre} game for {game_console}. It was published in {game_year} by {game_publisher}."
    return string

