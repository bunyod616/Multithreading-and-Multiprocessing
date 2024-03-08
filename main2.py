import multiprocessing

def write_to_file(file_path, data):
    with open(file_path, 'w') as file:
        file.write(data)
        print(f"Data written to {file_path}")

def main():
    file_path1 = 'file1.txt'
    file_path2 = 'file2.txt'
    data1 = 'Hello from Process 1!'
    data2 = 'Greetings from Process 2!'

    # Create processes
    process1 = multiprocessing.Process(target=write_to_file, args=(file_path1, data1))
    process2 = multiprocessing.Process(target=write_to_file, args=(file_path2, data2))

    # Start processes
    process1.start()
    process2.start()

    # Wait for both processes to finish
    process1.join()
    process2.join()

    print("Main process continues execution.")

if __name__ == "__main__":
    main()