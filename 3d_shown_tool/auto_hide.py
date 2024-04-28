import sys
import os

def show_hide_3d(mode, file_path):
    # Define the search texts and corresponding replace texts for each extension
    extensions_replace = {
        ".STEP\"\n": ".STEP\" hide\n",
        ".WRL\"\n": ".WRL\" hide\n",
        ".wrl\"\n": ".wrl\" hide\n",
        ".stp\"\n": ".stp\" hide\n"
    }

    # If mode is set to show (mode = 1), reverse the keys and values in the extensions_replace dictionary
    if mode == 1:
        extensions_replace = {v: k for k, v in extensions_replace.items()}

    # Open the text file in read mode
    with open(file_path, 'r') as file:
        # Read the content of the file
        data = file.read()

        # Replace each extension with its corresponding replace text
        for ext, replace_text in extensions_replace.items():
            data = data.replace(ext, replace_text)

    # Open the text file in write mode to write the replaced content
    with open(file_path, 'w') as file:
        # Write the replaced data back to the file
        file.write(data)  

def process_mod_files_in_directory(mode,directory,specific_file=None):
    if specific_file:
        specific_file_path = os.path.join(os.getcwd(),directory, specific_file)
        if os.path.exists(specific_file_path):
            show_hide_3d(mode,specific_file_path)
            
       
        else:
            print("Error: Specified file '{}' not found.".format(specific_file_path))
    else:
        for filename in os.listdir(os.path.join(os.getcwd(),directory)):
            if filename.endswith('.kicad_pcb'):
                file_path = os.path.join(os.getcwd(), directory, filename)
                show_hide_3d(mode,file_path)

def main():
    if len(sys.argv) < 4:
        print("Usage:")
        print("1. For hiding/showing extensions in all files in a directory:")
        print("   python auto_hide.py <hide/show_mode> <directory> 0")
        print("2. For hiding/showing extensions in specific files:")
        print("   python auto_hide.py <hide/show_mode> <directory> <number_of_files> [<file1> <file2> ...]")
        print("\nExplanation of hide/show_mode:")
        print("  - 0: Hide extensions (replace extensions with 'hide' version)")
        print("  - 1: Show extensions (restore extensions to original version)")
        return

    mode = int(sys.argv[1])
    directory = sys.argv[2]
    num_files = int(sys.argv[3])

    if num_files < 1:
        process_mod_files_in_directory(mode,directory)
        return

    files_to_process = sys.argv[3:]

    if len(files_to_process) < num_files:
        print("You must provide the filenames for all specified files.")
        return

    for specific_file in files_to_process[:num_files]:
        process_mod_files_in_directory(mode,directory, specific_file)

if __name__ == '__main__':
    main()
