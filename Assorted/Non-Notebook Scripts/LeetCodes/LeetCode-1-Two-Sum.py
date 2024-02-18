#1. Two Sum
def two_sum(arr, target):
    hash_map = {}
    for i in range(len(arr)):
        hash_map[arr[i]] = i
    for i in range(len(arr)):
        res = target - arr[i]
        if res in hash_map and hash_map[res] != i:
            return [i, hash_map[res]]

t = 18
l = [9,1,7,5,4,4,9,6,4,7,6,5,4,2,8,8,9,0]
print(two_sum(l,t))