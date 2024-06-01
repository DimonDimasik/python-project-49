#!/usr/bin/env python3


from brain_games.games.progress_log import prog_ques_gen, min_num, max_num, amount_ques
from brain_games.games.engine import progress_start, game_engine


def main():
    game_engine(prog_ques_gen, min_num, max_num, amount_ques, progress_start)


if __name__ == '__main__':
    main()
