import json

class EVALUATE():
    def __init__(self, api, scenario):
        self.scenario = scenario
        self.api = api

    def evaluate_turn(self, userinfo):
        token = self.api.gameresult()
        self.userinfo = userinfo
        self.parse_game_result(token)

        command = self.evaluate_algorithm()
        # print("EVAL", token, command)
        self.api.changegrade(command)
    
    def evaluate_algorithm(self):
        command_list = []
        for result in self.game_result:
            win_id = result['win']
            lose_id = result['lose']
            taken = result['taken']

            gap = (99/35)*(40-taken)*10
            win_grade = self.userinfo[win_id]+1
            lose_grade = self.userinfo[lose_id]+1
            win_gap = gap*(win_grade/(win_grade+lose_grade))
            lose_gap = gap*(lose_grade/(win_grade+lose_grade))

            abuse = False
            if self.scenario == 2:
                abuse = self.detect_abuse(win_id, lose_id, taken, gap)

            action = {"id":win_id, "grade":self.userinfo[win_id]+win_gap}
            command_list.append(action)

            # if abuse:
            #     action = {"id":lose_id, "grade":0.2*(self.userinfo[lose_id]+lose_gap)}
            #     command_list.append(action)

        return self.dump_command(command_list)
    
    def detect_abuse(self, win_grade, lose_grade, taken, gap):
        if taken <= 10:
            if lose_grade > win_grade+50:
                return True
        return False

    def parse_game_result(self, token):
        self.game_result = token["game_result"]
        return
    
    def dump_command(self, command_list):
        return json.dumps(command_list)

