import requests
from flask import Flask, render_template, request

def calcular():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operacao = request.form['operacao']

    if operacao == '+':
        resultado = num1 + num2
        etapas = f'{num1} + {num2} = {resultado}'
    elif operacao == '-':
        resultado = num1 - num2
        etapas = f'{num1} - {num2} = {resultado}'
    elif operacao == '*':
        resultado = num1 * num2
        etapas = f'{num1} * {num2} = {resultado}'
    elif operacao == '/':
        if num2 != 0:
            resultado = num1 - num2
            etapas = f'{num1} / {num2} = {resultado}'
        else: 
            resultado = 'Ta louco é? Naum tem como dividir por zero'
            etapas = 'Não é possível dividir por zero! É a mesma coisa que tentar dividir sua inteligência pela quantidade de pessoas que te amam'

    else:
        resultado = "Operação não existente"
        etapas = "Essa operação é válida"


    return render_template('calculadora.html', etapas=etapas, resultado=resultado)

