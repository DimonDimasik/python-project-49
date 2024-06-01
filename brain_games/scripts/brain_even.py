#!/usr/bin/env python3


from brain_games.games.even_log import even_ques_gen, min_num, max_num, amount_ques
from brain_games.games.engine import even_start, game_engine


def main():
    game_engine(even_ques_gen, min_num, max_num, amount_ques, even_start)


if __name__ == '__main__':
    main()
