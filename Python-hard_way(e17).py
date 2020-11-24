from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}.")

in_file = open(from_file)
in_data = in_file.read()

print(f"The input file is {len(in_data)} bytes long")

print(f"Does the out put file exist?  \n{exists(to_file)}"
)
print("Ready, hit ETURN to continue, CTRL-C to abort.")
input()

outfile = open(to_file, 'w')
outfile.write(in_data)

print("Alright, Done!")

outfile.close()
in_file.close()