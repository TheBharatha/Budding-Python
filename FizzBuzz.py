class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        fb = list(map(self.check,list(range(1,n+1))))
        return fb
    
    def check(self, number):
        if number%3 == 0 and number%5 != 0:
            return('Fizz')
        elif number%5 == 0 and number%3 != 0:
            return('Buzz')
        elif number%3 == 0 and number%5 == 0:
            return('FizzBuzz')
        else:
            return(str(number))