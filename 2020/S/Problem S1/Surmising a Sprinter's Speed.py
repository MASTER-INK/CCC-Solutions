import numpy as np
def speed():
    speeds = []
    N = int(input())
    for i in range(N):
        speeds = np.concatenate((speeds, input().split()))
    print(speeds)

if __name__ == "__main__":
    speed()
