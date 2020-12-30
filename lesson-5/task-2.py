# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.

out_f = open("task-2.txt", "r")
count_line = 0
s = 0
for line in out_f:
    if line == '\n':
        continue
    else:
        count_line += 1
        s = len(line.split())
        print (f'В {count_line}-й строке файла {s} слов.')
        s = 0
print (f'В файле {count_line} непустых строк')
out_f.close()
