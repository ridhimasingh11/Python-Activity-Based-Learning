##Algorithm

1. Start 
2. Declare team statistics.
3. Store the match results.
4. For every match, update goals scored and goals conceded.
5. Award 3 points for a win, 1 point for a draw, and 0 points for a loss.
6. Calculate goal difference.
7. Sort teams by points, goal difference, goals scored, and team name.
8. Display the final rankings.
9. Stop.

## Flowchart

#              ( START )
#                  |
#          [ Initialize team statistics ]
#                  |
#             / Read match data /
#                  |
#          [ Update goals for and against ]
#                  |
#             < Team 1 wins? >
#               /          \
#             Yes           No
#              |             |
#       [ Team 1 gets 3 ] < Team 2 wins? >
#                           /         \
#                         Yes          No
#                          |            |
#                  [ Team 2 gets 3 ] [ Both get 1 ]
#                          |            |
#                          +------+-----+
#                                 |
#                      < More matches? >
#                          /        \
#                        Yes         No
#                         |           |
#                   [ Next match ] [ Calculate goal difference ]
#                         |           |
#                         +--> LOOP  [ Sort teams by ranking rules ]
#                                         |
#                                  / Display rankings /
#                                         |
#                                      ( STOP )

##Python code

matches = [
    ("Tigers", "Eagles", 2, 1),
    ("Lions", "Tigers", 1, 1),
    ("Eagles", "Lions", 3, 0),
    ("Tigers", "Lions", 2, 0)
]

teams = ["Tigers", "Eagles", "Lions"]

# Statistics: points, goals for, goals against, goal difference
stats = {}

for team in teams:
    stats[team] = [0, 0, 0, 0]

for t1, t2, g1, g2 in matches:
    stats[t1][1] += g1
    stats[t1][2] += g2
    stats[t2][1] += g2
    stats[t2][2] += g1

    if g1 > g2:
        stats[t1][0] += 3
    elif g2 > g1:
        stats[t2][0] += 3
    else:
        stats[t1][0] += 1
        stats[t2][0] += 1

for team in teams:
    stats[team][3] = stats[team][1] - stats[team][2]

ranking = sorted(
    teams,
    key=lambda team: (
        -stats[team][0],
        -stats[team][3],
        -stats[team][1],
        team
    )
)

print("RANK TEAM POINTS GF GA GD")

for rank, team in enumerate(ranking, start=1):
    points, gf, ga, gd = stats[team]
    print(rank, team, points, gf, ga, gd)

##Output

RANK TEAM POINTS GF GA GD
1 Tigers 7 5 2 3
2 Eagles 3 4 2 2
3 Lions 1 1 6 -5