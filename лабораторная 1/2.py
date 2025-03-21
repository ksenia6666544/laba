players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Определяем общее количество игроков
total_players = len(players)
print(f"Общее количество игроков: {total_players}")

# Разделяем игроков на две равные команды
team_size = total_players // 2
team1 = players[:team_size]
team2 = players[team_size:]

# Распечатываем каждую команду
print("Команда 1:", team1)
print("Команда 2:", team2)
