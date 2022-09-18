from get_image import GetImage

'''Modified this file so it will dowamolad the images
but for more repetitive tasks there need to be some more, better approach.
If links' text are easy to loop it still can be used to dowload some local images, like series of img, png from site'''


def repeted_download(start:int, stop:int) -> None: 
    for i in range(start, stop):
        if i < 10:
            chapter_number = "0" + str(i)
        else:
            chapter_number = str(i)

        j = 1
        run = True
        while run:
            if j < 10:
                page_number = "0" + str(j)
            else:
                page_number = str(j)
            #you add here any url you want if its repetitive
            img = GetImage(f"https://cdn.onepiecechapters.com/file/opctcb/onepiece/onepiecechapters_{chapter_number}_{page_number}.jpg")
            succes = img.download()
            if succes:
                j += 1
            else:
                run = False

if __name__ == "__main__":
    repeted_download(100,101)
    #in this example you can start=1 and stop < 1030, but you can try more if you like
