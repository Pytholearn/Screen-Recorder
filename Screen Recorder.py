import cv2
import numpy as np
from PIL import ImageGrab


def screenRec():

    # طعریف کد اصلی
    fourcc = cv2.VideoWriter_fourcc(*'XVID')

    # بهش میگیم با چه اف پی اسی ظبت کنه
    fps = 8.0

    # تنظیم خروجی کد
    out = cv2.VideoWriter('output.avi', fourcc, fps, (1366, 768))

    while(True):

        # گزاشتن عکس برای اول ویدیو
        img = ImageGrab.grab()

        # تبدیل عکس به حالت نام پای
        img_np = np.array(img)

        # ساخت فریم و ارجی بی کردن اون
        frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)

        # ساخت صفحه اصلی و نمایش دسکتاپ در ان
        win_title = "Screen Recorder"
        cv2.imshow(win_title, frame)

        # گرفتن خروجی
        out.write(frame)

        # wait for 'q' key to stop recording (program)
        if(cv2.waitKey(1) & 0XFF == ord('~')):
            break

    # بستن تمام پنجره ها
    out.release()

    # de-allocate any associated memory usage
    cv2.destroyAllWindows()


# برگشت
screenRec()