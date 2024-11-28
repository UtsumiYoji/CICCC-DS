import shutil


class View:
    def clear_line(self, lines=1):
        width = shutil.get_terminal_size().columns
        
        for _ in range(lines):
            print("\033[A" + " " * width + "\r", end="", flush=True)