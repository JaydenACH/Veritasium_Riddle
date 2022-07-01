import random
import time

def main():
    starttime = time.time()
    repeat = 10000
    probability = 0
    for i in range(repeat):
        room_of_box = compute_randombox()
        open_box = chance_of_finding(room_of_box)
        if probability != 0:
            probability = probability + compute_probability(open_box)
        else:
            probability = compute_probability(open_box)
    endtime = time.time()
    ttime = endtime-starttime
    ttime = float("{:.2f}".format(ttime))
    prob_percent = probability / repeat * 100
    print(f"time needed is {ttime} seconds")
    print(prob_percent)


def compute_randombox():
    box = {}
    for i in range(101)[1:]:
        num = random.randint(1, 100)
        if i == 1:
            box[i] = num
        else:
            while num in box.values() or num > 100:
                if num > 100:
                    num = num - 100
                else:
                    num += 1
            box[i] = num
    # print(box)
    return box

def chance_of_finding(thebox):
    prob_openbox = []
    for i in thebox:
        boxvalue = thebox[i]
        openbox = 1
        while boxvalue != i:
            boxvalue = thebox[boxvalue]
            openbox += 1
        if openbox not in prob_openbox:
            prob_openbox.append(openbox)
    # print(prob_openbox)
    return prob_openbox

def compute_probability(open_box):
    for prob in open_box:
        if prob > 50:
            percent = 0
            return percent
        else:
            percent = 1
            return percent

if __name__ == '__main__':
    main()
