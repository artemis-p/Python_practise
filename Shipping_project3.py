# Sal runs the biggest shipping company in the tri-county area, Sal’s Shippers.
# Sal wants to make sure that every single one of his customers has the best,
# and most affordable experience shipping their packages. In this project,
# you’ll build a program that will take the weight of a package and determine
# the cheapest way to ship that package using Sal’s Shippers.

# Sal’s Shippers has several different options for a customer to ship their
# package. They have ground shipping, which is a small flat charge plus a rate
# based on the weight of your package. Premium ground shipping, which is a
# much higher flat charge, but you aren’t charged for weight. They recently
# also implemented drone shipping, which has no flat charge, but the rate
# based on weight is triple the rate of ground shipping.

# Here are the prices:

def ground_shipping(weight):
  flat_ground = 20 
  if (weight <= 2):
    price_per_pound = 1.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 3
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 4
  else:
    price_per_pound = 4.75
  return (price_per_pound * weight) + flat_ground

flat_premium = 125
premium_ground_shipping = flat_premium


def drone_shipping(weight):
  if (weight <= 2):
    price_per_pound = 4.50
  elif (weight > 2) and (weight <= 6):
    price_per_pound = 9
  elif (weight > 6) and (weight <= 10):
    price_per_pound = 12
  else:
    price_per_pound = 14.25
  return (price_per_pound * weight)


def cheapest_shipping(weight):
  ground = ground_shipping(weight)
  premium = premium_ground_shipping
  drone = drone_shipping(weight)
  
  if ground < premium and ground < drone:
    method = "standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "premium ground"
    cost = premium
  else:
    method = "drone"
    cost = drone

  print(
    "The cheapest option is £%.2f with %s cost"
    % (cost, method)
  )

cheapest_shipping(15)