import subprocess
import matplotlib.pyplot as plt

def compile_and_run(arraysize):
    # Compile the program.
    compile_process = subprocess.run(['g++', '-o', 'program', 'program.cpp', '-fopenmp', '-mavx'], check=True)

    # Run the program and capture the stderr output.
    run_process = subprocess.run(['./program'], input=str(arraysize), text=True, stderr=subprocess.PIPE)

    # Extract the operations per second from the stderr output.
    output_lines = run_process.stderr.split('\n')
    operations_per_second = []
    for line in output_lines:
        if line.startswith('S'):
            operations_per_second.append(float(line.split()[1]))

    return operations_per_second

# Iterate over different array sizes.
array_sizes = [2**i for i in range(10, 24)]  # This will generate sizes up to 2^23.

results = []
for array_size in array_sizes:
    result = compile_and_run(array_size)
    results.append(result)

# Plot the results.
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, results)
plt.xlabel('Array Size')
plt.ylabel('Operations per Second')
plt.title('Performance of C++ Program')
plt.grid(True)
plt.show()
