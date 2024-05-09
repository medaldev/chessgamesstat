import chess.pgn
import pandas as pd


header_list = ['Event',
 'Site',
 'Date',
 'Round',
 'White',
 'Black',
 'Result',
 'BlackElo',
 'BlackRatingDiff',
 'ECO',
 'Opening',
 'Termination',
 'TimeControl',
 'UTCDate',
 'UTCTime',
 'WhiteElo',
 'WhiteRatingDiff']



def open_and_scrape_headers(filepath):
    game_id = 0
    g = pd.DataFrame(columns=['game_id'] + header_list)

    with open(filepath) as f:

        while True:
            game = chess.pgn.read_game(f)
            game_id += 1

            # If there are no more games, exit the loop
            if game is None:
                break

            value_list = [game_id]
            for header in header_list:
                try:
                    value_list.append(game.headers[header])
                except:
                    value_list.append('')

            g.loc[len(g)] = value_list

            if (game_id % 20000 == 0):
                print('Now adding game_id: ' + str(game_id))

    return g


filepath = '/home/amedvedev/PycharmProjects/chessgamesstat/data/drakar1/drakar1-white.pgn'
g = open_and_scrape_headers(filepath)
print(g)
