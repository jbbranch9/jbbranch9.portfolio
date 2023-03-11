from PIL import Image as PIL_Image
import base64


class Base64Factory():

    def base64_string(self, filename: str):
        with open(filename, "rb") as img_file:
            b64_string = base64.b64encode(img_file.read())
            img_file.close()

        return b64_string


def main():
    pass


if __name__ == '__main__':
    main()
