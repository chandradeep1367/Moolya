*** Variables ***
#common locators for all
${URL}                https://coinswitch.co/pro/
${WebDriver}          chrome

${text_on_assertion} =        Xpath =    (//*[contains(text(),'The only trading platform you’ll need')])
${Sheet_id} =         1GuQUYMkLPPlw1qAWVG0y2oh7_SXHz7z5W13cMgYEC9M
${location_of_json} =      C://Users//Hp//Desktop//Robot Framework Final//moolya1-9deed4cfd190.json


#____****************** Xpaths for coinpages************************___________

${webpage_data}     =             //*[@class='tw-text-center tw-text-3xl
...    tw-font-extralight md:tw-max-w-lg md:tw-text-5xl']


#_____**************Api data *****************___________

${base_url} =            https://coinswitch.co/pro/
${Resouces_url}          api/v1/realtime-rates/depth?symbol=btc,inr&exchange=csx

${Domain_url}            api/v1/realtime-rates
${end_point_btc}         depth?symbol=btc
${end_point_gas}         depth?symbol=gas
${end_point_Url2}         ,inr&exchange=csx
# https://coinswitch.co/pro/api/v1/realtime-rates/depth?symbol=gala,inr&exchange=csx
#___________*******get lowest price xpaths*********_________

${scroll_tittle}=        xpath =        //*[@class='tw-h-4 tw-w-36']
${getlowprice}=          xpath =        (//*[contains(text(),'Get Lowest Price')])
${dropdown_exc}=         xpath =         //*[@class='tw-h-6 tw-w-6']
${wazir}=                xpath =        (//*[@class='tw-text-gray-400 tw-font-normal tw-text-xs lg:tw-text-sm'])[2]
${bit_coin}=            xpath =     (//*[contains(text(),'Buy Bitcoin')])[2]
${pop_up1}=             Xpath =        (//*[contains(text(),'EXPLORE')])
${pop_up2}=             xpath =        (//*[contains(text(),'Skip All')])
${pop_up3}=             xpath =        (//*[contains(text(),'Done')])

${value_path}=          xpath =        //input[@name='limit_price']
${lowest_price}=        xpath =        (//*[contains(text(),'Get Lowest Price')])

#Xpath for the TC_001
${Buy_bitcoinbtn}=      xpath =        (//*[@class='tw-group tw-relative tw-flex 
...    tw-min-w-fit tw-cursor-pointer tw-items-center'])[1]

#Xpath for the TC_002
${Buy_Ethereum}=               xpath =        (//*[@class='tw-group tw-relative tw-flex 
...    tw-min-w-fit tw-cursor-pointer tw-items-center'])[2]    
#Xpath for the TC_003
${Buy_tether}=                 xpath =        (//*[@class='tw-group tw-relative tw-flex tw-min-w-fit
...    tw-cursor-pointer tw-items-center'])[3]   
#Xpath for the TC_004
${Dropdown_of_products}=        xpath =        (//*[contains(text(),'Products')])[2]
${Dropdown_list}=               xpath =        (//*[contains(text(),'Crypto Rupee Index')])[2]
${Productpage_name}=            xpath =        (//*[contains(text(),'Crypto Rupee Index (CRE8)')])[1]

#XPath for TC_005
${Dropdown_of_company}  =        xpath =     (//*[contains(text(),'Company')])[2]
${Dropdown1_list}       =        xpath =     (//*[contains(text(),'About Us')])[2]
${companypage_name}     =        xpath =     (//*[contains(text(),'About Us')])[3]

#XPath for TC_006
${Multipl Exchanges, One Platform} =             xpath =    (//*[contains(text(),'Try Now')])[1]
${Preform_Multipl Exchanges, One Platform} =     xpath =    (//*[contains(text(),'Try Now')])[1]

#Xpath for TC_007 
${Rupee-Powered} =            xpath =        (//*[contains(text(),'Try Now')])[2]
${Preform_Rupee-Powered} =    xpath =        (//*[contains(text(),'Try Now')])[2] 

#Xpath for TC_008
${Data-Driven Decisions} =               xpath =        (//*[contains(text(),'Try Now')])[2]
${Preform_Data-Driven Decisions} =       xpath =        (//*[contains(text(),'Try Now')])[2] 

