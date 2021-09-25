import requests
import json

class API:
    def __init__(self):
        self.BASE_URL = 'https://huqeyhi95c.execute-api.ap-northeast-2.amazonaws.com/prod'
        self.X_AUTH_TOKEN = '52bb8d8934828d06d4b6150f936a6fb3'
        self.AUTH_KEY = None
    
    def start(self, problem=1):
        self.problem = problem
        headers = {'X-Auth-Token': f'{self.X_AUTH_TOKEN}','Content-Type': f'application/json'}
        data = f'{{"problem": {problem} }}' #TODO
        response = requests.post(f'{self.BASE_URL}/start', headers=headers, data=data)
        token = response.json()

        self.AUTH_KEY = token['auth_key']
        self.problem = token['problem']
        self.time = token['time']
        print("Generated AUTH_KEY", self.AUTH_KEY, self.problem, self.time)
        return

    def waitingline(self):
        headers = {'Authorization': f'{self.AUTH_KEY}','Content-Type': 'application/json'}
        response = requests.get(f'{self.BASE_URL}/waiting_line', headers=headers)
        token = response.json()
        return token

    def gameresult(self):
        headers = {
            'Authorization': f'{self.AUTH_KEY}',
            'Content-Type': f'application/json',
        }
        response = requests.get(f'{self.BASE_URL}/game_result', headers=headers)
        token = response.json()
        return token

    def userinfo(self):
        headers = {
            'Authorization': f'{self.AUTH_KEY}',
            'Content-Type': f'application/json',
        }
        response = requests.get(f'{self.BASE_URL}/user_info', headers=headers)
        token = response.json()
        return token

    def match(self, commands= [[1, 2], [9, 7], [11, 49]]):
        headers = {
            'Authorization': f'{self.AUTH_KEY}',
            'Content-Type': 'application/json',
        }
        
        data = f'{{ "pairs": {commands} }}'

        response = requests.put(f'{self.BASE_URL}/match', headers=headers, data=data)
        token = response.json()
        return token

    def changegrade(self, commands='[{ "id": 1, "grade": 1900 }]'):
        headers = {
            'Authorization': f'{self.AUTH_KEY}',
            'Content-Type': 'application/json',
        }
        
        data = f'{{ "commands": {commands} }}'

        response = requests.put(f'{self.BASE_URL}/change_grade', headers=headers, data=data)
        token = response.json()
        return token

    def score(self):
        headers = {
            'Authorization': f'{self.AUTH_KEY}',
            'Content-Type': 'application/json',
        }

        response = requests.get(f'{self.BASE_URL}/score', headers=headers)
        token = response.json()

        print(token)
        return token


if __name__ == "__main__":
    temp_api = API()
    temp_api.start()
    temp_api.waitingline()
    temp_api.match()
    temp_api.gameresult()
    temp_api.changegrade()
    temp_api.userinfo()
    temp_api.score()



