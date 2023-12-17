*** Settings ***
Resource     C:/Users/Hp/Desktop/Coin_Switch_Webpage/Robot_Framework/Keywords/Keywords.robot  

Suite Setup    Open Browser And navigated to URL
Suite Teardown    Close Browser
# To run all test cases
# cmd == robot -d Results 

# for tags 
# robot -d Results -i TAG Tests/CSPro_Sample.robot

*** Test Cases ***
TC_001: Verify the 'Buy Bitcoin' Button in coinswitch webpage
    [Tags]    Smoke
    Given Clik on Buy Bitcoin button
    when Navigate to bit coin trade page
    And Verify the tittle on navigated page bitcoin
    Then Return back to home page form bitcoin page

TC_002: Verify the 'Buy Ethereum' button in coinswitch webpage  
    [Tags]    Smoke
    Given Click on 'Buy Ethereum' button
    when Navigate to Ethereum trade page
    And Verify the tittle on navigated page of Ethereum
    Then Return back to home page from ethereum trade page

TC_003: Verify the 'Buy Tether' button in coinswitch webpage  
    [Tags]    Smoke
    Given Click on 'Buy Tether' button
    when Navigate to Tether trade page
    And Verify the tittle on navigated page of Tether
    Then Return back to home page from Tethe page


TC_004: Verify the 'Product Dropdown' in coinswitch webpage
    [Tags]    Sanity
    Given Mouse over on 'Products Dropdown'
    when Select 'Crypto Rupee Index' from dropdown and navigate to next page
    And Assert product name is same are not
    Then Return back from product Page to home page

TC_005: Verify the 'Company Dropdown' in coinswitch webpage
    [Tags]    Sanity
    Given Mouse over on 'Company Dropdown'
    when Select 'About Us' from dropdown and navigate to next page
    And Assert company name is same are not
    Then Return back from company Page to home page 

TC_006: Verify the 'Multiple Exchanges, One Platform' in coinswitch webpage
    [Tags]    Regression
    Given Scroll till 'Multipl Exchanges, One Platform' in coinswitch page
    when Click on Try Now button in Multipl Exchanges, One Platform module
    And Verify the tittle on navigated page of one platform
    Then Return back to home page from one platform

TC_007: Verify the 'Rupee-Powered' in coinswitch webpage
    [Tags]    Regression
    Given Scroll till 'Rupee-Powered' in coinswitch page
    when Click on Try Now button in Preform_Rupee-Powered
    And Verify the tittle on navigated page Rupee Powered
    Then Return back to home page from Rupee Powered

TC_008: Verify the 'Data-Driven Decisions' in coinswitch webpage
    [Tags]    Regression
    Given Scroll till 'Data-Driven Decisions' in coinswitch page
    when Click on Try Now button in Data-Driven Decisions module
    And Verify the tittle on navigated page from Data Driven Decisions
    Then Verify the tittle on navigated page from Data Driven Decisions
    
#Tc_001
Tc_009: User Verifies The Landing Page tittle
        [Tags]    somke
    Given Navigate to coin switch URL
    When Read the values from google Sheet_id
    Then Assert the web page dispaly message in langing page of coinSwitch webpage
#Tc_002
Tc_010: User has to test lowest price from API and Get lowest price on coin page
        [Tags]    apis
    Given Verify the API  
