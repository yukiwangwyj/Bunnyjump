

Array1 = [0, 40, 65, 120, 140, 155, 180, 195, 210, 240, 260, 300, 320, 370, 400, 420, 480, 500]
Array2 = [0, 15, 30, 50, 75, 85, 145, 165, 200, 270, 300, 350, 390, 405, 420, 440, 455, 470, 500]
Array3 = [0, 60, 70, 120, 140, 160, 200, 250, 290, 340, 355, 410, 445, 460, 475, 500]

S = Array3

# f(n) between 50 to 70
# g(n) less than 50

n = len(S)

#Basecase
f = [None]
g = [0]

for i in range(1, n):
    f_min = 500
    g_min = 500

    # going back to review all the stones within one step
    for j in range(i-1, -1, -1):
        if S[i] - S[j] > 70:
            break
        elif S[i] - S[j] < 50:
            g_min = min(g_min, 500 if f[j] is None else f[j], 500 if g[j] is None else g[j])
        else:
            f_min = min(f_min, 500 if g[j] is None else g[j])

    # update the min step for current stone
    if f_min == 500:
        f.append(None)
    else:
        f.append(f_min + 1)
    if g_min == 500:
        g.append(None)
    else:
        g.append(g_min + 1)

step = min(500 if f[-1] is None else f[-1], 500 if g[-1] is None else g[-1])

print(step)


