import os
DIR_DOC = "StudentDoc"
DIR_PICTURE = "StudentObrazy"

os.makedirs(DIR_DOC, exist_ok=True)
os.makedirs(DIR_PICTURE, exist_ok=True)

with open(os.path.join(DIR_DOC, "note.txt"), "w", encoding="utf-8") as f:
    f.write("Something something.")

with open(os.path.join(DIR_DOC, "report.txt"), "w", encoding="utf-8") as f:
    f.write("This is report. ADNVLSNDLKVNKLSDNVKLSNDLKBVNKSDNBVSNDKLBNS DBKSDMV;ke mpoqweJ OPSKS DNLKVNSJLDvnljsdnvlkS")

with open(os.path.join(DIR_PICTURE, "schemat.png"), "wb") as f:
    f.write(b"\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR" + b"\x00" * 44)

with open(os.path.join(DIR_PICTURE, "picture.jpg"), "wb") as f:
    f.write(b"\xff\xd8\xff\xe0\x00\x10JFIF" + b"\x1A" * 140)


def show_directory_and_size_of_files(directory):
    print(f"\n📂 Contents of directory: '{directory}'")

    files = os.listdir(directory)

    if not files:
        print(" └── Directory is empty.")
    else:
        for file in files:
            file_path = os.path.join(directory, file)
            size = os.path.getsize(file_path)

            print(f" ├── {file} | Size: {size} bytes")

show_directory_and_size_of_files(DIR_DOC)
show_directory_and_size_of_files(DIR_PICTURE)
