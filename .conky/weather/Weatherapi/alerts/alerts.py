# Lock file to tell conky that the script is running
lock_file = "/tmp/script_wacurrent.lock"
try:
    # Check for file lock
    open(lock_file, 'w').close()
    import os
    import requests
    import textwrap
    from geopy.geocoders import Photon
    geolocator = Photon(user_agent="measurements")
    ################################ get your HOME name automatically
    homepath = os.environ['HOME']
    homename = homepath
    homename = homename[6:]
    ################################ set your latitude, longitude, city and APPID
    mylat = 45.40713
    mylon = 11.87680
    mycity = 'Padova'
    myAPPID = ''
    ################################ pattern url forecast
    #                  my API url forecast (insert between apostrophe, DON'T DELETE THE apostrophe)
    url = 'https://api.weatherapi.com/v1/forecast.json?key=' + myAPPID + '&q=' + mycity + '&days=10&aqi=yes&alerts=yes'
    res = requests.get(url).json()
    data = res
    ################################ set variables
    forecastday = 3
    grouph = 24
    groupa = 3
    temporary = ''
    vtext = 'n/a'
    ################################ set error variables
    coderr = 0
    ################################ set default conky folder (change it if needed)
    home = '/home/'
    conky = '/.conky/'
    defconkyfol = '/weather/Weatherapi/'
    ################################ set the paths for the API files
    ptemp = defconkyfol + 'alerts/'
    ################################ set paths
    ptemp2 = defconkyfol
    ptemp3 = " $HOME" + defconkyfol
    ptemp4 = " $HOME" + defconkyfol + "alerts/"
    ################################ get data for ERROR section
    #                   set the paths for the ERROR
    perr = home + homename + conky + ptemp + '-error.txt'
    ################################ get data for ERROR section
    responseHTTP = requests.get(url)
    # get status code
    status_code = responseHTTP.status_code
    ################################ write raw data for ERROR section
    fo = open(perr, 'w')
    fo.write('error: {}\n'.format(status_code))
    fo.close()
    if status_code != 200:
        #                   set the path for the ALERTS conky section
        pathalertsc = home + homename + conky + ptemp + 'alertsconky.txt'
        fo = open(pathalertsc, 'w')
        fo.write("ERROR: ", status_code)
        fo.close()
    else:
        ################################ get data for ALERTS
        #                   set the array (block=13)
        ahl = []
        ames = []
        asev = []
        aurg = []
        aarea = []
        acat = []
        acert = []
        aevent = []
        anote = []
        aeff = []
        aexp = []
        adesc = []
        ains = []
        #                   get data
        for j in range(0, groupa):
            try:
                ahl.append(data['alerts']['alert'][j]['headline'])
            except:
                ahl.append(vtext)
            try:
                ames.append(data['alerts']['alert'][j]['msgtype'])
            except:
                ames.append(vtext)
            try:
                asev.append(data['alerts']['alert'][j]['severity'])
            except:
                asev.append(vtext)
            try:
                aurg.append(data['alerts']['alert'][j]['urgency'])
            except:
                aurg.append(vtext)
            try:
                aarea.append(data['alerts']['alert'][j]['areas'])
            except:
                aarea.append(vtext)
            try:
                acat.append(data['alerts']['alert'][j]['category'])
            except:
                acat.append(vtext)
            try:
                acert.append(data['alerts']['alert'][j]['certainty'])
            except:
                acert.append(vtext)
            try:
                aevent.append(data['alerts']['alert'][j]['event'])
            except:
                aevent.append(vtext)
            try:
                anote.append(data['alerts']['alert'][j]['note'])
            except:
                anote.append(vtext)
            try:
                aeff.append(data['alerts']['alert'][j]['effective'])
            except:
                aeff.append(vtext)
            try:
                aexp.append(data['alerts']['alert'][j]['expires'])
            except:
                aexp.append(vtext)
            try:
                adesc.append(data['alerts']['alert'][j]['desc'])
            except:
                adesc.append(vtext)
            try:
                ains.append(data['alerts']['alert'][j]['instruction'])
            except:
                ains.append(vtext)
        ################################ choose how many rows write for some alerts variable
        def writedata(var, counter):
            text2 = '-'
            i = counter
            z = 0
            j = 0
            y = 0
            nchars = 100
            myrowsad = 3
            #                 format wmoareaDesc and it writes 3 rows for it (you can change the number of rows you want)
            strlenght = len(var)
            if strlenght == 0:
                var = text2
                #print('{}\n'.format(text2))
            wrapper = textwrap.TextWrapper(width=nchars, max_lines=(myrowsad))
            word_list = wrapper.wrap(text=var)
            for element in word_list:
                fo.write('{}\n'.format(element))
                y = y + 1
                if (strlenght <= nchars) and (y == 1):
                    fo.write('{}\n'.format(text2))
                    #print('{}\n'.format(text2))
                    y = y + 1
                if (strlenght <= nchars*2) and (y == 2):
                    fo.write('{}\n'.format(text2))
                    #print('{}\n'.format(text2))
                    y = y + 1
                # if (strlenght <= nchars*3) and (y == 3):
                #     fo.write('{}\n'.format(text2))
                #     y = y + 1
                # if (strlenght <= nchars*4) and (y == 4):
                #     fo.write('{}\n'.format(text2))
                #     y = y + 1
                # if (strlenght <= nchars*5) and (y == 5):
                #     fo.write('{}\n'.format(text2))
                #     y = y + 1
                # if (strlenght <= nchars*6) and (y == 6):
                #     fo.write('{}\n'.format(text2))
                #     y = y + 1
                # if (strlenght <= nchars*7) and (y == 7):
                #     fo.write('{}\n'.format(text2))
                #     y = y + 1
                if y == 3:
                    y = 0
        ################################ write ALERTS raw data
        #                   set the paths for raw ALERTS
        prawalerts = home + homename + conky + ptemp + '-alerts.txt'
        fo = open(prawalerts, 'w')
        for y in range(0, groupa):
            if ahl[y] != vtext:
                writedata(ahl[y], y)
            else:
                fo.write('headline: {}\n'.format(ahl[y]))
            fo.write('msgtype: {}\n'.format(ames[y]))
            fo.write('severity: {}\n'.format(asev[y]))
            fo.write('urgency: {}\n'.format(aurg[y]))
            fo.write('areas: {}\n'.format(aarea[y]))
            fo.write('category: {}\n'.format(acat[y]))
            fo.write('certainty: {}\n'.format(acert[y]))
            fo.write('event: {}\n'.format(aevent[y]))
            if anote[y] != vtext:
                writedata(anote[y], y)
            else:
                fo.write('note: {}\n'.format(anote[y]))
            fo.write('effective: {}\n'.format(aeff[y]))
            fo.write('expires: {}\n'.format(aexp[y]))
            if adesc[y] != vtext:
                writedata(adesc[y], y)
            else:
                fo.write('desc: {}\n'.format(adesc[y]))
            if ains[y] != vtext:
                writedata(ains[y], y)
            else:
                fo.write('instruction: {}\n'.format(ains[y]))
        fo.close()
        ################################ write ALERTS clean data
        #                   set the paths for clean ALERTS
        pcleanalerts = home + homename + conky + ptemp + 'alerts.txt'
        fo = open(pcleanalerts, 'w')
        for y in range(0, groupa):
            fo.write('{}\n'.format(ahl[y]))
            writedata(ahl[y], y)
            fo.write('{}\n'.format(ames[y]))
            fo.write('{}\n'.format(asev[y]))
            fo.write('{}\n'.format(aurg[y]))
            fo.write('{}\n'.format(aarea[y]))
            fo.write('{}\n'.format(acat[y]))
            fo.write('{}\n'.format(acert[y]))
            fo.write('{}\n'.format(aevent[y]))
            fo.write('{}\n'.format(anote[y]))
            writedata(anote[y], y)
            fo.write('{}\n'.format(aeff[y]))
            fo.write('{}\n'.format(aexp[y]))
            fo.write('{}\n'.format(adesc[y]))
            writedata(adesc[y], y)
            fo.write('{}\n'.format(ains[y]))
            writedata(ains[y], y)
        fo.close()
        ################################ create ALERTS statements for conky
        #       block=29
        rowheada = []
        rowheada1 = []
        rowheada2 = []
        rowheada3 = []
        rowmsga = []
        rowseva = []
        rowurga = []
        rowareaa = []
        rowcata = []
        rowcerta = []
        roweventa = []
        rownotea = []
        rownotea1 = []
        rownotea2 = []
        rownotea3 = []
        roweffa = []
        rowexpa = []
        rowdesca = []
        rowdesca1 = []
        rowdesca2 = []
        rowdesca3 = []
        rowinsa = []
        rowinsa1 = []
        rowinsa2 = []
        rowinsa3 = []
        rowcount = 0
        alertsblock = 25
        rowcolor = '${color}'
        rowcolor1 = '${color1}'
        rowcolor2 = '${color2}'
        rowcolor3 = '${color3}'
        rowcolor4 = '${color4}'
        rowcolor5 = '${color5}'
        rowcolor6 = '${color6}'
        rowcolor9 = '${color9}'
        rowfont6 = '${font URW Gothic L:size=6}'
        rowfont7 = '${font URW Gothic L:size=7}'
        rowfont8 = '${font URW Gothic L:size=8}'
        rowheadinga = rowcolor3 + '${alignc}----------------- ALERTS -----------------'
        for i in range(0, groupa):
                # block control
            rowcount = 1 + (alertsblock * i)
            rowheada.append(rowcolor2 + rowfont7 + "Headline: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowheada1.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowheada2.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowheada3.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}" + rowfont7 + rowcolor)
            rowcount = rowcount + 1
            rowmsga.append(rowcolor2 + "msg: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowseva.append(rowcolor2 + "eva: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowurga.append(rowcolor2 + "urg: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowareaa.append(rowcolor2 + "area: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowcata.append(rowcolor2 + "cat: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowcerta.append(rowcolor2 + "cert: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            roweventa.append(rowcolor2 + "event: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rownotea.append(rowcolor2 + "note: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rownotea1.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rownotea2.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rownotea3.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}" + rowfont7 + rowcolor)
            rowcount = rowcount + 1
            roweffa.append(rowcolor2 + "eff: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowexpa.append(rowcolor2 + "esp: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowdesca.append(rowcolor2 + "desc: " + rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + '}' + rowcolor)
            rowcount = rowcount + 1
            rowdesca1.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + '}' + rowcolor)
            rowcount = rowcount + 1
            rowdesca2.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + '}' + rowcolor)
            rowcount = rowcount + 1
            rowdesca3.append(rowcolor1 + rowfont6 + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + '}' + rowfont7 + rowcolor)
            rowcount = rowcount + 1
            rowinsa.append(rowcolor2 + "instructions: " + rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowinsa1.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowinsa2.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}")
            rowcount = rowcount + 1
            rowinsa3.append(rowcolor + "${execpi 600 sed -n '" + str(rowcount) + "p' " + pcleanalerts + "}" + rowfont7 + rowcolor)
        #                 write conky syntax in alertsconky.txt
        #                   set the path for the ALERTS conky section
        pathalertsc = home + homename + conky + ptemp + 'alertsconky.txt'
        fo = open(pathalertsc, 'w')
        fo.write('{}\n'.format(rowheadinga))
        for i in range(0, groupa):
            fo.write('{}\n'.format(rowheada[i]))
            fo.write('{}\n'.format(rowheada1[i]))
            fo.write('{}\n'.format(rowheada2[i]))
            fo.write('{}\n'.format(rowheada3[i]))
            fo.write('{}\n'.format(rowmsga[i]))
            fo.write('{}\n'.format(rowseva[i]))
            fo.write('{}\n'.format(rowurga[i]))
            fo.write('{}\n'.format(rowareaa[i]))
            fo.write('{}\n'.format(rowcata[i]))
            fo.write('{}\n'.format(rowcerta[i]))
            fo.write('{}\n'.format(roweventa[i]))
            fo.write('{}\n'.format(rownotea[i]))
            fo.write('{}\n'.format(rownotea1[i]))
            fo.write('{}\n'.format(rownotea2[i]))
            fo.write('{}\n'.format(rownotea3[i]))
            fo.write('{}\n'.format(roweffa[i]))
            fo.write('{}\n'.format(rowexpa[i]))
            fo.write('{}\n'.format(rowdesca[i]))
            fo.write('{}\n'.format(rowdesca1[i]))
            fo.write('{}\n'.format(rowdesca2[i]))
            fo.write('{}\n'.format(rowdesca3[i]))
            fo.write('{}\n'.format(rowinsa[i]))
            fo.write('{}\n'.format(rowinsa1[i]))
            fo.write('{}\n'.format(rowinsa2[i]))
            fo.write('{}\n'.format(rowinsa3[i]))
        fo.close()
except Exception as e:
    # Manage exceptions (optional)
    filelockerror = (f"Error during script execution: {e}")
finally:
    # remove lock file
    try:
        os.remove(lock_file)
    except FileNotFoundError:
        pass  # file already removed