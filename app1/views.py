from django.shortcuts import render

# Create your views here.
def app_view(request):
    return render(request,'wish.html')

def movies_info(request):
    head_msg = 'Movies news!'
    m1 = 'BADHAAI DO’ 2ND WEEK COLLECTIONS FEBRUARY 18-24, 2022 | 26 February, 2022'
    m2 = 'LATEST POSITION | 26 February, 2022‘GANGUBAI KATHIAWADI’ SURPRISES ALL, MARATHI ‘PAWANKHIND’ SCORES'
    m3 = 'With all the old releases except PUSHPA: THE RISE PART 1 having almost exhausted their runs at the ticket-windows'
    m4 = '83 (Hindi and all dubbed versions) netted Rs. 0.77 crore in its sixth weekend, and another Rs. 0.45 crore in the weekdays'
    m5 = 'TIGER 3 21st April, 2023'
    type = 'movie'
    dic = {'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'demo.html',dic)

def sport_info(request):
    head_msg = 'Sports news!'
    m1 = 'Australian cricket icon Shane Warne passes away at 52'
    m2 = 'Women’s World Cup: Problem of plenty yet plenty of problems for Team India'
    m3 = 'Need to work on execution and avoid conceding soft goals: Indian hockey players ahead of Germany Pro League tie'
    m4 = 'Cristiano Ronaldo broke the Bayern Munich Twitter admin in 2017'
    m5 = 'Why did Messi have to leave? - Koeman questions Barcelonas motives following €55 Ferran Torres transfer'
    type = 'sport'
    dic = {'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'demo.html',dic)

def politics_info(request):
    head_msg = 'Politics news!'
    m1 = 'Essential to bring women to centre of politics: Priyanka Gandhi'
    m2 = 'Russia-Ukraine War LIVE Updates: Ukraine Plans Third Round of Peace Talks With Russia'
    m3 = 'Akhilesh Yadav Only Cares For "One Community, One Caste": Amit Shah'
    m4 = 'Chhattisgarh: Journalist Nilesh Sharma arrested for his political satire after Congress accuses him of spreading ‘fake news’'
    m5 = 'A new pole in Indian politics'
    type = 'politics'
    dic = {'head_msg':head_msg,'m1':m1,'m2':m2,'m3':m3,'m4':m4,'m5':m5,'type':type}
    return render(request,'demo.html',dic)