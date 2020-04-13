# reproduces one of the bugs discovered by `staking2.py`

from staking2 import doit

# this repro was created before fake stakes were introduced, so each stake after the first one is duplicated to account for that
sequence = [
    [0, 73215476000000000000000000000000, 73203310000000000000000000000000],
    [0, 95711839000000000000000000000000, 75774073000000000000000000000000],
    [0, 95711839000000000000000000000000, 75774073000000000000000000000000],
    [0, 84382393000000000000000000000000, 98749818000000000000000000000000],
    [0, 84382393000000000000000000000000, 98749818000000000000000000000000],
    [0, 0, 90224511000000000000000000000000]       ,
    [0, 0, 90224511000000000000000000000000]       ,
    [86432337000000000000000000000000, 76422536000000000000000000000000, 0],
    [86432337000000000000000000000000, 76422536000000000000000000000000, 0],
    [75063341000000000000000000000000, 0, 80786582000000000000000000000000],
    [75063341000000000000000000000000, 0, 80786582000000000000000000000000],
    [86164122000000000000000000000000, 0, 73964803000000000000000000000000],
    [86164122000000000000000000000000, 0, 73964803000000000000000000000000],
    [70076530000000000000000000000000, 0, 0]       ,
    [70076530000000000000000000000000, 0, 0]       ,
    [0, 78553537000000000000000000000000, 0]       ,
    [0, 78553537000000000000000000000000, 0]       ,
    [85364825000000000000000000000000, 0, 81322978000000000000000000000000],
    [85364825000000000000000000000000, 0, 81322978000000000000000000000000],
    [98064272000000000000000000000000, 0, 0]       ,
    [98064272000000000000000000000000, 0, 0]       ,
    [0, 0, 78616653000000000000000000000000]       ,
    [0, 0, 78616653000000000000000000000000]       ,
    [99017960000000000000000000000000, 78066788000000000000000000000000, 0],
    [99017960000000000000000000000000, 78066788000000000000000000000000, 0],
    [83587257000000000000000000000000, 0, 0]       ,
    [83587257000000000000000000000000, 0, 0]       ,
    [81625375000000000000000000000000, 0, 90569985000000000000000000000000],
    [81625375000000000000000000000000, 0, 90569985000000000000000000000000],
    [76171853000000000000000000000000, 70811780000000000000000000000000, 0],
    [76171853000000000000000000000000, 70811780000000000000000000000000, 0],
]

doit(sequence)
