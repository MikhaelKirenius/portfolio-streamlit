import kagglehub
import os
import shutil

def download_dataset():
    print("[INFO] Downloading dataset from Kaggle...")
    path = kagglehub.dataset_download("vishakhdapat/customer-segmentation-clustering")

    # Pastikan folder data ada
    data_dir = "data"
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Cari file CSV di folder hasil download
    for file_name in os.listdir(path):
        if file_name.endswith(".csv"):
            src = os.path.join(path, file_name)
            dst = os.path.join(data_dir, file_name)
            shutil.copy(src, dst)  # Gunakan copy agar file di cache tetap ada
            print(f"[INFO] Dataset copied to {dst}")


    

if __name__ == "__main__":
    download_dataset()