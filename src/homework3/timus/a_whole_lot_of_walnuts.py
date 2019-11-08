"""Ten big walnuts is a whole lot of walnuts, that's for sure! Two walnuts
is too little for anybody. How about six walnuts? Is it a small number of
walnuts or a large one? The Parrot has already found an answer to this
question: after eating a small amount of walnuts he wants to eat some more,
while after eating a large amount of walnuts he feels satisfied. The Parrot
enjoys eating and hates overeating; that's why he wants to know a minimal
number of walnuts that is enough to get satisfied.
In order to calculate this number, he conducted a series of experiments.
Each experiment went like that: the Parrot, being quite hungry, ate a number
of walnuts and checked if this was enough to get himself satisfied. Of
course, if some number of walnuts is enough, any larger number will do
either; vice versa, if after eating a number of walnuts he is still hungry,
no smaller number can get the parrot satisfied. You should help the Parrot
to process the results of the experiments.
Input
The first line of the input contains an integer n — the number of
experiments conducted by the parrot (0 ≤ n ≤ 100). The following n lines
contain descriptions of these experiments. A description of an experiment
consists of a number of walnuts eaten by the parrot (an integer from 3 to 9)
and an outcome: “satisfied” in case this number was enough to get the parrot
satisfied or “hungry” otherwise. It is known as a fact, that ten walnuts is
always enough and two walnuts are always not enough.
Output
Output the minimal number of walnuts that is enough to get the parrot
satisfied. If the results of the experiments are inconsistent, output
“Inconsistent”."""
experiment_number = int(input())
experiments = {i: "" for i in range(2, 11)}
HUNGRY = "hungry"
SATISFIED = "satisfied"
experiments[2], experiments[10] = HUNGRY, SATISFIED
for i in range(experiment_number):
    number, result = input().split()
    number = int(number)
    if experiments[number] and experiments[number] != result:
        print("Inconsistent")
        break
    else:
        experiments[number] = result
else:
    max_hungry = max(
        [key for key in experiments if experiments[key] == HUNGRY])
    min_satisfied = min(
        [key for key in experiments if experiments[key] == SATISFIED])
    if max_hungry > min_satisfied:
        print("Inconsistent")
    else:
        print(min_satisfied)
