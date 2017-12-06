def calc(h,ha,ta,p0):
    a = 0.0065
    T = ta - a * (h - ha)
    P = p0 * (1 - (a * h / (T + a * h + 273.15))) ** 5.257
    return T, P

if __name__ == '__main__':
    try:
        height = int(input('目的地の標高を入力(m): '))
        NowHeight = int(input('現在地の標高を入力(m): '))
        temp = int(input('現在地の気温を入力(℃): '))
        atm = float(input('海面気圧を入力(hPa): '))
    except ValueError:
        print('無効な値が入力されました．')
    else:
        res = calc(height, NowHeight, temp, atm)
        print('気温 : {:.1f}℃ 気圧 : {:.2f}hPa'.format(res[0], res[1]))
