from sympy import symbols, diff, sympify


def bisection_method(function: str, low_border: float, up_border: float, epsilon: float = 1e-5) -> object:
    global mid_x
    while up_border - low_border >= 2 * epsilon:
        x = (up_border + low_border) / 2
        mid_x = x
        mid_y = eval(function)
        x = low_border
        low_y = eval(function)
        x = up_border
        up_y = eval(function)

        if low_y < 0 < mid_y:
            up_border = mid_x
        elif up_y > 0 > mid_y:
            low_border = mid_x
        elif mid_y > 0 > up_y:
            low_border = mid_x
        elif mid_y < 0 < low_y:
            low_border = mid_x
        elif abs(mid_y) + abs(low_y) + abs(up_y) == abs(low_y + mid_y + up_y):
            return None
        elif mid_y == 0:
            return mid_x
        else:
            return None

    return mid_x


def chord_method(function: str, low_border: float, up_border: float, epsilon: float = 1e-5):
    prev_x = 1e+10
    skip_first = False

    while True:
        x = low_border
        low_y = eval(function)
        x = up_border
        up_y = eval(function)

        if abs(low_y) < epsilon:
            return low_border

        if abs(up_y) < epsilon:
            return up_border
        denominator = up_y - low_y
        if denominator == 0:
            # Если знаменатель равен нулю, выходим из цикла
            return None
        cur_x = low_border - (low_y * (up_border - low_border)) / denominator

        x = cur_x
        mid_y = eval(function)

        if abs(mid_y) < epsilon:
            return cur_x

        if abs(cur_x - prev_x) < epsilon and skip_first:
            return cur_x

        if low_y * mid_y < 0:
            up_border = cur_x
        else:
            low_border = cur_x

        prev_x = cur_x
        skip_first = True


def Newtons_method(function: str, low_border: float, up_border: float, epsilon: float = 1e-5):
    variable = symbols('x')
    func_expr = sympify(function)
    derivative = diff(func_expr, variable)
    prev_x = (low_border + up_border) / 2
    skip_firs = False

    while True:
        x = low_border
        low_y = eval(function)

        x = up_border
        up_y = eval(function)

        derivative_value = derivative.subs(variable, prev_x)

        x = prev_x
        mid_y_prev = eval(function)

        cur_x = prev_x - mid_y_prev / derivative_value

        x = cur_x
        mid_y = eval(function)

        if prev_x - cur_x < epsilon and skip_firs:
            return cur_x

        if low_y < 0 < mid_y:
            up_border = cur_x
        elif up_y > 0 > mid_y:
            low_border = cur_x
        elif mid_y > 0 > up_y:
            low_border = cur_x
        elif mid_y < 0 < low_y:
            low_border = cur_x
        elif abs(mid_y) + abs(low_y) + abs(up_y) == abs(low_y + mid_y + up_y):
            return None
        elif mid_y == 0:
            return cur_x
        else:
            return None

        prev_x = cur_x
        skip_firs = True


if __name__ == "__main__":
    function = "x**2 -4*x+5"
    result = chord_methodGPT(function, -2, 6)
    if result is not None:
        print(result)
    else:
        print("No solution")

# x**2 -4*x+5 парабола не пересекает х
# 2*x +2 линия пересекает в -1
# x**2 + 5*x-10 пересекает в
