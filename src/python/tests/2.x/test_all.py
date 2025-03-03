import subprocess

# Run a simple command
command = [r"C:\Program Files\National Instruments\LabVIEW 2021\LabVIEW.exe", r"C:\Git_Repos\lv-ui-testing\src\lv\examples\example 1 - plot.vi"]  # Replace with your desired command
result = subprocess.run(command, capture_output=True, text=True)

# Print the command's output
print(result.stdout)
