#homework_04_ready

team: list[dict] = [
    {"name": "John", "age": 20, "number": 1},
    {"name": "Mark", "age": 33, "number": 3},
    {"name": "Cavin", "age": 17, "number": 12},
]


def show_players(players: list[dict]) -> None:
    for member in team:
        print(member)
    """This function should print all players to the client"""



def add_player(num: int, name: str, age: int) -> None:
    team.append({"name": name, "age": age, "number":num})
    """This function adds the new player."""


def remove_player(players: list[dict], num: int) -> None:
    for player in players:
        if player['number'] == num:
            players.remove(player)
            break
    """This function removes the player by his/her number."""


def main():
    show_players(team)

    add_player(num=17, name="Cris", age=31)
    add_player(num=17, name="Bob", age=39)
    remove_player(players=team, num=17)

    show_players(team)



if __name__ == "__main__":
    main()
else:
    raise SystemExit("This module in only for running")