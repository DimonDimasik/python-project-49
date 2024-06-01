#!/usr/bin/env python3


from brain_games.games.prime_log import prime_ques_gen, min_num, max_num, amount_ques
from brain_games.games.engine import prime_start, game_engine


def main():
    game_engine(prime_ques_gen, min_num, max_num, amount_ques, prime_start)


if __name__ == '__main__':
    main()
