#!/usr/bin/env python3


from brain_games.games.calc_log import calc_ques_gen, min_num, max_num, amount_ques
from brain_games.games.engine import calc_start, game_engine


def main():
    game_engine(calc_ques_gen, min_num, max_num, amount_ques, calc_start)


if __name__ == '__main__':
    main()
