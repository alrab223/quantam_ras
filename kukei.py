import cv2 as cv
def main():
    # ファイルを読み込み
    image_file = 'target.jpg'
    src = cv.imread(image_file, cv.IMREAD_COLOR)
    img_gray = cv.cvtColor(src, cv.COLOR_RGB2GRAY)
    # 結果を保存
    cv.imwrite('result.jpg', img_gray)
    
if __name__ == '__main__':
    main()