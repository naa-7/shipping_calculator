# This is a program that asks the user for the weight of their package and 
# then tells them which method of shipping is cheapest and how much it will 
# cost to ship their package

# The cheapest way to ship 4.8 pound package is using ground shipping and it will cost $34.40.
# The cheapest way to ship a 41.5 pound package is using premium ground shipping and it will cost $125.00.

import subprocess

def ground_shipping(weight):
  flat_charge = 20.00
  premium_shipping = 125.00
  if (weight <= 2):
    cost = (weight * 1.50) + flat_charge
  elif (2 < weight <= 6):
    cost = (weight * 3.00) + flat_charge
  elif (6 < weight <= 10):
    cost = (weight * 4.00) + flat_charge
  else:
    cost = (weight * 4.75) + flat_charge
  return cost, premium_shipping

def drone_shipping(weight):
  flat_charge = 0.00
  if (weight <= 2):
    cost = weight * 4.50
  elif (2 < weight <= 6):
    cost = weight * 9.00
  elif (6 < weight <= 10):
    cost = weight * 12.00
  else:
    cost = weight * 14.25
  return cost

def cheapest_shipping(weight):
  ground, premium = ground_shipping(weight)
  drone = drone_shipping(weight)
  if (ground < premium) and (ground <drone):
    return ("Cheapest shipping is ground shipping = \$" + str(ground))
  elif (drone < premium) and (drone < ground):
    return ("Cheapest shipping is drone shipping = \$" + str(drone))
  else:
    return ("Cheapest shipping is premium shipping = \$" + str(premium))

def main():
    #ground_shipping, premium_shipping = ground_shipping(8.4)
    #drone_shipping = drone_shipping(1.5)
    #cheapest_shipping = cheapest_shipping(41.5)
    #print("Ground shipping cost = $" + str(ground_shipping))
    # should print "Ground shipping cost = $53.60"
    #print("Premium shipping cost = $" + str(premium_shipping))
    # should print "Premium shipping cost = $125.00"
    #print("Drone shipping cost = $" + str(drone_shipping))
    # should print "Drone shipping cost = $6.75"
    #print("Cheapest shipping is " + str(cheapest_shipping))
    # should print "Cheapest shipping is premium shipping = $125.00"

    answer = subprocess.Popen('zenity --forms --add-entry="Enter weight" --add-combo="Shipping Method"\
            --combo-values="Ground Shipping|Premium Shipping|Drone Shipping|Cheapest Shipping"', shell=True, stdout=subprocess.PIPE, universal_newlines=True)

    answer = answer.stdout.readline()
    answer = answer.strip()
    answer = answer.split('|')
    weight = int(answer[0])
    shipping_method =  answer[1]

    if shipping_method == "Ground Shipping" or shipping_method == "Premium Shipping":
        ground_price, premium_price = ground_shipping(weight)
        if shipping_method == "Ground Shipping":
            output_price = ("Ground shipping = \$" + str(ground_price))
        else:
            output_price = ("Premium Shipping = \$" + str(premium_price))
    elif shipping_method == "Drone Shipping":
        output_price = drone_shipping(weight)
        output_price = ("Drone shipping = \$" + str(output_price))
    elif shipping_method == "Cheapest Shipping":
        output_price = cheapest_shipping(weight)

    else:
        print("Error, Program Exit")
        return 1 

    output = "echo " + output_price + '|' + ' zenity --width=230 --height=120 --title="Result" --text-info'
    output = subprocess.call(output, shell=True)

if __name__ == "__main__":
    main()
