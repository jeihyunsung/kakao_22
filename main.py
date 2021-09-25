from API import *
from match_engine import *
from evaluate_engine import *

class MAIN():
    def __init__(self, scenario=1):
        self.api = API()
        self.match = MATCH(self.api)
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
                print(self.evaluate.userinfo)
                print(idx)
            idx += 1

        self.api.score()

    def get_userinfo(self):
        token = self.api.userinfo()
        self.userinfo = {}
        for x in token['user_info']:
            self.userinfo[x['id']] = x['grade']

if __name__=="__main__":
    main = MAIN()
    main.simulate()


