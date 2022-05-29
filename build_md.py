
import os


source_path = os.path.join('.','source')
markdown_path = os.path.join(source_path,'_posts')
image_path = os.path.join(source_path,'image')


def make_mk(file_path):
    file_name,file_ext = os.path.splitext(file_path)
    file_data = '''
---
title: %s
date: 2022-05-29 08:43:19
tags:
cover_index: /image/%s
---
![%s](/image/%s)
''' % (file_name,file_path,file_name,file_path)

    return file_data

def filter_exist_data(image_list,md_list):
    result = []

    for image_file_path in image_list:
        image_file_name,_ = os.path.splitext(image_file_path)
        md_image_file_name = '%s.md' % (image_file_name)
        
        if not md_image_file_name in md_list:
            result.append(image_file_path)

    return result

def filter_remove_data(image_list,md_list):
    process_image_name_list = []

    for image_file_path in image_list:
        image_file_name,_ = os.path.splitext(image_file_path)
        process_image_name_list.append(image_file_name)

    result = []

    for md_file_path in md_list:
        md_file_name,_ = os.path.splitext(md_file_path)
        
        if not md_file_name in process_image_name_list:
            result.append(md_file_path)

    return result

def create_new_markdown(file_path,file_data):
    file_path = os.path.join(markdown_path,file_path)
    file = open(file_path,'w')

    file.write(file_data)
    file.close()


if __name__ == '__main__':
    image_list = os.listdir(image_path)
    md_list = os.listdir(markdown_path)
    new_image_list = filter_exist_data(image_list,md_list)
    remove_md_image_list = filter_remove_data(image_list,md_list)

    if not new_image_list:
        print('no new image')
        exit()

    for image_index in new_image_list:
        image_name,_ = os.path.splitext(image_index)
        image_name += '.md'
        new_md_data = make_mk(image_index)

        create_new_markdown(image_name,new_md_data)

    print('build new markdown for pic Success!')

    if not remove_md_image_list:
        print('no remove image')
        exit()

    for md_image_index in remove_md_image_list:
        os.remove(os.join(markdown_path,md_image_index))

    print('remove old markdown Success!')
