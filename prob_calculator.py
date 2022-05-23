import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for k, v in kwargs.items():
            for i in range(v):
                self.contents.append(k)
            print(self.contents)

    def draw(self, number):
        removed = []
        if number > len(self.contents):
            return self.contents
        else:
            for i in range(number):
              r = random.randint(0, (len(self.contents))-1)
              popped = self.contents.pop(r)
              removed.append(popped)
        return removed
      
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count = 0
  for i in range(num_experiments):
    copy_expected = copy.deepcopy(expected_balls)
    copy_hat = copy.deepcopy(hat)
    colors = copy_hat.draw(num_balls_drawn)
    for c in colors:
      if (c in copy_expected):
        copy_expected[c] =- 1
    if (all(x<=0 for x in copy_expected.values())):
      count += 1
  return count / num_experiments
