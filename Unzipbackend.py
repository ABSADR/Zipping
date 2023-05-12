import zipfile

def extract_archive(archievepat, dest_dir):
    with zipfile.ZipFile(archievepat, 'r') as archive:
        archive.extractall(dest_dir)

if __name__ == '__main__':
    extract_archive(r"C:\Users\Adrian\OneDrive\Desktop\NewProjects\BonusApps\zippy.zip",
                    r"C:\Users\Adrian\OneDrive\Desktop\NewProjects\BonusApps\destination")


