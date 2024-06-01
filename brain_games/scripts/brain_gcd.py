#!/usr/bin/env python3


from brain_games.games.gcd_log import gcd_ques_gen, min_num, max_num, amount_ques
from brain_games.games.engine import gcd_start, game_engine


def main():
    game_engine(gcd_ques_gen, max_num, min_num, amount_ques, gcd_start)


if __name__ == '__main__':
    main()
