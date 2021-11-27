# get "start_num, difference, end_num" and print the arithmetic progression


def main():
    start_num, difference, end_num = map(int, input().split())
    print(list(range(start_num, end_num + 1, difference)))


# if __name__ == '__main__':
#     main()

input_str = input()
start_num = int(input_str.split(',')[0])
difference = int(input_str.split(',')[1])
end_num = int(input_str.split(',')[2])

while start_num <= end_num:
    print(start_num, end=' ')
    start_num += difference