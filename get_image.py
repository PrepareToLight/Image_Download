import requests # to get image from the web
import shutil # to save it locally

## Set up the image URL and filename 
class GetImage:
    def __init__(self, url:str) -> None:
        self.url = url
        self.run = True
        self.i = 1

    def download(self):
        filename = self.url.split("/")[-1]
        # Open the url image, set stream to True, this will return the stream content.
        r = requests.get(self.url, stream = True)
        # Check if the image was retrieved successfully
        if r.status_code == 200:
            # Set decode_content value to True, otherwise the downloaded image file's size will be zero.
            r.raw.decode_content = True
            
            # Open a local file with wb ( write binary ) permission.
            with open(filename,'wb') as f:
                shutil.copyfileobj(r.raw, f)

            print('Image sucessfully Downloaded: ', filename)
            return True
        else:
            print("Image Couldn't be retreived")
            return False


def test():
    img = GetImage("https://sbanaszek.w3spaces.com/441c0ddc_1.png")
    img.download()

if __name__ == "__main__":
    #test()
    pass