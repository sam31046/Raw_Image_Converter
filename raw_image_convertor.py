import rawpy
import imageio
import os


if __name__ == '__main__':

    cwd = os.curdir
    # Create folder for saving results
    save_folder = os.path.join(cwd, "JPG_files")
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)

    raw_images = [f for f in os.listdir(cwd)
                  if os.path.isfile(os.path.join(cwd, f))
                  and ".nef" in f.lower()]

    print(f"All Images: {raw_images}")

    image_count = len(raw_images)
    print(f"Total Raw Images {image_count}")

    for image_num, image in enumerate(raw_images):

        print(f"Process: {image_num + 1}/{image_count}")

        if os.path.isfile(image) is True:
            new_path = os.path.join(
                save_folder, image).replace(".NEF", ".jpg")

            # May be .NEF or .nef
            if ".jpg" not in new_path and ".NEF" in new_path:
                new_path = os.path.join(
                    save_folder, image).replace(".nef", ".jpg")

                if ".jpg" not in new_path:
                    print("Filename Convert Error!")
                    exit(1)

            raw = rawpy.imread(image)
            rgb = raw.postprocess(use_camera_wb=True, bright=1.2)
            imageio.imsave(new_path, rgb)
        else:
            print(f"Error! Image File Not Found: {image}")
            exit(1)

    print("Completed!")
