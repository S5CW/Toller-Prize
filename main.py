import data, shapley, checks

#unis  = ["Oxford", "Cambridge", "Imperial", "UCL", "Edinburgh", "King's", "LSE", "Manchester", "Bristol", "St Andrews", "Loughborough", "Durham", "Bath", "Warwick", "Glasgow", "Southampton", "Sheffield", "Leeds", "Nottingham", "Birmingham"]
# quotas = [3300, 3500, 3200, 6300, 6500, 7000, 2000, 8500, 6500, 1800, 4500, 4700, 4200, 5800, 6100, 4800, 5700, 7900, 8300, 7200]
# print(sum(quotas))
# uP, aP = data.generate(sum(quotas)//1000)

# assingment = shapley.match(uP, aP, [i//1000 for i in quotas])
# print(checks.stability(assingment, uP, aP))

uP, aP = data.generate(40)
assingment = shapley.match(uP, aP, [2 for i in range(20)])
print(assingment)
print(checks.stability(assingment, uP, aP))