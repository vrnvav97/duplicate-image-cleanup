import os
import image
import logging



logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def list_files_in_directory(directory_path):
    try:
        # Check if the provided path is a directory
        if not os.path.isdir(directory_path):
            print(f"The path '{directory_path}' is not a valid directory.")
            return

        # List all files and directories
        files = os.listdir(directory_path)
        
        logger.info(f"{len(files)} items available in directory '{directory_path}'")

        user_input = input("Do you want to see the list of files? (Y/N): ").strip().lower()
        if user_input in ['yes', 'y']:
            for file in files:
                logger.info(file)     
        

        logger.info(image.get_image_paths(os.path.join(directory_path, files[0]), os.path.join(directory_path, files[1])))
        # image.get_image_paths(os.path.join(directory_path, files[0]), os.path.join(directory_path, files[1]))


    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    user_input = input("Enter the path to the directory: ")
    list_files_in_directory(user_input)
