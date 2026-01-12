class Solution:
    def countSeniors(self, details: List[str]) -> int:
        nr_passangers = 0
        for passanger in details:
            if int(passanger[11:13]) > int(60):
                nr_passangers+=1
        return nr_passangers