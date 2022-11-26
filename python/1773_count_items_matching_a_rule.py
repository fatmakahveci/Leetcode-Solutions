class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:

        rule_dict = { 'type': 0, 'color': 1, 'name': 2 }
        match_counter = 0
        for item in items:
            if item[rule_dict[ruleKey]] == ruleValue:
                match_counter += 1
        return match_counter
