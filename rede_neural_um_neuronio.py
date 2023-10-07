import math

input = 0
output_desire = 0

input_weight = 0.5
learning_rate = 0.02

def activation (sum):
    if sum >= 0:
        return 1
    else:
        return 0

print("entrada",input, "saida desejada",output_desire)

error = math.inf  #erro inicial infinito
iteration = 0

bias = 1  #neuronio virtual
bias_weight = 0.5

while not error == 0:
    iteration +=1
    print("interações totais",iteration) #quantidade iterações até aprender
    print("peso de entrada",input_weight)
    sum = (input * input_weight) + (bias * bias_weight)

    output = activation(sum)

    print("saida",output)

    error = output_desire - output

    print("erro", error)

    if not error == 0:
         input_weight = input_weight + (learning_rate * input * error)
         bias_weight = bias_weight + (learning_rate * bias * error)
print("parabens a rede aprendeu e eu tbm +1 neuronio pra gente")