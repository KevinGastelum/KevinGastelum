import math


def mean(*args):
  val_sum = sum(args)
  return val_sum / len(args)


def median(*args):
  if len(args) % 2 == 0:
    i = round((len(args) + 1) / 2)
    j = i - 1
    return (args[i] + args[j]) / 2
  else:
    k = round(len(args) / 2)
    return args[k]


def mode(*args):
  dict_vals = {i: args.count(i) for i in args}
  max_list = [k for k, v in dict_vals.items() if v == max(dict_vals.values())]
  return max_list


def variance(*args):
  mean_val = mean(*args)
  numerator = 0
  for i in args:
    numerator += (i - mean_val) ** 2
  denominator = len(args) - 1
  return numerator / denominator


def standard_deviation(*args):
  return math.sqrt(variance(*args))

# print(f"Median : {median(1, 2, 3, 4, 5)}") # Ans = 3
# print(f"Median : {median(1, 2, 3, 4, 5, 6)}") # Ans = 3.5
# print(f"Mode : {mode(1, 2, 3, 4, 5, 5, 4)}") # Ans = [4, 5]
print(f"Variance : {variance(4, 6, 3, 5, 2)}") # Ans = 2.5 (Uses Variance formula to solve)
