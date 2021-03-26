#
# Создать структуру файлов и папок, как написано в задании 2 (при помощи скрипта или «руками» в проводнике). Написать скрипт, который собирает все шаблоны в одну папку templates, например:
#
# |--my_project
#    ...
#   |--templates
#    |   |--mainapp
#    |   |  |--base.html
#    |   |  |--index.html
#    |   |--authapp
#    |      |--base.html
#    |      |--index.html
# Примечание: исходные файлы необходимо оставить; обратите внимание,
# что html-файлы расположены в родительских папках (они играют роль пространств имён);
# предусмотреть возможные исключительные ситуации; это реальная задача, которая решена,
# например, во фреймворке django
import shutil
import os


folder = '/Users/nikitapurnov/PycharmProjects/Geek HW/Geek_HW7/Task_3/my_project'
directory = [os.path.join(folder, item) for item in os.listdir(folder)]


shutil.copytree('my_project', 'Templates')
shutil.move('Templates', 'my_project')


for item in directory[:2]:
    shutil.rmtree(item)

# PS Надеюсь, что прваильно понял задание