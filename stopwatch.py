import time
import sys
import msvcrt

class Stopwatch:
    def __init__(self) -> None:
        self.startTime = None
        self.elapsedTime = 0  # Initialize elapsedTime to 0
        self.isRunning = False

    def startWatch(self):
        if not self.isRunning:
            self.startTime = time.time()
            self.isRunning = True
            print("Stopwatch has started")

    def stopWatch(self):
        if self.isRunning:
            self.elapsedTime = time.time() - self.startTime
            self.isRunning = False
            print("Stopwatch has stopped")

    def resetWatch(self):
        self.elapsedTime = 0
        self.isRunning = False
        print("Stopwatch has been reset")

    def logWatchTime(self):
        totalTime = self.elapsedTime
        if self.isRunning:
            totalTime += time.time() - self.startTime
        print(f'Time: {totalTime:.2f} seconds')

def main():
    stopwatch = Stopwatch()
    print("Press 's' to start, 't' to stop, 'r' to reset, and 'q' to quit.")
    
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch().decode('utf-8').lower()
            if key == 's':
                stopwatch.startWatch()
            elif key == 't':
                stopwatch.stopWatch()
            elif key == 'r':
                stopwatch.resetWatch()
            elif key == 'q':
                print("Exiting...")
                break
        if stopwatch.isRunning:
            stopwatch.logWatchTime()

if __name__ == "__main__":
    main()