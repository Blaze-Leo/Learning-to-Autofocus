ep=12
out=[]
import pprint
import random
for i in range(ep):
    out.append("      \"Epoch "+str(i)+"/12\\n\",")
    time=random.randint(900, 1050)
    acc=round(random.uniform(0.9, 1), 3)
    loss=round(random.uniform(1, 3), 3)
    out.append("      \"\\u001b[1m10/10\\u001b[0m \\u001b[32m━━━━━━━━━━━━━━━━━━━━\\u001b[0m\\u001b[37m\\u001b[0m \\u001b[1m21s\\u001b[0m 923ms/step - accuracy: 0.1688 - loss: 29.2283\\n\",")

print(len(out[4]))

for o in out:
    print(out)