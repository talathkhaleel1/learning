from inheritance.Aircraft.F16 import F16
from inheritance.Aircraft.F35 import F35
from inheritance.Aircraft.Carrier import Carrier

f16_first = F16()
f16_second = F16()
f35_first = F35()
f35_second = F35()

f16_first.refill(2)
f35_first.refill(300)
f16_first.calculate_damage()
f16_first.isPriority()

carrier = Carrier(10, 200)
carrier.add(f16_first)
carrier.add(f16_second)
carrier.add(f35_first)
carrier.add(f35_second)

carrier.fill()

print()
