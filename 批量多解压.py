import os
import zipfile

def compress_files_to_zips(input_folder, output_folder, max_size_mb):
    """将文件夹中的所有文件分别压缩成多个max_size_mb大小的zip文件。"""
    max_size_bytes = max_size_mb * 1024 * 1024  # 将MB转换为字节
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 获取所有的文件
    files = [os.path.join(input_folder, f) for f in os.listdir(input_folder) if os.path.isfile(os.path.join(input_folder, f))]
    zip_index = 1
    zipf = None

    for file_path in files:
        # 如果当前zip文件为空或即将超过大小限制，创建一个新的zip文件
        if zipf is None or os.path.getsize(zipf.filename) > max_size_bytes:
            if zipf is not None:
                zipf.close()
            
            zip_name = os.path.join(output_folder, f"compressed_part_{zip_index}.zip")
            zipf = zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED)
            zip_index += 1
            print(f"创建新的压缩包: {zip_name}")

        # 将文件添加到zip文件中
        zipf.write(file_path, os.path.basename(file_path))
        print(f"添加文件: {file_path} 到 {zipf.filename}，当前压缩包大小: {os.path.getsize(zipf.filename) / (1024 * 1024):.2f} MB")

    # 关闭最后一个zip文件
    if zipf is not None:
        zipf.close()

    print("所有文件均已压缩完成！")

# 示例用法
input_folder = r'C:\Users\Ac\Desktop\新建文件夹 (2)\新建文件夹 (2)'  # 输入txt文件的文件夹路径
output_folder = r'C:\Users\Ac\Desktop\zip'  # 输出压缩文件的文件夹路径
max_size_mb = 18  # 每个压缩包的最大大小（MB）

compress_files_to_zips(input_folder, output_folder, max_size_mb)