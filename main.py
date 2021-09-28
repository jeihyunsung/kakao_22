import argparse
from API import *
from match_engine import *
from evaluate_engine import *

# 토큰 앞 6자리 52bb8d 141등?
# Maximum score
# Scenario 1
# 77.778	62.577	95.38	244.73
# Scenario 2
# 52.2032	58.1978	99.7876	212.3113
# 451.19


class MAIN():
    def __init__(self, scenario=1):
        self.api = API()
        self.match = MATCH(self.api, scenario)
        self.evaluate = EVALUATE(self.api, scenario)
        self.api.start(scenario)

    def simulate(self):
        idx = 0
        while(True):
            self.get_userinfo()
            finished = self.match.match_turn(self.userinfo)
            self.evaluate.evaluate_turn(self.userinfo)

            if finished:
                break
            elif idx%50 == 0:
                print(max(self.evaluate.userinfo.values()))
                print(idx)
            idx += 1

        self.api.score()

    def get_userinfo(self):
        token = self.api.userinfo()
        self.userinfo = {}
        for x in token['user_info']:
            self.userinfo[x['id']] = x['grade']

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('scenario', type=int, default=1)
    args = parser.parse_args()
    main = MAIN(args.scenario)
    main.simulate()


