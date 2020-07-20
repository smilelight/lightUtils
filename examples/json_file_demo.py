from lightutils import read_json_line, write_json_line

if __name__ == '__main__':
    for obj in read_json_line('test.json'):
        print(obj)
    with open('./write_json.json', 'w', encoding='utf-8') as file:
        write_json_line(file, {'a': 3})
