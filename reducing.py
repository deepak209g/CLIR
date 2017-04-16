import os
import pickle
print(os.getcwd())

files = os.listdir("./models")
print(files)

red_model = {}
last_file = ''
cwd = os.getcwd()
for file in files:
    f_h = open(cwd + '/models/' + file, 'rb')
    model = pickle.load(f_h)
    # model [french][english]
    for f_tok in model:
        if f_tok not in red_model:
            red_model[f_tok] = {}
        for e_tok in model[f_tok]:
            if e_tok not in red_model[f_tok]:
                red_model[f_tok][e_tok] = model[f_tok][e_tok]
            else:
                # Take the max from the consolidated model and the current
                # model and put that value in the consolidated model
                s_model = model[f_tok][e_tok]
                c_model = red_model[f_tok][e_tok]
                red_model[f_tok][e_tok] = max(c_model, s_model)
    last_file = file.split('.')[0]
# after the consolidated model has been created dump it into a pickle
red_model_file = open("./reduced_models/reduced_" + last_file + '.obj')
pickle.dump(red_model, red_model_file)
