import os


def delete_old_files(file):
    if file:
        file_path = file.path
        file_path = os.path.abspath(file_path)

        try:
            os.remove(file_path)
        except Exception:
            pass
