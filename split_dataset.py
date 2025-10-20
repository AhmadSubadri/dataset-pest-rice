import os
import random
import shutil
from tqdm import tqdm

# Folder asal dataset kamu (ubah sesuai nama folder kamu sekarang)
source_images = "train/images"
source_labels = "train/labels"

# Folder tujuan hasil split
output_dir = "dataset_split"

# Buat struktur folder baru
splits = ["train", "valid", "test"]
for s in splits:
    os.makedirs(f"{output_dir}/{s}/images", exist_ok=True)
    os.makedirs(f"{output_dir}/{s}/labels", exist_ok=True)

# Ambil semua nama file gambar
images = [f for f in os.listdir(source_images) if f.endswith(('.jpg', '.jpeg', '.png'))]
random.shuffle(images)

# Rasio pembagian
train_ratio = 0.8
valid_ratio = 0.1
test_ratio = 0.1

train_end = int(len(images) * train_ratio)
valid_end = train_end + int(len(images) * valid_ratio)

# Proses pemindahan
for i, img_name in enumerate(tqdm(images, desc="📦 Memindahkan gambar")):
    label_name = os.path.splitext(img_name)[0] + ".txt"

    if i < train_end:
        split = "train"
    elif i < valid_end:
        split = "valid"
    else:
        split = "test"

    # Copy image
    shutil.copy(
        os.path.join(source_images, img_name),
        os.path.join(output_dir, split, "images", img_name)
    )

    # Copy label jika ada
    if os.path.exists(os.path.join(source_labels, label_name)):
        shutil.copy(
            os.path.join(source_labels, label_name),
            os.path.join(output_dir, split, "labels", label_name)
        )

print("\n✅ Dataset berhasil dipisah menjadi train/valid/test di folder 'dataset_split'")
