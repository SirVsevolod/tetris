from time import perf_counter
import tetris


if __name__ == '__main__':
    a = [(3, 5), [((2, 2), 1)], [((3, 2), 1), ((2, 2), 2)]]
    start = perf_counter()
    tetris.Main(a)
    end = perf_counter()
    #print(str (end - start) + ' time')