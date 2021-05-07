from time import perf_counter
import tetris
import tracemalloc

if __name__ == '__main__':
    a = [(3, 5), [((2, 2), 1)], [((3, 2), 1), ((2, 2), 2)]]
    tracemalloc.start()
    start = perf_counter()
    tetris.Main(a)
    end = perf_counter()
    print(str (end - start) + ' time')
    print("Current: %d, Peak %d" % tracemalloc.get_traced_memory())