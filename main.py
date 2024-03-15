import time
import methods_of_finding as methods


def input_function():
    print("""Данная программа проводит сравнение скорости работы трёх алгоритмов для решения нелинейных уравнений
1. Метод бисекции
2. Метод хорд
3. Метод Ньютона
""")
    function = input("Введите функцию: ")
    low_border = float(input("Введите нижнюю границу поиска: "))
    up_border = float(input("Введите верхнюю границу поиска: "))
    check_time(function, low_border, up_border)


def check_time(function, low_border, up_border):
    start_time_bis = time.time()
    result_bis = methods.bisection_method(function, low_border, up_border)
    end_time_bis = time.time()
    diff_bis = end_time_bis - start_time_bis

    start_time_chord = time.time()
    result_chord = methods.chord_method(function, up_border, low_border)
    end_time_chord = time.time()
    diff_chord = end_time_chord - start_time_chord

    start_time_newton = time.time()
    result_newton = methods.Newtons_method(function, low_border, up_border)
    end_time_newton = time.time()
    diff_newton = end_time_newton - start_time_newton

    print_result(result_bis, result_chord, result_newton, diff_bis, diff_chord, diff_newton)


def print_result(res_bis, res_chord, res_newton, time_bis, time_chord, time_newton):
    print('--------------------------------')
    print(f"результат вычисления с помощью бисекции {res_bis:.3f}, время выполнения {time_bis:.3f}")
    print(f"результат вычисления с помощью хорд {res_chord:.3f}, время выполнения {time_chord:.3f}")
    print(f"результат вычисления с помощью Ньютона {res_newton:.3f}, время выполнения {time_newton:.3f}")


if __name__ == "__main__":
    input_function()
