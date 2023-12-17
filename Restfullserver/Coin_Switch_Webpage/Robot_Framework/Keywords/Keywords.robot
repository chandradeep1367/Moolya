
*** Settings ***
Library    SeleniumLibrary
Library    chromedriver_binary
Library    RPA.Cloud.Google
Library    String
Library    JSONLibrary
Library    Collections
Library    XML
Library    RequestsLibrary


Resource    C:/Users/Hp/Desktop/Coin_Switch_Webpage/Robot_Framework/Locators/Locators.robot

*** Keywords ***
Open Browser And navigated to URL
    Open Browser    ${Url}    ${WebDriver}
    Maximize Browser Window
    Init Sheets    ${location_of_json}
#Tc_001
Clik on Buy Bitcoin button
    Wait Until Element Is Visible    ${Buy_bitcoinbtn}
    
Navigate to bit coin trade page
    Click Element    ${Buy_bitcoinbtn}
    Log To Console    User has navigated to Buy_bitcoinbtn trade page
    
Verify the tittle on navigated page bitcoin
   # ${actual_title}    Set Variable   BTC to INR | Buy BTC in India at best price at ₹24,56,206 | CoinSwitch
    ${current_title}    Get Title    
    Log To Console    Current Page Title: ${current_title} 
    #Should Be Equal    ${actual_title}    ${current_title}        
    Log To Console    User has landed in buy_bit_coin trade page.

Return back to home page form bitcoin page
 
    Go To    ${url}


#Tc_002
Click on 'Buy Ethereum' button
    Wait Until Element Is Visible    ${Buy_Ethereum}
    Click Button    ${Buy_Ethereum}
    
Navigate to Ethereum trade page
    Log To Console    User has navigated to Buy Ethereum  trade page
    
Verify the tittle on navigated page of Ethereum
   # ${actual_title}    Set Variable   BTC to INR | Buy BTC in India at best price at ₹24,56,206 | CoinSwitch
    ${current_title}    Get Title    
    Log To Console    Current Page Title: ${current_title} 
    #Should Be Equal    ${actual_title}    ${current_title}        
    Log To Console    User has landed in Buy Ethereum trade page.

Return back to home page from ethereum trade page 
    Go To    ${url}

#TC_003
Click on 'Buy Tether' button
    Wait Until Element Is Visible    ${Buy_tether}
    Click Button    ${Buy_tether}
    
Navigate to Tether trade page
    Log To Console    User has navigated to Buy Tether trade page
    
Verify the tittle on navigated page of Tether
   # ${actual_title}    Set Variable   BTC to INR | Buy BTC in India at best price at ₹24,56,206 | CoinSwitch
    ${current_title}    Get Title    
    Log To Console    Current Page Title: ${current_title} 
    #Should Be Equal    ${actual_title}    ${current_title}        
    Log To Console    User has landed in Buy Tether trade page.

Return back to home page from Tethe page
    Go To    ${url}

#TC_004
Mouse over on 'Products Dropdown'
    Wait Until Element Is Visible    ${Dropdown_of_products}
    Mouse Over    ${Dropdown_of_products}
Select 'Crypto Rupee Index' from dropdown and navigate to next page    
    Wait Until Element Is Visible    ${Dropdown_list}
    Click Element    ${Dropdown_list}
    Sleep    3s

Assert product name is same are not    
    ${actual_productpage_name} =    Set Variable    Crypto Rupee Index (CRE8)
    ${Expected_name} =   Get Text     ${Productpage_name}
    Should Be Equal    ${Expected_name}    ${actual_productpage_name}
    Log To Console    Productpage name has matched

Return back from product Page to home page   
    Go To    ${URL}

#TC_005
Mouse over on 'Company Dropdown'
    Wait Until Element Is Visible    ${Dropdown_of_company}
    Mouse Over    ${Dropdown_of_company}
Select 'About Us' from dropdown and navigate to next page    
    Wait Until Element Is Visible    ${Dropdown1_list}
    Click Element    ${Dropdown1_list}
    Sleep    3s

Assert company name is same are not    
    ${actual_Companypage_name} =    Set Variable    About Us
    Wait Until Element Is Visible    ${companypage_name}
    ${Expected_name1} =   Get Text     ${companypage_name}
    Should Be Equal    ${Expected_name1}     ${actual_Companypage_name}
    Log To Console    companypage name has matched

Return back from company Page to home page   
    Go To    ${URL}

#TC_006
Scroll till 'Multipl Exchanges, One Platform' in coinswitch page
    Scroll Element Into View    ${Multipl Exchanges, One Platform}

Click on Try Now button in Multipl Exchanges, One Platform module   
    Click Button    ${Preform_Multipl Exchanges, One Platform}

Verify the tittle on navigated page of one platform
    ${current_title4}    Get Title    
    Log To Console    Current Page Title: ${current_title4}        
    Log To Console    User has landed in multiple Exchamge, one platform trade page.

Return back to home page from one platform
    Go To    ${url}

#TC_007
Scroll till 'Rupee-Powered' in coinswitch page
    Scroll Element Into View    ${Rupee-Powered}

Click on Try Now button in Preform_Rupee-Powered  
    Click Button    ${Preform_Rupee-Powered}

Verify the tittle on navigated page Rupee Powered
    ${current_title4}    Get Title    
    Log To Console    Current Page Title: ${current_title4}        
    Log To Console    User has landed in multiple Exchamge, one platform trade page.

Return back to home page from Rupee Powered
    Go To    ${url}

#TC_008
Scroll till 'Data-Driven Decisions' in coinswitch page
    Scroll Element Into View    ${Data-Driven Decisions}

Click on Try Now button in Data-Driven Decisions module
    Click Button    ${Preform_Data-Driven Decisions}

Verify the tittle on navigated page from Data Driven Decisions
    ${current_title4}    Get Title    
    Log To Console    Current Page Title: ${current_title4}        
    Log To Console    User has landed in multiple Exchamge, one platform trade page.

Return back to home page
    Go To    ${url}
# Extracting the Api and validating with web page value
#Tc__009
Navigate to coin switch URL
    Wait Until Element Is Visible    ${text_on_assertion}    
    
Read the values from google Sheet_id
    Init Speech To Text    ${location_of_json}
Assert the web page dispaly message in langing page of coinSwitch webpage

    ${spreadsheet_data} =    Get Sheet Values    ${Sheet_id}    Sheet1!A1:A1
    ${convert_to_string} =    Set Variable    ${spreadsheet_data}
    ${json_data}    Evaluate    eval('''${convert_to_string}''')
    ${googlesheet_data}    Set Variable    ${json_data['values'][0][0]}
    ${webpage} =    Set Variable    The only trading platform you’ll need
    Should Be Equal    ${webpage}    ${googlesheet_data}
    Log To Console    ${googlesheet_data}

#Tc__010
User Verifes The Headers In coiswitch pro page
    
    # Go To    ${base_url}
    Wait Until Element Is Visible    ${bit_coin}    
    Click Element    ${bit_coin}   
    Wait Until Element Is Visible    ${pop_up1} 
    Sleep    5s   
    Click Element    ${pop_up1}
    Wait Until Element Is Visible    ${pop_up2}   
    Sleep    5s
    Click Element    ${pop_up2} 
    Wait Until Element Is Visible    ${pop_up3}  
    Sleep    5s
    Click Element    ${pop_up3}  
    Scroll Element Into View    ${scroll_tittle}

User Verifes The Headers In coiswitch pro page2
    Sleep    15s
    Go To    ${base_url}
    Wait Until Element Is Visible    ${bit_coin}    
    Click Element    ${bit_coin}
    Wait Until Element Is Visible    ${getlowprice}
    Sleep    10s
    Click Element    ${getlowprice}
    Wait Until Element Is Visible    ${value_path}    30s
    ${lowest_price_value} =    Get Element Attribute    ${value_path}    value
    Log To Console    ${lowest_price_value}
    Set Suite Variable    ${lowest_price_value}

  
Retrieve Data From API and Verify Lowest Price
    [Arguments]    ${Exchange_keys}    
    Create Session    MySession    ${URL}
    ${Domain_url} =    Get On Session    MySession    ${Domain_url}/${Exchange_keys}${end_point_Url2}
    Log To Console    ${Domain_url.content}
    ${Value} =    Get Value From Json    ${Domain_url.json()}    $..asks[0][0]
    ${Lowest_Price} =    Get From List    ${Value}    0
    Log To Console    ${Lowest_Price}
    Set Suite Variable    ${Lowest_Price}
    
    User Navigates To Buy Bitcoin Header And Verify the Lowest Price Button
    
User Navigates To Buy Bitcoin Header And Verify the Lowest Price Button
    
    User Verifes The Headers In coiswitch pro page
    Click Element    ${getlowprice}
    Wait Until Element Is Visible    ${value_path}    30s
    ${lowest_price_value} =    Get Element Attribute    ${value_path}    value
    Log To Console    ${lowest_price_value}
    Set Suite Variable    ${lowest_price_value}
    
    # Wait Until Element Is Visible    ${dropdown_exc}
    # Click Button    ${dropdown_exc}
    # Wait Until Element Is Visible    ${wazir}
    # Click Button    ${wazir}

Verify the API

    Retrieve Data From API and Verify Lowest Price    ${end_point_btc}  
    # Run Keyword If    '${Lowest_Price}' == '${lowest_price_value}':
    # ...  User Verifes The Headers In coiswitch pro page2
    IF    ${Lowest_Price} != ${lowest_price_value} :
    User Verifes The Headers In coiswitch pro page
        
    END
    

#     [Arguments]    ${Exchange_keys}
#     Log To Console    ${Exchange_keys}
#     create session    MySession    ${URL}  
#     ${Domain_url}=    GET On Session    MySession    ${Domain_url}/${Exchange_keys}
#     Log To Console    ${Domain_url.content}
#     # FOR    ${index}    IN RANGE    1    100
#     #     ${Value} =    Get Value From Json    ${Domain_url.json()}    $..asks[${index}][0]
#     #     # ${low_value} =    Get From List    ${Value}    0
#     #     ${low_value} =     Convert To String    ${Value}
#     #     Log To Console    ${low_value}
#     # END
#     ${Value} =    Get Value From Json    ${Domain_url.json()}    $..asks[0][0]
#     ${low_value} =    Get From List    ${Value}    0
#     # ${ValueString} =    Convert To String    ${ValueString}
#     Log To Console    ${low_value}
#     Set Suite Variable    ${low_value}
#     User Navigates To buy bit coin header And Verify the lowest price button

# User Navigates To buy bit coin header And Verify the lowest price button
    
#     Click Element    ${click_getlowprice}
#     Wait Until Element Is Visible    ${value_to from path}    30s
#     ${lowest_price_value} =    Get Element Attribute    ${value_to from path}    value
#     # Wait For And Click On Element    ${Get_Lowest_Price}    15s
#     Log To Console    ${lowest_price_value}
#     Set Suite Variable    ${lowest_price_value}
    

# Verify the api

#     Retrive the data from API    ${end_point_url}
#     Run Keyword If   ${Lowest_Price} "=!" ${lowest_price_value}   Fail
#     User Navigates To buy bit coin header And Verify the lowest price button
#     Run Keyword If      ${Lowest_Price} "==" ${lowest_price_value}   Fail
   
    
    
    
    # Run Keyword If    '${low_value}' != '${lowest_price_value}'  Fail
    # Log   User Navigates To buy bit coin header And Verify the lowest price button
    # Should Be Equal    ${lowest_price_value}    ${low_value} 

    # FOR    ${retry}    IN RANGE    5 
    # Retrive the data from API    ${end_point_url}
    # Should Be Equal    ${lowest_price_value}    ${low_value}
    # Run Keyword If    '${low_value}' != '${lowest_price_value}'    
    # ...  ELSE
    # Log    Values Match: ${low_value} == ${lowest_price_value}
    # Log    Iteration ${retry}
    # END
    
    # Retrive the data from API    ${end_point_url}
    # Run Keyword If    '${low_value}' != '${lowest_price_value}'  Fail
    # Log   User Navigates To buy bit coin header And Verify the lowest price button
    # Should Be Equal    ${lowest_price_value}    ${low_value} 

# Check Values Match
#     [Arguments]    ${expected_value}
#     ${lowest_price_value} =    User Navigates To Buy Bitcoin Header And Verify The Lowest Price Button
#     Run Keyword If    '${lowest_price_value}' != '${expected_value}'
#     Log    Values do not match: ${lowest_price_value} != ${expected_value}
#     ...  ELSE     Log    Values match: ${lowest_price_value} = ${expected_value} 
# Check Values Until They Match
#     ${expected_value} =    Retrive the data from API
#     Run Keyword And Continue On Failure    Check Values Match    ${expected_value}
#     Log To Console    heloo the robot
