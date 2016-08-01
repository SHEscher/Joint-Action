from SA_Evolution import *

"""
__author__  = Simon Hofmann"
__credits__ = ["Simon Hofmann", "Katja Abramova", "Willem Zuidema"]
__version__ = "1.0.1"
__date__ "2016"
__maintainer__ = "Simon Hofmann"
__email__ = "simon.hofmann@protonmail.com"
__status__ = "Development"
"""
# TODO: Run evolution with long simulation, ergo scalar = 2 (>1)
# For the CPU split:
# Type in Terminal (-P*, * must be equal to n_cpu):
#  cat args_splitter | xargs -L1 -P6 python3 SA_Server_Sim.py
# Note: args_splitter must contain numbers from 1 to n_cpu

n_cpu = 6

if len(sys.argv) > 1 and sys.argv[1].isdigit():
        split = int(sys.argv[1]) if int(sys.argv[1]) <= n_cpu else False
else:
    split = False


if not split:  # is False
    audicon = audio_condition_request()
    number_of_generations = generation_request()
    filename = filename_request("single")

    # If e.g. scalar = 0.336 => Target just makes one turn
    scalar = simlength_scalar_request()

    # Whether sensory and motor weights suppose to be symmetrical:
    symmetry = symmetrical_weights_request()


else:  # if splitter is used, these values must be pre-given, here in python file
    # Manually adjust the following parameters:
    audicon = True     # True or False
    number_of_generations = 10000
    scalar = 1          # 1 == no scaling [Default], 1/3 == first turn
    symmetry = True     # True or False
    filename = "Gen1001-10000.popsize110.mut0.02.sound_cond=True.sym_weights.JA.single(Fitness9.94)"  # or None
    print("Splitter {} started!".format(split))


sa = SA_Evolution(auditory_condition=audicon, pop_size=110, simlength_scalar=scalar, symmetrical_weights=symmetry)


if isinstance(filename, str):
    sa.reimplement_population(filename=filename, plot=False)
    if not split or split == n_cpu:
        if audicon != sa.condition:
            print("...")
            print("Note: Initial Sound Condition differs from the one in implemented file!")
            print("...")


# RUN:
if not split or split == n_cpu:
    print("Run Evolution: {} Generations, Single Condition, Sound Condition={}, simlength-scalar {}, sym. weights={}".format(number_of_generations,
                                                                                                                             sa.condition,
                                                                                                                             scalar,
                                                                                                                             symmetry))
sa.run_evolution(generations=number_of_generations, splitter=split, n_cpu=n_cpu)
