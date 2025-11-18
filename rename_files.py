import subprocess as sp

for i in range(1, 11):
    oldname = f'./subjects/math/english_level{i}.txt'
    newname = f'./subjects/math/math_level{i}.txt'
    sp.run(f'mv {oldname} {newname}', shell=True)