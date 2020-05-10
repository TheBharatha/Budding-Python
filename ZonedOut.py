class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        start = set(map(lambda x:x[0], paths))
        end = set(map(lambda y:y[1], paths))
        city = list(end.difference(start))[0]
        return(city)