def celsius_para_fahrenheit(c):
    return (c * 9 / 5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = celsius_para_fahrenheit(celsius)

print("{:.1f}ºC equivale a {:.1f}ºF".format(celsius, fahrenheit))
