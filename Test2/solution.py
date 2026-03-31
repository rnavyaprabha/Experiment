def solution(C, U, colorRects, uncolorRects):
    xs = set()
    ys = set()

    for x1, y1, x2, y2 in colorRects:
        xs.add(x1); xs.add(x2)
        ys.add(y1); ys.add(y2)
    for x1, y1, x2, y2 in uncolorRects:
        xs.add(x1); xs.add(x2)
        ys.add(y1); ys.add(y2)

    xs = sorted(xs)
    ys = sorted(ys)

    if not xs or not ys:
        return 0

    xi = {v: i for i, v in enumerate(xs)}
    yi = {v: i for i, v in enumerate(ys)}

    nx = len(xs) - 1
    ny = len(ys) - 1

    if nx <= 0 or ny <= 0:
        return 0

    colored = [[False] * ny for _ in range(nx)]
    uncolored = [[False] * ny for _ in range(nx)]

    for x1, y1, x2, y2 in colorRects:
        for i in range(xi[x1], xi[x2]):
            for j in range(yi[y1], yi[y2]):
                colored[i][j] = True

    for x1, y1, x2, y2 in uncolorRects:
        for i in range(xi[x1], xi[x2]):
            for j in range(yi[y1], yi[y2]):
                uncolored[i][j] = True

    total = 0
    for i in range(nx):
        for j in range(ny):
            if colored[i][j] and not uncolored[i][j]:
                total += (xs[i + 1] - xs[i]) * (ys[j + 1] - ys[j])

    return total


if __name__ == "__main__":
    C, U = map(int, input().split())
    colorRects = []
    for _ in range(C):
        colorRects.append(list(map(int, input().split())))
    uncolorRects = []
    for _ in range(U):
        uncolorRects.append(list(map(int, input().split())))
    print(solution(C, U, colorRects, uncolorRects))
