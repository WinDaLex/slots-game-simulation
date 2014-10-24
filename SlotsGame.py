import random
import time

class SlotMachine(object):
    awards = (500, 150, 125, 100, 75, 50, 10, 0)

    def score(self, slots):
        slots.sort()
        if slots[0] == slots[1] == slots[2]: return self.awards[slots[0]]
        if slots[0] == slots[1] == 0:
            return self.awards[slots[2]]
        if slots.count(0) == 1:
            if slots[1] != slots[2]: return 10
            else: return self.awards[slots[2]]
        return 0

    def pull(self, coin=1):
        total_score = 0
        for i in range(coin):
            slots = [random.randint(0, 5) for j in range(3)]
            total_score += self.score(slots)
        return total_score, slots


def simulation(number = -1, interval = 1):
    machine = SlotMachine()
    no = 0; total = 0; expectation = 0
    while (no != number):
        time.sleep(interval)
        award, slots = machine.pull()
        total += award
        no += 1
        expectation = float(total) / no
        print "No. %d\tslots: %d%d%d\taward: %d\t total: %d\t E: %f" %\
                (no, slots[0], slots[1], slots[2], award, total, expectation)

