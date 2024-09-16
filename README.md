# Лабораторная работа по Информатике №1

## Общие пояснения по работе с системой

Здесь описан общий алгоритм выполнения и отправки на проверку ваших лабораторных работ.

Для каждой лабораторной работы существует отдельный репозиторий. По умолчанию в них есть файлы, в которые вы вписываете ваш isu, а также прочую информацию, необходимую для тестирования.

**Первый этап:** 
Делаем форк репозитория.

**Второй этап:** 
Выполняем лабораторную работу в этом форке, а также заполняем config файлы согласно инструкциям в readme для лабы. При каждом коммите будет прогоняться CI-CD, в котором ссылка на ваш форк будет отправлена на сервер, на котором лабораторная работа будет протестирована, а вам возвращен результат, в котором будет указано число пройденных и не пройденных тестов(и опционально текст ошибки).

**Третий этап:** 
Делаем pull request и радуемся.

## Алгоритм заполнения config файлов

**"informatics-lab1.docx"**:\
Файл с вашим отчетом. Название должно остаться таким же.

**"stud-info.json"**:\
Config файл, в котором есть поля:
* **isu** - ваш isu

1 лабораторная тестовая, настоящих тестов здесь нет. Единственный тест - тест на размер шрифта в отчете. Он должен быть не менее 12pt.

