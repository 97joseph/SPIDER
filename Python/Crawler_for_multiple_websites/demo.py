import os

#Create and check if directory exists

def create_project_dir(directory):
    if not os.path.exists(directory):
        print("Creating the directory"+directory)
        os.makedirs(directory)

def create_data_files(project_name,base_url):
    queue=os.path.join(project_name,'queue.txt ')
    crawled=os.path.join(project_name,'crawled.txt')
    if not os.path.isFile(queue):
        write_file(queue,base_url)
    if not os.path.isfile(crawled):
        write_file(crawled,'')

def write_file(path,data):
    with open(path,'w')as f:
        f.write(data)
    

def append_to_file(path,data):
    with open(path,'a') as f:
        f.write(data,'\n')

def delete_file_contents(path):
    open(path,'w').close()


#Speed up execution by allowing data conversion to a set for RAM handling as opposed to the hard-disk
#Copy the contents of a file into  a set

def file_to_set(file_name):
    results=set()
    with open(file_name,'rt') as f:
        for line in f:
            results.add(line.replace('\n',''))
    return results

#Return copy the contents of  a file from a set to a file

def set_to_file(links,file_name):
    with open(file_name,"w") as f:
        for l in sorted(links):
            f.write(l+"\n")