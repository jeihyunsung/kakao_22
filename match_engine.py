class MATCH():
    def __init__(self, api, scenario):
        self.api = api
        self.critical_gap = 500 if scenario == 1 else 750 # Parameter
        self.critical_time = 4 # Parameter
        self.curr_turn = 0

    def match_turn(self, userinfo):
        self.userinfo = userinfo
        token = self.api.waitingline()
        self.parse_wating_line(token)
        match_list = self.match_algorithm()
        # print("match", self.waiting_list, match_list)
        token = self.api.match(match_list)

        self.curr_turn = token['time']

        if token['status'] == 'finished':
            return True
        else:
            return False

    def match_algorithm(self):
        # TODO - temporary algorithm
        match_list = []
        next_continue = False
        for idx, x in enumerate(self.waiting_list):
            if idx == len(self.waiting_list)-1:
                break
            a = x
            b = self.waiting_list[idx+1]

            grade_gap = abs(a[1]-b[1])
            time_wait_avg = (a[2]+1+b[2]+1)/2

            critical_ratio = grade_gap/self.critical_gap
            time_critical = True if time_wait_avg >= self.critical_time else False

            if (critical_ratio > 1 or next_continue == True) and time_critical == False:
                next_continue = False
                continue
            else:
                match_list.append([a[0],b[0]])
                next_continue = True

        return match_list

    def parse_wating_line(self, token):
        # line up based on gap
        lineup = []
        for x in token['waiting_line']:
            grade = self.userinfo[x['id']]
            lineup.append([x['id'],grade,self.curr_turn-x['from']])
        lineup.sort(key=(lambda x:x[1]))

        self.waiting_list = lineup
