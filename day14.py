import re


class Reindeer(object):

    def __init__(self, name, speed, flight_time, rest_time):
        self.name = name
        self.speed = int(speed)
        self.flight_time = int(flight_time)
        self.rest_time = int(rest_time)

    def dist(self, time):
        cycle_time = self.flight_time + self.rest_time
        cycles, remain = divmod(time, cycle_time)
        dist = cycles * self.speed * self.flight_time
        if remain > self.flight_time:
            dist += self.speed * self.flight_time
        else:
            dist += remain * self.speed
        return dist


if __name__ == "__main__":

    specs = re.findall(r'(\w+) can fly (\d+) .* (\d+) .* (\d+)',
                       open('inputs/input14.txt').read())
    barn = [Reindeer(*spec) for spec in specs]

    # part one
    print(max([reindeer.dist(2503) for reindeer in barn]))

    # part two
    for reindeer in barn:
        reindeer.points = 0
    for time in range(1, 2504):
        dists = [reindeer.dist(time) for reindeer in barn]
        max_dist = max(dists)
        for i, reindeer in enumerate(barn):
            if dists[i] == max_dist:
                reindeer.points += 1
    print(max([reindeer.points for reindeer in barn]))
