import os
os.chdir("C:/Users/91738/Videos/Captures/")
for f in os.listdir():
    file_name, file_ext = os.path.splitext(f)
    print(file_name)
    f_date, f_time = file_name.split('')
    # print(f_date)
