from selenium import webdriver
import time
import random
import csv
from datetime import datetime
def auto_likes(id, password, keyword, count):
    cnt = 0;
    user = ""
    nowcomment = ""
    user = ""
    likerow = ["계정", "좋아요여부"]
    today = str(datetime.now().day)
    nowtime = str(datetime.now().microsecond)
    print("좋아요 작업을 시작합니다: 좋아요 목표 " + str(count) + "개, 해시태그 키워드 : " + keyword)

    URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"
    driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(URL)

    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
        id)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
    print("로그인 완료")
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div').click()

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(keyword)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()  # 키워드 검색
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]').click()  # 최근게시물의 첫번째 항목
    print("키워드 검색 후 최근게시물의 첫번째 항목부터 작업합니다.")
    with open('insta_likes' + today + nowtime + '.csv', 'w', -1, newline='')as likes:
        w = csv.writer(likes)
        w.writerow(likerow)
        while (count != cnt):
            try:
                user = str(driver.find_element_by_css_selector('div.e1e1d').text)  # 계정정보
                driver.find_element_by_css_selector('span.fr66n').click()
                likerow[0] = user
                likerow[1] = "완료"
                w.writerow(likerow)
                print("좋아요 : [계정 : " + user + "]")
            except:
                pass

            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()  # 옆으로 넘어감
            cnt = cnt + 1
            print("[현재 작업 수 / 최종 목표] : [" + str(cnt) + "/" + str(count) + "]")
            if (count == cnt):
                break
            else:
                time.sleep(random.randrange(40, 60))
    print("작업완료")


def auto_comment(id, password, keyword, comment, count):
    cnt = 0;
    print("댓글 작업을 시작합니다: 댓글 목표 " + str(count) + "개, 해시태그 키워드 : " + keyword)
    nowcomment = ""
    user = ""
    commentrow = ["계정", "댓글"]
    account_List = []
    today = str(datetime.now().day)
    nowtime = str(datetime.now().microsecond)
    URL = "https://www.instagram.com/accounts/login/?source=auth_switcher"
    driver = webdriver.Chrome("C:\\chromedriver_win32\\chromedriver.exe")
    driver.implicitly_wait(10)
    driver.get(URL)

    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[2]/div/label/input').send_keys(
        id)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[3]/div/label/input').send_keys(password)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div').click()
    print("로그인 완료")
    driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div').click()

    driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys(keyword)
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div').click()  # 키워드 검색
    driver.find_element_by_xpath(
        '//*[@id="react-root"]/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]').click()  # 최근게시물의 첫번째 항목
    print("키워드 검색 후 최근게시물의 첫번째 항목부터 작업합니다.")
    with open('insta_comment' + today + nowtime + '.csv', 'w', -1, newline='')as comm:
        w = csv.writer(comm)
        w.writerow(commentrow)
        while (count != cnt):
            try:
                user = str(driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[2]/div[1]/ul/div/li/div/div/div[2]/h2/div/a').text)  # 계정정보
                driver.find_element_by_xpath(
                    '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').click()
                nowcomment = comment[int(random.randrange(0, len(comment)))]
                commentrow[0] = user
                commentrow[1] = nowcomment
                w.writerow(commentrow)
                print("게시된 댓글 : [계정 : " + user + "/ " + nowcomment + "]")
                if (user in account_List):
                    pass
                else:
                    driver.find_element_by_css_selector('span.fr66n').click()
                    driver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/textarea').send_keys(
                        nowcomment)
                    driver.find_element_by_xpath(
                        '/html/body/div[4]/div[2]/div/article/div[2]/section[3]/div/form/button').click()  # 댓글 게시
                    cnt = cnt + 1
                    print("[현재 작업 수 / 최종 목표] : [" + str(cnt) + "/" + str(count) + "]")
                account_List.append(user)
            except:
                pass
            if (count == cnt):
                break
            driver.find_element_by_css_selector('a._65Bje.coreSpriteRightPaginationArrow').click()  # 옆으로 넘어감
            time.sleep(random.randrange(30, 60))
    print("작업완료")


def main():
    id = "아이디입력"
    password = "비밀번호입력"
    keyword = "좋아요반사"
    count = 200  # 목표작업수
    # auto_likes(id, password, keyword, count)
    comment = ["사진이 너무 이쁘네요.", "사진이 넘 이쁘네요!", "잘보고 갑니다~", "잘보고 갑니다~ 시간되시면 제피드도 놀러와주세요 ㅜㅜ", "잘보고 가요!", "맞팔해요 ~ ", ]
    auto_comment(id, password, keyword, comment, count)


if __name__ == '__main__':
    main()


