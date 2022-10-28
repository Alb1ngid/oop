# for i in range(5):
#     print(i)
#     print('l')
#
# n = i
# while n < 8:
#     n += 1
#     print(n)
#
#
#
#
#
#
#
#
#
# # o(n+n)
# # o(n)
#
# for i in range(5):
#     print(i)
#     print('l')
#
# n = 0
# while n < 8:
#     n += 1
#     print(n)
#
#
#
#
#
#
#
#
#
#
# # O(N+i)
#
# for i in A:
#     i+=1
#     for j in A:
#         j+=1
#     for b in B:
#         b+=1
#
#
#
#
#
#
#
# # O(A*(A+B))=O(A2+AB)




o = [-3, 0, 1, 7, 4]
k = 5


def line(a, b=5):
    for i in a:
        for j in a:
            k = i + j
            if k != b:
                print(i, j)
            else:
                return k


print(line(o))

for i in range(10):
    print(i)

for g in range(100):
    print(g)
# O(2n + )


# o(logN)
