import threading

def read_file(file_path):
    with open(file_path, 'r') as file:
        data = file.read()
        print(f"Data read from {file_path}: {data}")

def main():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'

    # Create threads
    thread1 = threading.Thread(target=read_file, args=(file_path1,))
    thread2 = threading.Thread(target=read_file, args=(file_path2,))

    # Start threads
    thread1.start()
    thread2.start()

    # Wait for both threads to finish
    thread1.join()
    thread2.join()

    print("Main thread continues execution.")

if __name__ == "__main__":
    main()