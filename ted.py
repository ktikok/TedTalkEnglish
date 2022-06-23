# -*- coding: utf-8 -*-
"""
Created in 2018

@author: tikim
"""
"""
Spyder Editor

This is a temporary script file.
"""

"""
2021.07.06
this file is tested on Ubuntu
1. 원래는 영어 자막을 클릭했지만, select에서 옵션을 선택하는 것으로 바꿨다.
"""

from selenium import webdriver
from selenium.webdriver.support.select import Select

import time
# for time sleep

from selenium.webdriver.common.keys import Keys
# to scroll up a webpage


special_symbal=[]
for i in range(65,91):
    special_symbal.append(chr(i))
    # capital letters A-Z
for i in range(97,123):
    special_symbal.append(chr(i))
    # a-z

try:
    browser=webdriver.Chrome('chromedriver_linux64/chromedriver')
    print('open linux broswer')
    # for ubuntu
except:
    browser=webdriver.Chrome('chromedriver_win32\chromedriver.exe')
    print('open windows broswer')
    # for windows
browser.maximize_window()
# 브라우저 창을 최대로
browser.get('https://www.ted.com/talks?sort=popular&duration=0-6&language=ko')
# &language=ko&duration=0-6, popular


# bring my finished video titles
try:
    with open('finished_videos.txt', encoding='utf-8') as f:
        # for windows and linux os
        f_list=f.readlines()
        print('open utf8 file')
        #print(f_list[0])
except: 
    with open('finished_videos.txt', encoding='cp949') as f:
        f_list=f.readlines()
        print('open linux file')
        #print(f_list)   


for i in range(1,999):
    title = browser.find_element_by_xpath('//*[@id="browse-results"]/div[1]/div['+str(i)+']/div/div/div/div[2]/h4[2]/a').text
    #print('i1 :',i)    
    if title+'\n' not in f_list:
        #print('X')
        # check if I have already finished the video or not 
        try:
            browser.find_element_by_xpath('//*[@id="browse-results"]/div[1]/div['+str(i)+']/div/div/div/div[2]/h4[2]/a').click()
            print('clicking title')
            # my laptop title
            # //*[@id="browse-results"]/div[1]/div[6]/div/div/div/div[2]/h4[2]/a 
            # picture
            # //*[@id="browse-results"]/div[1]/div[6]/div/div/div/div[1]/a/span/span[1]/span/img
            # picture link
            # //*[@id="browse-results"]/div[1]/div[6]/div/div/div/div[1]/a
            break
        except:
            for j in range(10):
                time.sleep(1)
                try:
                    browser.find_element_by_xpath('//*[@id="browse-results"]/div[1]/div['+str(i)+']/div/div/div/div[1]/a').click()
                    print('clicking picture')
                    # my laptop
                    # //*[@id="browse-results"]/div[1]/div[5]/div/div/div/div[2]/h4[2]/a
                    break        
                except:
                    pass
            break
            #print('i2 :',i)
print('Title :',title)

# print(f_list[0])
# print(title)
# print(f_list[0]==title+'\n')
# click transcript
for i in range(10):
    try:
        browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[1]/div/a[3]').click()
        # If there are theree options
        print('there are three options')
        break
    except:
        try:
            browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[1]/div/a[2]/span[1]').click()
            # if there are two options : details, transicript
            print('there are two options')
            break
        except:
            try:
                browser.find_element_by_xpath('//*[@id="tabs--1--tab--1"]/span').click()
                # if the pane is located on the left
                print('options are located on the right side of the webpage')
                break
            except:
                print('Waiting for webpage(I will click "transcript")')
                time.sleep(1)
                # sometimes, loading elements takes long time.

select_element = browser.find_element_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div[1]/div[1]/select')
# 목차 가져오기
select_object = Select(select_element)
select_object.select_by_visible_text('English')
# 영어 선택하기

for i in range(10):
    try:
        browser.find_element_by_xpath('//*[@id="ted-player"]/div[4]/div/div/div[2]/div/div[5]/button').click()
        break
    except:
        print('loading for subtitle controls')
        time.sleep(1)
        # click subtitle controls
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[2]/div/div[1]/button').click()
# click 'off'
browser.find_element_by_xpath('/html/body/div[3]/div/div/div/div[1]/div/button').click()
# click 'x'

for i in range(10):
    try:
        english_sentences=browser.find_elements_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div/div[2]/p/span/a') 
        # this for big window
        # //*[@id="content"]/div/div[4]/div[2]/section/div/div[2]/p/span/a
        # //*[@id="content"]/div/div[4]/div[2]/section/div[2]/div[2]/p/span[1]/a
        # //*[@id="content"]/div/div[4]/div[2]/section/div[2]/div[2]/p/span[1]/a
        # //*[@id="content"]/div/div[4]/div[2]/section/div[3]/div[2]/p/span[1]/a
        #  시간 별로 파트가 나눠진 경우까지 포함하기 위해서 div[2]>div로 바꿈.
        #print(english_sentences)
        break
    except:
        print('Wating for webpage(bringing sentences)')
        time.sleep(1)

print("how many sentences? :",len(english_sentences))

url=browser.current_url

f=open('score_list7.txt')
# f=open('score_score.txt')
f_list=f.readlines()
writer_title1=f_list[-1].split(' ')[3]
# writer_title1=f_list[-1].split(' ')[3].split('/')[4]
# title, in the text file
writer_title2=url.split('/')[4]
# webpage's title

if writer_title2==writer_title1:
    # if int(f_list[-1].split(' ')[1])+int(f_list[-1].split(' ')[0])<len(english_sentences):
    #     # if wrong + crrect < total sentence nunber
    #     answer_count=[int(f_list[-1].split(' ')[0]), int(f_list[-1].split(' ')[1]), 0, url]
    #     # [correct, wrong, 0, url]
    #     for i in f_list[-1].split(' ')[4:-1]:
    #         answer_count.append(int(i))
    # elif len(f_list[-1].split(' ')[4:-1])<len(english_sentences):
    #     answer_count=[0,0,0,url]
    #     for i in f_list[-1].split(' ')[4:-1]:
    #         answer_count.append(int(i))
    if len(f_list[-1].split(' ')[4:-1])<len(english_sentences):
        answer_count=[0,0,int(f_list[-1].split(' ')[2]),writer_title2]
        for i in f_list[-1].split(' ')[4:-1]:
            answer_count.append(int(i))        
    else:
        answer_count=[0,0,0,writer_title2]
else:        
    answer_count=[0,0,0,writer_title2]
    # answer_count=[0,0,0,url]

f.close()
english_count=[answer_count[2]]
# english_count=[answer_count[0]+answer_count[1]]
#'''
#print(url)

def pause(pause_count):
    # I hope that one of these bottons will work.

    if pause_count==10:
        pass
    else:
        try:
            # //*[@id="ted-player"]/div[4]/button
            # //*[@id="ted-player"]/div[4]/div/div/div[2]/div/div[1]/button
            # //*[@id="ted-player"]/div[3]/button
            browser.find_element_by_xpath('//*[@id="ted-player"]/div[3]/button').click()# 버튼이 보여야함, 자막이 없으면 'div3', 있으면 'div4'
            #print("script off")
        except:
            try:
                browser.find_element_by_xpath('//*[@id="ted-player"]/div[3]/div/div/div[2]/div/div[1]/button').click()
            except:
                try:
                    browser.find_element_by_xpath('/div/div/div[2]/div/div[1]/button').click()
                except:
                    try:
                        browser.find_element_by_xpath('//*[@id="ted-player"]/div[4]/button').click()# 2021.07.01추가
                        
                        #print("script on")
                    except:
                        try:
                            # //*[@id="ted-player"]/div[4]/button
                            # //*[@id="ted-player"]/div[4]/button
                            browser.find_element_by_xpath('//*[@id="ted-player"]/div[4]/div/div/div[2]/div/div[1]/button').click()# 2021.07.01추가
                            #print("clicked play button")
                        except:
                            try:
                                browser.find_element_by_xpath('//*[@id="ted-player"]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div/button').click()# cancel moving on next video
                                #                              //*[@id="ted-player"]/div[3]/div[2]/div/div/div[2]/div/div[1]/div/div/div/button
                                print("You've finished the last line. Congratulation")
                            except:
                                try:
                                    browser.find_element_by_xpath('//*[@id="ted-player"]/div[3]/button').click() 
                                    # windows, on my laptop
                                except:
                                    print("try to pause again")
                                    browser.find_element_by_tag_name('html').send_keys(Keys.HOME)

                                    time.sleep(0.1)
                                    pause(pause_count+1)
                

def english(english_count):
    print('')
    if english_count!=1:
        print(english_sentences[english_count-2].text)
    words = english_sentences[english_count-1]
    words=words.text
    letter=''
    for words_1 in words:
        if (letter not in special_symbal):
            print(words_1,end='')
            letter=words_1
        elif(words_1 not in special_symbal):
            print(words_1,end='')
            letter=words_1
        else:
            print('*',end='')
            letter=words_1
    print('')#이게 없으면 어디까지가 정답인지 모르뮤ㅠ

def play(sentences,english_count):
    if english_count==1:
        #print(sentences[english_count-1])
        for i in range(10):
            try:
                sentences[english_count-1].click()
                break
            except:
                print("trying to click a sentence")
                time.sleep(1)
    else:
        sentences[english_count-2].click()

    browser.find_element_by_tag_name('html').send_keys(Keys.HOME)

def finish(url):
    global answer_count

    # answer_count[2]=answer_count[0]/(answer_count[1]+answer_count[0])
    # answer_count[2]=answer_count[0]/(answer_count[0]+answer_count[1])
    answer_count[2]=english_count[0]
    f=open('score_list7.txt','a')
    for i in answer_count: 
        f.write('%s ' % str(i))
    f.write('\n')
    f.close()
    print('it is',english_count[0],'th sentence')
    print('correct : ', answer_count[0], 'wrong : ', answer_count[1])
    print('score:',answer_count[0]/(answer_count[0]+answer_count[1]))
    print('done')
    

        
def main(url):
    #english_count=8
    #sentence_count=0
    #print(answer_count)
    #print(english_count)
    global english_sentences
    print("you will listen", len(english_sentences)-len(answer_count[4:]), "lines")
    
    if english_count[0] != 0:
        english_count[0] = english_count[0] - 1
    
    while(english_count[0]<len(english_sentences)):
        #sentence_count=sentence_count+1
        english_count[0]=english_count[0]+1
        if english_count[0] in answer_count[4:]:
            
            #print(english_count[0])
            
            # answer_count[0]=answer_count[0]+1
            continue
            
        english(english_count[0])
            
        play(english_sentences,english_count[0])
        answer=(english_sentences[english_count[0]-1]).text
        while(1):
            #print((english_sentences[english_count+sentence_count-1]).text)
            guess=input()
            check=1
            for i, j in zip(guess,answer):
                if i != j and i in special_symbal:
                    check=0
                    break
                else:
                    pass
                
            if(guess==''):
                pause(0)
            
            elif(guess=='reload'):
                pause(0)
                #print(url)
                #print(url.split('=')[0]+'=en')
                browser.get(url.split('=')[0]+'=en')
                # reload page
                # break
                while (guess != 'ok' ):
                    guess=input()     
                english_sentences=browser.find_elements_by_xpath('//*[@id="content"]/div/div[4]/div[2]/section/div/div[2]/p/span/a') # this for big window

            elif(guess=='save'):
                raise
            
            elif check==1 and len(guess)==len(answer):                    
                #print('Correct answer!')
                answer_count[0]=answer_count[0]+1
                answer_count.append(english_count[0])
                break
            else:
                print(english_sentences[english_count[0]-1].text)
                print('Wrong answer!')
                answer_count[1]=answer_count[1]+1
                break
    print('\ncorrect : ', answer_count[0], 'wrong : ', answer_count[1], 'score:',answer_count[0]/(answer_count[0]+answer_count[1]))
    if len(answer_count[4:]) != english_count[0]:
        answer_count[0]=0
        answer_count[1]=0
        # answer_count[2]=0
        english_count[0]=0
        
        main(url)
    else:
        f=open('finished_videos.txt', 'a', encoding='utf-8')
        f.write('%s' % str(title))
        f.write('\n')
        f.close()

if __name__=='__main__':
    try:
        #print("you will listen", len(english_sentences), "lines")
        print('if you want to do some thing, use the below special keywords.')
        print("reload : reload your webpage(use something goes wrong)\nsave : raise an error and your progress will be saved\nenter : if you want to pause or play your video, enter without any other letter")
        main(url)
        print("\nno error in main function")
        finish(url)
    except:
        print("An error has occurred in main function.")
        finish(url)
        raise
        # two see error log
