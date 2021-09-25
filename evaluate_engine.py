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

            gap = (99/35)*(40-taken)

            # TODO - detect abuse based on grades and taken time
            if self.scenario == 2:
                self.detect_abuse()

            action = {"id":win_id, "grade":self.userinfo[win_id]+gap}
            command_list.append(action)

        return self.dump_command(command_list)
    
    def detect_abuse(self):
        # TODO
        return

    def parse_game_result(self, token):
        self.game_result = token["game_result"]
        return
    
    def dump_command(self, command_list):
        return json.dumps(command_list)

