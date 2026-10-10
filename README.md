# cs-master-road

My journey as a computer science graduate student.

记录 Python、Java、MySQL 的学习练习，以及从练习到完整小工具的过程。

## Goals

- Become a strong software engineer
- Learn backend development
- Learn AI engineering

## 从这里开始

| 内容 | 入口 | 当前内容 |
| --- | --- | --- |
| Python / OOP | [Python 练习](practice/python/) | 类、继承、CSV 读取和 JSON 导出 |
| MySQL | [连接与查询练习](practice/mysql/mysql_test.py) | 连接本机数据库，读取学生表 |
| 学生工具 | [student_tool](projects/student_tool/) | 读取成绩、过滤无效数据、计算平均分 |
| 商品工具 | [product_tool](projects/product_tool/) | 读取商品、过滤无效数据、计算库存总值 |
| Java | [基础练习](java/basics/Main.java) | 控制台输入与条件判断 |
| 科研准备 | [research/zinet](research/zinet/) | 保留模拟脚本位置，目前尚未实现 |

## 目录

```text
practice/
  python/                 # Python / OOP 练习和样例数据
  mysql/                  # MySQL 连接与查询练习
projects/
  student_tool/           # 学生成绩工具及数据
  product_tool/           # 商品库存工具及数据
research/
  zinet/                  # 科研准备
java/
  basics/                 # Java 基础练习
.vscode/                  # VS Code 项目配置
```

## 运行 Python 程序

本机已在 Python 3.10 环境验证。以下命令在仓库根目录的 PowerShell 中执行。
首次下载仓库时先创建虚拟环境；已有 `.venv` 时直接使用即可：

```powershell
py -3 -m venv .venv
```

Python 练习和两个工具只使用标准库：

```powershell
.\.venv\Scripts\python.exe practice/python/oop_basics.py
.\.venv\Scripts\python.exe practice/python/oop_advanced.py
.\.venv\Scripts\python.exe practice/python/oop_practice.py
.\.venv\Scripts\python.exe practice/python/final_check.py
.\.venv\Scripts\python.exe projects/student_tool/student_tool.py
.\.venv\Scripts\python.exe projects/product_tool/main.py
```

工具按脚本所在目录定位 CSV，因此从 VS Code 或其他目录运行也可以找到数据。
各自的 `summary.json` 写入各自目录，运行时会更新对应结果。
当前样例的学生平均分是 **85.0**，商品库存总值是 **4483.0**。

两个工具也支持从仓库根目录通过模块方式启动：

```powershell
.\.venv\Scripts\python.exe -m projects.student_tool.student_tool
.\.venv\Scripts\python.exe -m projects.product_tool.main
```

### MySQL 练习

```powershell
.\.venv\Scripts\python.exe -m pip install PyMySQL
.\.venv\Scripts\python.exe practice/mysql/mysql_test.py
```

运行前需要本机 MySQL 服务，以及已有的 `study_db.students` 表。
脚本使用 `localhost:3306` 和 `root` 账号，只执行查询，不创建数据库或表。
密码在运行时通过终端隐藏输入；也可以从本机 `MYSQL_PASSWORD` 环境变量读取。
请在 VS Code 终端中运行，以便输入密码。

### Java 练习

安装 JDK 后，在仓库根目录执行：

```powershell
javac -encoding UTF-8 java/basics/Main.java
java -cp java/basics Main
```

## 数据与文件约定

- CSV 样例与对应工具放在一起，提交到仓库，方便下载后运行。
- `practice/python/products.csv` 是综合练习自己的样例，与商品工具数据分别维护。
- `input.txt` 和本地 `result.json` 保留自早期词频练习；目前没有对应的现存脚本。
- `result.json`、`students.json`、`summary.json` 为本地输出，不上传 GitHub。
- 虚拟环境、Python 缓存、Java 编译文件和本地 `.env` 配置由 `.gitignore` 忽略。
- `research/zinet/rlcs_sim.py` 目前是空文件，后续研究代码放在这里。

## Progress

2026-09-20:
- Created GitHub account
- Installed Git
- Created first repository
- Set up VS Code

2026-10-10:
- 分开整理语言练习、完整项目和研究目录
- 修正工具的数据路径，验证 OOP、CSV / JSON 工具及 MySQL 查询
- 完善仓库导航与运行说明，改为运行时读取数据库密码
