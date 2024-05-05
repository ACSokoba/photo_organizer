This is a simple script to organize photos from my phone when I want to save them on my external disks.

before script

```
photos/
├─ 20240409.png
├─ 20221120.png
├─ 20220715.png
├─ 20230715.png
```

after script

```
photos/
├─ 2022/
│  ├─ 20221120.png
│  ├─ 20220715.png
├─ 2023/
│  ├─ 20230715.png
├─ 2024/
│  ├─ 20240409.png
```

How to use it ?

Install python

Run `python file_organizer C:/global/path/to/folder`
