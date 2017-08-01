from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
import numpy as np
from scipy.stats import norm
import matplotlib.pyplot as plt
'''
SUBJECT LISTS
'''
ss_list = []
os_list = []
dbms_list = []
cn_list = []
flat_list = []
l1_list = []
l2_list = []
se_list = []
'''
LIST OF NON WORKING USN'S
'''
not_work_usn = [5,14,22,23,32,39,48,52,54,86,98,100,111,113,114,63,65,66]
'''
only 180 students per department
'''

for usn in range (1,180): 
    if usn in not_work_usn:
        usn = usn + 3
    if usn < 10:
        usn = "00" + str(usn)
    elif usn < 100:
        usn = "0" + str(usn)
    fullusn = "[insert 7 char start of usn here]" + str(usn)
    my_url ='http://results.vtu.ac.in/results/result_page.php?usn='+fullusn
    uClient = uReq(my_url)
    page_html = uClient.read()
    # close the connection
    uClient.close()

    # html parsing
    page_soup = soup(page_html, "html.parser")
    table_container = page_soup.findAll("table", {"class": "table table-bordered"})
    Grades_container = table_container[0].findAll("tbody")
    sub_marks = Grades_container[0].findAll("td")
    # print(sub_marks[3])


    i = 0
    while i < len(Grades_container):
        sub_marks = Grades_container[i].findAll("td")
        new_word = str(sub_marks[3])
        ConcatedString = new_word[31] + new_word[32]
        final_marks_ext = int(ConcatedString)
        # print(final_marks_ext," ")
        if i == 0:
            ss_list.append(final_marks_ext)
        elif i == 1:
            os_list.append(final_marks_ext)
        elif i == 2:
            dbms_list.append(final_marks_ext)
        elif i == 3:
            cn_list.append(final_marks_ext)
        elif i == 4:
            flat_list.append(final_marks_ext)
        elif i == 5:
            l1_list.append(final_marks_ext)
        elif i == 6:
            l2_list.append(final_marks_ext)
        elif i == 7:
            se_list.append(final_marks_ext)

        i += 1


#print(ss_list)
#print(dbms_list)
print(os_list)
#ss_list.sort()



def marks_plotter (list_name):
    mu, std = norm.fit(list_name)
    plt.hist(list_name, bins=25, normed=True, alpha=0.7, color='g')
    xmin, xmax = plt.xlim()
    x = np.linspace(xmin, xmax, 100)
    p = norm.pdf(x, mu, std)
    plt.plot(x, p, 'k', linewidth=2)
    title = "Fit results: mu = %.2f,  std = %.2f" % (mu, std)
    plt.title(title)
    plt.show()

marks_plotter(os_list)
marks_plotter(ss_list)
marks_plotter(dbms_list)
marks_plotter(cn_list)
