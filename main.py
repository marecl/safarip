import sys
import time
import os
import filetype
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from watchdog.events import FileCreatedEvent


class Handler(FileSystemEventHandler):

    def nop(self, src_path: str, extension: str):
        print(f"Detected: [{extension}]\t{os.path.basename(src_path)}")
        return

    def copy_file(self, src_path: str, extension: str):
        file_name = os.path.basename(src_path)
        dst_path = os.path.join(self.output_dir, file_name)
        if not os.path.exists(src_path):
            print(f"File disappeared before copying: {src_path}")

        os.system(f'cp "{src_path}" "{dst_path}.{extension}"')
        filetype.application_match
        print(f"Copied: [{extension}]\t{file_name}")
        return

    def __init__(self, watch_dir: str, output_dir: str | None = None):
        self.watch_dir = watch_dir
        self.output_dir = output_dir
        self.copy_to_target_cb = self.nop if self.output_dir is None else self.copy_file
        self.files_detected = 0

    def on_created(self, event):
        if event.is_directory:
            return

        file_extension = filetype.guess_extension(event.src_path)
        file_extension = file_extension or "none"
        self.files_detected += 1

        self.copy_to_target_cb(event.src_path, file_extension)


class OnMyWatch:
    # Set the directory on watch
    watch_dir = os.path.join(
        os.environ["HOME"],
        "Library/Containers/com.apple.Safari/Data/Library/Caches/com.apple.Safari/WebKitCache/Version 17/Blobs",
    )

    def __init__(self, output_dir: str | None = None):
        self.observer = Observer()
        self.output_dir = output_dir

    def run(self):
        event_handler = Handler(self.watch_dir, self.output_dir)
        self.observer.schedule(
            event_handler,
            self.watch_dir,
            recursive=False,
            event_filter=[FileCreatedEvent],
        )
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

        return event_handler.files_detected


if __name__ == "__main__":
    copy_destination = None
    if len(sys.argv) > 1:
        copy_destination = sys.argv[1]
        if not os.path.exists(copy_destination):
            print("Target directory doesn't exist")
            copy_destination = None

    print(f"Watching: {OnMyWatch.watch_dir}")
    if copy_destination is None:
        print("Output directoy not specified")
    else:
        print("Output directory:", copy_destination)
    input("Press ENTER to begin")
    watch = OnMyWatch(copy_destination)
    files_detected = watch.run()

    print("Files detected:", files_detected)
